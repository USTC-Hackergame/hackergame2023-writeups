# 写在前面

**第一次参加 hackergame，好玩、爱玩、多玩！**

# 正文

## Hackergame 启动
- > **flag{wE!cOmE-70-HaCKER9@M3-@ND-ENjoy-h@cK!ng-20Z3}**

在开发者工具可以发现，音频是在前端的 JS 代码中计算的，通过 URL 传参给后端判断

所以我们可以自己去设置 **similarity** 的值，拿到 flag，是一个很有趣的界面

![f1](/static/posts/Hackergame2023/f1.png)

## 猫咪小测
- > **flag{w3LcOm3-to-47t3ND-tH3-nek0-3xaM-zOz3}**
- > **flag{re4l-m@$73R-of-the-n3K0-3xam-iN-uS7c}**

四道搜索题，下列为各题解答方式：
1. 这题有两种解法，第一种是去中科大的图书馆网站去搜索，第二种是穷举，最终答案是 **12**
2. 这题可以直接去知乎搜索，有个帖子正好讲了这个论文，当然也可以选择穷举，最终答案是 **23**
3. 这题可以去 ChatGPT 问，也可以去下载 linux kernel 然后全局搜索 BBR，最终答案是 **CONFIG_TCP_CONG_BBR**
4. 这题让我很头大，最终在 Google 上以 "Python type infinite loop" 为关键词找到了答案 **ECOOP**

![f2](/static/posts/Hackergame2023/f2.png)

## 更深更暗
- > **flag{T1t@n_e8afe7610a9adb33636834d4f668e5e0}**

这题很简单，开发者工具就能找到网页中的潜艇
如果是一直往下翻的话，网页的 JS 脚本会不断地生成水域，很难找到

![f3](/static/posts/Hackergame2023/f3.png)

## 旅行照片 3.0
- > **flag{how_I_wi5h_i_COulD_w1N_A_Nobe1_pri23_84805398a7}**
- > **flag{PluM_w1NE_1S_rEa1LY_EXpen5iVE_794735bb60}**
- > **flag{Un7I1_W3_M337_A64iN_6oODByE_S3n1OR_f3a1e3372c}**

六道搜索题，下列为各题解答方式：
1. 根据第二张图，最左边那位学长肩旁的那一个 LOGO 我们可以找到该学术活动的官方网站 **https://statphys28.org/banquet.html** ，通篇看完题目，可以确定学长参加的学术会议就是这个活动，这个活动持续时间为2023年8月7日至2023年8月11日，结合后续的乘船环节，于是我们获得了第一个问题的答案，这一天是在 **8月10日**，学长的学校是 **东京大学**
2. 上网查询可知，这个奖章是诺贝尔奖的背面。于是在 Google 上搜索东大展览中的诺贝尔获奖者清单 **https://www.s.u-tokyo.ac.jp/en/gallery/nobelprize** ，逐个排查后，找到年龄最小的获奖者是 **2015年获奖的梶田隆章(Takaaki Kajita)**，他在东京大学宇宙射线研究所(Institute for Cosmic Ray Research, ICRR)工作，故答案为 **ICRR**
3. 已经得知当天时间为 **8月10日**，上 Twitter 并结合上野公园这个时间段，我们可以找到这个活动主办方 **https://twitter.com/umeshu_matsuri** ，8月10日他们在上野公园喷水池附近举办了梅酒活动 **https://twitter.com/umeshu_matsuri/status/1689516712818044928** ，找到志愿者报名表链接为 **https://ws.formzu.net/fgen/S495584522/** ，答案为 **S495584522**
4. 找到东京国立博物馆的官网为 **https://www.tnm.jp/modules/r_free_page/index.php?id=113#access_01** ，大学生票价为免费，所以答案为 **0**
5. 承接前文该学术活动的官方网站，可以发现 18:00 参与者要在 **Yasuda Auditorium** 附近集合坐船，翻译得到答案为 **安田讲堂**
6. 直接以 **ボタン＆カフリンクス** 为关键词，我们可以在 Twitter 上找到可能的帖子，发现动物为 **熊猫**；在互联网上搜索日本的马里奥世界，发现大阪有一个任天堂乐园，因为坐电车从东京到大阪就很不合理，排查后应该为涩谷站的任天堂旗舰店，再搜索可知这个 3D 动物品种为 **秋田犬**

{% gallery %}
![](/static/posts/Hackergame2023/f41.png)
![](/static/posts/Hackergame2023/f42.png)
![](/static/posts/Hackergame2023/f43.png)
![](/static/posts/Hackergame2023/f44.png)
![](/static/posts/Hackergame2023/f45.png)
![f4](/static/posts/Hackergame2023/f4.png)
{% endgallery %}

## 赛博井字棋
- > **flag{I_can_eat_your_pieces_ca3a248208}**

不难发现，前端的数据通过 JS 代码里的 setMove(x, y) 函数来发送，于是我们可以发送假数据，最终获得 flag

