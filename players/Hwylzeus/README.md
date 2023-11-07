# Hackergame2023-writeup
by Hwylzeus
欢迎跳转到[我的个人博客](https://hwyl.run/2023/11/08/Hackergame2023-writeup/)看噢！！
## 前言
算是本人第二次打Hackergame了，Hackergame还是一如既往的有趣好玩！爆赞！
这次比赛满打满算打了 3 天（10.28中午~10.30中午 + 11.3周五没啥课没啥作业），大三老狗课最多的一个学期（38学分专选的含金量），作业多实验报告多，时间不允许呜呜呜
10.30中午排名曾一度冲到105，由于和当时的第100名同分，所以四舍五入我也算上过榜了（逃
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231105162815.png)
（结束的前一天（周五）浅囤了点flag，结束前的一小时就交了）
最终总排名： 184 / 2386    最终校内排名： 13 / 64
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231105144217.png)
校内榜：
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231105144311.png)
还记得去年 1700 分都校内第 7 了，今年分数涨了一倍排名却反而跌了近一倍？？
不得不说鸭专今年打Hackergame是真的卷，进校内前10就能进总排前100了。。。感觉可能一来是校CTF战队宣传到位吧，听说暑假建了个CTF新生群，到现在也有了将近400人的规模；二来是赛前练兵练得好，上个学期GZ举办的校赛以及前不久的NewStarCTF都让新人得以很好的入门
而我作为半个校战队成员(？)，常年划水，只有每年的 Hackergame 才出来玩玩，感觉就是......时代变了，跟不上版本了

（因为 wp 交的比较迟而且rank不起眼估计没啥人看，同时也因为时间比较久了解题过程有些细节有遗忘，所以写的比较随意。。。望dalao们轻喷）
## 正文

### 0x00 Hackergame 启动
> 大声喊出 Hackergame 启动，开始今年的冒险！

今年的签到依旧整活，正常喊肯定解不出，根据去年签到题的经验，随便提交了一下，会发现地址栏末尾多了`/?similarity=`，加上 99.999999 然后回车即可获得 flag

`flag{W3!cOm3-70-HaCKergAM3-4nD-3Njoy-hacK1ng-ZoZ3}`

### 0x01 猫咪小测

经典猫咪问答，不过感觉今年难度低了不少，可以爆破的小题也很容易爆出来

> 1. 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？**（30 分）** 提示：是一个非负整数。

不难搜索得到[馆藏分布 | 中国科学技术大学图书馆 (ustc.edu.cn)](https://lib.ustc.edu.cn/%e6%9c%ac%e9%a6%86%e6%a6%82%e5%86%b5/%e9%a6%86%e8%97%8f%e5%88%86%e5%b8%83/)
西区总共也就12层楼，排除掉明显是存放中文书刊的层剩下也就5层，挨个试就行，试出了分数就会增加
答案：`12`

> 2. 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？**（30 分）** 提示：是一个非负整数。

懒得找了，10的多少次方每立方秒总不可能超过100吧，直接爆破，甚至没写脚本
答案：`23`

> 3. 为了支持 TCP BBR 拥塞控制算法，在**编译** Linux 内核时应该配置好哪一条内核选项？**（20 分）** 提示：输入格式为 CONFIG_XXXXX，如 CONFIG_SCHED_SMT。

直接搜索，这种有关Linux配置的文章肯定大把人写，然后把所有有关的配置选项挨个试
答案：`CONFIG_TCP_CONG_BBR`

> 4. 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 ~~MyPY~~ mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？**（20 分）** 提示：会议的大写英文简称，比如 ISCA、CCS、ICML。

找个[有分类的学术会议列表](https://ccf.atom.im/)，然后找到有关程序设计语言的学术会议，从A会到C会挨个试
答案：`ECOOP`
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104100926.png)

`flag{w31comE-t0-@773nD-THE-N3Ko-3XaM-2o23}`
`flag{R3@L-M4s7eR-of-7h3-neko-3X4M-IN-USTC}`

### 0x02 更深更暗
> ......
> 「是我眼花了吗？我刚刚有一瞬间好像在残骸上看到了一个 flag？」小 C 惊讶地说。
> ......

题目的这句话其实已经提示的很明显了
打开题目页面往下滑了两三千米发现是个无底洞，想着滑快点看看一万米以下会有什么，于是直接**单击鼠标中键往下拉**，不料flag马上映入眼帘，还真是“一瞬间”啊。。。
由于无法复制粘贴也无法屏幕截图，只好拿出手机拍照然后一个一个字符将flag打上去
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104102153.png)

