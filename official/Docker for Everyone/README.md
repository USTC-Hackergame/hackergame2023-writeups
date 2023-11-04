# Docker for Everyone

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：general

- 题目分值：150

X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 docker，他把同学的账号加入了 docker 用户组，这样就不需要给同学 sudo 权限了！

但果真如此吗？

---

提供的环境会自动登录低权限的 `hg` 用户。登录后的提示信息显示了如何在该环境中使用 docker。读取 `/flag`（注意其为软链接）获取 flag。

题目环境运行 15 分钟后会自动关闭。

你可以在下面列出的两种方法中任选其一来连接题目：

- 点击下面的「打开/下载题目」按钮通过网页终端与远程交互。如果采用这种方法，在正常情况下，你不需要手动输入 token。
- 在 Linux、macOS、WSL 或 Git Bash 等本地终端中使用 `stty raw -echo; nc 202.38.93.111 10338; stty sane` 命令来连接题目。如果采用这种方法，你必须手动输入 token（复制粘贴也可）。**注意，输入的 token 不会被显示，输入结束后按 Ctrl-J 即可开始题目。**

无论采用哪种方法连接题目，启动题目均需要数秒时间，出现黑屏是正常现象，请耐心等待。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

## 题解

这题是 @zzh1996 的 idea，我负责实现。Docker 在配置的时候，很多人为了方便，会把自己加到 docker 的用户组里面，这么做在单人的环境下问题倒也不太大，但是在多人使用的服务器的场景下，这样做就有很大的问题，因为 docker 用户组和 root 事实上是等价的，本题也在尝试证明这一点。

解法很简单，在打开之后等待 alpine 开机，然后把 rootfs 挂（bind mount）进要运行的容器里即可：

```
docker run -it --rm -v /:/outside alpine
```

那么实际的 rootfs 就在 `/outside` 目录，注意 `/flag` 是个软链接，所以实际上 flag 位于 `/outside/dev/shm/flag`。如果希望能直接读根目录的软链接的话，得设置一下 IPC 模式为 `host`，这样的话主机和容器的 `/dev/shm` 就共享了：

```
docker run -it --rm --ipc=host -v /:/outside alpine
```

于是 flag 就在 `/dev/shm/flag`，可以直接读 `/outside/flag` 获取。

那么如果希望在保证安全的前提下让服务器的各个用户都能用上容器该怎么办？近年来流行的办法是启用 user namespace，然后配置 [rootless container](https://rootlesscontaine.rs/)。虽然 user namespace 这个内核特性是否安全还是个[颇具争议的话题](https://security.stackexchange.com/questions/209529/what-does-enabling-kernel-unprivileged-userns-clone-do)。

如果不希望开启 user namespace 的话，[PRoot](https://github.com/proot-me/PRoot/) 通过 `ptrace()` 来对程序假装自己的文件目录树、权限等信息，是一种可行的方案，但是 `ptrace` 带来的性能损失是远大于 user namespace 的；另一种方案是使用一个 root SUID 程序来做这个事情，例如 [bubblewrap](https://github.com/containers/bubblewrap) 就支持在 user namespace 关闭的时候通过 SUID 以 root 的身份提供服务，但是 SUID binary 本身的安全性也就成了很大的问题。

## 其他

在做这题的镜像的时候，我一开始用的方案是 buildroot，甚至内核编译参数都花了不少时间调，最后发现 docker 开不出来，`pivot_root` 会报错——然后发现 `pivot_root` 的限制使得我没有办法在 initramfs 里面跑 Docker 容器。

最后用了 Alpine，其实也还不错，改起来可能还比 buildroot 舒服点，虽然 OpenRC 开机好像确实不如 busybox 快就是（没有 KVM 加速的情况下）……

另外验题的时候发现有个「非预期解」：可以改 doas（sudo 的类似物）的配置让自己获得 root 权限，然后我就把 doas 的 binary 和配置删了，虽然都能改 doas 配置了，拿到 flag 应该是小菜一碟。
