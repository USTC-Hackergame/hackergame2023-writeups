# HackerGame 2023 部分题解

> Author: yezhiyi9670 #____，启动！ (239)
>
> [查看原仓库](https://github.com/yezhiyi9670/hackergame-2023-personal-writeup)
>
> [比赛平台](https://hack.lug.ustc.edu.cn/) · [排行榜存档](https://hg2023.lug.ustc.edu.cn/) · [官方题解仓库与题目源代码存档](https://github.com/USTC-Hackergame/hackergame2023-writeups)

这是我的 [USTC HackerGame](https://hack.lug.ustc.edu.cn/README.md) 2023 个人题解。此题解旨在详尽地记录题目内容、交互方式与我的思考/尝试过程。

此仓库在比赛期间建立并有过数次 commit（目的是备份数据），但是在比赛结束前并没有公开。

## 0. 目录

点击题目名称访问题目的题解内容。

|题号|标签|个人技能|题目|分值|开题时间|完成时间|
|-|-|-|-|-|-|-|
|1|web|trivial|[HackerGame 启动](./hackergame-start/README.md)|50/50|0-下午|0-12:08|
|2|general|search|[猫咪小测](./meow-exam/README.md)|250/250|0-下午|0-21:56|
|3|web|trivial|[更深更暗](./deep-dark/README.md)|100/100|0-下午|0-12:51|
|5|web|frontend|[赛博井字棋](./tictactoe/README.md)|150/150|0-下午|0-13:36|
|6|general|search|[奶奶的睡前 flag 故事](./grandma-story/README.md)|150/150|0-晚上|0-22:19|
|7|web|frontend|[组委会模拟器](./retract-messages/README.md)|200/200|0-下午|0-13:43|
|8|general|search|[虫](./insect/README.md)|150/150|0-晚上|1-11:41|
|9|general|search, xp|[JSON ⊂ YAML?](./json-in-yaml/README.md)|200/200|0-晚上|0-23:14|
|10|general|search|[Git? Git!](./git-object/README.md)|200/200|0-晚上|0-23:30|
|11|web|search, xp|[HTTP 集邮册](./http-collecting/README.md)|500/500|0-下午|1-10:06|
|14|general|automate|[🪐 高频率星球](./session-record/README.md)|200/200|1-上午|1-12:03|
|21|web|frontend, xp|[微积分计算小练习 2.0](./calculus-quiz-bot/README.md)|250/250|0-下午|1-11:12|
|▲| **---** | **---** | **结算 1** | **2350/2350** | **0-下午** | **1-12:58** |
|4|general|search|[旅行照片 3.0](./travel-photo/README.md)|450/450|0-晚上|5-21:46|
|12|general|search|[Docker for Everyone](./docker-escalation/README.md)|150/150|2-下午|2-16:52|
|13|math|trivial|[惜字如金 2.0](./xzrj/README.md)|200/200|2-下午|2-16:24|
|15|AI|search, luck|[~~🪐 小型大语言模型星球~~](./language-ai/README.md)|300/800|2-下午|4-21:07|
|16|general|automate|[🪐 流式星球](./pixel-stream/README.md)|200/200|2-下午|2-15:07|
|17|general|trivial, xp|[~~🪐 低带宽星球~~](./image-compression/README.md)|150/400|2-下午|2-13:56|
|18|general|xp|[~~Komm, süsser Flagge~~](./iptable-trust/README.md)|400/600|2-下午|4-01:43|
|19|binary|linux, search|[~~为什么要打开 /flag 😡~~](./why-open-flag/README.md)|200/450|2-晚上|2-22:27|
|20|binary|trytry|[异星歧途](./mindustry/README.md)|250/250|4-凌晨|4-16:36|
|▲| **---** | **---** | **结算 2** | **2300/3250** | **2-下午** | **5-02:53** |
|**\***| **===** | **===** | **合计** |**4650/5600**| **0-下午** | **5-02:53** |

题解中可能包含“我们”。这是习惯说法，并不是说“我们”有一个团队在一起做题。此文件在比赛结束前并未公开。题解中的 flag 仅为示例，请注意实际情况下部分题目的 flag 与选手 token 有关（称为动态 flag，是判断作弊的一种依据）。

个人技能：

- `trivial` 初学者应当知道的简单小技巧
- `search` 通过网络搜索获取信息
- `frontend` Web 前端相关问题（脚本、修改前端行为、伪造请求、XSS 攻击等）
- `xp` 需要一定的折腾或专业学习经验
- `automate` 题目本身可以手动完成，但简单的自动化代码可以减小工作量
- `trytry` 多试试

个人分类仅代表个人水平条件下的个人做法所涉及的核心难点，不表征题目的特性。