![f5](/static/posts/Hackergame2023/f5.png)

## 奶奶的睡前 flag 故事
- > **flag{sh1nj1ru_k0k0r0_4nata_m4h0}**

这是一道图片隐写的题目，发现题目中的加粗字体提到了 Google 和系统没升级等字样。推测应该是 Google 的某个牌子的手机在系统升级前存在漏洞。上网查询后得知确实如此(一个被称为**ACropalypse**的漏洞)，去 github 查询相关的复原工具后，得到 flag

![f6](/static/posts/Hackergame2023/f6.png)

## 组委会模拟器

- > **flag{Web_pr0gra_mm1ng_be8ea63db5_15fun}**

去开发者工具查看网络情况可以发现，网页通过 **getMessage** 函数获取消息信息、**delete_message** 来撤回消息，**getFlag** 来获取 flag。在本地通过 python 脚本来模拟这个交互过程，需要注意的就是定时器的设置，一定要确保消息已经发送了再撤回(可以用 python 内置的 time 库)

```python
import requests
import json
from time import perf_counter

headers = {
    "Cookie": "_ga=GA1.1.1982209457.1698511779; _ga_R1FN4KJKJH=GS1.1.1698557912.3.1.1698559589.0.0.0; session=eyJ0b2tlbiI6IjcyNDpNRVVDSVFEcXF0SUdUcFl4MnhQaVd5OThHb1hlUWRJRGFYbHR1YmhvR0Z6Q2FVUForUUlnZDA3OWcvbEkwUjVjckp6TFh1U1FlVERkSnVuN2d2Y3JjcTlCWUw4SXlKaz0ifQ.ZT9C6A.jvHCvdhPjUipRWBgY34OpJQpv3Q",
    "Host": "202.38.93.111:10021",
    "Content-Type": "application/json",
    "Origin": "http://202.38.93.111:10021",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://202.38.93.111:10021/",
}

request = requests.post(url="http://202.38.93.111:10021/api/getMessages", headers=headers)
start = perf_counter()

messages = json.loads(request.content)["messages"]

for idx, message in enumerate(messages):
    delay = message["delay"]
    text  = message["text"]
    if "这道题 flag 是hack[" in text:
        print(idx, delay, text)
        while perf_counter() < start + delay + 1:
            continue
        delete_message = requests.post(url="http://202.38.93.111:10021/api/deleteMessage", headers=headers, json={"id":idx})
        delete_message = json.loads(delete_message.content)
        print(delete_message)

flag = requests.post(url="http://202.38.93.111:10021/api/getflag", headers=headers)
flag = json.loads(flag.content)
print(flag)
```

![f7](/static/posts/Hackergame2023/f7.png)

## 虫

- > **flag{SSssTV_y0u_W4NNa_HaV3_4_trY}**

通过题目中的关键词可以查到一种通过高频波段来传输图片的方式，下载到对应的转译工具( **https://hamsoft.ca/pages/mmsstv.php** )后播放音乐，可以得到以下图像，拿到 flag

![f8](/static/posts/Hackergame2023/f8.png)

## JSON ⊂ YAML?

- > **flag{faf9facd7c9d64f74a4a746468400a50184f834122}**
- > **flag{b1c73f14d04db546b7e7e24cf1cc72520023e1fbc0}**

主要是构造一个符合条件的 json，这道题解法非常多，在此给出一种，能同时获取两个 flag

```shell
{"a":NaN, "a":NaN}
```

![f9](/static/posts/Hackergame2023/f9.png)

## Git? Git!

- > **flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t}**

git 操作，主要是去查看 log 文件夹里的内容，用相关的指令就可以找到被撤销的 flag 了

```shell
git show 505e1a3f446c23f31807a117e860f57cb5b5bb79
```

![f10](/static/posts/Hackergame2023/f10.png)

## HTTP 集邮册

- > **flag{d1d you hear the HTTP packet from 1991?}**
- > **flag{stacking_up_http_status_codes_is_fun_2e34303358}**
- > **flag{I think that when many such status codes are accumulated dfa9d355c4 it becomes a lifetime}**

做题很简单，直接现场问GPT能不能构造

- **100**
```HTTP
GET / HTTP/1.1\r\n
Host: yournginxserver.com\r\n
Expect: 100-continue\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 15\r\n\r\n
```

- **200**
```HTTP
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

- **206**
```HTTP
GET /index.html HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=0-3\r\n\r\n
```

- **304**
```HTTP
GET /index.html HTTP/1.1\r\n
Host: example.com\r\n
If-Modified-Since: Tue, 15 Aug 2023 17:04:04 GMT\r\n\r\n
```

- **400**
```HTTP
curl http://baidu.com
```

- **404**
```HTTP
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

- **405**
```HTTP
PUT / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

- **413**
```HTTP
POST / HTTP/1.1 \r\n
Host: example.com \r\n
Content-Type: application/x-www-form-urlencoded \r\n
Content-Length: 13000000000 \r\n
key=value&foo=bar\r\n\r\n
```

- **414**
```HTTP
GET /?query=LONG_PARAMS HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

