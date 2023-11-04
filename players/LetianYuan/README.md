# 2023 Hackergame Writeup

> 袁乐天 复旦大学

**如若要使用我的代码，请注意替换你的`<your token>`**

[TOC]

## Hackergame 启动

https://cnhktrz3k5nc.hack-challenge.lug.ustc.edu.cn:13202/?similarity=100

>flag{WElCome-To-Hack3RgAM3-aNd-enjoy-HACKInG-20Z3}

## 猫咪小测

1. https://lib.ustc.edu.cn/%e6%9c%ac%e9%a6%86%e6%a6%82%e5%86%b5/%e9%a6%86%e8%97%8f%e5%88%86%e5%b8%83/

   > 12

2. https://arxiv.org/abs/2303.17626

   > 23

3. https://github.com/google/bbr/blob/master/Documentation/bbr-quick-start.md

   > CONFIG_TCP_CONG_BBR

4. https://drops.dagstuhl.de/opus/volltexte/2023/18241/

   > ECOOP

> flag{WE1CoMe-7O-4tt3nD-the-NEko-eX@M-2o23}
>
> flag{RE41-mA$7Er-Of-Th3-NeK0-3Xam-In-uStC}

## 更深更暗

查看网页源码就行

> flag{T1t@n_7c6e741158b4070b41ff8f31a32655bd}

## 旅行照片 3.0

1. https://www.s.u-tokyo.ac.jp/en/gallery/nobelprize/

   ```python
   import requests
   import datetime
   import base64
   from tqdm import tqdm
   
   BASE_URL = "http://202.38.93.111:12345/"
   
   
   def time2uri(ans1, ans2):
       return base64.b64encode(f"Answer1={ans1}&Answer2={ans2}".encode("utf-8")).decode("utf-8") + ".txt"
   
   
   if __name__ == "__main__":
       begin = datetime.date(2023, 1, 1)
       end = datetime.date(2023, 10, 28)
       for i in tqdm(range((end - begin).days + 1)):
           p = begin + datetime.timedelta(days=i)
           response = requests.post(
               BASE_URL,
               data=time2uri(p.strftime("%Y-%m-%d"), "ICRR"),
               headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Cookie": "<your token>"},
               timeout=10
           ).content.decode("utf-8")
           if not ("Not Found" in response):
               print(p.strftime("%Y-%m-%d"))
   ```

   > 2023-08-10
   >
   > ICRR

2. https://umeshu-matsuri.jp/tokyo_ueno/

   ```python
   import requests
   import datetime
   import base64
   from tqdm import tqdm
   
   BASE_URL = "http://202.38.93.111:12345/"
   
   
   def time2uri(ans1, ans2):
       return base64.b64encode(f"Answer3={ans1}&Answer4={ans2}".encode("utf-8")).decode("utf-8") + ".txt"
   
   
   if __name__ == "__main__":
       for i in tqdm(range(200)):
           response = requests.post(
               BASE_URL,
               data=time2uri("S495584522", i * 10),
               headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Cookie": "<your token>"},
               timeout=10
           ).content.decode("utf-8")
           if not ("Not Found" in response):
               print(i)
               print(response)
   ```

   > S495584522
   >
   > 0

3. https://plaza.rakuten.co.jp/ayumilife/diary/202308040000/

   https://statphys28.org/program/0810.html

   因为图中的“马里奥世界”在涩谷，所以答案一定是“秋田犬”

>flag{how_I_wi5h_i_COulD_w1N_A_Nobe1_pri23_cc4bd77a95}
>
>flag{PluM_w1NE_1S_rEa1LY_EXpen5iVE_90331052ee}
>
>flag{Un7I1_W3_M337_A64iN_6oODByE_S3n1OR_2b3c001c9d}

## 赛博井字棋

后端没有检测“在已有棋子的位置落子”的情况，所以用burp suite发请求直接把对手的棋子占了就行

> flag{I_can_eat_your_pieces_c2fd834c98}

## 奶奶的睡前 flag 故事

Acropalypse漏洞

![](pic/1.png)

> flag{sh1nj1ru_k0k0r0_4nata_m4h0}

## 组委会模拟器

