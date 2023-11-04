# HackerGame 2023 Write up By LiBr

首先本人不是专业ctf选手所以...各位将就看吧x

## 题解

### Hackergame 启动

到页面直接点提交，发现是`?similarity=`的格式

所以直接改成100即可

启动！

### 猫咪小测

第一题在USTC官网找 12

第二题Google一下，会发现一篇知乎的论文摘要 23

第三题...Google一下 CONFIG_TCP_CONG_BBR

第四题...~~因为网上找了篇~~![5e4e476ab1d2537411ed7cfe6bd30a9c](https://cdn.nvme0n1p.dev/picstorage/2023-10-28-23/10-28200019.png)

遂一片一片试 ECOOP

答案是 `12,23,CONFIG_TCP_CONG_BBR,ECOOP`

### 更深更暗

F12 即可

### 旅行照片

首先根据信息大学在东京，诺奖得主也是东京大学

故搜索东京大学理学部诺贝尔奖得主

找到年龄最小的 梶田隆章 

看维基百科中“东京大学宇宙射线研究所”->ICRR 

然后旁边有几个景点，喷泉、彩虹大桥、上野站（坐电车

猜测是东京大学

东京大学周围的湖/水池有几个

![image-20231029164456135](https://cdn.nvme0n1p.dev/picstorage/2023-10-29-23/10-29164456.png)

可以找到喷泉（谷歌街景）->上野公园，对比一下差不多（2014年的街景

![image-20231029164432300](https://cdn.nvme0n1p.dev/picstorage/2023-10-29-23/10-29164432.png)

上述信息直接得出学校为东京大学

喷泉所在位置是上野公園  大噴水

Google  搜索6-8月内容发现有一个"全国梅酒まつりin東京2023"

![image-20231030075749788](https://cdn.nvme0n1p.dev/picstorage/2023-10-30-23/10-30075751.png)

去社交媒体搜素也差不多

![image-20231030080446066](https://cdn.nvme0n1p.dev/picstorage/2023-10-30-23/10-30080446.png)

所以参观时间在8.10-13号 第一问试一试就拿到了

官网上可以找到志愿者的页面中的问卷编号S495584522

对面是东京国立博物馆，查询价格（这里需要看底下一句话）常设展免费 答案0

3-4的flag拿到了

时效性问题去搜索twitter-熊猫——

![image-20231030082241366](https://cdn.nvme0n1p.dev/picstorage/2023-10-30-23/10-30082241.png)

由于最后那张马里奥的图片丢到Google里搜索只有涩谷的任天堂总店有

所以我们下车的站点是涩谷站。搜索涩谷 3D 动物可以看到一些新闻报道是秋田犬。

第五题由于拉面店学长的脖子上挂了个STATPHYS28

于是搜索，找到https://statphys28.org/发现集合地点是安田讲堂

答案：`2023-08-10,ICRR,S495584522,0,安田讲堂,熊猫-秋田犬`

### 赛博井字棋

两种办法：1.后端暴力填格子

2.前端改动setMove抢机器人的格子

两边都是最优解所以直接下只能平局/输

### 奶奶的睡前flag故事

推测是lsb隐写但是扔到stegsolve并没有找到

然后用pngcheck查看之后发现在`IEND`块之后还有内容。查看发现后面也是IDAT块，但是前面的IDAT是zlib包后面不是，重组之后也不是

后面查到https://zh.wikipedia.org/wiki/ACropalypse，发现是pixel截图的漏洞。

故可以直接使用某工具https://acropalypse.app/

### 组委会模拟器

F12然后一行搞定 `setInterval(()=>{document.querySelectorAll(".fakeqq-message__bubble").forEach(u=>{if(/hack\[.*?\]/.test(u.innerText))u.click()})},500)`

### 虫

搜索ISS发送图片知道是SSTV信号

网上随便找个Decoder就好了

图片如下

![image-20231028200416022](https://cdn.nvme0n1p.dev/picstorage/2023-10-28-23/10-28200416.png)

### JSON ⊂ YAML?

网上查 json yaml可以找到一篇[stackoverflow](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)

遂构造两个`{"1":12345e999}` `{"1":1,"1":2}`

### Git？Git！

直接在Git文件夹里找文件就行

每个`.git/object`中的文件，直接`find ./.git/objects -type f | sed 's,^./.git/objects/,,' | tr -d '/' | grep -v idx | grep -v pack | xargs -I {} git cat-file -p {} | grep flag `即可（写得有点丑凑合看吧

![image-20231028230804383](https://cdn.nvme0n1p.dev/picstorage/2023-10-28-23/10-28230804.png)

### HTTP集邮册

收集了12个

#### 空状态

关于状态码的定义：在**http/https**请求中需要有状态码....

那如果不是http请求呢...?

```
GET /\r\n
```
还有个忘掉了（

#### 404

```
GET /404 HTTP/1.1\r\n
Host: example.com\r\n
\r\n
```

#### 200

```
GET / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 206

```
GET / HTTP/1.1\r\n
Range: bytes=0-0\r\n
Host: example.com\r\n\r\n
```

#### 100

```
GET / HTTP/1.1\r\n
Expect: 100-continue\r\n
Host: example.com\r\n\r\n
```

#### 416

```
GET / HTTP/1.1\r\n
Range:bytes=0--1\r\n
Host: example.com\r\n\r\n
```

#### 505

```
GET / HTTP/3\r\n
Host: example.com\r\n\r\n
```

### 405

```
POST / HTTP/1.1\r\n
Host: example.com\r\n\r\n
```

#### 412

```
GET / HTTP/1.1\r\n
If-Match: 123\r\n
Host: example.com\r\n\r\n
```

#### 414

```js
$("textarea").value=`GET /${"a".repeat(100000)} HTTP/1.1\r\n
Host: example.com\r\n
\r\n`
```

#### 304

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
If-None-Match: "64dbafc8-267"\r\n
\r\n
```

#### 413

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 100000000\r\n
\r\n
```

### Docker for Everyone

喜闻乐见的权限问题（docker中可以直接得到root权限）

`docker run -it -e PUID=0 -e PGID=0 -e MASK=22 -v /flag:/flag --rm alpine`

![image-20231028201000926](https://cdn.nvme0n1p.dev/picstorage/2023-10-28-23/10-28201001.png)

### 高频率星球

`asciinema`是有查看功能的

故`asciinema cat ./file.rec > 1.txt`

然后删掉某些字符即可

![image-20231102213408229](https://cdn.nvme0n1p.dev/picstorage/2023-11-02-23/11-02213408.png)

### 小型大语言星球

第一问简单, the smart boy asks,are you clever

第二问查了一些资料找到了提示词攻击🤔LLM-attack（

但是代码力不够没有写出来

### 流式星球

照着给的代码反过来写一个就好了

麻烦的点是图像的拉伸问题

一个分辨率一个分辨率试就好了

最后视频分辨率设成（427,253）的时候刚刚好

最后好评BanG Dream

![e4cceae7ae93d7e55c23f4da4a3d5595](https://cdn.nvme0n1p.dev/picstorage/2023-10-29-23/10-29100557.png)

### 为什么要打开 /flag 😡

呵呵舔狗（为什么骂我呜呜

#### LD_PRELOAD

gcc会将文件编译成动态库

然后交由ld执行，然后设置的LD_PRELOAD就会加载

如果我静态编译呢

```c
#include<stdio.h>
#include<stdlib.h>
int main(){
    freopen("/flag","r",stdin);
    char flag[1100];
    fgets(flag,1100,stdin);
    printf("%s",flag);
}
```

编译命令`gcc 1.cpp -o 1 -static`

#### seccomp

看沙箱的文档https://crates.io/crates/greenhook发现~~最后贴心的列出了几种attack方式~~

![image-20231102213710056](https://cdn.nvme0n1p.dev/picstorage/2023-11-02-23/11-02213710.png)

tictou攻击中有一些问题，他syscall的函数限制了很多，然后不太好直接使用。

最后想法是用open函数，然后不停修改目标的参数最后得到某次成功。

### 异星崛起

大概意思是让四个模块都输出

第一组：点开微型处理器即可10100101

![image-20231103223843703](https://cdn.nvme0n1p.dev/picstorage/2023-11-03-23/11-03223843.png)

第二组：同样是逻辑处理器，number是一个8位二进制数，然后并且第1和第6个开关必须开，也就是对应二进制位必须1。枚举得到 $14^2=(11000100)_2$。于是开关为 11000100。

第三组：目标是启动反应堆，需要冷却水然后启动反应堆故开关为10001100（先后面两个再前面一个

第四组：电路图，倒推即可01110111