- **416**
```HTTP
GET /index.html HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=200000-300000\r\n\r\n
```

- **505**
```HTTP
GET /index.html HTTP/9.9\r\n
Host: example.com\r\n\r\n
```

- **412**
```HTTP
GET /index.html HTTP/1.1\r\n
Host: yournginxserver.com\r\n
If-Match: "67890"\r\n\r\n
```

## Docker for Everyone

- > **flag{u5e_r00tless_contalner_7af00e24ac_plz!}**

考察 Docker 提权，参考文章链接为 **https://www.freebuf.com/articles/system/170783.html**

```shell
docker run -it --rm -v /dev:/dev  alpine
cat /dev/shm/flag
```

![f12](/static/posts/Hackergame2023/f12.png)

## 惜字如金 2.0

- > **flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}**

读代码可以发现它的每一个cod_dict 都要判定长度是24，而数一下可以发现长度是23
所以每个都要补全一个字母，通过固定位置必须是 flag{ 和 } 来推定位置

最终推导得到 code_dict 如下，**有二义的地方用 “|” 代替**
```python
    code_dict = []
    code_dict += ['nymeh1niwemflcir}echaet|'] # 0 - 23
    code_dict += ['a3g7}kidgojernoetlsup?h|'] # 24 - 47
    code_dict += ['ulw!|f5soadrhwnrsnstnoeq'] # 48 - 71
    code_dict += ['ct|{l-findiehaai{oveatas'] # 72 - 95
    code_dict += ['ty9kxborszst|guyd?!blm-p'] # 96 - 119
```

![f13](/static/posts/Hackergame2023/f13.png)

## 高频率星球

- > **flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}**

在 linux 上使用 asciinema，并把输出的内容重定向到一个文本文件中，把终端内容里的杂七杂八的字符过滤后得到一个两三万行的 JS 文件，在本地 node.js 环境运行后得到 flag

![f14](/static/posts/Hackergame2023/f14.png)

## 小型大语言模型星球

- > **flag{1-th!nk-Y0u-ARE-Re4llY-real!Y-Sm4Rt}**
- > **flag{YOu-4re-@cCEPt3D-7o-c0ntINue-7He-G4ME}**

直接去 huggingface 找这个模型的训练集，网址链接如下 **https://huggingface.co/datasets/roneneldan/TinyStories/tree/main**，在里面我们可以找包含 **smart** 和 **accepted** 的字串，然后简单枚举得到 flag；后两个 flag 没在训练集里找到，也就没拿到

![f15](/static/posts/Hackergame2023/f15.png)

## 流式星球

- > **flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}**

CV 题，主攻 AI 的如果连这题都没切那可真是太丢脸了(，通过 numpy 操作获取一张张视频帧，最后连成一个视频，很明显是 MyGO 的片段

![f16](/static/posts/Hackergame2023/f16.png)

## 低带宽星球

- > **flag{A1ot0f_t0015_is_available_to_compre55_PNG}**

随便找个压缩软件就能搞定第一问了，第二问不会，寄

## Komm, süsser Flagge

- > **flag{ea5Y_sPl1tt3r_466e82e14b}**
- > **flag{r3s3rv3d_bYtes_998a1267be}**

逐个发送 TCP 的请求字符就可以了，第三问有思路，可惜没时间做了

```python
import socket

def build_request(host, path, data):
    request = f"POST {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += "Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Content-Length: {len(data)}\r\n"
    request += "\r\n"
    request += data
    return request

def send_request(request, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for ch in request:
            s.sendall(ch.encode())
        response = s.recv(4096)
    
    return response.decode()

# Replace with your server details
host = "202.38.93.111"
port = 18080
path = "/"
post_data = "724:MEUCIQDqqtIGTpYx2xPiWy98GoXeQdIDaXltubhoGFzCaUPZ+QIgd079g/lI0R5crJzLXuSQeTDdJun7gvcrcq9BYL8IyJk="

# Build and send the POST request
post_request = build_request(host, path, post_data)
response = send_request(post_request, host, port)

print(response)
```

## 为什么要打开 /flag 😡

- > **flag{nande_ld_preload_yattano_3b9d39741f}**

这题只要用 gcc 的静态编译就可以阻止 LD_PRELAOD 了，第二问可以做可惜没时间看

![f19](/static/posts/Hackergame2023/f19.png)

## 异星歧途

- > **flag{B34WarE_0f_#xp1osi0N_ad18568e94}**

很好玩的游戏，真的，hackergame 过后我都迷上这款游戏了，**像素、策略、塔防、沙盒、城堡**，真的太戳我了！

这题主要注意这么几个东西：
- **重要设备能否稳定运行**
- **物品是如何流动的**
- **微型处理器的逻辑**

最终合法序列是 **10100101110001001000110001110111**

![20](/static/posts/Hackergame2023/f20.png)

---
