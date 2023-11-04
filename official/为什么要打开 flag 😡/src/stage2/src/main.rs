// This source code modifies code from [greenhook crate](https://crates.io/crates/greenhook).
use std::{
    collections::HashMap,
    ffi::CStr,
    fs::File,
    io::{self, IoSliceMut},
    mem::{self, size_of},
    os::{
        fd::{AsRawFd, RawFd},
        unix::process::CommandExt,
    },
    process::{Child, Command, ExitStatus},
    ptr,
    sync::Arc,
    thread::JoinHandle,
};

use libseccomp::{
    ScmpAction, ScmpFilterContext, ScmpNotifReq, ScmpNotifRespFlags,
    ScmpSyscall,
};
use log::{error, info, warn};
use nix::{
    cmsg_space,
    errno::Errno,
    libc::{
        self, c_uint, c_void, cmsghdr, ioctl, msghdr, CMSG_DATA, CMSG_FIRSTHDR, CMSG_LEN,
        CMSG_SPACE,
    },
    poll::{PollFd, PollFlags},
    sys::{
        socket::{
            recvmsg, socketpair, AddressFamily, ControlMessageOwned, MsgFlags, SockFlag, SockType,
        },
        uio::{process_vm_readv, RemoteIoVec},
        utsname::uname,
    },
    unistd::{close, Pid},
};
use procfs::process::Process;
use threadpool::ThreadPool;

// SocketPair is used to copy fd from child to parent
// with sendmsg/recvmsg and SCM_RIGHTS
#[derive(Debug)]
struct SocketPair {
    // child fd
    sender: RawFd,
    // parent fd
    receiver: RawFd,
}

struct Sender {
    fd: RawFd,
}

struct Receiver {
    fd: RawFd,
}

impl SocketPair {
    pub(crate) fn init() -> Result<Self, io::Error> {
        let pairs = socketpair(
            AddressFamily::Unix,
            SockType::Stream,
            None,
            SockFlag::SOCK_CLOEXEC,
        )?;
        Ok(SocketPair {
            sender: pairs.0,
            receiver: pairs.1,
        })
    }

    pub(crate) fn channel(&self) -> (Sender, Receiver) {
        (Sender { fd: self.sender }, Receiver { fd: self.receiver })
    }
}

impl Drop for SocketPair {
    fn drop(&mut self) {
        let _ = close(self.sender);
        let _ = close(self.receiver);
    }
}

impl Sender {
    // nix::sys::socket::sendmsg allocates when cmsgs is not empty
    // which is not a good idea inside pre_exec
    // ref: nix's sendmsg implementation (MIT license)
    // (https://github.com/nix-rust/nix/blob/c6f9e2332efcf62c751d7a0174bb791e732b90a8/src/sys/socket/mod.rs#L1474)
    pub(crate) fn sendfd(&self, fd: RawFd) -> Result<(), io::Error> {
        const FD_SIZE: c_uint = size_of::<RawFd>() as c_uint;
        const CAPACITY: u32 = unsafe { CMSG_SPACE(FD_SIZE) };
        const ALIGNMENT: usize = mem::align_of::<cmsghdr>();
        let buf = [0u8; ALIGNMENT + CAPACITY as usize];
        let (_prefix, aligned_buf, _suffix) = unsafe { buf.align_to::<cmsghdr>() };
        let cmsg_ptr = aligned_buf.as_ptr() as *mut c_void;
        let mut _binding = [0; 1];
        let mut _iov_buffer = [IoSliceMut::new(&mut _binding); 1];

        let mhdr = unsafe {
            // Musl's msghdr has private fields, so this is the only way to
            // initialize it.
            let mut mhdr = mem::MaybeUninit::<msghdr>::zeroed();
            let p = mhdr.as_mut_ptr();
            (*p).msg_name = ptr::null::<()>() as *mut _;
            (*p).msg_namelen = 0;
            // transmute iov into a mutable pointer.  sendmsg doesn't really mutate
            // the buffer, but the standard says that it takes a mutable pointer
            (*p).msg_iov = _iov_buffer.as_ref().as_ptr() as *mut _;
            (*p).msg_iovlen = 1;
            (*p).msg_control = cmsg_ptr;
            (*p).msg_controllen = CAPACITY as _;
            (*p).msg_flags = 0;
            mhdr.assume_init()
        };

        let pmhdr: *mut cmsghdr = unsafe { CMSG_FIRSTHDR(&mhdr) };

        unsafe {
            (*pmhdr).cmsg_level = libc::SOL_SOCKET;
            (*pmhdr).cmsg_type = libc::SCM_RIGHTS;
            (*pmhdr).cmsg_len = CMSG_LEN(FD_SIZE) as usize;
            ptr::copy_nonoverlapping(
                &[fd] as *const _ as *const u8,
                CMSG_DATA(pmhdr),
                FD_SIZE as usize,
            )
        }
        let ret = unsafe { libc::sendmsg(self.fd, &mhdr, 0) };

        if ret < 0 {
            Err(io::Error::last_os_error())
        } else {
            Ok(())
        }
    }
}

