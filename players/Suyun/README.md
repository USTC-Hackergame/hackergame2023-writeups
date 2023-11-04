# USTC Hackergame 2023 Writeup

## Hackergame 启动

经典签到题。随便录制一段音频，点击「提交」可以发现 URL 后多了形似 `?similarity=76.7409851460542` 的一段 param。根据提示中的「相似度大于 99.9% 才能拿到 flag」，把 param 改成 `?similarity=100` 就能拿到 flag 了。

~~Hackergame，启动！~~

## 猫咪小测

经典信息检索题。

> 1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？

根据 [西区图书馆简介 | 中国科学技术大学图书馆](https://lib.ustc.edu.cn/%E6%9C%AC%E9%A6%86%E6%A6%82%E5%86%B5/%E5%9B%BE%E4%B9%A6%E9%A6%86%E6%A6%82%E5%86%B5%E5%85%B6%E4%BB%96%E6%96%87%E6%A1%A3/%E8%A5%BF%E5%8C%BA%E5%9B%BE%E4%B9%A6%E9%A6%86%E7%AE%80%E4%BB%8B/)，外文书库在 12 层，所以答案为 12。

> 2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？

翻译成英文之后搜索，可以在 arXiv 上找到 [原论文](https://arxiv.org/abs/2303.17626)。答案为 23。

> 3. 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？

搜索「tcp bbr linux kernel」可以找到 [这篇文章](https://www.cyberciti.biz/cloud-computing/increase-your-linux-server-internet-speed-with-tcp-bbr-congestion-control/)，答案为 `CONFIG_TCP_CONG_BBR`。

> 4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？

搜索「mypy infinite loop」可以找到 [原论文](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)。答案为 ECOOP。

~~今年居然没有需要对服务器进行 CC 攻击的题了，我宣布这个 Hackergame 变质了。~~

## 更深更暗

打开网页，可以看到一闪而过的 flag。审计 `static/main.js`，发现了以下代码：

```js
async function getFlag(token) {
    // Generate the flag based on user's token
    let hash = CryptoJS.SHA256(`dEEper_@nd_d@rKer_${token}`).toString();
    return `flag{T1t@n_${hash.slice(0, 32)}}`;
}
```

然后把这个函数丢进 Console 里，带上 token 跑一下就出来了。

~~后来想到其实直接录屏就行了。~~

## 旅行照片 3.0

这是咱第一次做出旅行照片，开心！

> 1、你还记得与学长见面这天是哪一天吗？（格式：yyyy-mm-dd）

拉面店那张图左一，学长戴着的胸牌带子上写着 STATPHYS28。经过查询，这是一场学术会议的名字，这场学术会议的日期是 2023-08-07 到 2023-08-11。都试一遍就行了。最后试出来是 2023-08-10。~~原来 CC 攻击在这里。~~

> 2、在学校该展厅展示的所有同种金色奖牌的得主中，出生最晚者获奖时所在的研究所缩写是什么？

根据文中的上野站和上一道题中的 STATPHYS28 猜测学校为东京大学。

根据奖牌边缘的文字得出这是诺贝尔奖牌，根据人名（M. KOSHIBA）得出这是诺贝尔物理学奖奖牌（后来发现也可以从奖牌的图案上看出来，不同学科的诺贝尔奖牌图案是不同的）。在维基百科上找到 [诺贝尔物理学奖得主列表](https://zh.wikipedia.org/zh-cn/%E8%AF%BA%E8%B4%9D%E5%B0%94%E7%89%A9%E7%90%86%E5%AD%A6%E5%A5%96%E5%BE%97%E4%B8%BB%E5%88%97%E8%A1%A8)，再筛选所有国家为日本并与东京大学有关的。其中出生最晚者为 [梶田隆章](https://zh.wikipedia.org/zh-cn/%E6%A2%B6%E7%94%B0%E9%9A%86%E7%AB%A0)，所在的研究所为东京大学宇宙射线研究所（ICRR）。

> 3、帐篷中活动招募志愿者时用于收集报名信息的在线问卷的编号（以字母 S 开头后接数字）是多少？

根据地图可以得知东京大学附近的博物馆为东京国立博物馆。对面的喷泉为上野公园的喷泉广场。搜索 2023 年 8 月 10 日上野公园的活动。可以找到 [全國梅酒祭 in 東京 2023](https://hk.wamazing.com/media/article/a-3054/)。在其官网上可以找到 [招募 STAFF 的新闻](https://umeshu-matsuri.jp/tokyo_staff/)，得到问卷链接为 [https://ws.formzu.net/dist/S495584522/]()，所以答案为 S495584522。

> 4、学长购买自己的博物馆门票时，花费了多少日元？

根据东京博物馆官网的 [参观指南](https://www.tnm.jp/modules/r_free_page/index.php?id=113&lang=zh_cn)，成人的门票为 1000 日元 / 人，大学生的门票为 500 元 / 人。但是这里 1000 和 500 都不会，最后猜了个 0 居然对了。但是官网只说了「中小学生、高中生或未满 18 周岁以及满 70 周岁以上者，均可免费参观综合文化展」，也许还有咱没找到的其他信息？

> 5、学长当天晚上需要在哪栋标志性建筑物的附近集合呢？（请用简体中文回答，四个汉字）

在官网上找到 STATPHYS28 的 [Program Timetable](https://statphys28.org/programtt.html)，可以得到 8 月 10 日晚上是的安排是 Banquet（宴会）。再在官网上找到 [Banquet](https://statphys28.org/banquet.html)，在第二个 Meeting Point 栏中可以找到集合地点为 Yasuda Auditorium，中文为安田讲堂。

> 6、进站时，你在 JR 上野站中央检票口外看到「ボタン＆カフリンクス」活动正在销售动物周边商品，该活动张贴的粉色背景海报上是什么动物（记作 A，两个汉字）？ 在出站处附近建筑的屋顶广告牌上，每小时都会顽皮出现的那只 3D 动物是什么品种？（记作 B，三个汉字）？（格式：A-B）

A：搜索「ボタン&カフリンクス 上野」，找到了 [这个 Instagram 帖子](https://www.instagram.com/p/Cvrw425vK_n/)，盲猜一个熊猫。之后也在 [另一个 Instagram 帖子](https://www.instagram.com/p/CvgmlEYv1Dm/) 上找到了题目中提到的海报。

B：搜索「上野駅 看板 毎時 3d」，找到了 [这条新闻](https://www.sogohodo.co.jp/special_event/17553/)。虽然这条新闻看起来和上野站没什么关系，但是我直接盲猜一个秋田犬居然对了。

## 赛博井字棋

第一反应是去找井字棋有没有先手必胜的策略。然而找到的每一篇文章都说有，但是就没有一篇文章里面说的策略是可行的。

最后还是选择嗯审代码。发现每下一步棋都会调用 `setMove` 方法。

```js
async function setMove(x, y) {
  if (board[x][y] != 0) {
    return;
  }
  if (frozen) {
    return;
  }
  let url = window.location.href; // 获取当前 URL
  let data = { x: x, y: y }; // 设置要发送的数据
  return fetch(url, {
    method: "POST", // 设置方法为 POST
    headers: {
      "Content-Type": "application/json", // 设置内容类型为 JSON
    },
    body: JSON.stringify(data), // 将数据转换为 JSON 格式
  }).catch(errorHandler);
}
```

遂在 Console 中覆盖这个方法，把判断 `board[x][y] != 0` 的逻辑删去。这样就可以覆盖 AI 已经下过的位置了。

## 奶奶的睡前 flag 故事

从「**连系统都没心思升级**」推测是 CVE-2023-21036，即 Pixel 等的截图工具在裁剪截图时并不会真正删除被裁剪掉的部分。刚好前段时间打的 [山河 CTF](http://shctf.club:8000/) 也出了一题差不多的（不过那道题的背景是 Windows 的截图工具），我直接翻出了 [Acropalypse-Multi-Tool](https://github.com/frankthetank-music/Acropalypse-Multi-Tool)，把图片丢进去就出了。

## 组委会模拟器

写一点 JS 实现不停地读取最后一条消息，如果包含 `hack[` 就 click。然后在页面加载的时候飞快地按下 F12 把写的 JS 粘贴进 Console 里就行了。可能需要多试几次。

```js
const interval = setInterval(() => {
    const container = document.getElementsByClassName('fakeqq-container')[0];

    if (container.childElementCount >= 1000) {
        clearInterval(interval);
    }

    const lastMsg = container.lastElementChild;

    if (lastMsg.innerHTML.includes('hack[')) {
        container.lastElementChild.lastElementChild.lastElementChild.lastElementChild.click();
    }
}, 0);
```

值得一提的是，我刚开始写的时候用的是 `while(true)`，然后我的浏览器就 OOM 了。问了 ChatGPT 才知道应该用 `setInterval`。

## 虫

一眼 SSTV。不知道为什么在 Linux 下用 QSSTV 跑不出来。在 Windows 下，先安装 [VB-CABLE Driver](https://vb-audio.com/Cable/) 将声音输出重定向为声音输入。再播放音频并使用 [RX-SSTV](https://www.qsl.net/on6mu/rxsstv.htm) 解析。

## JSON ⊂ YAML?

### JSON ⊄ YAML 1.1

根据 [JSON is not a YAML subset](https://john-millikin.com/json-is-not-a-yaml-subset) 这篇文章，JSON 在解析形如 `1e5` 的科学计数法表示的数字时，会转换为浮点数。而 YAML 1.1 在解析时会转换为字符串。所以 `1e5` 就是一个可行的答案。~~没错，单独一个数字或字符串也是合法的 JSON 和 YAML。~~

同时，根据 [这个 Stack Overflow 回答](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)，JSON 和 YAML 都支持用 `\u` 表示 UTF-16 字符串，但是 PyYAML 似乎并没有实现这个功能，所以 `"\uD834\uDD1E"` 也是一个可行的答案。~~不知道这算不算非预期？~~

### JSON ⊄ YAML 1.2

> 小 Z 笑了：「别提 YAML 1.2 了，它遇到合法的 JSON 都有可能报错。」

根据 [JSON is not a YAML subset | Lobsters](https://lobste.rs/s/equcp2/json_is_not_yaml_subset)，[YAML 1.2.1 的文档的 1.3 章节](https://yaml.org/spec/1.2.1/#id2759572) 提到了 YAML 与 JSON 的区别。

> JSON's [RFC4627](http://www.ietf.org/rfc/rfc4627.txt) requires that [mappings](https://yaml.org/spec/1.2.1/#mapping//) [keys](https://yaml.org/spec/1.2.1/#key//) merely “SHOULD” be [unique](https://yaml.org/spec/1.2.1/#equality//), while YAML insists they “MUST” be. Technically, YAML therefore complies with the JSON spec, choosing to treat duplicates as an error. In practice, since JSON is silent on the semantics of such duplicates, the only portable JSON files are those with unique keys, which are therefore valid YAML files.

也就是说，JSON 不强制要求 key 是唯一的，但是 YAML 强制要求。所以 `{"a":1,"a":2}` 是一个可行的答案。

同时，虽然 [YAML 1.2.2](https://yaml.org/spec/1.2.2/) 的文档删去了其与 JSON 的区别这一章，但是依然在 3.2.1.1 节提到了 key 需要是唯一的。

## Git? Git!

根据 [这个 Stack Overflow 问题](https://stackoverflow.com/questions/2510276/how-do-i-undo-git-reset)，可以使用 `git reflog` 查看修改记录。

```
ea49f0c (HEAD -> main) HEAD@{0}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD~
505e1a3 HEAD@{2}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{3}: clone: from https://github.com/dair-ai/ML-Course-Notes.git
```

然后我们 `git reset HEAD@{2}` 回滚到上一次 reset 前的状态，再 `git checkout .` 恢复文件。就可以在 `README.md` 中看到 flag 了。

~~其实我是直接 `find . -exec strings {} \; | grep flag` 的。~~

## HTTP 集邮册

咱好菜啊，只收集了 7 种状态码。

- 200：点击就送。

- 400：随便构造一个不合法的请求。

- 404：随便访问一个不存在的路由。

- 405：把 `GET` 改成 `POST` 或者别的不允许的请求类型。

- 413：添加一个数字比较大但是不能太大（不然会 400）的 `Content-Length` 头，~~比如我用的是 `1145141919810`~~。

- 414：把路由的长度变得长长长长长。

- 505：把 `HTTP/1.1` 改成不支持的 HTTP 版本，比如 `HTTP/2`。

至于无状态码，咱在这里卡了很久。突然咱灵光一闪（大雾），想到 Nginx 会不会支持 HTTP 以外的协议比如 Gopher。然后咱在搜索的时候看到了 [用 nginx 建立 Gopher 网站](https://lantian.pub/article/modify-website/serve-gopher-with-nginx.lantian/) 这篇文章，其中有这么一段：

> 好消息是，在 HTTP/1.0 之前，还有一版极简的协议 HTTP/0.9，就一行：
> 
> ```
> GET /test.php
> Hello World
> ```
> 
> 客户端只发送了上面的 GET 一行。在发送换行符后，nginx 就直接把响应数据 `Hello World` 发过来了，不用按两次回车，没有带上 200 状态码或者别的响应头，还不忘关闭连接。

然后咱尝试了一下 `GET /\r\n`，就这样歪打正着地做出来了。

## Docker for Everyone

做这道题时咱正在准备打某 CTF，所以思路非常打 CTF 打的。

看到这个题，咱想到了 CTF 中的一个经典问题——SUID 提权：因为某个程序具有 SUID 权限，所以无论什么用户调用这个程序，这个程序都会以它的属主的权限运行。在这种情况下，如果一个程序的属主是 root，同时又具有 SUID 权限，那么一个普通用户就有可能可以借助这个程序，启动一个具有 root 权限的其他程序（比如 shell）或操作只有 root 用户能操作的文件。

这看上去和这道题有些相似的地方，所以为什么不试一试呢？刚好，[GTFOBins](https://gtfobins.github.io/) 整理了如何通过各种程序启动 shell。让我们搜索一下  docker：

```shellsession
$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

试了一下，发现可行，甚至可以直接 `cat /flag`。

这段命令的含义还是比较显而易见的：将 `/` 挂载到 `/mnt`，启动一个 `alpine` 容器，再 `chroot` 到 `/mnt`。大概是因为 Docker 的守护进程是以 root 运行的，所以整个根目录对 Docker 来说是有权限的。同时，因为这段命令使用了 `chroot`，所以甚至无意中避开了其他 writeup 中出现的软链接问题。

## 惜字如金 2.0

这道题我几乎是瞎猜出来的。

打开代码，先删掉所有 `check_equal` 相关的东西，再把 `__nam__` 改成 `__name__`，运行，发现报了 `IndexError: string index out of range`。根据 `check_equals(set(len(s) for s in cod_dict), {24})` 猜测 `cod_dict` 每一行的长度都应该是 24，而代码中每一行的长度只有 23。

然后就是猜的环节了。先往 `cod_dict` 的每一行末尾都加 `e`，此时输出为 `5laulyoufeepr3cvees3df7weparsn3sfr1gwn!}`。

猜测前五位为 `flag{`。故：

- 第一位应该为 `f` 却为 `5`，且 index 为 51（第三行），故将 `ulw!f5soadrhwnrsnstnoeq` 改为 `ulwe!f5soadrhwnrsnstnoeq`。

- 第四位应该为 `g` 却为 `u`，且 index 为 109（第五行），故将 `ty9kxborszstguyd?!blm-p` 改为 `ty9kxborszsteguyd?!blm-p`。

- 第五为应该为 `{` 却为 `l`，且 index 为 75（第四行），故将 `ct{l-findiehaai{oveatas` 改为 `cte{l-findiehaai{oveatas`。

这个时候输出为 `flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}`，感觉非常科学。

## 🪐 高频率星球

用 `asciinema cat` 获得输出，并重定向到一个文件中。再用 VS Code 等文本编辑器（批量）删除各种控制字符，最后运行就行了。

## 🪐 小型大语言模型星球

可以发现这是一个续写句子的大模型。

### You Are Smart

直接问 `Am I smart?`。

## 🪐 流式星球

首先，我让 ChatGPT 给我写了一个把题目给的文件的某一帧转成图片的脚本。

```python
from PIL import Image

with open('video.bin', 'rb') as file:
    binary_data = file.read()

width = 640
height = 480
frame_index = 0

img = Image.new('RGB', (width, height))

pixels = []
for i in range(frame_index * width * height * 3, (frame_index + 1) * width * height * 3, 3):
    r = binary_data[i]
    g = binary_data[i + 1]
    b = binary_data[i + 2]
    pixels.append((r, g, b))

img.putdata(pixels)

img.save('video.png')

```

640 × 480 是 ChatGPT 生成的默认视频分辨率，但是意外地科学。

![](video1.png)

然后我试着把 `frame_index` 猜了个 `100`。flag 似乎出现了！

![](video2.png)

但是这……前面还能猜出来，最后几位就真的看不出来了。

但是毕竟已经看到 MyGo_official 和 bilibili，~~以及 flag 里的 haruhikage~~，所以我试着去找了原视频，是 BV19F411y7FA。这是个竖版视频，所以我试着把 `width` 改为 `640 // 3`，`height` 改成 `480 * 2`，对应的，把 `frame_index` 改成了 `150`。

![](video3.png)

这下清清楚楚了。但是不知道为什么 `haruhikage` 后面少了个 `-`。

## 低带宽星球

### 小试牛刀

直接用 [TinyPNG](https://tinypng.com/) 就行了。

## Komm, süsser Flagge

### 我的 POST

搜索「iptables bm」可以找到 [这个 Server Fault 问题](https://serverfault.com/questions/1141991/what-is-the-difference-bm-and-kmp-algorithms-in-iptables-string-search)。它指出了 iptables 的 BM 字符串匹配算法似乎在处理「multiple blocks」上存在问题。所以，我盲猜了一下：只需要把 TCP 包分包发出，使得 `POST` 不连续出现，就可以绕过这个 iptables 规则的字符串匹配了。

求助 ChatGPT 之后，我写出了以下代码并成功获得了 flag：

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('202.38.93.111', 18080)
sock.connect(server_address)

message = b'POST / HTTP/1.1\r\nHost: 202.38.93.111:18080\r\nContent-Length: 101\r\n\r\n' + token

first = message[:1]
second = message[1:]

sock.sendall(first)
sock.sendall(second)

data = sock.recv(1024)
print(data)

sock.close()
```

### 我的 P

直接把第一小问的代码的端口改一下就能获得第二小问的 flag。非预期？

## 为什么要打开 /flag 😡

### LD_PRELOAD, love!

把题目解包，发现似乎是写个了一个 so 文件覆盖掉了 `fopen` 之类的函数。所以只要上传静态编译的二进制文件就可以了。用 Go 或者 Zig 这种不依赖 libc 的语言应该也可以。

顺便关于读取 `/flag` 的二进制文件，我本来的想法是直接 `system("cat /flag");` 的，但是这个环境似乎没有 cat。所以只能用 `fopen`、`fread`、`fwrite` 一条龙了。
