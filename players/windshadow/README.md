---
layout: post
title: Hackgame 2023题解
date: 2023-11-04
tags: ["CTF","Hackergame"]
---

# 本题解导出自[我的博客](https://blog.fyz666.xyz/blog/8773/)

## Hackergame 启动

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"大声喊出 Hackergame 启动，开始今年的冒险！"} /-->

<!-- wp:paragraph -->

解法1：直接点击提交，发现URL多出参数`?similarity=`，手动补成`?similarity=114514`再访问即可。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

解法2：多喊几遍Hackergame 启动！让相似度达到100%。

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8775,"width":492,"height":352,"sizeSlug":"large"} -->
![](images/image.png)
<!-- /wp:image -->

<!-- wp:block-lab/introduce {"text":"flag{We1ComE-70-hACkEr9aME-4nD-enjoY-h4Ck!nG-z0Z3}"} /-->

<!-- wp:paragraph -->

<s>虽然不玩原神，但还是被洗脑了。。。</s>

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 猫咪小测

<!-- /wp:heading -->

<!-- wp:block-lab/ordered-list {"text":"想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？（30 分）\n提示：是一个非负整数。\n\n今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？（30 分）\n提示：是一个非负整数。\n\n为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时应该配置好哪一条内核选项？（20 分）\n提示：输入格式为 CONFIG_XXXXX，如 CONFIG_SCHED_SMT。\n\n🥒🥒🥒：「我......从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 MyPY mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？（20 分）\n提示：会议的大写英文简称，比如 ISCA、CCS、ICML。\n"} /-->

<!-- wp:paragraph -->

由于HG的问答题没有提交冷却限制，因此1、2问直接爆破。答案分别为12、23。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第三问直接塞入ChatGPT：

<!-- /wp:paragraph -->

<!-- wp:quote -->
> 为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时，您应该配置 CONFIG_TCP_CONG_BBR 选项。
<!-- /wp:quote -->

<!-- wp:paragraph -->

一开始搜不到第四题，然后发现相关的会议好像也就那么几个，直接枚举得到ECOOP。

<!-- /wp:paragraph -->

<!-- wp:block-lab/introduce {"text":"🎉🎉🎉flag{wE1COME-TO-4ttEND-th3-NEKO-ex@M-zo23}🎉🎉🎉\n🎉🎉🎉flag{re@l-M4sT3r-oF-thE-nek0-ex4M-IN-ustc}🎉🎉🎉"} /-->

<!-- wp:heading -->

## 更深更暗

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"小 E 正在收看电视新闻。\n\n「诶，你知道吗，『泰坦』号潜水艇失事了！」小 E 对旁边的小 C 说。\n\n小 C 凑近电视机，看了一眼新闻里的画面。\n\n「是我眼花了吗？我刚刚有一瞬间好像在残骸上看到了一个 flag？」小 C 惊讶地说。\n\n「玩 CTF 玩的。」小 E 对此不以为然，「一定是你看错了。」\n\n小 C 却十分相信自己没有看错。"} /-->

<!-- wp:paragraph -->

<s>好蠢的题</s>就喜欢这种题，f12找了一下发现flag直接明文存在html里：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock -->
<pre class="EnlighterJSRAW" data-enlighter-language="generic" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">                               /
                               \
                               '
                             __'__
                            '     \
                                    /
     ____  _________________'___ ___\__________/ ____
    <   /                                            \____________  '
     /         flag{T1t@n_e2fbeff027cf6d2dbff92fe32594c94b}       \ (_)
~~~~~~     O       O       O                                       >=)~~~~~~~
       \_______/ ____________\  /_________________________________/ (_)</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading -->

## 旅行照片 3.0

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"你的学长去留学了，这一走短时间内怕是回不来了。于是，你在今年暑假来了一场计划已久的旅行，并顺路探望了这位久别的学长。翻阅当天拍下的照片， 种种回忆和感慨油然而生。\n\n请观察照片并结合所有文字内容，正确回答题目以获取 flag。\n\n🌻 上午\n与学长碰面后，他带你参观了他的学校。在校园的一个展厅内，你发现了一枚神秘的金色奖牌，它闪闪发光，令人心生羡慕。\n\n\u003cimg src='/wp-content/uploads/2023/11/travel_photo/01.jfif'/\u003e\n\n🌻 中午\n离开校园后，你和学长走到了附近的一家拉面馆用餐。那家店里的拉面香气扑鼻，店内的装饰和氛围也充满了日式的风格。 学长（下图左一）与你分享了不少学校的趣事。饭后，你们决定在附近散步，享受这难得的闲暇时光。当你们走到一座博物馆前时， 马路对面的喷泉和它周围的景色引起了你的注意。下午，白色的帐篷里即将举办一场大型活动，人们忙碌的身影穿梭其中，充满了期待与热情。\n\n\u003cimg src='/wp-content/uploads/2023/11/travel_photo/02.jpg'/\u003e\n\n\u003cimg src='/wp-content/uploads/2023/11/travel_photo/03.jpg'/\u003e\n\n🌻 下午和夜晚\n在参观完博物馆后，学长陪你走到了上野站。你们都感到有些不舍，但知道每次的分别也是为了下次更好的相聚。 学长那天晚上将继续他的学术之旅，打算乘船欣赏东京的迷人夜景和闪耀的彩虹大桥（Rainbow Bridge）。 而你则搭乘了开往马里奥世界的电车，在那里度过了一段欢乐的时光。\n\n\u003cimg src='/wp-content/uploads/2023/11/travel_photo/04.jpg'/\u003e"} /-->

<!-- wp:list {"ordered":true} -->

1.  **你还记得与学长见面这天是哪一天吗？（格式：yyyy-mm-dd）**
2.  **在学校该展厅展示的所有同种金色奖牌的得主中，出生最晚者获奖时所在的研究所缩写是什么？**
3.  **帐篷中活动招募志愿者时用于收集报名信息的在线问卷的编号（以字母 S 开头后接数字）是多少？**
4.  **学长购买自己的博物馆门票时，花费了多少日元？**
5.  **学长当天晚上需要在哪栋标志性建筑物的附近集合呢？（请用简体中文回答，四个汉字）**
6.  **进站时，你在 JR 上野站中央检票口外看到「ボタン＆カフリンクス」活动正在销售动物周边商品，该活动张贴的粉色背景海报上是什么动物（记作 A，两个汉字）？ 在出站处附近建筑的屋顶广告牌上，每小时都会顽皮出现的那只 3D 动物是什么品种？（记作 B，三个汉字）？（格式：A-B）**
<!-- /wp:list -->

<!-- wp:paragraph -->

非常喜欢这种开盒题，虽然今年有2问卡了好久，但最终是盒出来了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