impl Receiver {
    pub(crate) fn recvfd(&self) -> Result<RawFd, io::Error> {
        let mut cmsg_buffer = cmsg_space!(RawFd);
        let mut _binding = [0; 1];
        let mut _iov_buffer = [IoSliceMut::new(&mut _binding); 1];
        let res = recvmsg::<()>(
            self.fd,
            &mut _iov_buffer,
            Some(&mut cmsg_buffer),
            MsgFlags::empty(),
        )
        .map_err(|e| io::Error::from_raw_os_error(e as i32))?;
        for cmsg in res.cmsgs() {
            if let ControlMessageOwned::ScmRights(fds) = cmsg {
                return Ok(fds[0]);
            }
        }
        Err(io::Error::from_raw_os_error(libc::EINVAL))
    }
}

/// UNotifyEventRequest is the type of parameter that user's function
/// would get.
#[derive(Debug)]
pub struct UNotifyEventRequest {
    request: libseccomp::ScmpNotifReq,
    notify_fd: RawFd,
}

impl UNotifyEventRequest {
    fn new(request: libseccomp::ScmpNotifReq, notify_fd: RawFd) -> Self {
        UNotifyEventRequest { request, notify_fd }
    }

    /// Returns the unotify request (`libseccomp::ScmpNotifReq`) of
    /// this event.
    pub fn get_request(&self) -> &libseccomp::ScmpNotifReq {
        &self.request
    }

    /// Let the kernel continue the syscall.
    pub fn continue_syscall(&self) -> libseccomp::ScmpNotifResp {
        libseccomp::ScmpNotifResp::new(self.request.id, 0, 0, ScmpNotifRespFlags::CONTINUE.bits())
    }

    /// Returns error to supervised process.
    /// `err` parameter should be a number larger than 0.
    pub fn fail_syscall(&self, err: i32) -> libseccomp::ScmpNotifResp {
        debug_assert!(err > 0);
        libseccomp::ScmpNotifResp::new(self.request.id, 0, -err, 0)
    }

    /// Returns value to supervised process.
    pub fn return_syscall(&self, val: i64) -> libseccomp::ScmpNotifResp {
        libseccomp::ScmpNotifResp::new(self.request.id, val, 0, 0)
    }

    /// Check if this event is still valid.
    /// In some cases this is necessary, please check seccomp_unotify(2) for more information.
    pub fn is_valid(&self) -> bool {
        libseccomp::notify_id_valid(self.notify_fd, self.request.id).is_ok()
    }

    /// Add a file descriptor to the supervised process.
    pub fn add_fd(&self, src_fd: RawFd) -> Result<RawFd, io::Error> {
        let addfd: libseccomp_sys::seccomp_notif_addfd = libseccomp_sys::seccomp_notif_addfd {
            id: self.request.id,
            flags: 0,
            srcfd: src_fd as u32,
            newfd: 0,
            newfd_flags: 0,
        };
        const SECCOMP_IOCTL_NOTIF_ADDFD: u64 = 0x40182103;

        let new_fd = unsafe {
            ioctl(
                self.notify_fd,
                SECCOMP_IOCTL_NOTIF_ADDFD,
                &addfd as *const _,
            )
        };
        if new_fd < 0 {
            Err(io::Error::last_os_error())
        } else {
            Ok(new_fd as RawFd)
        }
    }
}

