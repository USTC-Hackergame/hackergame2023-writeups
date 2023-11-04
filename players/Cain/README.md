## 高频率星球

也许是个非预期解？
asciinema play 执行一个类似git log的过程，会不断清除屏幕上的内容
asciinema cat 保留所有内容但多了其他符合，试着删掉但没匹配对

看录像文件\u0x01b[有很多，搜到是ANSI Escape Codes的ESC(CSI)，看https://en.wikipedia.org/wiki/ANSI_escape_code里面的解释，主要是Some ANSI control sequences (not an exhaustive list) 和 Some popular private sequences两部分

CSI ? 1004h CSI ?1004l...这些和控制台显示模式有关，大概就是切换控制台显示模式的，全删掉；
CSI n J和CSI n K是清屏用的，也删掉

剩下的不动（大概吧，不确定有没有删更多东西），asciinema play一下就能得到完整的文件内容，不带ANSI Escape Codes，也没有限制滚动，复制下来就行

不过文件真的长...长到超过屏幕缓存长度，实际上我分了三次才复制完（或者似乎改一下屏幕缓存长度也行？）

