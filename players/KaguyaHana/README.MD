# Hackergame 2023
> Scores
> AI：300 ， binary：450 ， general：2450 ， math：400 ， web：1000， Total：4600

Only you need is:
  Chrome 118.0.5993.118 (Official Build) (64-bit)

  Google.com

  ChatGPT 3.5
 
## Hackergame 启动
Submit
[提交](https://cnhktrz3k5nc.hack-challenge.lug.ustc.edu.cn:13202/?similarity=100)

## 猫咪小测
### 及格喵
1.Google Prompt: `中国科学技术大学西区图书馆`

[12楼	外文书库	引进版权外文图书	外借及室内阅览	63607942](https://lib.ustc.edu.cn/%e6%9c%ac%e9%a6%86%e6%a6%82%e5%86%b5/%e9%a6%86%e8%97%8f%e5%88%86%e5%b8%83/)

2.Google Prompt: `Upper Limit on the Number Density of Chickens in the Universe`

[We find the most restrictive upper limit from the domains considered to be 10²³ pc-³](https://arxiv.org/abs/2303.17626)
### 满分喵
3.Google Prompt: `TCP BBR CONFIG_`

[您应该安装 Linux 内核版本 4.9 或更高版本，并使用这些选项进行编译（作为模块或内置于其中）：CONFIG_TCP_CONG_BBR](https://cn.linux-console.net/?p=558)

4.Google Prompt: `Mypy halting problem`

[Supplementary Material Software (ECOOP 2023 Artifact Evaluation approved artifact)](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)

## 更深更暗
Inspect Elements and Search for `flag`

```
                               /
                               \
                               |
                             __|__
                            |     \
                                    /
     ____  _________________|___ ___\__________/ ____
    <   /                                            \____________  |
     /         flag{T1t@n_10644721419d355f3cd57796f580ec16}       \ (_)
~~~~~~     O       O       O                                       >=)~~~~~~~
       \_______/ ____________\  /_________________________________/ (_)
```

## 旅行照片 3.0
Google Prompt
Photo 1：`Inventas vitam iuvat excoluisse per artes` `M.KOSHIBA`

Photo 2：`STATPHYS28` `一信ラーメン`

Photo 3：`公园` `喷泉` `帐篷`

Photo 4：`Nintendo`
### 神秘奖牌
1.Google Prompt: `STATPHYS28`

[Date August 7th-11th, 2023](https://statphys28.org/)

2.Google Prompt: `Tokyo ` `Nobel Prize`

[Takaaki Kajita was born in 1959](https://www.s.u-tokyo.ac.jp/en/gallery/nobelprize/)
### 这是什么活动？
3.Google Prompt: `上野公園` `STAFF大募集`

[https://ws.formzu.net/dist/S495584522/](https://umeshu-matsuri.jp/tokyo_staff/)

4.Google Prompt: `东京国立博物馆`

[残障人士及陪伴者一名免费/中小学生、高中生或未满18周岁以及满70周岁以上者，均可免费参观综合文化展（常设展](https://www.tnm.jp/modules/r_free_page/index.php?id=113)
### 后会有期，学长！
5.Google Prompt: `STATPHYS28` `Tokyo`

[35°42'48.7"N 139°45'44.1"E](https://goo.gl/maps/pbhL4pAKVJgG115FA)

6(a).Google Prompt: `ボタン＆カフリンクス` `上野駅`

[PANDA panda LIFE***イベント](ttps://plaza.rakuten.co.jp/ayumilife/diary/202308110000/)

(b).Google Prompt:`上野駅``動物` `3D`

[可爱立体「3D秋田犬」广告牌](https://wow-japan.com/news-flash-shibuya-3d-akida-dog-ads/)

## 赛博井字棋
Inspect Elements `clickedCell` found in`script.js`
```
function clickedCell(cell) {
  var x = cell.id.split("")[0];
  var y = cell.id.split("")[1];

  asyncQueue.addTask(async () => {
    await setMove(x, y)
      .then((response) => response.json()) // 解析响应为 JSON
      .then((data) => {
        renderBoard(data); // 渲染棋盘
      });
  }, null);
}
```
Click and `setMove()` in Console and Click to win

## 奶奶的睡前 flag 故事
Google Prompt:`Google Pixel` `screenshot` `CVE`

[Hack for Google Pixel](https://acropalypse.app/)

## 组委会模拟器
ChatGPT Prompt:
```
写一个js脚本自动点击页面上包含hack[...]的字符串


每年比赛，组委会的一项重要工作就是时刻盯着群，并且撤回其中有 flag 的消息。今年因为人手紧张，组委会的某名同学将这项工作外包给了你，你需要连续审查 1000 条消息，准确无误地撤回其中所有含 flag 的消息，并且不撤回任何不含 flag 的消息。

本题中，你需要撤回的 "flag" 的格式为 hack[...]，其中方括号内均为小写英文字母，点击消息即可撤回。你需要在 3 秒内撤回消息，否则撤回操作将失败。在全部消息显示完成后等待几秒，如果你撤回的消息完全正确（撤回了全部需要撤回的消息，并且未将不需要撤回的消息撤回），就能获得本题真正的 flag

这是一个网页，你需要点击信息以撤回

消息是连续不断即时发送的，你需要对每一条进行检查并删除包含hack字符的消息

我想在node中使用

我是说，chrome的console

消息元素是fakeqq-message__content，而且你需要点击被选中的消息而不是remove

一条消息的结构类似<div class="fakeqq-message left-chat"><div class="fakeqq-message__avatar"><span class="fakeqq-message__text-avatar">j</span></div><div class="fakeqq-message__content"><div class="fakeqq-message__name">jgwzZc0AOXaUWvac</div><div class="fakeqq-message__bubble"><div class="fakeqq-message__bubble-arrow"></div><span>这道题 flag 是hack[rutklo]</span></div></div></div>
```
Save-Copy-Paste to run

## 虫
ChatGPT Prompt:
```
我可以用什么软件接收ISS通过无线信道传输图片的方式
```

## JSON ⊂ YAML?
Google Prompt:`JSON ⊂ YAML`

[YAML 1.2 won't save you](https://john-millikin.com/json-is-not-a-yaml-subset)
### JSON ⊄ YAML 1.1
`{"a":1e2}`
### JSON ⊄ YAML 1.2
`{"a":1,"a":2}`

## Git? Git!
ChatGPT Prompt:
```
在Git中撤销更改
```
Save-Copy-Paste to run

## HTTP 集邮册
Google Prompt: `HTTP Code`
### 5 种状态码
ChatGPT Prompt:
```
请你写一个GET样例来获得HTTP[100, 200, 206, 304, 400, 404, 405, 412, 413, 414, 416, 505]错误
```
### 没有状态……哈？
Just delete last `\r\n`
### 12 种状态码
Just continue asking ChatGPT

## Docker for Everyone
Google Prompt：`docker提权`

[Privileged 特权模式容器逃逸](https://wiki.teamssix.com/CloudNative/Docker/docker-privileged-escape.html)

### 惜字如金 2.0
ChatGPT Prompt:
```
惜字如金化指的是将一串文本中的部分字符删除，从而形成另一串文本的过程。该标准针对的是文本中所有由 52 个拉丁字母连续排布形成的序列，在下文中统称为「单词」。一个单词中除「AEIOUaeiou」外的 42 个字母被称作「辅音字母」。整个惜字如金化的过程按照以下两条原则对文本中的每个单词进行操作：

第一原则（又称 creat 原则）：如单词最后一个字母为「e」或「E」，且该字母的上一个字母为辅音字母，则该字母予以删除。
第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。
容易证明惜字如金化操作是幂等的：惜字如金化多次和惜字如金化一次的结果相同。

附件包括了一个用于打印本题目 flag 的程序，且已经经过惜字如金化处理。你需要做的就是得到程序的执行结果。


内容如下：

根据惜字如金化算法反推源代码
```
It's easy to delete `check_equals()` function，and add `e` to every line.

Then change the `code_dict`(duplicate any consonant and delete `e`) to make sure that you got a output like:`flag{`

### 🪐 高频率星球
Google Prompt:`记录终端会话`
```
asciinema play asciinema_restore.rec
script recording.txt
```
recording.txt is easier to work out

###  🪐 小型大语言模型星球
## You Are Smart
`"I am smart", I said. The girl replies, "Yes,`
##  Accepted
`dju`

### 🪐 流式星球
ChatGPT Prompt:
```
解释以下代码：

请你写一段代码把video.bin 还原成MP4
```

### 🪐 低带宽星球
## 小试牛刀
Covert to WEBP

### Komm, süsser Flagge
## 我的 POST
ChatGPT Prompt:
```
写一个python程序，将POST 请求分为 'P' 和 其他部分 发送到http://202.38.93.111:18080
```
## 我的 P
ChatGPT Prompt:
```
写一个python程序，将POST 请求分为 'P' 和 其他部分 发送到http://202.38.93.111:18081
```

### 为什么要打开 /flag 😡
## LD_PRELOAD, love!
ChatGPT Prompt:
```
用静态链接绕开LD_PRELOAD写一个读取并打印example的程序
```

### 异星歧途
Group1:Randomly click the switch

Group2:Randomly click the switch(Last one enable reactor)

Group3:Randomly click the switch(3rd one disable reactor)

Group4:Randomly click the switch(to enable Incinerator)

### 小 Z 的谜题
## Easy
It equals another question: Put 16 patterns into a 5*5*5 cube.Your INPUT is 16 `x1 x2 y1 y2 z1 z2`


>See also https://椛.みんな/20231104-hack