/// By using `RemoteProcess`, you can get some information about the supervised process.
#[derive(Debug)]
pub struct RemoteProcess {
    pid: Pid,
    fd: RawFd,
}

impl RemoteProcess {
    /// Create a `RemoteProcess` object from a `Pid`.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// let remote = RemoteProcess::new(Pid::from_raw(req.request.pid as i32)).unwrap();
    /// ```
    pub fn new(pid: Pid) -> Result<Self, io::Error> {
        // get TGID of given pid (TID)
        let tid_stat = Process::new(pid.as_raw())
            .and_then(|p| p.status())
            .map_err(|e| {
                io::Error::new(
                    io::ErrorKind::Other,
                    format!("failed to get stat of pid {}: {}", pid, e),
                )
            })?;
        let tgid = tid_stat.tgid;

        let fd = unsafe { libc::syscall(libc::SYS_pidfd_open, tgid, 0) };
        if fd < 0 {
            Err(io::Error::last_os_error())
        } else {
            Ok(RemoteProcess {
                pid: Pid::from_raw(tgid),
                fd: fd as RawFd,
            })
        }
    }

    /// Get file descriptor from remote process with `pidfd_getfd()`.
    /// This function requires Linux 5.6+.
    pub fn get_fd(&self, remote_fd: RawFd) -> Result<RawFd, io::Error> {
        let local_fd = unsafe { libc::syscall(libc::SYS_pidfd_getfd, self.fd, remote_fd, 0) };
        if local_fd < 0 {
            Err(io::Error::last_os_error())
        } else {
            Ok(local_fd as RawFd)
        }
    }

    /// Read data from remote process's memory with `process_vm_readv()`.
    /// You should run is_valid() after this method to check if the remote process and corresponding syscall
    /// is still alive.
    ///
    /// # Examples
    /// ```ignore
    /// let mut buf = [0u8; 256];
    /// remote.read_mem(&mut buf, path as usize).unwrap();
    /// ```
    pub fn read_mem(
        &self,
        local_buffer: &mut [u8],
        remote_addr: usize,
    ) -> Result<usize, io::Error> {
        let len = local_buffer.len();
        let mut local_iov = [IoSliceMut::new(local_buffer)];
        let remote_iov = [RemoteIoVec {
            base: remote_addr,
            len,
        }];
        process_vm_readv(self.pid, &mut local_iov, &remote_iov)
            .map_err(|e| io::Error::from_raw_os_error(e as i32))
    }
}

impl Drop for RemoteProcess {
    fn drop(&mut self) {
        let _ = close(self.fd);
    }
}

type UserHookFunc = Box<dyn Fn(&UNotifyEventRequest) -> libseccomp::ScmpNotifResp + Send + Sync>;

const ALLOWLIST: &[&str] = &[
    "brk",
    "arch_prctl",
    "access",
    "newfstatat",
    "mmap",
    "close",
    "read",
    "pread64",
    "set_tid_address",
    "exit_group",
    "set_robust_list",
    "rseq",
    "mprotect",
    "prlimit64",
    "munmap",
    "getrandom",
    "sendmsg",
    "write",
    "execve",
    "getdents64",
    "statx",
    "ioctl",
    "lseek",
    "rt_sigprocmask",
    "futex",
    "writev",
    "clone",
];

pub struct Supervisor {
    handlers: HashMap<ScmpSyscall, Arc<UserHookFunc>>,
    socket_pair: SocketPair,
    thread_pool: ThreadPool,
}

macro_rules! loop_while_eintr {
    ($poll_expr: expr) => {
        loop {
            match $poll_expr {
                Ok(nfds) => break Ok(nfds),
                Err(Errno::EINTR) => (),
                Err(e) => break Err(e),
            }
        }
    };
}