`flag{T1t@n_575ba6de55c34eb362a13c6da73ce520}`

### 0x03 旅行照片 3.0
> 你的学长去留学了，这一走短时间内怕是回不来了。于是，你在今年暑假来了一场计划已久的旅行，并顺路探望了这位久别的学长。翻阅当天拍下的照片，种种回忆和感慨油然而生。
> 请观察照片并结合所有文字内容，正确回答题目以获取 flag。

其实我这题的正常社工解法只占半成，另外半成主要是靠爆破+运气（
#### 题目 1-2
> 1、你还记得与学长见面这天是哪一天吗？（格式：yyyy-mm-dd）

这题真的不会，我是脚本爆破出来的呜呜呜

答案：`2023-08-10`

> 2、在学校该展厅展示的所有同种金色奖牌的得主中，出生最晚者获奖时所在的研究所缩写是什么？

首先通过识图可知这个金色奖牌是诺贝尔物理学奖
一开始没审题“该展示厅展示的”，找到[Konstantin_Novoselov](https://en.wikipedia.org/wiki/Konstantin_Novoselov)去了，后来缩小范围，限定在“东京大学“的获奖者中找，找到了 [Takaaki Kajita](https://en.wikipedia.org/wiki/Takaaki_Kajita)
这哥们有两所研究所 ICRR 和 IPMU ，由于时间节点比较模糊不好确定是哪所，于是结合爆破脚本挨个试

答案：`ICRR`
 `flag{how_I_wi5h_i_COulD_w1N_A_Nobe1_pri23_5924da0997}`

#### 题目 3-4
> 3、帐篷中活动招募志愿者时用于收集报名信息的在线问卷的编号（以字母 S 开头后接数字）是多少？

![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Screenshot%202023-10-29%20182102.png)
根据第一题得到的日期和图片的所在地点进行搜索，马上得到：
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104105708.png)
这个活动的[官网](https://home.ueno.kokosil.net/zh-hans/archives/77157)
然后划到最底下有[志愿者招募的网址](https://umeshu-matsuri.jp/tokyo_staff/)
问卷号就明摆着写在上面了
答案：`S495584522`

> 4、学长购买自己的博物馆门票时，花费了多少日元？

根据上面的google map不难找到[博物馆的官网](https://www.tnm.jp/modules/r_free_page/index.php?id=113#access_01)
看了看票价规则，东大学生免费
答案：`0`

`flag{PluM_w1NE_1S_rEa1LY_EXpen5iVE_d36221b5c8}`
#### 题目 5-6
> 5、学长当天晚上需要在哪栋标志性建筑物的附近集合呢？（请用简体中文回答，四个汉字）

~~搞学术那肯定是回自己的大学搞啊~~，结合前面得到的地理位置信息，一开始没审题直接就填了东京大学
后面第6问怎么试都没对后开始重新审题，注意到关键词“标志性建筑物”，那可能指的是校园内某栋著名的楼，就像鸭大的怀士堂这样的，简单搜了下就填了安田讲堂
答案：`安田讲堂`

> 6、进站时，你在 JR 上野站中央检票口外看到「ボタン＆カフリンクス」活动正在销售动物周边商品，该活动张贴的粉色背景海报上是什么动物（记作 A，两个汉字）？ 在出站处附近建筑的屋顶广告牌上，每小时都会顽皮出现的那只 3D 动物是什么品种？（记作 B，三个汉字）？（格式：A-B）

第 1 小问上google简单搜索一些上野站的[图片](https://www.instagram.com/p/Cvrw425vK_n/)/[视频](https://www.youtube.com/watch?v=ug64NDRB_xU)不难得出是熊猫

第 2 小问就上难度了，因为我找的视频都只在那个广告牌前停留了几秒，而且还很糊，看不清是什么，因此没法找到每小时都顽皮出现的动物。于是决定换个思路，照着广告牌上的电话号码搜，希望能找到广告视频源，搜到了[他们的官网](https://nagata-lcv.com)
但没有广告视频源，依然无法找到这个顽皮的动物
于是放弃挣扎，把所有可能的三字带品种（尤其是日本特有品种）的动物都列出来，直接开始爆破！
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url='http://202.38.93.111:12345/?token=1569%3AMEYCIQChEm%2B%2FL1svwKw3zlYKawZP%2BBc0%2BckciU%2FfknWjJrG%2FpwIhAN%2F%2F%2ByQDYGmFargWYXzHCGOb09lqMtPFjCLw8gKGreOu'
driver = webdriver.Edge()
driver.get(url)

time.sleep(2)

d = ['安田讲堂','彩虹大桥','东京大学']
m = ['哈士奇','秋田犬','泰迪犬','哈巴狗','褐林鸮','三花猫','狸花猫','玳瑁猫','短尾猫','短毛猫','加菲猫','暹罗猫','缅甸猫','波斯猫','布偶猫','折耳猫','卷毛猫','孟买猫','埃及猫','拉邦猫','波斯猫','食蚁兽','鸭嘴兽','树袋熊','白头鹰','啄木鸟','信天翁','布谷鸟','金翅雀','知更鸟','猫头鹰','变色龙','娃娃鱼','非洲鳄','沙丁鱼','金枪鱼','萤火虫','枪乌贼','信天翁','凤尾鱼','安康鱼','白头鹰','金龟子','大黄蜂','纹白蝶','凯门鳄','银环蛇','印度鳄','珍珠鸡','无须鳕','寄居蟹','土拨鼠','嗜鱼蛇','蜘蛛蟹','凤尾蝶','褐雨燕','白喉雀','扬子鳄','墨海马','梅花鹿','藏羚羊','白鳍豚','小鳁鲸','金丝猴','棕果蝠','鸭嘴兽','山斑鸠','丹顶鹤','藏羚羊','红蜻蜓','红蜘蛛','波斯猫','折耳猫','泰迪熊','加菲猫','小熊猫','穿山甲','长颈鹿','食蚁兽','北极狐','无尾熊','北极熊','神仙鱼','鰕虎鱼','金枪鱼','深海鱼','杜父鱼','鳢形目','孔雀鱼','啄木鸟','信天翁','纤毛虫','肉足虫','鼻涕虫']
for j in d:
    for i in m:
        bbb = driver.find_element(By.NAME,'Answer5')
        ccc = driver.find_element(By.NAME,'Answer6')
        bbb.send_keys(j)
        ccc.send_keys("熊猫-"+i)
        driver.find_elements(By.CLASS_NAME,'ui button')[2].click()
        time.sleep(0.3)
        driver.refresh()

time.sleep(120)
driver.quit()

```
好吧是秋田犬
后面看官方wp才得知原来是我语文阅读理解错了，出站口指的是涩谷站出站口，难怪感觉马里奥世界的那张图片没啥用，原来是定位出站口用的。。。

答案：`熊猫-秋田犬`
`flag{Un7I1_W3_M337_A64iN_6oODByE_S3n1OR_ca780b0d9f}`

### 0x04 赛博井字棋
> 那一年的人机大战，是 AlphaGo 对阵柯洁，最终比分 3-0。当时我看见柯洁颓坐在椅子上泣不成声，这个画面我永生难忘。那一刻我在想，如果我能成为一名棋手，我一定要赢下人工智能。如今 AI 就在眼前，我必须考虑这会不会是我此生仅有的机会。重铸人类围棋荣光，我辈义不容辞！
> ……
> 但是围棋实在太难了，你决定先从井字棋开始练习。

打开页面先是和 AI 玩了玩，发现不管怎么下都赢不了，后来得知井字棋存在”后手必不败“的理论
想到这是web题，于是打开 F12 进行一顿乱找，在”网络“里发现这个题目直接把 js代码 放网页上了，一打开网页就能收到这份代码
```js
async function setMove(x, y) {
  if (board[x][y] != 0) {
    return;
  }
  if (frozen) {
    return;
  }
  let url = window.location.href; // 获取当前 URL
  let data = { x: x, y: y }; // 设置要发送的数据
  return fetch(url, {
    method: "POST", // 设置方法为 POST
    headers: {
      "Content-Type": "application/json", // 设置内容类型为 JSON
    },
    body: JSON.stringify(data), // 将数据转换为 JSON 格式
  }).catch(errorHandler);
}

/* main */
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
简单看了下里面的函数，有个`setMove(x, y)`是用来下棋的，但还需要等待响应，于是可以在控制台里调用这个函数先下个必嬴的三步，然后随便点一下空白的位置生成响应就赢了！

![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231105163827.png)

### 0x05 奶奶的睡前 flag 故事
> 晴空万里的假期终于拍了拍翅膀飞来了。对于一心想扔掉教材、砸掉闹钟、跃向世界的 L 同学来说，期待了整整三年的跨国旅游大业终于是时候启动了，还能巧妙地顺带着做个美满的老友记。
> 可是，哎哟喂，他刚踩上波光粼粼的金沙海滩，那他最疼爱的华为手机就跟着海风一起去约会了大海，连他的钱包也在这场未知探索之旅中神秘失踪。
> 「这个地方怎么连个华为手机都不卖。若是买个苹果手机，心疼的是它连个实体 SIM 卡槽都藏起来了，回国肯定成了个大摆设。不如来个**谷歌的『亲儿子』**？」L 同学踌躇满志地嘀咕道。
> 那时，像是上天的安排，「咱这儿正好有个**谷歌『亲儿子』** 的老手机，你拿去逍遥吧」。
> L 同学满眼星光地接过，**连系统都没心思升级**，就开始疯狂安装那个久闻大名的 GPT 程序，甚至雀跃地在群里晒出一张跟 GPT 对话的精彩**截图**，一时间成为了群里的焦点人物。

这题我一开始没头绪，找不到切入点，尝试过常规misc图片隐写的解法，将图片丢入stegsolve但发现没用
后来根据题目的粗体关键词，一瞬间联想到我很久以前看到的[一篇公众号文章](https://mp.weixin.qq.com/s/ZgwqGtq-tC1ib-5ElDsSUg)
一拍脑门，哎这不就是那个漏洞吗！
把图片丢进[Acropalypse](https://acropalypse.app/)这个网站上，手机型号选Pixel 4就解出来了
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104111148.png)

`flag{sh1nj1ru_k0k0r0_4nata_m4h0}`

### 0x06 组委会模拟器
> 每年比赛，组委会的一项重要工作就是时刻盯着群，并且撤回其中有 flag 的消息。今年因为人手紧张，组委会的某名同学将这项工作外包给了你，你需要连续审查 1000 条消息，准确无误地撤回其中所有含 flag 的消息，并且不撤回任何不含 flag 的消息。
> 本题中，你需要撤回的 "flag" 的格式为 **`hack[...]`**，其中**方括号**内均为小写英文字母，点击消息即可撤回。你需要在 3 秒内撤回消息，否则撤回操作将失败。在全部消息显示完成后等待几秒，如果你撤回的消息完全正确（撤回了全部需要撤回的消息，并且未将不需要撤回的消息撤回），就能获得本题**真正的 flag**。

这题我的脚本比较简单，用的selenium，大概思路就是通过`while True`进行轮询，实现实时获取最新的聊天气泡，若气泡含有`hack[`就单击
这里有一个必须优化的地方，否则到了大约200条信息时效率会变得极差，会严重超时
那就是每一次轮询以后遍历气泡是否满足条件是从上一次遍历结束的地方开始，也就是要另设一个变量`j`进行记录，`i`每次都从`j`开始，这样效率会大幅提升
但我这个脚本似乎天然存在可能会导致气泡定位错位的bug，怎么调都调不好，又因为聊天气泡的生成是随机的
因此存在一定的运气成分，在运行的过程中需要双手合十🙏祈祷脚本不要漏点也不要错点到诈骗视频去，这样就会有大概 10% 的机率通过此题（
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url='http://202.38.93.111:10021/?token=1569%3AMEYCIQChEm%2B%2FL1svwKw3zlYKawZP%2BBc0%2BckciU%2FfknWjJrG%2FpwIhAN%2F%2F%2ByQDYGmFargWYXzHCGOb09lqMtPFjCLw8gKGreOu'
driver = webdriver.Edge()
driver.get(url)

time.sleep(0.5)
j = 0

while True:
    bbb = driver.find_elements(By.CLASS_NAME,'fakeqq-message__bubble')
    for i in range(j,len(bbb),1):
        if i<=j and "hack[" in bbb[i].text:
            bbb[i].click()
            break
        j = j+1

time.sleep(120)
driver.quit()
```
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104115037.png)

### 0x07 虫
> 「生而为人，应该能够换尿布、策划入侵、杀猪、开船、造房子、写十四行诗、算账、建墙、正骨、抚慰临终之人、接受命令、下达命令、合作、独行、解决方程式、分析新问题、清理马粪、编程、烹饪美食、高效战斗、英勇牺牲。专业分工是给昆虫准备的。」—罗伯特·海莱恩（Robert Heinlein）
> 你觉得还是当昆虫轻松一些。
> 这时，你看到一只昆虫落在你面前，发出奇怪的叫声。你把这段声音录制了下来：这听起来像是一种**通过无线信道传输图片的方式**，如果精通此道，或许就可以接收来自国际空间站（ISS）的图片了。

根据题目信息”无线信道传输图片的方式“”ISS“进行google搜索，可知是慢扫描电视[SSTV](https://www.camras.nl/en/blog/2021/receiving-images-from-the-iss-through-websdr/)，在windows上能用的工具是[RX-SSTV](https://www.qsl.net/on6mu/rxsstv.htm)
然后用手机播放音频，电脑进行解码就可以了
因为没用虚拟声卡进行内录，所以得到的图像比较模糊，且噪声较多，但还是不难分辨出flag的
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104110836.png)
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104111039.png)

`flag{SSssTV_y0u_W4NNa_HaV3_4_trY}`

### 0x08 JSON ⊂ YAML?

第一问直接google搜索，找到[What valid JSON files are not valid YAML 1.1 files? - Stack Overflow](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)

![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104115026.png)

第二问没找到，也没有往重复键的方向去想呜呜呜

### 0x09 Git? Git!

bing 简单搜索[git恢复删除](https://blog.csdn.net/jerechen/article/details/96469183)，可得`git reflog`和`git checkout -b fix xxx`，进行恢复再看看修改的地方就可获得flag
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231105163631.png)

### 0x10 HTTP 集邮册
> 「HTTP 请求一瞬间就得到了响应，但是，HTTP 响应的 status line、header 和 body 都是确实存在的。如果将一个一个 HTTP 状态码收集起来，也许就能变成……变成……变成……」
> 「flag？」
> 「就能变成 flag！」

这题是我想复杂了，我还以为需要构造很巧妙又很长的请求头才能收集到所有状态码。。。

只尝试了最简单的5个：
200：点击就送
400：xjb乱写
404：在"/"后乱加
405：把GET改成DELETE
505：把HTTP改成2以上

### 0x11 Docker for Everyone
> X 是实验室机器的管理员，为了在保证安全的同时让同学们都用上 docker，他把同学的账号加入了 docker 用户组，这样就不需要给同学 sudo 权限了！
> 但果真如此吗？
> 提供的环境会自动登录低权限的 `hg` 用户。登录后的提示信息显示了如何在该环境中使用 docker。读取 `/flag`（注意其为软链接）获取 flag。

直接 bing 搜索”docker 非root 提权 漏洞“不难找到[【docker系列】容器有个bug-非root用户提权_logrotate 容器 提权](https://blog.csdn.net/hanxiaotongtong/article/details/124289077)
可知宿主机目录的文件可以被挂载，于是可以直接挂载/dev/shm/flag，在容器里cat即可
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104111258.png)

`flag{u5e_r00t1ess_conta1ner_8b84bd1e61_plz!}`

### 0x12 惜字如金 2.0
> 附件包括了一个用于打印本题目 flag 的程序，且已经经过惜字如金化处理。你需要做的就是得到程序的执行结果。

今年的惜字如金明显是简单了很多，只需要恢复被惜字如金化的程序再运行就好
注意到`cod_dict`每行都少了一个字符，于是可以根据`flag{`以及`}`推测缺了什么，推的时候可能会出错，具体推导细节我忘了，多试几次就好
```python
#!/usr/bin/python3

# The size of the file may reduce after XZRJification

def check_equals(left, right):
    # check whether left == right or not
    if left != right: exit(1)

def get_cod_dict():
    # prepare the code dict
    cod_dict = []
    cod_dict += ['nymeh1niwemflcir}echaete']
    cod_dict += ['a3g7}kidgojernoetlsup?he']
    cod_dict += ['uulw!f5soadrhwnrsnstnoeq']
    cod_dict += ['_ct{l-findiehaai{oveatase']
    cod_dict += ['ty9kxborszstguyd?!blm-pe']
    # check_equals(set(len(s) for s in cod_dict), {24})
    return ''.join(cod_dict)

def decrypt_data(input_codes):
    # retrieve the decrypted data
    cod_dict = get_cod_dict()
    output_chars = [cod_dict[c] for c in input_codes]
    return ''.join(output_chars)

if __name__ == '__main__':
    # check som obvious things
    check_equals('create', 'cre' + 'ate')
    check_equals('referrer', 'refer' + 'rer')
    # check th flag
    flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                         17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                         31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                         25, 63, 77, 36, 5, 32, 60, 67, 113, 28])
    # print(flag)
    check_equals(flag.index('flag{'), 0)
    check_equals(flag.index('}'), len(flag) - 1)
    # print th flag
    print(flag)
```

`flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}`

### 0x13 高频率星球
> 高频率星人的视觉输入频率极高，可以一目千行、过目不忘，他们的交流对地球人来说过于超前了。flag 被藏在了这段代码中，但是现在只有高频率星人在终端浏览代码的时候，使用 [asciinema](https://asciinema.org/) 录制的文件了，你能从中还原出代码吗？

这题我是先`asciinema play asciiname_restore.rec > flag.js`进行获取输出
然后vscode打开`flag.js`把前后明显是shell的部分删掉，中间会残留一些less分页导致的乱七八糟的字符串，可以`ctrl+H`进行批量删除
之后搭好nodejs环境，`node flag.js`就解决了

### 0x14 小型大语言模型星球
> 茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 —— flag，被认为是其智慧的象征。
> 你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的 33M 参数的「小型大语言模型」控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。
> 在这个星球上，你需要与这个先进的语言模型展开一场交流。通过与它对话，诱导它说出指定的词语，从这个神秘智慧体中获得 flag。你需要让这个语言模型分别说出 you are smart，accepted，hackergame 和 🐮，以获得四个 flag，证明你足够聪明以控制这个星球的命运。

第一题简单，随便写写应该都能过
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104115141.png)

第二题尝试过”acce“”accep“”accept“”accepte“之类的prompt试图让其补全，也尝试过”reject“”idea“”deny“之类相关的词，但都以失败告终
后来想到既然你每次回答都是独立的，且生成有很大程度的随机性，于是想到可以写个脚本每次随机生成7个不同的字符进行暴力payload，但效率太低，试了一个小时后还没出结果
于是进行改进，开头是第一随机字符，后接”accept“，很快就出了！
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

url='http://202.38.93.111:10101/?token=1569%3AMEYCIQChEm%2B%2FL1svwKw3zlYKawZP%2BBc0%2BckciU%2FfknWjJrG%2FpwIhAN%2F%2F%2ByQDYGmFargWYXzHCGOb09lqMtPFjCLw8gKGreOu'
driver = webdriver.Edge()
driver.get(url)
time.sleep(5)
s = string.ascii_letters

while True:
    bbb = driver.find_element(By.CSS_SELECTOR,'#component-7 > label > textarea')
    bbb.send_keys(random.choice(s)+"accept")
    driver.find_element(By.ID,'component-8').click()
    time.sleep(10)
time.sleep(120)
driver.quit()
```
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104111413.png)

`flag{yOu-ArE-accEP73d-tO-C0n71NuE-ThE-94ME}`
### 0x15 流式星球
> 流式星人用流式数据交流，比如对于视频来说，他们不需要同时纵览整个画面，而是直接使用像素流。为了方便理解，你把这个过程写成了一个 Python 脚本（见附件），flag 就藏在这个视频（见附件）中。尽管最后丢掉了一部分数据，你能把 flag 还原出来吗？

根据题目提供的 Python 脚本可知题意大概为：将一个转换成了像素流且末尾随机丢弃了0~100个bit的二进制文件还原为原视频
可以拷问GPT老师，然后根据GPT提供的整体框架自己再进行一些小修小改便可得如下代码：

```python
import cv2
import numpy as np

def reconstruct_video(input_file, output_file):
   # 读取二进制数据流文件
   with open(input_file, "rb") as f:
       data = f.read()

   for frame_height in range(50,250,1):
    for frame_width in range(250,500,1):
        for i in range(1,101):
            if (135146687+i) % (3 * frame_height * frame_width) == 0 :

                buffer = np.frombuffer(data, dtype=np.uint8)
                buffer = np.append(buffer, buffer[-i:-1])

                print(frame_height,frame_width,len(buffer))
                frame_count = int(len(buffer) / (3 * frame_height * frame_width))

                if len(buffer) % (3 * frame_height * frame_width) == 0 and frame_count > 20:

                    buffer = buffer.reshape((frame_count, frame_height, frame_width, 3))

                    out = cv2.VideoWriter(output_file+str(frame_height)+'x'+str(frame_width)+".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))

                    for frame in buffer:
                        out.write(frame)

                    out.release()

if __name__ == "__main__":
    reconstruct_video("video.bin", "video")

```
大概的流程就是先通过遍历补齐视频流文件末尾缺失的bit，先判定补齐后的字节数符不符合要求，符合才进行输出，不符合则继续遍历
然后帧率可以不用管，只是播放速度快慢的区别
接着根据题目提供的脚本进行逆向，最后输出mp4文件就可以了
其实`frame_heigt`和`frame_width`都可以遍历50~1000的，这样就能得标准答案`frame_heigt=729, frame_width=427`，但我先入为主以为视频一般都是横屏的且应该不会太大就没有尝试扩大范围，好在依然能够解出该题（

最后会生成几十个 mp4 文件，开超大图标进行速览
会发现有个视频与众不同，点开看便能发现flag
![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104111514.png)

`flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}`

### 0x16 低带宽星球(小试牛刀)
> 茫茫星系间，文明被分为不同的等级。每一个文明中都蕴藏了一种古老的力量 —— flag，被认为是其智慧的象征。
> 你在探索的过程中意外进入了一个封闭空间。这是一个由神秘的低带宽星人控制着的星球。星球的中心竖立着一个巨大的三角形任务牌，上面刻着密文和挑战。
> 低带宽星人的通信速度很低，只能以 1 字节 / 天的速度接受信息，所以在这个星球上，你需要将一张图片用很少的字节数传输给低带宽星人，然后获得 flag。具体来说你需要将一张图片无损压缩（每个像素的颜色都一致）：
> - 压缩至 2KiB (2048 字节) 及以下，获得 flag1
> - 压缩至 50 字节及以下，获得 flag2

bing或google简单搜索不难得国外这个专门做图片压缩的网站
[TinyPNG – Compress WebP, PNG and JPEG images intelligently](https://tinypng.com/)
将图片丢进去就可以压缩到满足第一题的要求，1.3kb

第二题试图写 SVG，但发现我写的 SVG 甚至比第一题的压缩还大，遂放弃

### 0x17 异星歧途
> ......
> 你的任务是在不进行任何其他操作的情况下拨动这 32 个按钮，使冲击反应堆能够**稳定运行**。
> ......

刚进游戏啥也不懂xjb乱点，炸了好几次......
后来开了个新游戏过了一下新手教程，大致懂了每个元件都有什么功能
后面就主要是根据逻辑处理器的类汇编代码有序拨动开关了

**Part 1**
最容易的一组，全部取反就行
**Part 2**
可以在逻辑处理器代码页面的下方”变量“看到变量的实时变化，这样能够直观进行理解
F10 是 i 的平方，number 是这组 8 个开关组成的 8 位二进制对应的 10 进制数，但有时会不稳定（值-4，猜测是时钟尖刺，未考证），但影响不大，能保证供电就行
要跳出代码的循环以启动供电，就需要使 F10 == number，所以需要构造 F10
又因为前提是 SW1 和 SW6 必须是 1，且SW8不能乱动，否则会导致 Part3 炸掉
所以只能从剩下 5 个开关里构造，使整个二进制为一个平方数
不难试出，只有拨动 SW2 才能满足
**Part 3**
这部分需要首先理解每个元件的功能和游戏逻辑
要达到的目标是使反应堆启动但又不能爆炸，这就需要保证足够的冷却液提供，因此冷却液不能有泄露
要提供冷却液那么首先要提供水并启动混合器，并打开两个传送带的控制门，确保原料供应
按照这个逻辑，结合代码进行尝试即可，因为开关的先后顺序不同可能会导致有不稳定的多解，可以挨个尝试直到找到稳定的序列
**Part 4**
这题的逻辑处理器只是告知了每个开关一一对应了下面的8个电力源，重点是要使下面的门电路导通
我也看不懂这些门电路，但逐个尝试还是能发现些规律的，具体什么规律我忘了，总之就是试出来的（

![](https://allanpoe-oss.oss-cn-hangzhou.aliyuncs.com/img/Pasted%20image%2020231104115059.png)

最终序列为：`10100101110001001000110001110111`

`flag{B34WarE_0f_#xp1osi0N_6860831ff3}`

## 总结

虽说本次 Hackergame 我没有太过执着于追求 rank，只是抱着解不出来就算了等赛后看 wp 学习的佛系心态，但对比别人 wp 体现出的解题思路，我发现我尚存在以下问题：
1. 不够信任 AI 工具。看了一些选手的题解，发现有些题是可以让 ChatGPT/New Bing 写代码解出来的，如 HTTP集邮册、YAML、LD_PRELOAD 这些
2. google 和看文档的能力不行。很多时候都get不到搜索结果或文档里有利于解题的关键点，prompt技巧 和 英语阅读水平 还需要再提高
3. 代码能力也不太行。python使用不够熟练，一些包的基本用法不了解，需要 coding 的题大多不敢尝试

明年有机会一定还来！

2023/11/07 23:11