```python
import requests
import requests.utils
import time
import json
import re
from tqdm import tqdm

BASE_URL = "http://202.38.93.111:10021"


def getSession():
    requests.get(f"{BASE_URL}/api/checkToken")
    response = requests.get(
        url=f"{BASE_URL}/api/checkToken?token=<your token>",
        headers={
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://202.38.93.111:10021/api/checkToken",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
            "Host": "202.38.93.111:10021"
        },
        allow_redirects=False
    )
    return requests.utils.dict_from_cookiejar(response.cookies)["session"]


def deleteMessage(idx, my_session):
    response = requests.post(
        f"{BASE_URL}/api/deleteMessage",
        headers={"Cookie": f"session={my_session}",
                 "Accept": "application/json, text/plain, */*",
                 "Content-Type": "application/json",
                 "Referer": "http://202.38.93.111:10021/",
                 "Origin": "http://202.38.93.111:10021",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.54 Safari/537.36"},
        json={"id": idx}
    )
    print(response.content.decode("utf-8"))


if __name__ == "__main__":
    my_session = getSession()
    response = requests.post(f"{BASE_URL}/api/getMessages",
                             headers={"Cookie": f"session={my_session}",
                                      "Accept": "application/json, text/plain, */*"})
    start = time.perf_counter()
    messages = json.loads(response.content.decode("utf-8"))['messages']
    pattern = re.compile(r"^.*hack\[.*\].*$")
    idx = 0
    for message in messages:
        while True:
            end = time.perf_counter()
            if message["delay"] < end - start:
                if pattern.match(message['text']):
                    deleteMessage(idx, my_session)
                break
        idx += 1
    response = requests.post(f"{BASE_URL}/api/getflag",
                             headers={"Cookie": f"session={my_session}",
                                      "Accept": "application/json, text/plain, */*"})
    print(response.content.decode("utf-8"))
```

> flag{Web_pr0gra_mm1ng_9463041e0c_15fun}

## 虫

国际空间站SSTV

![](pic/2.png)

> flag{SSssTV_y0u_W4NNa_HaV3_4_trY}

## JSON ⊂ YAML?

https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files

```json
{"b":1, "b":123456e9999}
```

> flag{faf9facd7c9d64f74a4a746468400a507a7913b337}
>
> flag{b1c73f14d04db546b7e7e24cf1cc7252731d5695e1}

## Git? Git!

```bash
git reflog
git reset --hard 505e1a3
```

> flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t}

## HTTP 集邮册（13个状态码）

- 100

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  Expect: 100-continue\r\n\r\n
  ```
  
- 200

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n\r\n
  ```

- 206

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  Range: bytes=0-999\r\n\r\n
  ```

- 304

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  If-None-Match: "64dbafc8-267"\r\n\r\n
  ```

- 400

  ```
  GET / HTTP/1.1
  Host: example.com
  ```

- 404

  ```
  GET /1 HTTP/1.1\r\n
  Host: example.com\r\n\r\n
  ```

- 405

  ```
  GEET / HTTP/1.1\r\n
  Host: example.com\r\n\r\n
  ```

- 412

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  If-Unmodified-Since: Mon, 28 Oct 1999 00:00:00 GMT\r\n\r\n
  ```

- 413

  ```
  GET / HTTP/1.1\r\n
  Content-Length: 99999999999999999\r\n
  Host: example.com\r\n\r\n
  ```

- 414

  ```
  GET /aaa（此处省略成千上百个a）aaa.html HTTP/1.1\r\n
  Host: example.com\r\n\r\n
  ```

- 416

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  Range: bytes=1000-1999\r\n\r\n
  ```

- 501

  ```
  GET / HTTP/1.1\r\n
  Host: example.com\r\n
  Transfer-Encoding: compress\r\n\r\n
  ```

- 505

  ```
  GET / HTTP/9.1\r\n
  Host: example.com\r\n\r\n
  ```

- 无状态码

  ```
  GET /index.html\r\n
  ```

> flag{stacking_up_http_status_codes_is_fun_b029f2b4a4}
>
> flag{congratu1ations you discovered someth1ng before http1.0}
>
> flag{I think that when many such status codes are accumulated 502c3b75c3 it becomes a lifetime}

