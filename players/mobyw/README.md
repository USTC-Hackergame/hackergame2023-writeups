# Hackergame 2023 Writeups

## Hackergame 启动

检查页面元素可以看到表单提交到的地址：

```html
<form action="" method="GET">
    <input type="hidden" id="similarity-value" name="similarity">
    <p>
        <span id="similarity"></span>
    </p>
    <p>
        <input type="submit" class="btn btn-success" id="btn-submit" value="提交">
    </p>
</form>
```

删去 `type="hidden"`，会显示一个输入框，输入 `100` 提交，即可获取 flag。

## 猫咪小测

### 第一题

> 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？
>
> 提示：是一个非负整数。

使用 Bing 搜索「中国科学技术大学 西区图书馆」，可以得到 [西区图书馆简介 | 中国科学技术大学图书馆](https://lib.ustc.edu.cn/%E6%9C%AC%E9%A6%86%E6%A6%82%E5%86%B5/%E5%9B%BE%E4%B9%A6%E9%A6%86%E6%A6%82%E5%86%B5%E5%85%B6%E4%BB%96%E6%96%87%E6%A1%A3/%E8%A5%BF%E5%8C%BA%E5%9B%BE%E4%B9%A6%E9%A6%86%E7%AE%80%E4%BB%8B/)，网页中有以下内容：

> 外文书库
>
> 位置：12 楼
>
> 馆藏：外文图书约 4.6 万种 9 万册。

可得上述外文图书的楼层是 12 楼。

### 第二题

> 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？
>
> 提示：是一个非负整数。

使用 Bing 搜索「"upper limit" chickens "observable universe" site:arxiv.org」，可以得到 [Nuggets of Wisdom: Determining an Upper Limit on the Number Density of Chickens in the Universe](https://arxiv.org/abs/2303.17626)，下载 [PDF](https://arxiv.org/pdf/2303.17626.pdf) 查看，CONCLUSION 章节第一段如下：

> In this work we have constrained the upper limit on the Chicken Density Function (CDF), the number density of unobserved chickens in the observable Universe. We have followed Solar System, interstellar, intergalactic, and cosmological considerations. We take the most restrictive of these limits to be the current best upper limit: 10<sup>23</sup> chickens per cubic parsec (10 million per cubic AU), constrained by the photometric precision of tip-of-red-giant-branch stars in faraway galaxies.

可得作者计算出的鸡密度函数的上限为 10 的 23 次方每立方秒差距。

### 第三题

> 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？
>
> 提示：输入格式为 `CONFIG_XXXXX`，如 `CONFIG_SCHED_SMT`。

使用 Bing 搜索「Linux TCP BBR compile "CONFIG\_"」，可以得到很多含有对应信息的网页，如 [BBR TCP - CONFIG_TCP_CONG_BBR](https://www.kernelconfig.io/config_tcp_cong_bbr)，可得内核选项为 `CONFIG_TCP_CONG_BBR`。

### 第四题

> 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？（20 分）
>
> 提示：会议的大写英文简称，比如 ISCA、CCS、ICML。

搜索「python "type hint\*" "mypy" "infinite loop"」，过滤关键词匹配的网页（使用 Google 可能比 Bing 更容易找到），可以得到 [Python type hints are Turing complete | Hacker News](https://news.ycombinator.com/item?id=32779296)，[Python Type Hints Are Turing Complete - DROPS](https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf)。

查看第二个链接中的文章可得会议名称为 ECOOP，该文章的 Introduction 部分如下：

> Python enhancement proposal (PEP) 484 introduced optional type hints to the Python programming language, together with a full-blown gradual type system. Tools such as Mypy use type hints to type-check Python programs. **Certain programs, however, cause Mypy to enter an infinite loop (we show an example below)**. We argue that the reason behind these failures is not a Mypy bug, but a deeper issue in the PEP 484 type system. We use Grigore’s reduction from Turing machines (TMs) to nominal subtyping with variance to prove that Python type hints are, in fact, Turing complete. In other words, checking whether a Python program is correctly typed is as hard as the halting problem.

## 旅行照片 3.0

\* 本题中搜索引擎为 Bing（国际版） 或 Google。仅给出与官方题解有差异的解法。

### 第一题

> 你还记得与学长见面这天是哪一天吗？

通过学术会议确定时间的方法参考官方题解，此处给出仅通过文字推断的方法。

根据：

> 你的学长去留学了，这一走短时间内怕是回不来了。于是，你在**今年暑假**来了一场计划已久的旅行，并顺路探望了这位久别的学长。翻阅当天拍下的照片， 种种回忆和感慨油然而生。

确定时间范围是 2023 年 7-8 月。

找到可能暗示具体时间的描述：

> 当你们走到一座博物馆前时， **马路对面的喷泉**和它周围的景色引起了你的注意。**下午**，**白色的帐篷**里**即将**举办一场**大型活动**，人们忙碌的身影穿梭其中，充满了期待与热情。

只需找到活动即可找到日期，首先确定活动地点，根据以下对地点转移的描述：

> 离开校园后，你和学长走到了附近的一家拉面馆用餐。
>
> 当你们走到一座博物馆前时， 马路对面的喷泉和它周围的景色引起了你的注意。
>
> 在参观完博物馆后，学长陪你走到了上野站。

由于地点的转移都是步行，可以推测博物馆、喷泉大概率在上野站周围，使用地图软件寻找上野站周围在博物馆对面的喷泉，可以找到是在上野公园。

- [百度地图](https://j.map.baidu.com/bb/4yzK)
- [Google Map](https://maps.app.goo.gl/riTzu6ExDgPzKoJp8)

搜索上野公园活动信息可以找到是 [上野恩賜公園 Ueno Park 公式<ruby>ホーム<rt>home</rt></ruby><ruby>ページ<rt>page</rt></ruby>](https://www.kensetsu.metro.tokyo.lg.jp/jimusho/toubuk/ueno/index_top.html)，打开该网站。

\* 由于该网站没有提供除日语外其他语言的主页之外的界面，如果不熟悉日语，可以使用 [片假名终结者](https://github.com/Arnie97/katakana-terminator) 之类的插件通过英语和汉字阅读，基本满足检索需求，本文档中直接标注了平假名对应的英文。

点击日语首页导航栏的「<ruby>イベント<rt>event</rt></ruby>案内」，可见正在进行的活动，没有提供历史数据，故再次搜索「上野公园 <ruby>イベント<rt>event</rt></ruby>」，得到另一个网站 [上野公園<ruby>イベント<rt>event</rt></ruby>＆<ruby>フェス<rt>festival</rt></ruby>2023 情報](https://www.uenopark.info/)，点击网页右侧的「過去の<ruby>イベント<rt>event</rt></ruby>」可以查看历史活动信息，选择 [2023](https://www.uenopark.info/ad2023/) 查看 7-8 月的活动中筛选在喷泉广场举行的，且在下午开始的大型活动，可以得到是 2023 年 8 月 10 日 15 时开始举行的「全国梅酒まつり in 東京」。

![全国梅酒まつりin東京](https://www.uenopark.info/wp-content/uploads/2023/07/IMG_8775.jpeg)

所以见面的日期为 2023 年 8 月 10 日。

### 第二题

> 在学校该展厅展示的所有同种金色奖牌的得主中，出生最晚者获奖时所在的研究所缩写是什么？

参考官方题解。

### 第三题

> 帐篷中活动招募志愿者时用于收集报名信息的在线问卷的编号（以字母 S 开头后接数字）是多少？

搜索「全国梅酒まつり in 東京 volunteer」，得到 [<ruby>ボランティア<rt>volunteer</rt></ruby> STAFF 大募集](https://umeshu-matsuri.jp/tokyo_staff/) 页面，可得到表单链接（数字已隐去）。

> 下記の応募<ruby>フォーム<rt>form</rt></ruby>から<ruby>エントリー<rt>entry</rt></ruby>してください。
>
> https://ws.formzu.net/dist/Sxxxxxxxxx/

### 第四题

> 学长购买自己的博物馆门票时，花费了多少日元？

根据地图得知上野公园喷泉马路对面为东京国立博物馆，搜索「东京国立博物馆」得到官方网站，在网站了解到大学生门票价是 500 日元/人，提交后显示错误，猜测为可能有特殊照顾政策。在「教育」标签页最后得知存在「校园会员」政策，所以门票价格可能为 0。

> 为了通过博物馆促进学生们对文物和日本文化的理解，我们设立了“东京国立博物馆校园会员”制度。成为会员的大学和专科学校的学生、教师们可以免费无限次参观综合文化展（常设展），另外还可享受特展门票和各种活动等的折扣服务。

如果想要验证可以修改网站语言为日语，即可显示出 [<ruby>キャンパス<rt>campus</rt></ruby><ruby>メンバーズ<rt>members</rt></ruby>の<ruby>ページへ<rt>page</rt></ruby>](https://www.tnm.jp/modules/r_free_page/index.php?id=167) 超链接（如果无法直接打开该网页，请先设置网站语言为日语），进入可以看到东京大学在列表内，得证。

### 第五题

> 学长当天晚上需要在哪栋标志性建筑物的附近集合呢？（请用简体中文回答，四个汉字）

参考官方题解。

### 第六题

> 进站时，你在 JR 上野站中央检票口外看到「ボタン＆カフリンクス」活动正在销售动物周边商品，该活动张贴的粉色背景海报上是什么动物（记作 A，两个汉字）？ 在出站处附近建筑的屋顶广告牌上，每小时都会顽皮出现的那只 3D 动物是什么品种？（记作 B，三个汉字）？（格式：A-B）

第一小问使用 Google 图片搜索「ボタン＆カフリンクス 上野」，寻找粉色背景海报即可得知是熊猫，时间与当天匹配。或使用 X/Twitter 搜索「ボタン＆カフリンクス」，可得到更多现场图片与视频。

![ボタン＆カフリンクス](https://image.space.rakuten.co.jp/d/strg/ctrl/9/c85f17f3efa6ec542ad0e33462ccb5ffe28ce004.79.9.9.3.jpeg)

第二小问需要先确定出站时的地铁站，根据随后一张图片搜索得知地点是任天堂东京官方商店，附近的电车为 JR 涩谷站。搜索「JR 涩谷站 3D 动物」或「JR 渋谷駅 3D 動物」，可得是秋田犬。

## 组委会模拟器

直接构造撤回消息对应的 HTTP 请求，按照需要的延时时间发送即可。

Python 异步代码示例：

_dependencies_

```
python = "^3.8"
httpx = ">=0.20.0,<1.0.0"
loguru = ">=0.6.0,<1.0.0"
```

```python
import re
from asyncio import AbstractEventLoop, gather, get_event_loop, sleep
from typing import Any, Coroutine, Dict, List, Literal, Union

from httpx import AsyncClient, Response
from loguru import logger

TOKEN = "114514:asdfgh="
HOST = "http://server:1919"

CHECK_TOKEN_URL = f"{HOST}/api/checkToken"
GET_MESSAGE_URL = f"{HOST}/api/getMessages"
DELETE_MESSAGE_URL = f"{HOST}/api/deleteMessage"
GET_FLAG_URL = f"{HOST}/api/getflag"

PATTERN = re.compile(r"hack\[[a-z]+\]")


async def request(
    method: Literal["GET", "POST"],
    url: str,
    headers: Dict[str, str] = {},
    params: Dict[str, Any] = {},
    json: Dict[str, Any] = {},
) -> Response:
    async with AsyncClient(headers=headers, timeout=10) as client:
        if method == "GET":
            responce: Response = await client.get(url, params=params)
        elif method == "POST":
            responce: Response = await client.post(url, json=json)
        if responce.is_error:
            raise RuntimeError(f"Request error: {responce.status_code}")
        return responce


async def set_token() -> str:
    responce: Response = await request("GET", CHECK_TOKEN_URL, params={"token": TOKEN})
    assert "Set-Cookie" in responce.headers
    return responce.headers["Set-Cookie"]


async def get_message(cookie: str) -> List[Dict[str, Union[float, str]]]:
    responce: Response = await request(
        "POST", GET_MESSAGE_URL, headers={"Cookie": cookie}
    )
    data = responce.json()
    assert "messages" in data
    return list(data["messages"])


async def delete_message(msg_id: int, delay: float, cookie: str) -> None:
    await sleep(delay)
    responce: Response = await request(
        "POST", DELETE_MESSAGE_URL, headers={"Cookie": cookie}, json={"id": msg_id}
    )
    data = responce.json()
    assert "success" in data
    assert data["success"] == True
    logger.info(f"Message {msg_id} deleted")


async def get_flag(cookie: str) -> str:
    responce: Response = await request("POST", GET_FLAG_URL, headers={"Cookie": cookie})
    data = responce.json()
    assert "success" in data
    assert data["success"] == True
    assert "flag" in data
    return str(data["flag"])


if __name__ == "__main__":
    logger.info("Start")
    loop: AbstractEventLoop = get_event_loop()

    logger.info("Processing set_token")
    cookie: str = loop.run_until_complete(set_token())

    logger.info("Processing get_message")
    msg_list: List[Dict[str, float | str]] = loop.run_until_complete(
        get_message(cookie)
    )

    tasks: List[Coroutine[Any, Any, None]] = []
    for msg_id, msg in enumerate(msg_list):
        assert isinstance(msg["delay"], float)
        assert isinstance(msg["text"], str)
        if re.search(PATTERN, msg["text"]):
            tasks.append(delete_message(msg_id, msg["delay"], cookie))
    logger.info(f"Total {len(tasks)} delete tasks")
    loop.run_until_complete(gather(*tasks))

    logger.info("Processing get_flag")
    flag: str = loop.run_until_complete(get_flag(cookie))
    logger.success(f"Flag: {flag}")

    loop.close()
```