impl Supervisor {
    /// Create a new `Supervisor` object. You can specify the number of threads in the thread pool.
    /// This function will also check your kernel version and show warning or return error if necessary.
    pub fn new(thread_num: usize) -> Result<Self, io::Error> {
        if thread_num == 0 {
            return Err(io::Error::new(
                io::ErrorKind::InvalidInput,
                "thread_num should be greater than 0",
            ));
        }
        // detect kernel version and show warning
        let version = uname().map_err(|e| io::Error::from_raw_os_error(e as i32))?;
        let version = version.release();

        macro_rules! parse_error {
            () => {
                io::Error::new(io::ErrorKind::Other, "unknown version")
            };
        }

        let (major, minor) = {
            let mut iter = version.to_str().ok_or_else(|| parse_error!())?.split('.');
            let major = iter
                .next()
                .unwrap()
                .parse::<u32>()
                .map_err(|_| parse_error!())?;
            let minor = iter
                .next()
                .unwrap()
                .parse::<u32>()
                .map_err(|_| parse_error!())?;
            (major, minor)
        };
        if major < 5 || (major == 5 && minor < 9) {
            Err(io::Error::new(
                io::ErrorKind::Other,
                "old unsupported kernel",
            ))?;
        }
        Ok(Supervisor {
            socket_pair: SocketPair::init()?,
            handlers: HashMap::new(),
            thread_pool: ThreadPool::new(thread_num),
        })
    }

    /// Insert a user-defined handler function for a syscall.
    pub fn insert_handler(
        &mut self,
        syscall: ScmpSyscall,
        handler: impl Fn(&UNotifyEventRequest) -> libseccomp::ScmpNotifResp + Send + Sync + 'static,
    ) {
        self.handlers.insert(syscall, Arc::new(Box::new(handler)));
    }

    /// Run a command with seccomp filter.
    /// This method will fork a child process, do some preparations and run the command in it.
    /// It returns a Child, a JoinHandle of supervising thread, and a ThreadPool handle of syscall user functions.
    /// It's recommended to use `Supervisor::wait()` to wait for the child process.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// let (mut child, handle, pool) = supervisor.exec(&mut cmd).unwrap();
    /// ```
    pub fn exec(self, cmd: &mut Command) -> Result<(Child, JoinHandle<()>, ThreadPool), io::Error> {
        let (sender, receiver) = self.socket_pair.channel();
        let syscall_list: Vec<_> = self.handlers.keys().copied().collect();
        unsafe {
            cmd.pre_exec(move || {
                let mut ctx =
                    ScmpFilterContext::new_filter(ScmpAction::Errno(114)).map_err(|e| {
                        io::Error::new(
                            io::ErrorKind::Other,
                            format!("failed to create seccomp filter: {}", e),
                        )
                    })?;
                for syscall in syscall_list.iter() {
                    ctx.add_rule_exact(ScmpAction::Notify, *syscall)
                        .map_err(|e| {
                            io::Error::new(
                                io::ErrorKind::Other,
                                format!("failed to add notify rule: {}", e),
                            )
                        })?;
                }
                for syscall in ALLOWLIST {
                    let syscall = ScmpSyscall::new(syscall);
                    ctx.add_rule_exact(ScmpAction::Allow, syscall)
                        .map_err(|e| {
                            io::Error::new(
                                io::ErrorKind::Other,
                                format!("failed to add allowlist rule: {}", e),
                            )
                        })?;
                }
                ctx.load().map_err(|e| {
                    io::Error::new(
                        io::ErrorKind::Other,
                        format!("failed to load seccomp filter: {}", e),
                    )
                })?;
                let ufd = ctx.get_notify_fd().map_err(|e| {
                    io::Error::new(
                        io::ErrorKind::Other,
                        format!("failed to get notify fd: {}", e),
                    )
                })?;

                sender.sendfd(ufd)?;
                close(ufd)?;
                Ok(())
            });
        }
        let child = cmd.spawn()?;
        let fd = receiver.recvfd()?;
        mem::drop(self.socket_pair);

        // debug!("receiver got fd: {}", fd);

        let pool_handle = self.thread_pool.clone();
        let thread_handle = std::thread::spawn(move || {
            loop {
                // Poll fd first: is it readable?
                let mut pollfd = [PollFd::new(fd, PollFlags::POLLIN)];
                let poll_res = loop_while_eintr!(nix::poll::poll(&mut pollfd, -1));
                if let Err(e) = poll_res {
                    error!("failed to poll: {}", e);
                    break;
                }
                match pollfd[0].revents() {
                    None => {
                        error!("unknown poll event");
                        break;
                    }
                    Some(revents) => {
                        if revents.contains(PollFlags::POLLHUP) {
                            break;
                        }
                    }
                }
                // debug!("{:?} {:?} {:?}", poll_res, pollfd[0].revents(), pollfd);

                let req = ScmpNotifReq::receive(fd);
                let req = match req {
                    Ok(req) => req,
                    Err(e) => {
                        error!("failed to receive notification: {}", e);
                        break;
                    }
                };
                let event_req = UNotifyEventRequest::new(req, fd);
                let syscall_id = event_req.get_request().data.syscall;

                let handler = match self.handlers.get(&syscall_id) {
                    Some(handler) => handler,
                    None => {
                        warn!("got unknown syscall to handle: {}", syscall_id);
                        match event_req.fail_syscall(libc::ENOSYS).respond(fd) {
                            Ok(_) => {}
                            Err(e) => {
                                error!("failed to send response: {}", e);
                                return;
                            }
                        };
                        continue;
                    }
                };
                let handler_in_thread = handler.clone();
                self.thread_pool.execute(move || {
                    let response = handler_in_thread(&event_req);

                    if !event_req.is_valid() {
                        info!("no need to respond to the request as it is invalid");
                        return;
                    }
                    match response.respond(fd) {
                        Ok(_) => {}
                        Err(e) => {
                            warn!("failed to send response: {}", e);
                        }
                    };
                });
            }
        });

        Ok((child, thread_handle, pool_handle))
    }

