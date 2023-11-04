## 19. 为什么要打开 /flag 😡

### 尝试与解决

> 关键词：LD_PRELOAD、静态链接

#### LD_PRELOAD

首先搜索，知道 [LD_PRELOAD 是什么](https://zhuanlan.zhihu.com/p/598346458)。

> LD_PRELOAD是Linux/Unix系统的一个环境变量，它可以影响程序的运行时的链接，它允许在程序运行前定义优先加载的动态链接库。通过这个环境变量，可以在主程序和其动态链接库的中间加载别的动态链接库，甚至覆盖系统的函数库。

也就是让程序优先使用自定义的动态链接库，覆盖系统的函数。看一下附件中的 `lib.c`，果真如此。`lib.c` 覆盖了包括 `freopen` `fopen` `open` `openat` 在内的函数，还禁用了 `system` `execl` 等函数阻止程序通过调用外部程序绕开限制。

但是等等，动态链接？

哦...

```cpp
#include <stdio.h>
#include <stdlib.h>

char buf[2048];

int main(int argc, char **argv) {
    FILE *fp = fopen("/flag", "r");
    fgets(buf, 2048, fp);
    printf("%s\n", buf);
}
```

```plain
$ gcc --static main.c -o main # 静态链接
```

好的，已经结束力！

#### seccomp-unotify

Seccomp 是监视或限制程序使用系统调用的手段，一旦设置不能取消，并且会继承到子进程中，无法通过调用外部程序绕过。

代码 `main.rs` 的意思似乎是劫持 `open` 和 `openat`，但是不知道为什么，`name_to_handle_at` `openat2` `symlink` 等各类系统调用都失效了，会获得 `128: Operation already in progress` 错误。这就没活了。

### Flag

```plain
flag{nande_ld_preload_yattano_d7b67c550b}
```
