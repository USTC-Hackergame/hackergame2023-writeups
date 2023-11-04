本人来自AHU，也是第一次参加Hackergame和CTF比赛，不得不说相较于ACM，这种类型的比赛更让我着迷。可惜成绩不如诸位大佬（`分数：2600， 总排名：278 / 2386`）

（博客地址不放前台了，感觉我的能力尚不足以推销自己（x）

接下来将为大家带来本人对部分题的解法。

### 猫咪小测

Q1 想要借阅世界图书出版公司出版的《A Classical Introduction To Modern Number Theory 2nd ed.》，应当前往中国科学技术大学西区图书馆的哪一层？

* 经搜索，发现中国科学技术大学的[图书馆opac系统](http://opac.lib.ustc.edu.cn/opac/search_adv.php)无需登录即可访问，遂进入系统搜索到了此图书（起初并未查询到任何结果，后来发现移除后缀`2nd ed.`即可搜到，想必是做了分开储存的处理）
* 得知此书位于西区图书馆外文书库，又在另一页面（ 忘记保存链接了:( ）得知外文书库位于12层，即可解出此题。

Q2 今年 arXiv 网站的天体物理版块上有人发表了一篇关于「可观测宇宙中的鸡的密度上限」的论文，请问论文中作者计算出的鸡密度函数的上限为 10 的多少次方每立方秒差距？

* 很巧，在进入arXiv之前就在知乎找到了[相同主题的文章](https://www.zhihu.com/question/20337132/answer/3023506910)，其中表明答案为10^23ps^-3,即23为本题答案。

Q3 为了支持 TCP BBR 拥塞控制算法，在编译 Linux 内核时应该配置好哪一条内核选项？

* `CONFIG_TCP_CONG_BBR`，略

Q4 🥒🥒🥒：「我……从没觉得写类型标注有意思过」。在一篇论文中，作者给出了能够让 Python 的类型检查器 MyPY mypy 陷入死循环的代码，并证明 Python 的类型检查和停机问题一样困难。请问这篇论文发表在今年的哪个学术会议上？

* 此题当时让我“抓狂”，大概是翻译的不好或耐心不够罢，没能从互联网找到正确答案，遂采用爆破方法，代码如下：

先从[中国计算机学会推荐国际学术会议和期刊目录（2022）](https://ccf.atom.im/)获得表格形式的会议列表（当时偷了个懒，想着2022年的数据也未尝不可，<s>不行再换嘛</s>），在DevTools采用如下代码，并对输出数组右键拷贝为Object可得到会议列表：
```js
a=[];for(let i of document.querySelectorAll("tr > td:nth-child(2)"))a.push(i.innerText);b=[];a.map(e=>{console.log(e);break;if(e.length==4 || 1)b.push(e)})
```
这时又暴露出了我的短板，没注意审题，以为满足条件的会议都是四字英文字母（
好在后面发现并改正了，这是后话了。

接下来，在猫咪小测网页运行如下代码，开始测试：
```js
// 在此处粘贴入复制的会议列表，之所以使用prompt()是不想在浏览器控制台历史记录增添乱七八糟的条目（

b=JSON.parse(prompt());


// 定义s1函数，执行发送指令并显示出正确结果
s1=(v4)=>fetch("http://202.38.93.111:10001/", {
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
  },
  "referrer": "http://202.38.93.111:10001/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "q1=12&q2=23&q3=CONFIG_TCP_CONG_BBR&q4="+v4,
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then(r=>r.text()).then(txt=>{
    console.log(txt.includes("总得分为 80")?("Not this..."+v4):txt);
});


// 自动版；每隔500ms发起一次测试
let currentIndex = 0,intv;intv=setInterval(()=>{
    s1(currentString);
    if(currentIndex++ == b.length)clearInterval(intv);
},500);

// 最初本人采用的手动版；每在网页按一次空格发起一次测试（不能在DevTools中按，因为后者是个独立的页面（）

document.addEventListener('keydown', function (event) {
    if (event.key === ' ') {
        if (currentIndex < b.length) {
            const currentString = b[currentIndex];
            console.log(s1(currentString));
            currentIndex++;
        } else {
            console.log("No more strings in the array.");
        }
    }
});
```
之后得到正确结果`ECOOP`。



### 组委会模拟器

* 简单来说，该页面会首先请求服务器`/api/getMessages`，得到含有“服务器开始时间”，每条消息相对开始时间的延迟及消息内容的响应。我所做的是利用如下js代码代替页面原有逻辑，完成整个撤回过程。

  ```js
  // 定义sendDel函数，执行撤回指令
  const sendDel = (id) => {
      fetch("http://202.38.93.111:10021/api/deleteMessage", {
          "headers": {
              "content-type": "application/json"
          },
          "referrer": "http://202.38.93.111:10021/",
          "referrerPolicy": "strict-origin-when-cross-origin",
          "body": `{\"id\":${id}}`,
          "method": "POST",
          "mode": "cors",
          "credentials": "include"
      }).then(resp => resp.json()).then(json => {
          if (!json.success) {
              console.warn(json.error);
              failTotal++;
          } else successTotal++;
      });
  };
  let hacksTotal = 0, successTotal = 0, failTotal = 0;
  fetch("http://202.38.93.111:10021/api/getMessages", {
      "headers": {
          "content-type": "application/json"
      },
      "referrer": "http://202.38.93.111:10021/",
      "referrerPolicy": "strict-origin-when-cross-origin",
      "body": "",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
  }).then(resp => resp.json()).then(json => {
      console.log(json);
      // json对象即为所有消息之数组 + 服务器开始时间
      const gets = json, getTime = () => (new Date() - new Date(gets.server_starttime))/1000;
      // 定义了getTime函数，方便快速判断当前是否符合撤回此消息的时间条件
      console.log(`getTime: ${getTime()}`);
      for (let a in gets.messages) {
          console.log(`${hacksTotal} ${successTotal} ${failTotal}`)
          // 利用正则表达式检测是否满足条件
          if (gets.messages[a].text.match(/hack\[([a-z]*?)]/)) {
              hacksTotal++;
              console.log(`Found ID=${a}, containing hack[]`);
              const targetTime = Math.ceil(gets.messages[a].delay);
              // 此处判断开始时间与delay值是否匹配，不符合则通过让CPU空算直到到达那个时间（）我知道这种写法不好，不过看着很直观（x
              while (getTime() < targetTime) {
                  for (let i = 0; i < 1800000; i++) {
                  }
              }
              console.log(`${getTime()} --==-- ${targetTime}`);
              sendDel(a);
          }
      }
  });

  ```

### 虫

* 只能说多亏了平时刷到的奇奇怪怪的内容，我第一反应就是SSTV，Slow-Scan Television，（不得不说无线电爱好者们潜力无限哈），在Windows PC上下载了相关软件 [RXSSTV](https://www.qsl.net/on6mu/rxsstv.htm)，并在`声音托盘图标->声音->录制`中打开“立体声混音”（非Realtek声卡我就不知道是否有此功能了，原本尝试过OBS但是并没有发现虚拟麦克风相关选项，不过只要有麦克风的话，还是可以外放的嘛（x）一边播放录音一边启动软件，就可以静候彩色flag图片出现了。

* 注1：我没想到PotPlayer是我尝试失败的罪魁祸首，由于前者是我PC上的默认播放软件，我也就一直使用它，结果使用上述软件以及MMSSTV均无法得到清晰可辨的图像（字符极其模糊，只有个别字母和大赛logo可见），就在我想要发送邮件询问的一刹那，我换用了Windows Media Player，结果居然可以得到清晰图像！这一问题我至今不知道原因为何。（已检查PotPlayer倍速设置为1.0）

* 注2：无Windows机器的小伙伴可能在安装上述软件时遇到了困难，因为我下载的这两款软件之安装包统统无法使用压缩软件（如`Bandizip`）解包并直接运行，无奈只好采用沙盒运行（是Sandboxie，并非Windows沙盒）不得不说Sbie的兼容性可比Wine好多了，至少奇奇怪怪的软件大多都可以正常运行（

  （绝无任何贬低Wine的意思，我深刻理解并感谢Wine维护者们在逆向Windows API以及其他方面的贡献，只是这条路确实任重道远）

### Git? Git!

  在接触此题之前，我便对Git的文件管理特殊之处有所耳闻，被撤销的更改仍旧位于`.git`中，且未经`git gc`命令不会消失。在询问GPT以及搜寻资料后，写出了如下<s>不用操心</s>的Bash脚本（因为不需要猜测哪个commit包含被修改的文件，经测数秒即可输出结果）

  ```bash
  #!/bin/bash
  # Define the target directory where .git/objects is located
  GIT_OBJECTS_DIR=".git/objects"

  # Iterate through the two-hex-named directories
  for dir in $(find "$GIT_OBJECTS_DIR" -type d -name "??"); do
      dir_name=$(basename "$dir")

      # Iterate through object files in the directory
      for obj_file in "$dir"/*; do
          # Combine directory name with object filename
          combined_path="$dir_name$(basename "$obj_file")"

          # Execute your command with the combined path
          git cat-file -p "$combined_path" | grep 'flag'
      done
  done
  ```


### 🪐 低带宽星球     (206 Partial Content)

* 第一问，我起初是通过压缩网站完成的，相信各位都明白，此略

* 为了将图片尽可能压缩，我通过比对图片细节，手搓了第一版svg代码，虽然通过了像素级比对，但大小将近200字节；后来经过人工压缩，

    * 将根元素svg的width等属性替换为viewBox

    * 将fill属性值从`rgb(111,222,30)`这样的值替换为Hex表示法`#5cabc1`

    * 移除rect元素中为0的x或y属性

    * 将rect元素直接替换为path，进一步缩减大小
      plaintext
       发现这样做也不可能将图片压缩至50字节，即使经过了gzip压缩成svgz格式也不行，因为仅仅一行rect元素就已经堪堪超限了，<s>早该及时止损的（）</s>

    ```
    <svg width="1024" height="1024">
        	<rect width="314" height="1024" fill="#5cabc1"/>
        	<rect x="314" width="426" height="1024" fill="#4edb0a"/>
        	<rect x="740" width="284" height="1024" fill="#44d404"/>
        </svg>
        <svg viewBox="1024 1024"><path d="M0 0h314v1024H0z" fill="#5CABC1"/> <path d="M314 0h426v1024H314z" fill="#4EDB0A"/><path d="M740 0h284v1024H740z" fill="#44D404"/> </svg>
    ```



这时很容易想到，需要寻求一个使用二进制而非ASCII字符控制绘图的矢量图形语言，这样才满足要求。接下来，通过询问GPT、查询libvips网站、在`convert.io`网站查看可供选择的矢量图形类型列表，我试图将此svg图形转换为`eps,ai,cgm,dxf,fig,plt,ppm,vips`，但要么无法被pyvips识别，要么不满足本题条件，只好放弃。

后面阅读了官方题解，才发现我漏掉了最重要的信息来源之一 `libvips`源码，<s>早知如此就不用试那么多图像类型了</s>，jxl格式或成最大赢家（        （本题请参考官方题解）

### 旅行照片

第一问，通过奖牌上人名`M.Koshiba`得知是获得诺贝尔物理学奖的小柴昌俊，从而得知学长在东京大学，通过维基百科可知满足第二问条件的东京大学诺贝尔奖得主为梶田隆章，所在研究所为`東京大学宇宙線研究所`，简称ICRR。通过第二张图片可知学长参加了国际统计物理会议STATPHYS第28次会议，通过[官网](https://statphys28.org/)得知会议举办时间在8月7-11日，手工尝试可得。

第三问，通过在Google上广撒网，看了不少街景图片，发现有一张背景的白色帐篷和本题十分相近，由此得知该活动名为“全国梅酒まつり”（即“祭”，应该是大会的意思），在其[官网](https://umeshu-matsuri.jp/tokyo_ueno/)上很容易得知，[在线表单](https://ws.formzu.net/dist/S495584522/)URL的末位。至于第四问，通过东京国立博物馆相关说明，得知**单人**门票价格只能是1000，500，0，所以成功试出结果（

第五问，谁知道当初的我盯着Google360°街景看了多长时间！那时刚巧是我第一次了解到谷歌街景的神奇之处，遂操纵它在`上野駅`的周围到处移动镜头，看到了周围的大型百货商场`0101`，不过找不到任何粉色海报和大型3D广告牌的踪迹。后来灵光一现，前往Twitter，果然很轻松搜到了`ボタン＆カフリンクス`活动的海报，背景上是一只熊猫；至于第六问，通过不断修改关键词`上野、3D、看板`，得知是“秋田犬”，结束。

（后来我发现了自己思维的局限性，题干中说“JR上野站”进站处云云没有问题，但“出站处”可并非指的是上野站，那么我在上野再怎么找都是找不到的，当初搜到了应该是因为碰巧删除了上野关键词才成功。看了官方题解才知道，通过任天堂logo可知“我”出的是`渋谷駅`，那里可以找到这样的3D大广告牌。

### 结语

这是本人第一次参加CTF比赛，通过此次锻炼我也发现了自身存在的诸多不足，例如眼界不宽广、思维不发散、技术知识储备不足等，目前只能仰视诸位大佬，希望自己再接再厉！同时郑重感谢USTC Hackergame 2023 全体幕后成员，提供了这样一个挑战自我的机会。

如有兴趣，欢迎查看

- 本人博客 https://blog.ryancc.top

- 本人Telegram频道 https://t.me/rych0814

- （如果您恰好需要联系本人，可选择在频道内留言，或跟踪我的Github主页，不便敬请谅解）

- （唉，技术没涨，人倒越来越懒了，博文懒得写，一般在技术探索中碰到的小tips就直接发频道了，最近正在试用[usememos/memos](usememos/memos)，希望它可以帮助我记录日常所思所想）

  谨在此贴出我的分数变更日志（懒得上传图片了，同时也为本项目的大小做了积极贡献），谢谢看到这里。

  | 时间             | 解出题目                             | 分数变化   | 排名变化 |
  | ---------------- | ------------------------------------ | ---------- | -------- |
  | 2023/10/28 12:15 | 更深更暗                             | 0->100     | 212->101 |
  | 2023/10/28 13:29 | Hackergame 启动                      | 100->150   | 375->371 |
  | 2023/10/28 14:11 | 虫                                   | 150->300   | 427->272 |
  | 2023/10/28 14:57 | 猫咪小测 / 及格喵                    | 300->400   | 312->260 |
  | 2023/10/28 15:06 | 🪐 低带宽星球 / 小试牛刀              | 400->550   | 263->173 |
  | 2023/10/28 15:59 | 组委会模拟器                         | 550->750   | 195->126 |
  | 2023/10/28 16:02 | HTTP 集邮册 / 5 种状态码             | 750->900   | 126->86  |
  | 2023/10/28 16:18 | Docker for Everyone                  | 900->1050  | 92->68   |
  | 2023/10/28 16:23 | 🪐 小型大语言模型星球 / You Are Smart | 1050->1150 | 68->58   |
  | 2023/10/28 20:14 | 旅行照片 3.0 / 这是什么活动？        | 1150->1300 | 113->96  |
  | 2023/10/28 20:21 | 旅行照片 3.0 / 神秘奖牌              | 1300->1450 | 97->76   |
  | 2023/10/28 21:59 | 奶奶的睡前 flag 故事                 | 1450->1600 | 90->79   |
  | 2023/10/28 22:22 | Git? Git!                            | 1600->1750 | 80->70   |
  | 2023/10/28 22:45 | 赛博井字棋                           | 1750->1900 | 72->63   |
  | 2023/10/30 19:46 | 猫咪小测 / 满分喵                    | 1900->2050 | 214->204 |
  | 2023/10/30 20:57 | 🪐 高频率星球                         | 2050->2250 | 206->182 |
  | 2023/10/31 0:58  | HTTP 集邮册 / 12 种状态码            | 2250->2450 | 196->168 |
  | 2023/11/2 21:05  | 旅行照片 3.0 / 后会有期，学长！      | 2450->2600 | 251->239 |