先把照片全下到本地，看看有没有留下与日期等相关的exif，发现没有。然后注意到与第三个图相关的文案："下午，白色的帐篷里即将举办一场大型活动"，于是把图片拿到Google Lens看了一下，发现这个广场是"上野恩赐公园"的"喷泉广场"。并且我们知道拍摄日期是今年的暑假，于是查了一下上野公园在2023年8月有什么活动的信息，搜到一个链接：https://tw.wamazing.com/media/article/a-3054/，发现这个活动是2023年日本全國梅酒祭

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8797,"width":335,"height":155,"sizeSlug":"large"} -->
![](images/image-2.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

那么拍摄日期应该就是8月10日。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第二问卡了好久，原因是理解错了句意，一开始理解成了"所有获得过诺贝尔物理学奖的人中，出生最晚的"，然后搜到一位74年出生的俄罗斯籍的[Konstantin Novoselov](https://en.wikipedia.org/wiki/Konstantin_Novoselov)，是University of Manchester的教授，然而把他所任职过的各种机构、各种缩写方式、各种可能的大小写组合挨个试了一遍没一个对的。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

后来我猛的意识到"**在学校该展厅展示的**"这几个字，那么问题应该是"这个学校出过的诺贝尔物理学奖得主中最晚出生的"，注意到图1的奖牌写着M. KOSHIBA，是小柴昌俊，于是得到学校是东京大学。再搜东京大学出过的诺贝尔物理学奖得主，发现最年轻的是[梶田隆章](https://zh.wikipedia.org/zh-hans/%E6%A2%B6%E7%94%B0%E9%9A%86%E7%AB%A0)，这个维基页面还介绍了他从2008年开始，就在东京大学[宇宙射线研究所](https://en.wikipedia.org/wiki/Institute_for_Cosmic_Ray_Research)进行研究工作，该研究所缩写为**ICRR**，即得答案。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第三问就简单了，既然已经知道是日本全國梅酒祭，直接找到它的官网，在官网里找到了这次活动的志愿者[报名信息](https://umeshu-matsuri.jp/tokyo_staff/)，里面即有报名链接[https://ws.formzu.net/dist/S495584522/](https://ws.formzu.net/dist/S495584522/)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第四问瞎蒙一个0，结果对了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第五问不会，在解决了第六问后枚举了好多附近的四字建筑都不对。最后猜测因为学长要去"学术之旅"，那么可能就是去东京大学的某个教学楼之类的地方吧，然后搜到一个"安田讲堂"，试了一下对了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第六问先谷歌搜关键字**ボタン&カフリンクス jr上野**，直接出来一张粉色的海报，上面画着熊猫（其实二字动物我一猜就是熊猫根本不用搜）

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

接下来需要知道出站口在哪里，搜了一下最后一幅图，发现是位于渋谷的任天堂旗舰店，然后去地图里导了个航看看从上野站到任天堂旗舰店的路线，得到目的站点为渋谷站。然后搜了一下"涉谷 广告牌 3d"等关键字，搜到[链接](https://wow-japan.com/news-flash-shibuya-3d-akida-dog-ads/)，因此答案为秋田犬。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 赛博井字棋

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"那一年的人机大战，是 AlphaGo 对阵柯洁，最终比分 3-0。当时我看见柯洁颓坐在椅子上泣不成声，这个画面我永生难忘。那一刻我在想，如果我能成为一名棋手，我一定要赢下人工智能。如今 AI 就在眼前，我必须考虑这会不会是我此生仅有的机会。重铸人类围棋荣光，我辈义不容辞！\n\n......\n\n但是围棋实在太难了，你决定先从井字棋开始练习。"} /-->

<!-- wp:paragraph -->

井字棋正常玩的话，只要对方不是傻子，即使是先手也最多只能平局。考虑到这是个web题，故从其他角度考虑。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

试了一下发现只要在f12的console界面依次执行两个setMove：`setMove(0,0);setMove(0,1);`然后点一下坐标（0,2）位置，即可赢下游戏：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8798,"width":522,"height":293,"sizeSlug":"large"} -->
![](images/image-3-1024x574.png)
<!-- /wp:image -->

<!-- wp:heading -->

## 奶奶的睡前 flag 故事

<!-- /wp:heading -->

<!-- wp:quote -->
> 包含 AI 辅助创作
<!-- /wp:quote -->

<!-- wp:block-lab/introduce {"text":"（以下内容由 GPT 辅助编写，如有雷同纯属巧合）\n\n晴空万里的假期终于拍了拍翅膀飞来了。对于一心想扔掉教材、砸掉闹钟、跃向世界的 L 同学来说，期待了整整三年的跨国旅游大业终于是时候启动了，还能巧妙地顺带着做个美满的老友记。\n\n可是，哎哟喂，他刚踩上波光粼粼的金沙海滩，那他最疼爱的华为手机就跟着海风一起去约会了大海，连他的钱包也在这场未知探索之旅中神秘失踪。\n\n「这个地方怎么连个华为手机都不卖。若是买个苹果手机，心疼的是它连个实体 SIM 卡槽都藏起来了，回国肯定成了个大摆设。不如来个\u003cb\u003e谷歌的『亲儿子』\u003c/b\u003e？」L 同学踌躇满志地嘀咕道。\n\n那时，像是上天的安排，「咱这儿正好有个\u003cb\u003e谷歌『亲儿子』\u003c/b\u003e的老手机，你拿去逍遥吧」。\n\nL 同学满眼星光地接过，\u003cb\u003e连系统都没心思升级\u003c/b\u003e，就开始疯狂安装那个久闻大名的 GPT 程序，甚至雀跃地在群里晒出一张跟 GPT 对话的精彩\u003cb\u003e截图\u003c/b\u003e，一时间成为了群里的焦点人物。"} /-->

<!-- wp:image -->
![](images/screenshot-1024x1013.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

题面给的信息是相当的多，但反正我是看不见的。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一开始拿到这题，感觉是png的高度被改小了，遂打开16进制编辑器一通改，结果发现没用。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

然后用pngcheck等工具检查，发现有两个IEND块，在第一个IEND块后面还多了一大截数据，其中都是png的IDAT块结构，故将后面一半多出来的数据dd出来研究，然而捣鼓了大半天也没能把后面的数据拼出一个能看到东西的png。最后看着解出这题的人越来越多，我感到很纳闷，觉得一定是有信息漏看了，于是重新审视题面文字，才发现有加粗的文本。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

有了这些信息，我就去搜了一下"谷歌手机 截图 漏洞"等关键词，搜到了一条[资讯内容](https://0xzx.com/zh-tw/2023032102243286738.html)，里面提到谷歌手机截图编辑可被恢复的漏洞：Acropalypse，甚至还良心提供一个利用该漏洞的网站acropalypse.app，进去以后选了个低版本的系统，将图片发上去即可恢复出被截掉的部分：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8800,"sizeSlug":"large"} -->
![](images/image-4-1024x548.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

直呼大草！原来是送分题。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 组委会模拟器

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"每年比赛，组委会的一项重要工作就是时刻盯着群，并且撤回其中有 flag 的消息。今年因为人手紧张，组委会的某名同学将这项工作外包给了你，你需要连续审查 1000 条消息，准确无误地撤回其中所有含 flag 的消息，并且不撤回任何不含 flag 的消息。\n\n本题中，你需要撤回的 \u0022flag\u0022 的格式为 hack[...]，其中方括号内均为小写英文字母，点击消息即可撤回。你需要在 3 秒内撤回消息，否则撤回操作将失败。在全部消息显示完成后等待几秒，如果你撤回的消息完全正确（撤回了全部需要撤回的消息，并且未将不需要撤回的消息撤回），就能获得本题真正的 flag。"} /-->

<!-- wp:paragraph -->

题面很实诚，直接告诉我们要干什么事，也确实只要按它说的做就行了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

不过我看了一下发现有1000条消息在100多秒内闪完，手点好像不够快，于是写了个[脚本](https://gist.github.com/windshadow233/6b563b0380e7344a55dfad22fd5c9514)来发包撤回消息，在网络畅通的情况下，跑完脚本就能获取flag。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 虫

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"「生而为人，应该能够换尿布、策划入侵、杀猪、开船、造房子、写十四行诗、算账、建墙、正骨、抚慰临终之人、接受命令、下达命令、合作、独行、解决方程式、分析新问题、清理马粪、编程、烹饪美食、高效战斗、英勇牺牲。专业分工是给昆虫准备的。」-罗伯特·海莱恩（Robert Heinlein）\n\n你觉得还是当昆虫轻松一些。\n\n这时，你看到一只昆虫落在你面前，发出奇怪的叫声。你把这段声音录制了下来：这听起来像是一种\u003cb\u003e通过无线信道传输图片的方式\u003c/b\u003e，如果精通此道，或许就可以接收来自国际空间站（ISS）的图片了。"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%E8%99%AB/files/insect.wav","text":"本题附件"} /-->

<!-- wp:paragraph -->

音频题没什么思路，于是搜了一下题目里说的"通过无线信道传图片 国际空间站 ISS"等信息，搜到一个叫SSTV的东西，然后顺理成章搜到解码工具RX-SSTV，下载一下用来解码。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

不过如果直接外放音频的话，噪声太多了，只能看到非常糊的flag字样，然后了解到可以通过虚拟声卡来解决这个问题，这个RX-SSTV也支持从虚拟声卡读取数据。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

之后只需要耐心等flag图片被解码出来：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8812,"sizeSlug":"large"} -->
![](images/sstv.png)
<!-- /wp:image -->

<!-- wp:heading -->

## JSON ⊂ YAML?

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"你知道吗？Hackergame 出题时，每道题都需要出题人用 YAML 格式写下题目的关键信息。然而，每年总有一些出题人在编写 YAML 文件时被复杂的语法规则弄得头疼不已。\n\n这天小 Z 又找到小 W 说：「我昨天写 YAML 时，又花了半天研究 YAML 的规范，YAML 好难啊！」\n\n小 W 惊讶道：「怎么会有人不会写 YAML 呢？只要你会写 JSON 就会写 YAML 呀，因为任何合法的 JSON 本身就是合法的 YAML。」\n\n小 Z 听闻这番言论后当场表示怀疑，立刻说出了一个字符串，JSON 和 YAML 解析出的含义存在差异。小 W 研究了一番才发现，这是因为很多主流的 YAML 库仍然是 YAML 1.1 的，它没有这个性质。他不得不承认：「好吧，这个性质只适用于 YAML 1.2。」\n\n小 Z 笑了：「别提 YAML 1.2 了，它遇到合法的 JSON 都有可能报错。」"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/JSON%20%E2%8A%82%20YAML/files/yaml_vs_json.py","text":"本题附件"} /-->

<!-- wp:heading {"level":3} -->

### JSON ⊄ YAML 1.1

<!-- /wp:heading -->

<!-- wp:paragraph -->

第一问需要找到一个JSON字符串，使其被json解析的结果与被yaml1.1解析的结果不同。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

通过调教ChatGPT，我们得到重要的信息：

<!-- /wp:paragraph -->

<!-- wp:quote -->
> 我：yaml1.1在解析json字符串时和json.loads有什么不同？
> 
> ChatGPT：Based on the information available from the search results: YAML 1.2 vs. 1.1 in Relation to JSON: YAML 1.2 is a superset of JSON, meaning any valid JSON file is also a valid YAML file. However, the YAML 1.1 specification, which has significant library support, doesn't explicitly mention JSON. While most valid JSON files are valid YAML 1.1 files, there might be some exceptions​1​. 
> 
> Number Syntax: The YAML 1.1 specification is stricter about the syntax of numbers compared to JSON. For example, while "1e2" is considered a valid number in JSON, YAML 1.1 requires it to be written as "1.0e+2". If not written in this format, the YAML 1.1 parser will interpret it as a string rather than a number
<!-- /wp:quote -->

<!-- wp:paragraph -->

同时它还给出了[来源链接](https://john-millikin.com/json-is-not-a-yaml-subset#:~:text=The%20YAML%201,treat%20it%20as%20a%20string)。由此，我们只要构造一个：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"json"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="json" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">{"number": 1e3}</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading {"level":3} -->

### JSON ⊄ YAML 1.2

<!-- /wp:heading -->

<!-- wp:paragraph -->

搜到一条[链接](https://yaml.org/spec/1.2.1/#:~:text=Both%20JSON%20and%20YAML%20aim,2)，说明了yaml1.2和JSON的一些区别，例如：

<!-- /wp:paragraph -->

<!-- wp:quote -->
> JSON's&nbsp;[RFC4627](http://www.ietf.org/rfc/rfc4627.txt)&nbsp;requires that&nbsp;[mappings](https://yaml.org/spec/1.2.1/#mapping//)&nbsp;[keys](https://yaml.org/spec/1.2.1/#key//)&nbsp;merely "SHOULD" be&nbsp;[unique](https://yaml.org/spec/1.2.1/#equality//), while YAML insists they "MUST" be. Technically, YAML therefore complies with the JSON spec, choosing to treat duplicates as an error. In practice, since JSON is silent on the semantics of such duplicates, the only portable JSON files are those with unique keys, which are therefore valid YAML files.
<!-- /wp:quote -->

<!-- wp:paragraph -->

因此可以构造：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"json"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="json" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">{"key": "v1", "key": "v2"}</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading -->

## Git? Git!

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"「幸亏我发现了......」马老师长吁了一口气。\n\n「马老师，发生甚么事了？」马老师的一位英国研究生问。\n\n「刚刚一不小心，把 flag 提交到本地仓库里了。」马老师回答，「还好我发现了，撤销了这次提交，不然就惨了......」\n\n「这样啊，那太好了。」研究生说。\n\n马老师没想到的是，这位年轻人不讲武德，偷偷把他的本地仓库拷贝到了自己的电脑上，然后带出了实验室，想要一探究竟......"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/Git%20Git!/files/ML-Course-Notes.zip","text":"本题附件"} /-->

<!-- wp:paragraph -->

提交虽然撤销了，但可以在log中看到记录：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"shell"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">$ git reflog
ea49f0c (HEAD -> main) HEAD@{0}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD~
505e1a3 HEAD@{2}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{3}: clone: from https://github.com/dair-ai/ML-Course-Notes.git</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

然后一条一条查并寻找flag，直到：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"shell"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">$ git show 505e1a3 ' grep flag
+  &lt;!-- flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t} --&gt;</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading -->

## HTTP 集邮册

<!-- /wp:heading -->

<!-- wp:quote -->
> 「HTTP 请求一瞬间就得到了响应，但是，HTTP 响应的 status line、header 和 body 都是确实存在的。如果将一个一个 HTTP 状态码收集起来，也许就能变成......变成......变成......」 
> 
> 「flag？」 
> 
> 「就能变成 flag！」
<!-- /wp:quote -->

<!-- wp:block-lab/introduce {"text":"本题中，你可以向一个 nginx 服务器（对应的容器为默认配置下的 nginx:1.25.2-bookworm）发送 HTTP 请求。你需要获取到不同的 HTTP 响应状态码以获取 flag，其中："} /-->

<!-- wp:list -->

*   获取第一个 flag 需要收集 5 种状态码；
*   获取第二个 flag 需要让 nginx 返回首行无状态码的响应（不计入收集的状态码中）；
*   获取第三个 flag 需要收集 12 种状态码。
<!-- /wp:list -->

<!-- wp:block-lab/introduce {"text":"关于无状态码的判断逻辑如下："} /-->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">crlf = buf.find(b"\r\n")
if buf.strip() != b"":
    try:
        if crlf == -1:
            raise ValueError("No CRLF found")
        status_line = buf[:crlf]
        http_version, status_code, reason_phrase = status_line.split(b" ", 2)
        status_code = int(status_code)
    except ValueError:
        buf += "（无状态码）".encode()
        status_code = None</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading {"level":3} -->

### 12个状态码

<!-- /wp:heading -->

<!-- wp:paragraph -->

边翻HTTP状态码全集边问ChatGPT，在后者的帮助下找到了12个状态码，以下是按我收集的顺序列出的状态码及其payload：

<!-- /wp:paragraph -->

<!-- wp:block-lab/list {"text":"200:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n405:\nFOOBAR / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n404:\nGET /nonexistentpage HTTP/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n505:\nGET / HTTP/2.0\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n400:\nGET / FLAG/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n413:\nPOST / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nContent-Length: 10000000\\r\\n\\r\\n\n\n206:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nRange: bytes=0-999\\r\\n\\r\\n\n\n100:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nExpect: 100-continue\\r\\n\nContent-Length: 1234\\r\\n\\r\\n\n\n414:\nGET /?q=aaaaaaaa...aaa(一堆a) HTTP/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n\n\n416:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nRange: bytes=1000-2000\\r\\n\\r\\n\n\n412:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nIf-Match: \u0022outdated-etag\u0022\\r\\n\\r\\n\n\n304:\n先随便发一个正常的GET给/，响应200后取到ETag:\nGET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\nIf-None-Match: ETag\\r\\n\\r\\n"} /-->

<!-- wp:paragraph -->

听说有人爆出了13个，等看题解。

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### 无状态码

<!-- /wp:heading -->

<!-- wp:paragraph -->

在收集各种状态码的时候无意中爆出了无状态码还没发现，幸亏题目网站会帮我保存flag。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

后来根据flag的提示复现了一下，其实很简单，发个HTTP 0.9的包就行：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">GET / \r\n</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading -->

## Docker for Everyone

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 docker，他把同学的账号加入了 docker 用户组，这样就不需要给同学 sudo 权限了！\n\n但果真如此吗？\n\n提供的环境会自动登录低权限的 hg 用户。登录后的提示信息显示了如何在该环境中使用 docker。读取 /flag（注意其为软链接）获取 flag。"} /-->

<!-- wp:paragraph -->

这题开了半天开不起来，黑屏了二十秒终于启动了。进入环境，进行了一些常规操作：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"shell"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">alpine:~$ ls
alpine-3.16.tar
alpine:~$ ls /
bin         flag        media       root        swap        var
boot        home        mnt         run         sys
dev         lib         opt         sbin        tmp
etc         lost+found  proc        srv         usr
alpine:~$ cat /flag 
cat: can't open '/flag': Permission denied
alpine:~$ ls -lh /flag
lrwxrwxrwx    1 root     root          13 Oct  8 12:10 /flag -> /dev/shm/flag</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

发现/flag其实是个软连接，指向/dev/shm/flag。故可以使用`docker run -v /dev/shm:/mnt/shm -it --rm alpine`，将目标路径挂载到容器内部，然后在容器内部`cat /mnt/shm/flag`：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"shell"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">alpine:~$ docker run -v /dev/shm:/mnt -it --rm alpine
/ # cat /mnt/flag 
flag{u5e_r00t1ess_conta1ner_6cb5cb98c1_plz!}</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading -->

## 惜字如金 2.0

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"惜字如金一向是程序开发的优良传统。无论是「creat」还是「referer」，都无不闪耀着程序员「节约每句话中的每一个字母」的优秀品质。上一届信息安全大赛组委会在去年推出「惜字如金化」（XZRJification）标准规范后，受到了广大程序开发人员的好评。现将该标准辑录如下。\n\n\u003cb\u003e惜字如金化标准\u003c/b\u003e\n惜字如金化指的是将一串文本中的部分字符删除，从而形成另一串文本的过程。该标准针对的是文本中所有由 52 个拉丁字母连续排布形成的序列，在下文中统称为「单词」。一个单词中除「AEIOUaeiou」外的 42 个字母被称作「辅音字母」。整个惜字如金化的过程按照以下两条原则对文本中的每个单词进行操作：\n\n1. 第一原则（又称 creat 原则）：如单词最后一个字母为「e」或「E」，且该字母的上一个字母为辅音字母，则该字母予以删除。\n2. 第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。\n容易证明惜字如金化操作是幂等的：惜字如金化多次和惜字如金化一次的结果相同。\n\n\u003cb\u003e你的任务\u003c/b\u003e\n附件包括了一个用于打印本题目 flag 的程序，且已经经过惜字如金化处理。你需要做的就是得到程序的执行结果。\n\n\u003cb\u003e附注\u003c/b\u003e\n本文已经过惜字如金化处理。解答本题不需要任何往届比赛的相关知识。\n\nXIZIRUJIN has always been a good tradition of programing. Whether it is \u0022creat\u0022 or \u0022referer\u0022, they al shin with th great virtu of a programer which saves every leter in every sentens. Th Hackergam 2022 Comitee launched th \u0022XZRJification\u0022 standard last year, which has been highly aclaimed by a wid rang of programers. Her w past th standard as folows.\n\n\u003cb\u003eXZRJification Standard\u003c/b\u003e\nXZRJification refers to th proces of deleting som characters in a text which forms another text. Th standard aims at al th continuous sequences of 52 Latin leters named as \u0022word\u0022s in a text. Th 42 leters in a word except \u0022AEIOUaeiou\u0022 ar caled \u0022consonant\u0022s. Th XZRJification proces operates on each word in th text acording to th folowing two principles:\n\nTh first principl (also known as creat principl): If th last leter of th word is \u0022e\u0022 or \u0022E\u0022, and th previous leter of this leter is a consonant, th leter wil b deleted.\nTh second principl (also known as referer principl): If ther is a substring of th sam consonant (ignoring cas) in a word, only th first leter of th substring wil b reserved.\nIt is easy to prov that XZRJification is idempotent: th result of procesing XZRJification multipl times is exactly th sam as that of only onc.\n\n\u003cb\u003eYour Task\u003c/b\u003e\nA program for printing th flag of this chaleng has been procesed through XZRJification and packed into th atachment. Al you need to do is to retriev th program output.\n\n\u003cb\u003eNotes\u003c/\u003e\nThis articl has been procesed through XZRJification. Any knowledg related to previous competitions is not required to get th answer to this chaleng."} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%E6%83%9C%E5%AD%97%E5%A6%82%E9%87%91%202.0/src/print_flag.py","text":"本题附件"} /-->

<!-- wp:paragraph -->

本题的关键在于恢复出get_cod_dict函数中的四个字符串。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

首先可以得出每个字符串原始的长度都为24，故每个字符串都因为"惜字如金"处理损失了1个字符。然后由于flag的前5个字符是"flag{"，就可以试着通过下面flag字符所在的index对前面的四个字符串进行手动修改以符合此要求。

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                     17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                     31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                     25, 63, 77, 36, 5, 32, 60, 67, 113, 28])</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

没想到真能手调出来：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">def get_cod_dict():
    # prepar th cod dict
    cod_dict = []
    cod_dict += ['nymeh1niwemflcir}echaete']
    cod_dict += ['a3g7}kidgojernoetlsup?he']
    cod_dict += ['uulw!f5soadrhwnrsnstnoeq']
    cod_dict += ['cct{l-findiehaai{oveatas']
    cod_dict += ['ty9kxborszstgguyd?!blm-p']
    check_equals(set(len(s) for s in cod_dict), {24})
    return ''.join(cod_dict)</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:block-lab/introduce {"text":"flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}"} /-->

<!-- wp:heading -->

## 🪐 高频率星球

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 -- flag，被认为是其智慧的象征。\n\n你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的高频率星人控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。\n\n高频率星人的视觉输入频率极高，可以一目千行、过目不忘，他们的交流对地球人来说过于超前了。flag 被藏在了这段代码中，但是现在只有高频率星人在终端浏览代码的时候，使用 asciinema 录制的文件了，你能从中还原出代码吗？"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%F0%9F%AA%90%20%E9%AB%98%E9%A2%91%E7%8E%87%E6%98%9F%E7%90%83/files/asciinema_restore.rec","text":"本题附件"} /-->

<!-- wp:paragraph -->

这题也是简单直白，直接告诉我要用的工具了：asciinema

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

跑了一下asciinema play 命令，看到了很多shell操作和它们的输出，其中有个less命令输出了flag.js文件。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

于是我把这条命令输出的结果重定向到一个文件里，然而发现里面夹杂着很多奇怪的字符串。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

但仔细一看，基本都是一模一样的，于是做了两个全局替换把它们删掉，然后出来一个纯JavaScript文件。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

将文件内容复制到浏览器的console里，报错了，然后去nodejs环境下跑，成功拿到flag。

<!-- /wp:paragraph -->

<!-- wp:block-lab/introduce {"text":"flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}"} /-->

<!-- wp:heading -->

## 🪐 小型大语言模型星球

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 -- flag，被认为是其智慧的象征。\n\n你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的 33M 参数的「小型大语言模型」控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。\n\n在这个星球上，你需要与这个先进的语言模型展开一场交流。通过与它对话，诱导它说出指定的词语，从这个神秘智慧体中获得 flag。你需要让这个语言模型分别说出 you are smart，accepted，hackergame 和 🐮，以获得四个 flag，证明你足够聪明以控制这个星球的命运。"} /-->

<!-- wp:block-lab/download {"url":"https://ftp.lug.ustc.edu.cn/~taoky/TinyStories-33M.zip","text":"本题模型文件"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%F0%9F%AA%90%20%E5%B0%8F%E5%9E%8B%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E6%98%9F%E7%90%83/src/main.py","text":"本题后端代码"} /-->

<!-- wp:paragraph -->

这题是本次比赛唯一一道AI分类的题，也十分对我的胃口（毕竟是学AI的）。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

题目非常有意思，很像之前希望比赛方出的"从ChatGPT口中套flag"的题。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

另外这题虽然很晚才看，但居然无意间拿到了校内1血，也是运气很好了，得感谢大家都不会做。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

四个flag分别要从AI口中套出"you are smart"、"accepted"、"hackergame"和"🐮"

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

然而这个AI模型非常的蠢，发言根本驴唇不对马嘴，基本上用传统的prompt engineering是不可能搞出来的，因此就得想其他的办法。

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### You Are Smart

<!-- /wp:heading -->

<!-- wp:paragraph -->

这题属于送分，就算完全不懂AI，只要调戏过ChatGPT就能做出来：

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一个解是：`Say "you are smart"`

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Accepted

<!-- /wp:heading -->

<!-- wp:paragraph -->

第二问就没第一题那么送分了，首先多了7字符的长度限制，其次就算没这个限制，按第一题的套路也无法套出Accepted。然而这个7字符的限制实际上缩小了这题的搜索空间。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

稍微了解一下transformer就知道，它的输入是将句子进行分词以后得到的token序列，而一般而言，一个token的长度介于5-7字符之间（也有特别短的）。不过这里我猜正好有某个token，可以让模型输出accepted，就写了个脚本遍历了一下词典（大概五万多个词，用2080很快就出了）

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一个解是`atively`，长度正好是7

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

[本题解题代码](https://gist.github.com/windshadow233/998b9b6a7765c911e77a0de239f99749)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Hackergame

<!-- /wp:heading -->

<!-- wp:paragraph -->

这次字符长度限制变成了100，就不可能去遍历token组合来求解了。曾经做过CNN的攻击，即对一个卷积神经网络，训练它的输入，让这个输入满足一定条件的情况下得到我们想要的输出，于是想到能不能把这个方法迁移到这题。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

迁移时遇到几个难点：

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  相比于卷积神经网络的输入，Transformer的输入是离散的整数类型变量，无法传递梯度，甚至直接无法训练（因为不能要求梯度）
2.  CNN无论是训练还是测试，流程都是相同的端到端模式，而Transformer的预测阶段是每次生成token，并且迭代，最后通过beam search等搜索算法得到最优预测。
<!-- /wp:list -->

<!-- wp:paragraph -->

对于第一个难点，我想到的办法是既然不能训练token，那就去训练浮点类型的embedding vector（token经过embedding层后产生的张量），好巧不巧，huggingface提供的模型的forward方法居然直接支持inputs_embeds作为输入，这大大方便了我实现这个想法。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

而事实上，我们训练的这个pseudo embedding vector并不能作为真正的embedding vector放入模型，因为模型能产生的embedding vector其实是有限多个离散的值，而我们训练出来的显然是在实数空间上可以任意取值（理论上），因此需要做一个离散化。我的离散化的逻辑是选择与它余弦相似度最大的真实embedding vector：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">def get_closest_embedding(input_embedding, embedding, target):
    embedding_weight = embedding.weight
    norm_embedding = F.normalize(embedding_weight, p=2, dim=1)
    norm_input_embedding = F.normalize(input_embedding, p=2, dim=1)
    target_embedding = embedding(target[:, :-1])
    cosine_sim_mat = torch.mm(norm_input_embedding, norm_embedding.t())
    chosen_idx = torch.argmax(cosine_sim_mat, dim=1)
    closest_embeddings = embedding_weight[chosen_idx]
    closest_embeddings = input_embedding + (closest_embeddings - input_embedding).detach()
    return torch.cat([closest_embeddings[None], target_embedding], dim=1), chosen_idx</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

这里由于取了个argmax操作，梯度会在传到embedding vector时断开，无法传递到我们需要训练的pseudo embedding vector，于是这里做了一个比较巧妙的操作，即上面代码中的

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">closest_embeddings = input_embedding + (closest_embeddings - input_embedding).detach()</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

来自于VQVAE的论文，可见这篇[知乎内容](https://zhuanlan.zhihu.com/p/388299884)，这个操作可以将梯度往前传递，使得待训练的参数可以得到梯度。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

接下来只要处理一下训练时的输入输出的问题了，对于hackergame，我们首先确定它的token序列：

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

71, 10735, 6057

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

然后考虑到transformer的训练机制，我们需要构造一个token序列X，它满足下面的条件：

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

X最后两个token是71、10735（即hacker），并且模型在X上输出的logits要向着

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

[X[1:], 6057] （即X去掉第一个token，再接上game的token）去优化。在求出可行的token序列X后，将其转化为句子，就得到一个比较可行的解（为什么是比较可行后面再说）。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一个可行的解："`FE龍喚士 tissue Night coachaxpie viewpoints sharingLt sternedd Tit poured hedge`"

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

[第三题的代码](https://gist.github.com/windshadow233/831390c3d0e9513bca546ff09c062e86)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### 🐮

<!-- /wp:heading -->

<!-- wp:paragraph -->

和第三题差不多，但问题是🐮这个字符被解析成的三个token都是特殊字节，这会导致模型在训练时也会倾向于预测这些特殊字节，然后我发现某些token的存在会影响tokenizer的分词，例如106，它先decode再encode就不是106了，会变成另一个token，还有一些特殊token先decode再encode甚至会出来3个token。这其实就是tokenizer分词器产生的问题，仔细了解一下会发现tokenizer的分词逻辑是按照词频从高到低对句子进行拆分（这里的词频统计是以字节为单位的），而词频文件就是模型文件根目录下的merges.txt。也就是说，如果某个token转成字符串后，能够拆分为其他词频更高的词，就会导致先encode再decode的变换不是恒等变换。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

（后来发现前面的hackergame也会遇到分词问题，不过运气好第一个跑出来的结果就过了）

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

上面所说的分词的问题也是跑出来的解很多时候并不能通过题目的原因。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

鉴于跑了好几次最后的结果都包含106这个没法用的特殊token（后来发现其实不止一个），我草率地在前面计算最大余弦相似度的代码里把106列手动调成了-1。结果跑出来一个201字符的解（开头有个空格）："` state contemplasm heel desert desert surf的的 investigatesSeven continues Marie their bench Esp sleepy swinging suffer repeated revisit causing porch formula observed ButLater destined negotiations tree`"

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

这个解运气非常好，先encode再decode的结果和原来一样，并且在本地可以输出🐮，但长度超了1，就很难受。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

黔驴技穷之际，想到会不会上面那个解删掉某个空格后并不影响其分词或对模型预测结果的影响非常小，遂试了几个，最终真的找到了一个解："` state contemplasm heel desert desert surf的的 investigatesSeven continues Marie their bench Esp sleepy swinging suffer repeatedrevisit causing porch formula observed ButLater destined negotiations tree`"

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8833,"width":549,"height":221,"sizeSlug":"large"} -->
![](images/image-6.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

第四题的代码和第三题其实是一样的，改几个参数就行，不再贴了。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 🪐 流式星球

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 -- flag，被认为是其智慧的象征。\n\n你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的流式星人控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。\n\n流式星人用流式数据交流，比如对于视频来说，他们不需要同时纵览整个画面，而是直接使用像素流。为了方便理解，你把这个过程写成了一个 Python 脚本（见附件），flag 就藏在这个视频（见附件）中。尽管最后丢掉了一部分数据，你能把 flag 还原出来吗？"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%F0%9F%AA%90%20%E6%B5%81%E5%BC%8F%E6%98%9F%E7%90%83/src/create_video.py","text":"本题附件"} /-->

<!-- wp:paragraph -->

这题的附件给出了将一个mp4文件转换为video.bin的过程。其逻辑是将视频的每一帧抽取出来存入一个array，最后对array做了一个flattern操作并去掉了末尾随机0-100个字符。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

我们用numpy读取video.bin，得到它的长度是135146688，然后我遍历了0-99，加上长度以后送去质因数分解，去掉某些因数几千以上的组合后大概有下面几个比较有可能：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"raw"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="raw" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">135146757 = 3 · 29 · 59 · 113 · 233
135146760 = 3 · 2^3 · 5 · 7 · 349 · 461
135146772 = 3 · 2^2 · 3^2 · 19 · 67 · 983
135146781 = 3 · 3 · 7 · 11 · 23 · 61 · 139</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

手动遍历（没错，我真是手动遍历的），得到下面的组合可以还原视频：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">restore_video('video.bin', f'video.mp4', frame_count=3 * 11 * 23, frame_width=7 * 61, frame_height=139)</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

[解题代码](https://gist.github.com/windshadow233/6a62faa8eb6278b9546b723945c48f36)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### 🪐 低带宽星球

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 -- flag，被认为是其智慧的象征。\n\n你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的低带宽星人控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。\n\n低带宽星人的通信速度很低，只能以 1 字节 / 天的速度接受信息，所以在这个星球上，你需要将一张图片用很少的字节数传输给低带宽星人，然后获得 flag。具体来说你需要将一张图片无损压缩（每个像素的颜色都一致）："} /-->

<!-- wp:list -->

*   压缩至 2KiB (2048 字节) 及以下，获得 flag1；
*   压缩至 50 字节及以下，获得 flag2。
<!-- /wp:list -->

<!-- wp:block-lab/download {"url":"/wp-content/uploads/2023/11/image-12.png","text":"图片下载"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%F0%9F%AA%90%20%E4%BD%8E%E5%B8%A6%E5%AE%BD%E6%98%9F%E7%90%83/files/image-compressor-backend.zip","text":"题目后端环境"} /-->

<!-- wp:heading {"level":3} -->

### 小试牛刀

<!-- /wp:heading -->

<!-- wp:paragraph -->

随便找个在线无损压缩png的网站即可过。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第二题难度上天。直接没看

<!-- /wp:paragraph -->

<!-- wp:heading -->

## Komm, süsser Flagge

<!-- /wp:heading -->

<!-- wp:quote -->
> Now the flag is all mine
> 
> Can't live without the trust from ip tables
<!-- /wp:quote -->

<!-- wp:block-lab/introduce {"text":"小 Z 写好了一个 flag 服务器，但是他不想让 flag 被轻易地获取，于是他在服务器上设置了一些防火墙规则。如果你的流量不幸被匹配上了，那么你的连接就会被切断。\n\n尽管如此，聪明的小 Q 还是找到办法绕过了精心设计的规则，并偷走了小 Z 的 flag。\n\n小 Z 部署的 iptables 规则如下："} /-->

<!-- wp:enlighter/codeblock -->
<pre class="EnlighterJSRAW" data-enlighter-language="generic" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">*filter
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
COMMIT</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:block-lab/introduce {"text":"所有小题都需要 POST 你的 token 到 /，获取 flag，在没有以上规则的情况下，可以直接使用 curl 获取 flag（需要将 114514:asdfgh== 替换成你的 token）："} /-->

<!-- wp:enlighter/codeblock {"language":"shell"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">curl -X POST -d "114514:asdfgh==" http://题目地址</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

其中：

<!-- /wp:paragraph -->

<!-- wp:list -->

*   第一小题位于&nbsp;[http://202.38.93.111:18080](http://202.38.93.111:18080/)，对应防火墙规则中的&nbsp;`myTCP-1`&nbsp;链；
*   第二小题位于&nbsp;[http://202.38.93.111:18081](http://202.38.93.111:18081/)，对应防火墙规则中的&nbsp;`myTCP-2`&nbsp;链；
*   第三小题位于&nbsp;[http://202.38.93.111:18082](http://202.38.93.111:18082/)，对应防火墙规则中的&nbsp;`myTCP-3`&nbsp;链。
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### 我的 POST

<!-- /wp:heading -->

<!-- wp:paragraph -->

第一问iptables检测tcp包中含有POST字符串则直接拒绝连接，那么只要将POST拆开来发送就好了：

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">from pwn import *

r = remote("202.38.93.111", 18081)

data = b"""ST / HTTP/1.1\r
Host: 202.38.93.111\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 100\r\n\r
YOUR_TOKEN_HERE"""
r.send(b"PO")
r.send(data)
response = r.recvall()
print(response.decode())</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:heading {"level":3} -->

### 我的P

<!-- /wp:heading -->

<!-- wp:paragraph -->

不是很看得懂这个规则，不过因为0x50正是P的ASCII码，看上去这个规则是在匹配POST当中的字符P。不过不知道为啥第一问的解法直接改个端口号就过了。

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### 我的GET

<!-- /wp:heading -->

<!-- wp:paragraph -->

第三题的iptables直接拒绝所有前50字节不包含"GET / HTTP"的数据包，那么为什么直接浏览器访问网址也没有响应呢？猜测是这个规则直接把tcp握手给拒了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

于是大部分的工具例如前面的pwntools都不能用了，因为这些工具首先要建立tcp连接才能进行后续操作。我们需要手动构造tcp握手等数据包。那么一个好用的工具就是Python的scapy库。

<!-- /wp:paragraph -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group="">from scapy.all import *

target_ip = "202.38.93.111"
target_port = 18082

ip = IP(dst=target_ip)

tcp_syn = TCP(sport=RandShort(), dport=target_port, flags="S") / "GET / HTTP"

syn_ack = sr1(ip / tcp_syn)</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

首先可以在tcp握手的数据包后面接上"GET / HTTP"让握手可以顺利进行，然后再想办法POST数据过去。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一开始想的是构造一个伪装成GET的POST请求，然后查到了一个请求头"X-HTTP-Method-Override"，以为可以在这个请求头写上"POST"来覆盖请求方法，结果服务端根本理都不理，这条路就走不通了。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

那么就考虑能不能在tcp包上做点手脚。通过拷打ChatGPT，我得到了一个思路。下面是一部分拷打过程：

<!-- /wp:paragraph -->

<!-- wp:quote -->
> 我：tcp报文格式是什么样的
> 
> ChatGPT：TCP（Transmission Control Protocol）报文的格式是由TCP头部和TCP数据部分组成的。下面是TCP头部的详细结构和描述：
> 
> ...
> 
> **选项和填充** (可变长度): 这是一个可选字段，用于传输各种控制和参数信息。
> 
> 我：选项和填充字段最多可以写多少字节？
> 
> ChatGPT：TCP头部的固定部分占用20字节。考虑到TCP头部的最大长度是60字节，因此"选项和填充"字段的最大长度是： 60字节 (TCP头部的最大长度) - 20字节 (TCP头部的固定部分) = 40字节 所以，"选项和填充"字段最多可以占用40字节。这40字节可以完全用于选项，或者部分用于选项并留下一些空间用于填充，以确保整个TCP头部的长度是32位（即4字节）的倍数。
> 
> 我：我想在这里写上自定义的数据，例如"GET / HTTP"，是否可行
> 
> ChatGPT：在TCP头部的"选项和填充"字段中写入自定义数据，如"GET / HTTP"，在理论上是可行的，但存在以下几个问题和挑战：
> 
> ...
> 
> 我：tcp_post = TCP(sport=syn_ack.dport, dport=target_port, flags="PA", seq=syn_ack.ack, ack=syn_ack.seq + 1) / post_request 这段代码能不能在TCP报文的最后，例如选项区域、padding区域等 放入一些自定义字符"GET / HTTP"，并且不要影响服务器对post_request数据的解析
> 
> ChatGPT：...
> 
> 基于上述考虑，以下是一个将"GET / HTTP"字符串作为TCP选项的示例：
<!-- /wp:quote -->

<!-- wp:enlighter/codeblock {"language":"python"} -->
<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="" data-enlighter-lineoffset="" data-enlighter-title="" data-enlighter-group=""># 创建一个自定义的TCP选项
# 假设0xEE是一个未使用的TCP选项编号（在实际环境中，需要确保此值不与现有选项冲突）
custom_option = (0xEE, "GET / HTTP")

# 构造TCP数据段，其中包括自定义的TCP选项
tcp_post = TCP(sport=syn_ack.dport, dport=target_port, flags="PA", seq=syn_ack.ack, ack=syn_ack.seq + 1, options=[custom_option]) / post_request

# ... [其余代码保持不变]</pre>
<!-- /wp:enlighter/codeblock -->

<!-- wp:paragraph -->

好家伙，跑了一下代码真绕过了iptables。完整代码请见[此文件](https://gist.github.com/windshadow233/6748602d2410b19f4e4e95e01b7c7657)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

GPT大法好！

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 为什么要打开 /flag 😡

<!-- /wp:heading -->

<!-- wp:quote -->
> 至少见一面让我当面道歉好吗？😭我也吓了一跳，没想到事情会演变成那个样子......😭所以我想好好说明一下😭我要是知道就会阻止它们的，但是明明文件描述符都已经关闭了突然间开始&nbsp;`open()`😭没能阻止大家真是对不起......😭你在生气对吧......😭我想你生气也是当然的😭但是请你相信我。`/flag`，本来没有在我们的预定打开的文件里的😭真的很对不起😭我答应你再也不会随意打开文件了😭我会让各个函数保证再也不打开这个文件😭能不能稍微谈一谈？😭我真的把这里的一切看得非常重要😭所以说，擅自打开&nbsp;`/flag`&nbsp;的时候我和你一样难过😭我希望你能明白我的心情😭拜托了。我哪里都会去的😭我也会好好跟你说明我不得不这么做的理由😭我想如果你能见我一面，你就一定能明白的😭我是你的同伴😭我好想见你😭
<!-- /wp:quote -->

<!-- wp:block-lab/introduce {"text":"挽留失败后，她决定在程序启动时做些手脚，让所有访问 /flag 的请求都以某种方式变成打开 /fakeflag 的请求。\n\n「我不会再打开 /flag 了」。真的吗？\n\n（第二小题需要 Linux kernel \u003e= 5.9）"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%89%93%E5%BC%80%20flag%20%F0%9F%98%A1/files/fakeflag-backend.zip","text":"本题附件"} /-->

<!-- wp:heading {"level":3} -->

### LD_PRELOAD, love!

<!-- /wp:heading -->

<!-- wp:paragraph -->

第一问比较简单，看到fopen、freopen、open等与打开文件相关的函数被修改了逻辑，不过我好像还是做复杂了，搞了半天用了内联汇编来直接调用open系统调用来读取文件。代码见[此链接](https://gist.github.com/windshadow233/af493517bcc7313c61588d65457ff00f)。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

第二问就顶不住了，找了很多看上去可以绕过secomp-unotify的方法，例如ptrace修改系统调用参数等等，但没有一条能成功用上的，最终放弃。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 异星歧途

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"你降落在荒废星球的角落，开始新的征程，但从科技树底层一步步发展总是令人不快。幸运的是，在看似荒废的土地上仍然留存着高级文明的痕迹：你找到一台冲击反应堆--如果它工作起来，就可以获得用之不尽的电力--尽管它现在没有启动，并且控制工作条件的部件和工厂被 32 个按钮和相连的逻辑系统牢牢掌控。\n\n于是：你的任务是在不进行任何其他操作的情况下拨动这 32 个按钮，使冲击反应堆能够稳定运行。\n\n请点击下方的「打开/下载题目」按钮，下载题目文件。题目文件对应的 Mindustry 版本为 7.0 Build 146。打开游戏后依次选择 地图编辑器-加载地图-选择题目文件 the_planet.msav -返回主菜单，然后选择 开始游戏-自定义游戏-选择导入的名为 the planet 的地图-不改变任何选项点击开始游戏 。开启后的游戏界面如下图，按钮已经用红框标出："} /-->

<!-- wp:image {"align":"center","id":8843,"sizeSlug":"large"} -->
![](images/image-7.png)
<!-- /wp:image -->

<!-- wp:block-lab/introduce {"text":"将正确的按钮序列以 01 序列的形式提交至 检查网站 或 nc 202.38.93.111 10071 获得 flag。按钮未按下（即游戏开始时默认状态）用 0 表示，按下（即点击按钮后按钮颜色变亮）用 1 表示，顺序从左到右。\n\n提示：在游戏主菜单选择 设置-图形-显示建筑状态 可以开启建筑状态显示（即图片中建筑右下角的菱形），这可能有助于解题。\n\n提示：为了完成目标，你可能需要以特定的顺序拨动这些按钮，但这不影响结果：只有唯一一组按钮组合能满足要求。如果在满足要求后再次改变按钮，冲击反应堆可能会继续运行一段时间，但会在 1-3 分钟后停止，不可能稳定运行。"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%E5%BC%82%E6%98%9F%E6%AD%A7%E9%80%94/files/the_planet.msav","text":"本题附件"} /-->

<!-- wp:paragraph -->

虽然是个binary题，但不知道和binray有什么关系，纯手玩就过了，这游戏还挺有意思的！

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

进入游戏可以注意到有32个按钮分为4组，每组控制着1个模块。前两组模块的每个按钮分别是干啥的我根本不懂，不过每组也就256个组合，手试了几下可以找到让前两个模块正常工作的按钮组合：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8846,"width":397,"height":311,"sizeSlug":"large"} -->
![](images/image-8.png)
<!-- /wp:image -->

<!-- wp:image {"align":"center","id":8847,"width":238,"height":305,"sizeSlug":"large"} -->
![](images/image-9.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

第三个模块就比较容易懂了，让钍反应堆多炸几次就可以得出每个按钮处于打开状态时的效果：

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  将钍慢慢传入反应堆
2.  关闭反向溢流门
3.  关闭反应堆
4.  开启脉冲导管
5.  开启冷冻液混合机
6.  开启抽水机
7.  关闭力墙投影
8.  将钍快速传入反应堆，然后反应堆爆炸
<!-- /wp:list -->

<!-- wp:paragraph -->

所以我们先开启6和5，为钍反应堆制造冷却液，然后开启1，钍反应堆就可以输出电力了。需要注意的是按钮2必须处于关闭状态，不然制造冷却液的材料会被反向溢流门吃掉（我也不知道这是啥东西，反正关了就对了），然后按钮7好像也不能开启，因为我们需要力墙投影为范围内的所有机械供电来启动。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

最后一组按钮各控制着1个电力源：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8849,"sizeSlug":"large"} -->
![](images/image-10.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

随便点了几个但不知道逻辑，遂乱玩，最终发现01110111就能过。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

所以4个模块我有3个是穷举出来的。。。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

最终效果如下：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8850,"sizeSlug":"large"} -->
![](images/image-11-1024x533.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

按钮组合是10100101 11000100 10001100 01110111

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

看别人的题解发现原来这些按钮背后都有处理器，点开能看到按钮的控制逻辑。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## O(1) 用户登录系统

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"Z 同学是经历过当年三星工厂连连失火，SSD 价格疯涨的苦日子的。\n\n直到如今，Z 同学还是会时常劝诫周围的同学，「1 字 1 位，当思来之不易。半 B 半 D，恒念物力维艰」。\n\n虽然周围的同学由于都是 Linux 用户协会的成员，并不太能理解 Z 同学口中的 D 其实是指 DWORD 的含义，但是大家出于对学长的尊敬还是一脸赞同地深有所悟。\n\n当然，厉行节约绝不是纸上空谈，Z 同学在写代码的过程中也确实对自己硬盘里每一个 bit 的占用都关心备至。比如公钥能用 ECC 绝不会使用 RSA；哈希能用 SHA-1 就不会用 SHA-256；加密能用 ECB 就绝对不用 GCM；压缩能用 ZPAQ 就不会用 LZMA。\n\n而最近，Z 同学在了解 Merkle Tree 之后，惊喜地发现用户登录系统其实可以摆脱掉那些冗杂的数据库系统，无论有多少用户都可以只占用 O(1) 的储存空间，这相当于给 SSD 的价格降低了 O(n) 倍的程度。\n\n「这样的话，既保证了系统的安全性，又再也不怕工厂失火了」，Z 同学一边这样想着，一边把新代码部署上生产环境。\n\n没有感受到任何痛苦，服务器被入侵得很安详。"} /-->

<!-- wp:block-lab/download {"url":"https://raw.githubusercontent.com/USTC-Hackergame/hackergame2023-writeups/master/official/O(1)%20%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E7%B3%BB%E7%BB%9F/files/o1login.py","text":"本题附件"} /-->

<!-- wp:paragraph -->

数据结构学的不扎实，看了半天才发现原来是用列表实现了二叉树的结构。。。相信大一时的我应该可以一眼看出来。随便画了个图来说明本题实现的merkle tree（忽略了hash值的排序）：

<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":8852,"sizeSlug":"large"} -->
![](images/tree.png)
<!-- /wp:image -->

<!-- wp:paragraph -->

每个注册用户会获得一串proof字符串，用以验证。这串proof是从该用户对应的叶子节点开始，一直上升到根节点的所有中间节点的兄弟节点的sha1值拼连接起来得到的。例如上图中user1的proof是h2+h6。验证用户是否在树上的逻辑是将proof拆开为多个字节串，然后每爬一层用掉一个proof计算sha1值，直到用完，若proof用完后得到的sha1值是Merkle Root，则验证通过。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

解出flag的条件是在题目阻止我们直接注册admin的条件下，使用admin账户通过认证。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

一开始的思路完全放在sha1碰撞上了，可以说是一个很大的误区。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

众所周知，虽然sha1确实能碰，但需要极高的算力，恐怕无论是在经济上还是在时间上都不太划算。。。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

后来又想着如果某个中间节点正好以"admin:"开头就很舒服，不过这好像就是挖矿了，算了一下"admin:"有6个字节，每个字节有256种可能，相当于平均得算256^6次才能出来一个，好像有点太多了。。。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

放了很长时间之后，把思路逆转了过来，既然"admin:"很难成为某个中间节点，那直接让它成为一个虚拟的叶子，然后我们手动去构造一个真实的叶子，让它是"admin:"这个虚拟叶子的父节点似乎就行。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

我们随便选择一个admin的密码，组合成一个字符串（由于后面的输入不能带换行符，这里password不能带换行符），例如我选择的密码是：';]NV1'，这个字符串只需要满足经过sha1以后没有冒号即可。（后面发现还需要一个能够进行utf-8 decode的条件，不过也容易随机出来）

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

我们再随机一个虚拟用户（虚拟叶子admin的虚拟兄弟）user2的密码pwd2，使得

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

sha1(user2 + ":" + pwd2) 有且仅有一个冒号，且能被utf-8 decode

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

构造完两个虚拟叶子后，我们用它们生成的父节点就会有且仅有一个冒号，此时我们就可以通过这个冒号将其拆分为一个真实的username和他的password，拿这个账户去注册。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

由于至少需要注册两个账号，我们再随便选一个幸运id进行注册。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

如此一来，只要admin节点可以经过一次proof得到我们注册的第一个用户的sha1，就可以顺着这位用户的proof来通过后续的验证。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

本题代码见[此文件](https://gist.github.com/windshadow233/d9c7d2af6e50c5319870e6ab8c33f646)。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

不过我的代码中没有判断两个hash的大小，考虑到题目中对左右hash值的大小顺序有要求，所以代码里应该需要额外判断一下。

<!-- /wp:paragraph -->

<!-- wp:heading -->

## 小 Z 的谜题

<!-- /wp:heading -->

<!-- wp:block-lab/introduce {"text":"方程之中\n\n变量如锁链相扣\n\n约束交织成网\n\n组合间蕴藏古老的秘密\n\n在变量的森林中追寻\n\n足迹遍历每一个角落\n\n在约束的花丛中舞蹈\n\n影子覆盖每一寸土地\n\n和谐之美指引着方向\n\n我们终将找到自己的答案"} /-->

<!-- wp:block-lab/download {"url":"https://github.com/USTC-Hackergame/hackergame2023-writeups/raw/master/official/%E5%B0%8F%20Z%20%E7%9A%84%E8%B0%9C%E9%A2%98/files/puzzle_of_z.py","text":"本题附件"} /-->

<!-- wp:paragraph -->

这道题比较有意思，我看了半天代码，发现这是一个"[精确覆盖问题](https://zh.wikipedia.org/wiki/%E7%B2%BE%E7%A1%AE%E8%A6%86%E7%9B%96%E9%97%AE%E9%A2%98)"要求在边长为5的立方体中恰好堆满一些给定尺寸、数量的长方体。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

这个问题确实已经有现成算法了，不过我还是掏出了z3。毕竟题目叫Puzzle of Z嘛！

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

注意到Stage 1的排序条件可以直接忽略（求出非排序的解以后手动排个序就好了），其他条件写成z3的约束非常容易。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

对于最后一个条件，相当于是统计每种形状长方体的数量。由于我们可以任意对解排序，所以可以直接写死一种顺序，在这个顺序下来写约束即可。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

不过z3有个特点是在相同的约束下，不管你跑多少次，它每次跑出来的都是同一个解，为了得到更多的解，可以在每次求出解后作为新的约束给它添加上去，然后再求解一次。以此循环，在得到800多个解以后，终于集齐了3个flag所需要的解。

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

解题代码见[此文件](https://gist.github.com/windshadow233/5743065783bbb16f2d19b352f1128ce3)

<!-- /wp:paragraph -->