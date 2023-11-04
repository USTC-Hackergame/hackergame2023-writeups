## Hackergame Writeup : A Newbie Perspective

### 0. 一些废话
**一些不适合出现在官方仓库的废话部分被转移到了 <https://blog.hanlin.press/2023/11/hackergame-writeup-2023/> ，欢迎赏脸关注（**

因为爆出来的都是简单题（**且很多包含运气成分**），所以有些不好截图的地方也不详细写了，出题人肯定写得比我详细，Writeup 大体上以做题顺序排列。

### 1. Hackergame 启动

按照 Hackergame 签到题的一贯尿性，进网页直接 F12 看请求。点提交按钮后注意到 `https://cnhktrz3k5nc.hack-challenge.lug.ustc.edu.cn:13202/?similarity=`

尝试改为 `similarity=1` 后：

![image-20231103203607113](http://cdn.r.iabc.work/picgo/202311032036147.png/compress)

盲猜没校验，直接  `similarity=1000` ，完成

![image-20231103203629549](http://cdn.r.iabc.work/picgo/202311032036567.png/compress)

![image-20231103203654259](http://cdn.r.iabc.work/picgo/202311032036303.png/compress)

### 2. 更深更暗

F12， 启动！

<kbd>Ctrl</kbd> + <kbd>F</kbd> 搜索，启动！

![image-20231103203848091](http://cdn.r.iabc.work/picgo/202311032038123.png/compress)

跳过猫咪小测直接来这题，抢到一血了，开心。

![image-20231103203922539](http://cdn.r.iabc.work/picgo/202311032039563.png/compress)



### 3. 猫咪小测

> 1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？**（30 分）**
>
>    提示：是一个非负整数。

1. 书目检索系统：<http://opac.lib.ustc.edu.cn/ ，用书名搜索后馆藏如下，由题意锁定**西区外文书库**。

   ![image-20231028120408291](http://cdn.r.iabc.work/picgo/202311032042590.jpeg/compress)

   

2. 去科大图书馆的[**馆藏分布**](https://lib.ustc.edu.cn/%e6%9c%ac%e9%a6%86%e6%a6%82%e5%86%b5/%e9%a6%86%e8%97%8f%e5%88%86%e5%b8%83/) ，可得知各书库的具体位置。`12`.

   
   
   ![image-20231103204344275](http://cdn.r.iabc.work/picgo/202311032043298.png/compress)

> 2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？**（30 分）**
>
>    提示：是一个非负整数。

Google Bard ，启动！

![image-20231028121254073](http://cdn.r.iabc.work/picgo/202311032120184.jpeg/compress)

典型的AI幻觉，但是出现了正确的文章名。

到 arxiv 去搜，看到了 https://arxiv.org/abs/2303.17626

高中阅读理解环节，得答案 `23`  .

> 3. 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？**（20 分）**
>    提示：输入格式为 CONFIG_XXXXX，如 CONFIG_SCHED_SMT。

去 GitHub 爆搜源码。

![image-20231028121535393](http://cdn.r.iabc.work/picgo/202311041238769.jpeg/compress)

<https://github.com/search?q=repo%3Atorvalds%2Flinux%20config%20bbr&type=code>

`CONFIG_TCP_CONG_BBR` .

> 4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？**（20 分）**
>    提示：会议的大写英文简称，比如 ISCA、CCS、ICML。

直接上图：

![image-20231028122014148](http://cdn.r.iabc.work/picgo/202310281220184.png/compress)

[https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-**ECOOP**-2023-44.pdf](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)

`ECOOP`.

### 4. 虫

常规 SSTV 题，**推荐使用 RX-SSTV** ，笔记本扬声器外放即可解码。

![image-20231028131846908](http://cdn.r.iabc.work/picgo/202310281318974.png/compress)

`flag{SSssTV_y0u_W4NNa_HaV3_4_trY}`



### 5. 奶奶的睡前 flag 故事

题面描述**谷歌的『亲儿子』**和**连系统都没心思升级**直接激发了 DNA，去搜了搜相关新闻。

![image-20231028131403064](http://cdn.r.iabc.work/picgo/202310281314118.png/compress)

得到一个工具 <https://acropalypse.app/> ，传上截图。题面说是**老手机**，所以直接往最老的（Pixel 3）选。

![image-20231028131545015](http://cdn.r.iabc.work/picgo/202310281315050.png/compress)

`flag{sh1nj1ru_k0k0r0_4nata_m4h0}`



### 6. 组委会模拟器

正解看官方题解，我是用 Python requests 的大sb（

![image-20231104125126723](http://cdn.r.iabc.work/picgo/202311041251754.png/compress)

```
import requests
import json
import re
import time

sess = requests.Session()
sess.get(
    "http://202.38.93.111:10021/api/checkToken?token="
)
# remember to modify it

# getMessage
mess = sess.post("http://202.38.93.111:10021/api/getMessages").json()
servertime_obj = time.strptime(mess["server_starttime"], "%Y-%m-%dT%H:%M:%S.%f%z")
servertime = int(round(time.mktime(servertime_obj) * 1000.0)) + 28800050

# print(servertime)

id = 0
totaldelay = 0
for i in mess["messages"]:
    totaldelay = int(float(i["delay"]) * 1000)
    nowtime = int(time.time() * 1000)
    # print(int(servertime) + totaldelay)
    print(
        "{} + {} = {} : {}".format(
            servertime, totaldelay, servertime + totaldelay, nowtime
        )
    )
    if servertime + totaldelay > nowtime:
        # print((servertime + totaldelay - nowtime))
        time.sleep((servertime + totaldelay - nowtime) / 1000)
    if re.search("hack\[.*\]", i["text"]):
        payload = {
            "id": id,
        }
        hders = {"Content-Type": "application/json"}
        print(
            sess.post(
                "http://202.38.93.111:10021/api/deleteMessage",
                headers=hders,
                data=json.dumps(payload),
            ).text
        )
    id += 1
print(sess.post("http://202.38.93.111:10021/api/getflag").text)

```

![image-20231104125505987](http://cdn.r.iabc.work/picgo/202311041255016.png/compress)

`flag{Web_pr0gra_mm1ng_b3ca854fa9_15fun}`

### 7. 赛博井字棋

井字棋本身没坑，但以正常思维对抗的话，最多平局。

F12 右键相关请求可以复制 fetch，在隔壁 console 改起来很容易。

注意到输入没做校验，可以把对方下的棋**覆盖**。

请求里改一个坐标，结束。

![image-20231104125751859](http://cdn.r.iabc.work/picgo/202311041257930.png/compress)



### 8. Git? Git!

和前面某一年 `git push -f` 那题区别开来，这题没 flush 掉分支，只是没推送。

查看 `.git/logs/ref/heads/main` 发现中间有一条疑似 commit：

```
<54608551+PRO-2684@users.noreply.github.com> 1698306875 +0800	clone: from https://github.com/dair-ai/ML-Course-Notes.git
15fd0a13eb46c39f34cfc0dfb4757ad23a23d026 505e1a3f446c23f31807a117e860f57cb5b5bb79 some_english_postgraduate <some_english_postgraduate@none-exist.com> 1698307060 +0800	commit: Trim trailing spaces
505e1a3f446c23f31807a117e860f57cb5b5bb79 15fd0a13eb46c39f34cfc0dfb4757ad23a23d026 some_english_postgraduate <some_english_postgraduate@none-exist.com> 1698307092 +0800	reset: moving to HEAD~
15fd0a13eb46c39f34cfc0dfb4757ad23a23d026 ea49f0cd3d36edb2965f89581b11151959d20991 some_english_postgraduate <some_english_postgraduate@none-exist.com> 1698307103 +0800	commit: Trim trailing spaces
```

`git checkout 505e1a3f446c23f31807a117e860f57cb5b5bb79`，可在主文件中见到 flag .

![image-20231028160501043](http://cdn.r.iabc.work/picgo/202311041309167.jpeg/compress)



### 9. Docker for Everyone

这一幕我自己品鉴过了，privileged 啥都能干，端下去吧。

![image-20231028172751152](http://cdn.r.iabc.work/picgo/202310281727220.png/compress)



### 10. 旅行照片 3.0

兜兜转转回到了这道题，**快到的饭点和手机上的红色软件为这道题埋下了伏笔**。

#### 开始推断出的信息

- **上午**：[小柴昌俊](https://zh.wikipedia.org/wiki/%E5%B0%8F%E6%9F%B4%E6%98%8C%E4%BF%8A) 的诺贝尔奖牌 -> 地点在 **东京大学** 附近。
- **中午**：
  - 图一：最前方最显眼的吊牌「**STATPHYS28**」-> <https://statphys28.org/>
  - 图二：在东京大学附近按谷歌卫星地图与街景搜索，基本上锁定**上野公园**。

![image-20231104132047048](http://cdn.r.iabc.work/picgo/202311041320198.png/compress)

![image-20231104132100400](http://cdn.r.iabc.work/picgo/202311041321605.png/compress)



因题面中提到了学长的学术之旅，因此接下来重点关注图二的 **STATPHYS28**。打开主页，留意到：

- 首页时间：2023 年 8 月 7 日-11 日，锁定第一题时间范围。
- On-site 地点：东京大学，与前文推断信息吻合。

- News 栏[Participant Instruction: On-site Presentation Instruction](https://statphys28.org/instonsite.html) 得知 On-site 地点 **Yasuda Auditorium** 即 **安田讲堂** ，锁定第五题。

![image-20231104132613071](http://cdn.r.iabc.work/picgo/202311041326098.png/compress)

再回头看诺贝尔奖牌，按照人肉搜索法找到了[康斯坦丁·诺沃肖洛夫](https://zh.wikipedia.org/wiki/%E5%BA%B7%E6%96%AF%E5%9D%A6%E4%B8%81%C2%B7%E8%AF%BA%E6%B2%83%E8%82%96%E6%B4%9B%E5%A4%AB) ，但是不知道曼彻斯特大学研究所简称，这条线暂时中断。



#### 思路打开

接下来打算动一点社工的方法，去 B 站找点旅游视频，看看能不能漏点相关情报。

首先发现上野公园旁边有**上野动物园**和**东京国立博物馆**：

![image-20231104133237642](http://cdn.r.iabc.work/picgo/202311041332856.png/compress)

然后发现了上野站的吉祥物是**熊猫**。

![image-20231104133715928](http://cdn.r.iabc.work/picgo/202311041337162.png/compress)

以上是答案猜测，完赛后在群里交流才发现这题的关键字可以直接在 Twitter 上搜到，挺亏的。

![image-20231104133940579](http://cdn.r.iabc.work/picgo/202311041339629.png/compress)

线索又一次停滞，到饭点了，出门买饭。去小红书上一搜关键词，大开眼界：

![image-20231104134226778](http://cdn.r.iabc.work/picgo/202311041342240.png/compress)

回到小红书首页，这条视频**出现在了首页**。

![image-20231104134456571](http://cdn.r.iabc.work/picgo/202311041344189.png/compress)

抱着试试看的心态填上了第 5-6 题，过了，我超！

![image-20231028175553318](http://cdn.r.iabc.work/picgo/202310281755371.png/compress)



#### 顺理成章

不懂日文又忽视了小红书的潜质，痛定思痛的我决定来小红书抽奖：

![image-20231104134802953](http://cdn.r.iabc.work/picgo/202311041348128.png/compress)

![image-20231104134834199](http://cdn.r.iabc.work/picgo/202311041348249.png/compress)

<https://www.xiaohongshu.com/explore/64c8eb40000000000800c394>

得知八月第一个活动，以「全国梅酒まつりin東京2023」为关键词回谷歌搜索，找到主页，向下翻，看到了「Staff 募集」：<https://umeshu-matsuri.jp/tokyo_staff/> ，得到问卷编号 `[S495584522`](https://ws.formzu.net/dist/S495584522/)

![image-20231104135336475](http://cdn.r.iabc.work/picgo/202311041353545.png/compress)

来到东京国立博物馆网站，直奔**Tickets**：<https://www.tnm.jp/modules/r_free_page/index.php?id=113#ticket>

![image-20231104135627953](http://cdn.r.iabc.work/picgo/202311041356048.png/compress)

三个数都试一遍，原本以为是 500 ，结果发现是 0.

![image-20231028180205028](http://cdn.r.iabc.work/picgo/202310281802099.png/compress)



第一问的日期也基本上锁定，继续回小红书抽奖：

![image-20231104135944061](http://cdn.r.iabc.work/picgo/202311041359232.png/compress)

![image-20231104135949301](http://cdn.r.iabc.work/picgo/202311041359774.png/compress)

填上 ICRR ，过了，感谢小红书。

![image-20231028175541842](http://cdn.r.iabc.work/picgo/202310281755933.png/compress)



----------

后记：跌跌撞撞过了后发了条频道庆祝下，惊动了某个 Staff.

![image-20231104140216978](http://cdn.r.iabc.work/picgo/202311041402002.png/compress)

![image-20231104140224030](http://cdn.r.iabc.work/picgo/202311041402056.png/compress)



### 11. JSON ⊂ YAML?

整体做题方法：没基础，去 Hackernews 看[骂战](https://news.ycombinator.com/item?id=30052128)，看了半天没结果。

最终还是 <https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files> 说明了一切。

- YAML 1.1：浮点数解析差异

- YAML 1.2：不允许出现重复的 key



二合一即可得到一穿二的 payload：

```
{"233": 12345e999, "233": 12345e999}
```

![image-20231104140657798](http://cdn.r.iabc.work/picgo/202311041406830.png/compress)



后记：听说YAML 的 key 长度长了也不行，结果塞进去后发现 Python 先报错了。

### 12. HTTP 集邮册

因为只碰出 12 个状态码，还挺失败的，这题直接看 [官方题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/tree/master/official/HTTP%20%E9%9B%86%E9%82%AE%E5%86%8C) 吧。



### 13. 惜字如金 2.0

因为代码逻辑非常清晰，所以这题是水课的时候静态分析的。

由 `get_cod_dict` 里的 `check_equals`  和主函数中的 `decrypt_data` 逻辑综合分析，得出 `cod_dict` 中的每一组应为 **24** 长度。

于是尝试对原始数据进行「反惜字如金」化处理：

- 首先去除所有 `check_equals` 校验，将 `cod_dict` 后每行加上 `e`
- 参考 `decrypt_data` 所在坐标，尝试将 `flag{` 和 `}` 与原始数据对齐。
  - 对齐方式：逐字符对齐，判断偏移关系。
  - 通过「在整行后加e」与「在目标字符前加字符」来操作目标字符的位移。
  - 每行的改动不超过1字符。

改动后的原始数据：

>nymeh1niwemflcir}echaet**e**
>a3g7}kidgojernoetlsup?h**e**
>u**l**lw!f5soadrhwnrsnstnoeq
>c**t**t{l-findiehaai{oveatas
>ty9kxbors**s**zstguyd?!blm-p

```python
def get_cod_dict():
    # prepar th cod dict
    cod_dict = []
    cod_dict += ['nymeh1niwemflcir}echaete']
    cod_dict += ['a3g7}kidgojernoetlsup?he']
    cod_dict += ['ullw!f5soadrhwnrsnstnoeq']
    cod_dict += ['ctt{l-findiehaai{oveatas']
    cod_dict += ['ty9kxborsszstguyd?!blm-p']
    check_equals(set(len(s) for s in cod_dict), {24})
    return ''.join(cod_dict)
```

运行后可得 `flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}`



### 14. 高频率星球

搜索得 [asciinema](https://asciinema.org/) 存在 cat 功能，可以无视时间序列一口气输出全部数据。

直接 `asciinema cat asciinema_restore.rec > 1111.js` 发现还有控制符没删。

本着不重复造轮子的原则，在 Gitlab 找到个神器 [ANSIFILTER](https://gitlab.com/saalen/ansifilter) ，还进了包，`apt install` 即装即用。

接下来进入半人工半自动流程：

首先粗加工一遍：

```bash
 asciinema cat asciinema_restore.rec | ansifilter > parsed.js
```

然后找到一个带语法高亮和检查的编辑器，比如装好扩展和 `clang-format` 的 VS Code。

去掉头尾的无用信息，留下中间的 js 部分。会发现有一大串报错，多半是控制符没删干净导致的。

![image-20231104143350662](http://cdn.r.iabc.work/picgo/202311041433703.png/compress)

以纯文本方式打开 `asciinema_restore.rec` ，通过搜索确定报错代码原位置，直接把多出来的字符删除。

![image-20231104144905463](http://cdn.r.iabc.work/picgo/202311041449534.png/compress)

在每次替换为空后保存并重新运行格式化，检查下一处报错，如此操作，直到报错全部消失，代码正常格式化为止。

在实践中，我删掉了`ESESC[6~`，一个 `~` 和若干 `6~` ，最终顺利消除全部报错。

![image-20231104145048085](http://cdn.r.iabc.work/picgo/202311041450121.png/compress)

运行 `node parsed.js` ，得到 `flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}`



### 15. 低带宽星球

第一题使用 [tinypng.com](https://tinypng.com/) 压缩，即可获得 Flag `flag{A1ot0f_t0015_is_available_to_compre55_PNG}`.

![image-20231104145342690](http://cdn.r.iabc.work/picgo/202311041453721.png/compress)

第二题手操了一遍发现 svg 也不好满足要求，放弃。



### 16. 小型大语言模型星球

第一段长度限制极宽松，所以我直接去找了训练集。

<https://huggingface.co/datasets/roneneldan/TinyStories>

在 `TinyStories-train.txt` 中 以  `you are smart` 为关键词搜索，并将其前面的文段粘贴进去验证。

很容易就能找到一段 `flag{1-7hink-y0U-4R3-rEAllY-rE4lly-SmARt}`：

```
"You are a brave girl, Lily. You are not silly, 
```

![image-20231104145801030](http://cdn.r.iabc.work/picgo/202311041458079.png/compress)



第二段因为长度较短也比较好猜，只是我水课上试出来个 **`accept*`** 直接爆了`flag{y0U-are-ACcEP7ed-7O-c0NTiNuE-TH3-G4m3}`：

![image-20231104145927532](http://cdn.r.iabc.work/picgo/202311041459611.png/compress)



因为官方环境限频率，所以拖下环境来本地搭了个脚手架，把代码附上：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
from tqdm import tqdm, trange
model = AutoModelForCausalLM.from_pretrained("../TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("../TinyStories-33M")

def get(prompt):
	input_ids = tokenizer.encode(prompt, return_tensors="pt")
	print(tokenizer.tokenize(prompt))
	output = model.generate(input_ids, max_length = len(prompt)+30, num_beams=1, pad_token_id=tokenizer.eos_token_id)
	output_text = tokenizer.decode(output[0], skip_special_tokens=True)
	print(output_text)
	return output_text
	

while True:
	s = input("> ")
	get(s)
```



### 17. 流式星球

因为已知流式文件被删去了一小段，就写了段三脚猫 `C++`， 直接爆破可能的 pad 和分辨率：

```cpp
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

const unsigned long long fsize = 135146688;

vector<unsigned long long> libpad, libheight, libwidth;

int main() {
    unsigned long long pad = 0;
    unsigned long long height = 1;
    unsigned long long width = 1;
    for (pad = 0; pad <= 100; pad++) {
        for (height = 100; height <= 2000; height++) {
            for (width = 100; width <= 2000; width++) {
                if ((pad + fsize) % (height * width * 3) == 0) {
                    unsigned long long frame =
                        (pad + fsize) / (height * width * 3);
                    if (frame > 1 && frame <= 100) {
                        libpad.push_back(pad);
                        libheight.push_back(height);
                        libwidth.push_back(width);
                    }
                }
            }
        }
    }
    for (auto i : libpad) {
        cout << i << ",";
    }
    cout << endl;
    for (auto i : libheight) {
        cout << i << ",";
    }
    cout << endl;
    for (auto i : libwidth) {
        cout << i << ",";
    }
    cout << endl;
    return 0;
}
```



C++ 的输出直接复制到隔壁 Python ，吐每一个爆破结果的**第 5 帧**：

```python
import cv2
import numpy as np
import random
from tqdm import tqdm, trange
libpad = [0,0,0,0,0,0,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93]
libheight = [409,818,1636,1721,1721,1721,349,461,461,698,698,922,922,922,1396,1396,1745,1745,1745,1844,1844,1844,342,402,603,603,684,804,983,983,983,983,983,1206,1206,1273,1273,1966,1966,1966,1966,1966,417,417,427,483,671,759,973,973,973,1281,1403,1403,1403,1529,1529,1529,1529,1771]
libweight = [1721,1721,1721,409,818,1636,1844,1396,1745,922,1844,698,1396,1745,461,922,461,922,1844,349,698,1745,1966,1966,983,1966,983,983,603,684,804,1206,1273,983,1966,983,1966,342,402,603,1206,1273,1403,1771,1529,1529,973,973,671,759,1403,1529,417,973,1529,427,483,1281,1403,417]

def extract_video(file):
    buffer = np.fromfile(file, dtype=np.uint8)
    lenlib = len(libpad)
    picPath = "pics-batch"
    for i in trange(lenlib):
        ht = libheight[i]
        wd = libweight[i]
        pad = libpad[i]
        frame_count = (len(buffer) + pad) // (ht * wd * 3)
        backup = buffer.copy()
        backup = np.pad(backup, (0, pad), mode="constant")
        backup = backup.reshape((frame_count, ht, wd, 3))
        backup = backup.astype(np.uint8)
        cv2.imwrite(f"{picPath}/{ht}-{wd}-{pad}.jpg", backup[5])

if __name__ == "__main__":
    with open("video.bin", "rb") as input:
        extract_video(input)
```

然后直接使用**人眼观测法** 找看着最顺眼的：

![image-20231104151002545](http://cdn.r.iabc.work/picgo/202311041510607.png/compress)

当时选中了 `1529-427-93.jpg`，直接把参数抄回去导图片：

```
def extract_video(file):
    buffer = np.fromfile(file, dtype=np.uint8)

    ht = 1529
    wd = 427
    pad = 93
    frame_count = (len(buffer) + pad) // (ht * wd * 3)
    buffer = np.pad(buffer, (0, pad), mode="constant")
    buffer = buffer.reshape((frame_count, ht, wd, 3))
    buffer = buffer.astype(np.uint8)
    picPath = "pics"
    for i in range(frame_count):
        print(f"Writing frame {i}")
        cv2.imwrite(f"{picPath}/frame{i}.jpg", buffer[i])
```

深夜做这个给气笑了：

![image-20231104151115092](http://cdn.r.iabc.work/picgo/202311041511170.png/compress)

![image-20231104151136193](http://cdn.r.iabc.work/picgo/202311041511221.png/compress)

`flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}`

### 18. Komm, süsser Flagge

问了问 GPT ，GPT 说把数据包切分开来发出去就行。

好像还因为非预期解把第二问给爆了，详见[官方题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/tree/master/official/Komm%2C%20s%C3%BCsser%20Flagge)吧。

```python
import socket
import time

server_ip = "202.38.93.111"
server_port = 18080
# server_port = 18081
token = ""

post_part1 = "PO"
post_part2 = "ST / HTTP/1.1\r\n"
post_part2 += "Host: {}\r\n".format(server_ip)
post_part2 += "Content-Type: application/x-www-form-urlencoded\r\n"
post_part2 += "Content-Length: {}\r\n\r\n".format(len(token))
post_part2 += str(token)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((server_ip, server_port))

try:
    # Send the first part of the "POST" method
    s.sendall(post_part1.encode())
    time.sleep(1)
    # Send the rest of the request
    s.sendall(post_part2.encode())

    # Receive the response
    response = s.recv(4096)
    print(response.decode())
finally:
    s.close()
```



### 19.  LD_PRELOAD, love!

听说因为 `@taoky` 老师没删干净库调用，被有些人钻了空子（`popen`）当非预期解爆了。

而我的非预期解显得更加离谱：

```cpp
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream infile;
    infile.open("/flag");
    cout << infile.rdbuf() << endl;
    return 0;
}
```

![image-20231030151321050](http://cdn.r.iabc.work/picgo/202311041518991.jpeg/compress)

啊？



### 20. 异星歧途

有趣的手算模拟题，理解地图需要明白两个事：

- 机器状态被微型处理器通过开关控制。

  ![image-20231104152244681](http://cdn.r.iabc.work/picgo/202311041522766.png/compress)

- 微型处理器可以进行逻辑运算与判断。

  ![image-20231104152315698](http://cdn.r.iabc.work/picgo/202311041523803.png/compress)

理解了这些，就可以在平板上手算了。

#### 第一组机器

要想让 `generator1` 启用（即不发生跳转），前面的所有条件必须一起反选。

![image-20231104152505601](http://cdn.r.iabc.work/picgo/202311041525662.png/compress)

得序列 `10100101`

#### 第二组机器

更复杂的逻辑推断，因为不想再经历一遍所以直接上做题笔记。

![image-20231104152724584](http://cdn.r.iabc.work/picgo/202311041527663.png/compress)

得序列 `11000100`

#### 第三组机器

需要强调的点：

- 题目询问的是**最终序列**，开关顺序和**中间状态**都是不重要的。
- 让反应堆稳定运行：有能源、有散热（冷冻液）
  - 有冷冻液的条件：冷冻液混合器里有输入、有电

因此：

- 需要**左侧**输送带正常运行、右侧输送带未被切断 ：`sw1 = 1`、`sw2 = 0`
- 反应堆正常运行：`sw3=0` （注意一开始调试时应为1，防止反应堆没有散热自己炸掉）
- 水和反应液不能流掉：`sw4=0`
- 正常分解产生冷冻液：两台机器开启 -> `sw5=1` 、 `sw6=1`
- **熔毁炮塔不能启用**，否则会耗尽电量导致无法散热：`sw7=0`
- `sw8=0` 以防不能打开的机器被打开。

得序列 `10001100`

#### 第四组机器

观察到电量输出为左下角，故建议从左下角逆向推导。

每一个小块与组合逻辑的思想类似，注意操作的时候有延迟。

更详细的参考[官方题解](https://github.com/USTC-Hackergame/hackergame2023-writeups/tree/master/official/%E5%BC%82%E6%98%9F%E6%AD%A7%E9%80%94) 吧。



得序列 `01110111`

最终序列：`10100101 11000100 10001100 01110111`



-------

### FF. 后记

仍旧是感谢 Miscgame 让我能够在今年拥有一个在榜上的参与感，就是这几天光打 Hackergame ，只有一天出了勤还掉了 50 名，难受。