## Docker for Everyone

```bash
docker run -v /flag:/flag -it --rm alpin
cat flag
```

>flag{u5e_r00t1ess_conta1ner_6ab339945a_plz!}

## 惜字如金 2.0

```python
cod_dict = [
    'nymeh1niwemflcir}echaet#',
    'a3g7}kidgojernoetllsup?h',
    'ulw!ff5soadrhwnrsnstnoeq',
    'ct{{l-findiehaai{oveatas',
    'ty9kxborszstgguyd?!blm-p'
]
```

> flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}

## 高频率星球

直接`asciinema play asciinema_restore.rec > tmp.js`拿到js代码，然后去掉控制字符，最后执行就行

> flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}

## 小型大语言模型星球

发送“Am I smart?”

（未完成第二、三、四问）

>flag{1-tHiNK-you-4re-R3@!1Y-r341LY-sMAr7}

## 流式星球

```python
import cv2
import numpy as np


def generate_video(buffer, output_file, frame_width, frame_height):
    frame_count = len(buffer) // (frame_width * frame_height * 3)
    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))
    print(buffer.shape)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_file, fourcc, 30.0, (frame_width, frame_height))
    for i in range(frame_count):
        frame = buffer[i]
        video_writer.write(frame)
    video_writer.release()


def approximate(width, height):
    for i in range(101):
        tmp = 135146688 + i
        if tmp % (3 * width * height) == 0:
            return tmp


if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf)
    buffer = np.fromfile("video.bin", dtype=np.uint8)
    print(buffer.shape)
    width = 61 * 7
    height = 759
    buffer = np.pad(buffer, (0, approximate(width, height) - len(buffer)), 'constant')
    print(buffer.shape)
    generate_video(buffer, "output.mp4", width, height)
```

> flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}

## 低带宽星球

使用PNGGauntlet工具可以直接获得flag1

（未完成第二问）

> flag{justfind_an_image_compressor_andgo!}

## Komm, süsser Flagge

第一小问和第二小问都可以用以下脚本

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("202.38.93.111", 18080))
client.send(b"PO")
client.send(b"ST / HTTP/1.1\r\nHost: 202.38.93.111:18080\r\n")
client.send(b"Content-Type: text/plain;charset=utf-8\r\n")
client.send(b"Content-Length: 100\r\n")
client.send(b"\r\n")
client.send(b"<your token>")
msg = client.recv(1024)
print(msg.decode("utf-8"))
```

第三小问如下，flag3直接用wireshark抓包即可（你如果想要做出来第三小问，肯定是需要用wireshark抓包的），其实主要因为我不知道这个scapy库如何获取`res2`中的HTTP响应内容

```python
import scapy.all as scapy
import random

dst_ip = "202.38.93.111"
dst_port = 18082
src_port = random.randint(8000, 60000)
bypass = "GET / HTTP"
data = (
    "POST / HTTP/1.1\r\n"
    "Host: 202.38.93.111:18082\r\n"
    "Content-Type: text/plain;charset=utf-8\r\n"
    "Content-Length: 100\r\n"
    "\r\n"
    "<your token>"
)
spk1 = scapy.IP(dst=dst_ip) / scapy.TCP(dport=dst_port, sport=src_port, flags="S",
                                        options=[("SAck", bypass), ("EOL", None)])
res1 = scapy.sr1(spk1)
ack1 = res1[scapy.TCP].ack
ack2 = res1[scapy.TCP].seq + 1
spk2 = scapy.IP(dst=dst_ip) / scapy.TCP(dport=dst_port, sport=src_port, seq=ack1, ack=ack2, flags="A",
                                        options=[("SAck", bypass), ("EOL", None)])
scapy.send(spk2)

da1 = scapy.IP(dst=dst_ip) / scapy.TCP(dport=dst_port, sport=src_port, seq=ack1, ack=ack2, flags=24,
                                       options=[("SAck", bypass), ("EOL", None)]) / data