    /// Wait for the child process to exit and cleanup the supervisor thread and thread pool.
    /// It returns `WaitStatus` of the child process.
    ///
    /// # Examples
    ///
    /// ```ignore
    /// let status = Supervisor::wait(&mut child, thread_handle, pool).unwrap();
    /// ```
    pub fn wait(
        child: &mut Child,
        thread_handle: JoinHandle<()>,
        pool_handle: ThreadPool,
    ) -> Result<ExitStatus, io::Error> {
        let status = child.wait()?;
        thread_handle.join().map_err(|_| {
            io::Error::new(io::ErrorKind::Other, "failed to join supervisor thread")
        })?;
        pool_handle.join();
        Ok(status)
    }
}

fn opening_handler(path_pos: usize, req: &UNotifyEventRequest) -> libseccomp::ScmpNotifResp {
    let path = req.get_request().data.args[path_pos];
    let remote = RemoteProcess::new(Pid::from_raw(req.get_request().pid as i32)).unwrap();
    let mut buf = [0u8; 256];
    remote.read_mem(&mut buf, path as usize).unwrap();
    // debug!("open (read from remote): {:?}", buf);
    let path = CStr::from_bytes_until_nul(&buf).unwrap();
    if !req.is_valid() {
        return req.fail_syscall(libc::EACCES);
    }
    info!("open (path CStr): {:?}", path);
    if path.to_str().unwrap().contains("flag") {
        let file = match File::open("/fakeflag") {
            Ok(file) => file,
            Err(e) => {
                error!("failed to open /fakeflag: {}", e);
                return req.fail_syscall(libc::EACCES);
            }
        };
        let fd = file.as_raw_fd();
        let remote_fd = req.add_fd(fd).unwrap();
        req.return_syscall(remote_fd as i64)
    } else {
        req.continue_syscall()
    }
}

fn main() {
    env_logger::init();
    // terminate whole process when a thread panics
    let orig_hook = std::panic::take_hook();
    std::panic::set_hook(Box::new(move |panic_info| {
        orig_hook(panic_info);
        std::process::exit(1);
    }));

    let args = std::env::args().skip(1).collect::<Vec<_>>();
    if args.len() == 0 {
        panic!("Usage: {} <program>", std::env::args().nth(0).unwrap());
    }
    let mut supervisor = Supervisor::new(1).unwrap();
    supervisor.insert_handler(ScmpSyscall::new("open"), |req| opening_handler(0, req));
    supervisor.insert_handler(ScmpSyscall::new("openat"), |req| opening_handler(1, req));

    let mut cmd = Command::new(args[0].clone());
    let cmd = cmd.args(&args[1..]);
    let (mut child, thread_handle, pool) = supervisor.exec(cmd).unwrap();
    let status = Supervisor::wait(&mut child, thread_handle, pool).unwrap();

    match status.code() {
        Some(code) => std::process::exit(code),
        None => std::process::exit(128),
    }
}