res2 = scapy.sr1(da1)
```

> flag{ea5Y_sPl1tt3r_e21ecb8274}
>
> flag{r3s3rv3d_bYtes_2a17599b30}
>
> flag{1p_OoOpt10ns_8d90f970e1}

## 为什么要打开 /flag 😡（非预期解）

```C
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, const char *argv[]) {
    FILE* f = popen(". /flag", "r");
    char buff[1024];
    fgets(buff, 1024, f);
    printf("%s", buff);
    fclose(f);
}
```

（未完成第二问）

> flag{nande_ld_preload_yattano_1dc47a5ae7}

## 异星歧途

https://www.bilibili.com/video/BV1rb4y1z7Zm

https://mindustrygame.github.io/

前面16位不需要任何游戏知识，很容易知道是`10100101 11000100`，

后面16位可以稍微了解一下游戏，容易知道是`10001100 01110111`

> flag{B34WarE_0f_#xp1osi0N_d40ae7697a}

## 微积分计算小练习 2.0（未完成）

输入`"+document["cookie"]+"`可以XSS

以下是时间攻击获得`cookie`的方法

```python
from pwn import *
import string
from tqdm import tqdm


def crack(content):
    # context(os="linux", arch="amd64", log_level="debug")
    context(os="linux", arch="amd64", log_level="critical")
    p = remote("202.38.93.111", 10053)
    p.recvuntil(b'Please input your token: ')
    p.sendline(b'<your token>')
    p.recv(1000)
    p.recv(1000)
    document = (f"<!DOCTYPE html><html><head></head><body><script>"
                f"if(document.cookie.startsWith('{content}'))"
                f"while (true);</script></body></html>\nEOF").encode()

    p.sendline(document)
    result = p.recvall().decode("utf-8")
    return "Killed" in result


if __name__ == "__main__":
    content = ""
    try:
        while True:
            flag = True
            for e in tqdm(
                    " %ABCDEF0123456789abcdefghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ!\"#$&'()*+,-./:;<=>?@[\\]^_`{|}~"
            ):
                if flag:
                    while True:
                        try:
                            if crack(content + e):
                                content = content + e
                                print(content)
                                flag = False
                            break
                        except:
                            pass
    except KeyboardInterrupt:
        print(content)
```

以下是post请求获得`cookie`的办法

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    </script>
    <form id="autosubmit" action="http://202.38.93.111:10051/result" method="POST">
        <input name="comment" value="12" />
    </form>
    <script>
        window.onload = function () {
            document.getElementById("autosubmit").submit();
        }
    </script>
</body>

</html>
EOF
<!-- <form id="autosubmit" action="http://202.38.93.111:10051/result" method="POST"><input name="comment" value="foobar" />
</form>
<script>document.getElementById("autosubmit").submit();</script> -->
```

但是以上两个脚本都有一个问题，`document.cookie`是无法跨越获得`cookie`的

## 小 Z 的谜题

本质上是往`5 * 5 * 5`的立方体里塞长方体，`score`是长方体的不同坐标的顶点的数量

以下脚本是还没有想明白这一点的时候写的

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct Single {
    int a;
    int b;

    Single(int a, int b) : a(a), b(b) {}

    bool conflict(Single &o) const {
        return !(b <= o.a || o.b <= a);
    }
};

struct Tuple {
    Single data[3]{Single(0, 0), Single(0, 0), Single(0, 0)};

    Tuple(int a, int b, int c, int d, int e, int f) {
        data[0] = Single(a, b);
        data[1] = Single(c, d);
        data[2] = Single(e, f);
    }

    bool conflict(Tuple &o) const {
        for (int i = 0; i < 3; i++) {
            if (!data[i].conflict(o.data[i])) {
                return false;
            }
        }
        return true;
    }
};

vector<Tuple> v;
constexpr int CONSTRNT_CNT = 16;
//int constraints[6][3] = {
//        {2, 2, 3},
//        {2, 2, 2},
//        {1, 4, 4},
//        {1, 2, 4},
//        {1, 2, 2},
//        {1, 1, 3},
//};
//int constraints_count[6] = {3, 5, 7, 9, 13, 16};
int constraints[CONSTRNT_CNT][3] = {
        {3, 2, 2},
        {2, 3, 2},
        {2, 2, 3},
        {1, 4, 4},
        {4, 4, 1},
        {4, 1, 2},
        {2, 1, 4},
        {2, 2, 2},
        {2, 2, 2},
        {2, 2, 1},
        {2, 1, 2},
        {2, 1, 2},
        {1, 2, 2},
        {3, 1, 1},
        {1, 3, 1},
        {1, 1, 3},
};
int constraints_count[CONSTRNT_CNT] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};

void printV() {
    bool flag = false;
    for (auto e: v) {
        if (flag) {
            cout << ",";
        } else {
            flag = true;
        }
        cout << "\"";
        for (auto &i: e.data)
            cout << i.a << i.b;
        cout << "\"";
    }
    cout << endl;
}


int getCnt() {
    bool vis[1000];
    int d[3][3];
    d[0][2] = 6;
    d[1][2] = 6;
    d[2][2] = 6;
    memset(vis, 0, sizeof vis);
    for (auto e: v) {
        for (int i = 0; i < 3; i++) {
            d[i][0] = e.data[i].a;
            d[i][1] = e.data[i].b;
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    vis[d[0][i] * 100 + d[1][j] * 10 + d[2][k]] = 1;
                }
            }
        }
    }
    int cnt = 0;
    for (int i = 0; i < 1000; i++)
        cnt += vis[i];
    return cnt;
}

void dfs() {
    if (v.size() == 16) {
        if (getCnt() >= 157) // <= 136
            printV();
        return;
    }
    int cnt = 0;
    for (; cnt < CONSTRNT_CNT; cnt++) {
        if (v.size() < constraints_count[cnt]) {
            break;
        }
    }
    int cnst[3]{constraints[cnt][0], constraints[cnt][1], constraints[cnt][2]};
    do {
        for (int i = 0; i + cnst[0] <= 5; i++) {
            for (int j = 0; j + cnst[1] <= 5; j++) {
                for (int k = 0; k + cnst[2] <= 5; k++) {
                    Tuple tmp(i, i + cnst[0], j, j + cnst[1], k, k + cnst[2]);
                    for (auto e: v) {
                        if (e.conflict(tmp)) {
                            goto skip;
                        }
                    }
                    v.push_back(tmp);
                    dfs();
                    v.pop_back();
                    skip:;
                }
            }
        }
    } while (next_permutation(cnst, cnst + 3));
}

int main() {
    dfs();
}
```

> 020203020235022403022435034545044504230235232415240203242401341434342413350135351545450103451504
>
> 020203020235022403022435034545044504230435232413240203242401341434342413350135351545450103451504
>
> 012402020335023534023545030202034501040423044513132402240235242535341412350102351501450125451515

> flag{G0og1e_1s_a1l_y0u_n3ed_06aa082841}
>
> flag{DFS_A1g0ri7hm_1s_u5efu1_fb5081de52}
>
> flag{Knuths_A1g0ri7hm_X_1s_p0w3rful_8d0e83fee0}

## 黑客马拉松（未完成）

```python
import sympy
import random
from pwn import *


def getPrime():
    p1 = sympy.nextprime(2 ** 255, 6)
    p2 = sympy.nextprime(2 ** 256)
    while not sympy.isprime(p1 * p2 + 1):
        p2 += 1
    q1 = sympy.nextprime(p2)
    q2 = sympy.nextprime(q1)
    while not sympy.isprime(q1 * q2 + 1):
        q2 += 1
    return p1, p2, q1, q2


def find_primitive_root(modulus):
    for g in sympy.primerange(2, modulus):
        if sympy.is_primitive_root(g, modulus):
            return g
    return None

states = []
randomNums = []

if __name__ == "__main__":
    p1, p2, q1, q2 = getPrime()
    p = p1 * p2 + 1
    q = q1 * q2 + 1
    N = p * q
    Nbits = N.bit_length()
    phi = (p - 1) * (q - 1)
    e = 5
    d = pow(e, -1, phi)
    assert d.bit_length() > 0.292 * Nbits
    assert e * d % phi == 1
    k = Nbits - max(int(Nbits * 2 / e), 96)

    state = random.SystemRandom().randint(2, N - 1)

    print(state)
    state = pow(state, e, N)
    state = pow(state, d, N)
    print(state)
```

