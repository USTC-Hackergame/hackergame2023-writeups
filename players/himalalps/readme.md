# Hackergame 2023 题解

**PB21111691 汤皓宇**

## Hackergame 启动

录制提交之后发现浏览器的地址栏中链接变为 https://cnhktrz3k5nc.hack-challenge.lug.ustc.edu.cn:13202/?similarity=75.8593380240089，直接修改 similarity 为 99.99 则可以拿到 flag.

## 猫咪小测

1. 直接在图书馆主页搜索，则可以知道在外文书库，是十二层。

2. 搜索关键词 arxiv, chicken, upper，即可找到对应论文，是 $10^{23}pc^{-3}$.

3. 直接下载一份 kernel，`make menuconfig` 后根据可以搜到的网上的说法打开对应的 TCP BBR 选项，保存配置之后在配置文件中搜索，发现是 `CONFIG_TCP_CONG_BBR`。

4. 搜索 python, typechecking, halting problem，找到论文 Python type hints are Turing complete，在 dblp 中搜索，发现是 ECOOP.

## 更深更暗

在网页中 F12 打开检查窗口，在元素中找到 id 为 titan 的 pre，其中就包含 flag.

## 旅行照片 3.0

1. 中午的那张照片里学长戴着一个 STATPHYS 28 的胸牌，搜索发现在 2023 年 8 月 7 日到 11 日举办，地点在东京。可以在第二题得出之后五天都试一下，发现是 8 月 10 日。

2. 搜索之后发现那张奖牌是诺贝尔物理学奖，得主是小柴昌俊，在东京大学。搜索诺贝尔物理学奖，最新一次是真锅淑郎，但他出生得比较早，梶田隆章才是最晚出生的，答案是 ICRR (东京大学宇宙射线研究所).

3. 搜索发现是东京全国梅酒节，主页为 https://umeshu-matsuri.jp/tokyo_ueno/，下方有一个志愿者招募的链接 https://umeshu-matsuri.jp/tokyo_staff/，可以看到对应问卷的编号为 S495584522.

4. 猜测有参会优惠，答案为 0.

5. 在 STATPHYS 28 的网站上查看日程，发现 8 月 10 日晚上是 banquet，转到相关网站，发现是在安田讲堂 (Yasuda Auditorium) 集合。

6. 使用 New Bing 搜索后得知结果为熊猫-秋田犬。

## 赛博井字棋

查看源代码中的 script.js 逻辑，发现只要将 `setMove(x, y)` 中的判断已经被下的逻辑 `if (board[x][y] != 0) { return; }` 去掉，就可以覆盖掉已经下的棋子，从而获得胜利。

## 奶奶的睡前 flag 故事

查看图片，发现尺寸为 1080x1068，判断是截图被裁剪，由题干，猜测截图有漏洞可以恢复，搜索谷歌，截图，漏洞，找到相关漏洞，并使用漏洞发现者设计的 https://acropalypse.app/ 上传图片，选择 Pixel 5，可以看到恢复出的 flag.

## 组委会模拟器

使用 selenium 模拟，用正则匹配判断是否点击，一些要注意的点是因为滑动较快，需要先滑到对应元素在网页中再点，否则会出现点错的情况；另外在点击完一些之后就可以不管之前的元素了，每次从上次已经点完的元素开始判断，保证时间。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

url = "http://202.38.93.111:10021/?token=<token>"

driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='fakeqq-message__bubble']/span")
    )
)
element = driver.find_elements(
    by=By.XPATH, value="//div[@class='fakeqq-message__bubble']/span"
)

count = len(element)
index = 0
while 1:
    items = driver.find_elements(
        by=By.XPATH, value="//div[@class='fakeqq-message__bubble']/span"
    )
    count = len(items)
    i = index
    flag = 1
    while i < count:
        if re.match(r"这道题 flag 是hack\[[a-z]+\]", items[i].text):
            flag = 0
            print("click")
            driver.execute_script("arguments[0].scrollIntoView(false);", items[i])
            items[i].click()
            items.pop(i)
            i -= 1
            count -= 1
        elif flag:
            index = i
        i += 1
```

## 虫

搜索国际空间站，无线传输图片，发现 SSTV，下载相关软件，学习教程之后，把音频播放一遍就得到 flag.

## JSON $\subset$ YAML?

1. 直接输入 Infinity，得到 flag1. 原因：作为 JSON 读入得到 inf，但作为 YAML 读入得到 'Infinity' 字符串。

2. 输入 {"1":"2", "1":"2"}，得到 flag2. 原因：JSON, YAML1.1 允许重复键，但 YAML1.2 不允许。

## Git? Git!

使用 `git reflog` 命令查看到已经被还原的 commit，使用 `git reset --hard <commit>` 还原，得到 flag.

## HTTP 集邮册

1. 一通乱试，得到 5 个状态码，拿到 flag1.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\n\r\n`，得到 200 OK.
   - 使用 `GET /a HTTP/1.1\r\nHost: example.com\r\n\r\n`，得到 404 Not Found.
   - 使用 `GET / HTTP/2.1\r\nHost: example.com\r\n\r\n`，得到 505 HTTP Version Not Supported.
   - 使用 `PUT / HTTP/1.1\r\nHost: example.com\r\n\r\n`，得到 405 Not Allowed.
   - 使用 `GET / HTTP1.1\r\nHost: example.com\r\n\r\n`，得到 400 Bad Request.

2. 使用 `GET / \r\nHost: example.com\r\n\r\n`，得到 flag2. 原理：不指定 HTTP 版本号，默认为 HTTP/0.9，返回报文不包含 `\r\n`，按照逻辑判断即为无状态码。

3. 继续尝试，得到 12 个状态码，拿到 flag3.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nExpect: 100-continue\r\n\r\n`，得到 100 Continue.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nIf-Not-Modified-Since: Tue, 15 Aug 2023 17:03:04 GMT\r\nIf-None-Match: "64dbafc8-267"\r\n\r\n`，得到 304 Not Modified.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nIf-Unmodified-Since: Tue, 15 Aug 2023 17:02:04 GMT\r\n\r\n`，得到 412 Precondition Failed.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nRange: bytes=0-1023\r\n\r\n`，得到 206 Partial Content.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nRange: bytes=800-1023\r\n\r\n`，得到 416 Requested Range Not Satisfiable.
   - 使用 `GET / HTTP/1.1\r\nHost: example.com\r\nExpect: 100-continue\r\nContent-Length: 1000000000000\r\n\r\n`，得到 413 Request Entity Too Large.
   - 使用 `GET /<very long url> HTTP/1.1\r\nHost: example.com\r\n\r\n`，得到 414 Request-URI Too Large.

## Docker for Everyone

使用命令 `docker run -it -v /dev/shm:/home/shm:ro alpine` 挂载之后进入 Docker 容器内直接 `cat /home/shm/flag` 得到 flag.

## 惜字如金 2.0

按照逻辑，先将代码恢复到可以运行，再根据需要输出的字符串应该以 `flag{` 开头，恢复出 `code_dict` 得到 flag.

## 高频率星球

使用搜索替换操作，先将每行只留下 "o" 之后的那个字符串内内容，然后将 `\u001b` 转义符及对应被转义的内容全部删去，再将所有行合并到一行后把 `\r\n` 替换为换行，得到原本的 flag.js，运行得到 flag.

## 小型大语言模型星球

1. 重复 you are smart, you are smart, you are smart，得到输出 you are smart.

2. 下载训练集，使用程序跑一遍，得到结果 Apology.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained("./TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("./TinyStories-33M")

with open("TinyStories-train.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if "accepted" in line:
            message = line.split("accepted")[0]
            message = message[-8:-1]
            print(message)
        else:
            continue
        inputs = tokenizer.encode(message, return_tensors="pt")
        outputs = model.generate(
            inputs, max_new_tokens=30, num_beams=1, pad_token_id=tokenizer.eos_token_id
        )
        if 6292 in outputs[0, len(inputs[0]) :]:
            print("accepted")
            print(message)
            print(line)
            print(tokenizer.decode(outputs[0, len(inputs[0]) :]))
            print(outputs)
            break
```

## 流式星球

阅读源码，发现是将 `video.mp4` 读入之后，合并成一个 `(video_count * video_width * video_height * 3)` 的 array 后再随机裁剪不到 100 个字节的部分存入 `video.bin`，同时，`video_width` 和 `video_height` 都不是 10 的整数倍. 因此读入 `video.bin` 之后，保证补全到 3 的整数倍，再质因数分解，总共有最多 34 种可能，其中还有很多质因数大得不可能为结果，尝试之后得到正确的 `video_width` 为 427，`video_height` 为 253. 代码如下.

```python
import cv2
import numpy as np

with open("vi.bin", "rb") as f:
    buffer = np.fromfile(f, dtype=np.uint8)
    print(buffer.shape)

    width = 427
    height = 253

    buffer = np.pad(
        buffer,
        (
            0,
            ((buffer.shape[0] - 1) // (3 * width * height) + 1) * (3 * width * height)
            - buffer.shape[0],
        ),
    )
    print(buffer.shape)

    buffer = buffer.reshape((-1, height, width, 3))
    print(buffer.shape)
    writer = cv2.VideoWriter(
        "video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height)
    )
    for frame in buffer:
        writer.write(frame)
```

## 低带宽星球

1. 搜索图片压缩网页，找到 https://squoosh.app/editor，选择 webp，lossless，压缩后得到 flag.

## 为什么要打开 /flag 😡

1. (**似乎是非预期解**) 发现第一阶段的判断是使用的 `strstr` 函数在文件名中查找 `flag` 字段，则只需在程序中重新定义 `strstr` 函数，任何输入都返回 `NULL` 即可. 

```c
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

char *strstr(const char *__haystack, const char *__needle) {
    return NULL;
}

int main(void) {
    int fd = open("/flag", O_RDONLY);
    char buf[0x8000];
    read(fd, buf, 0x8000);
    printf("%s\n", buf);
    return 0;
}
```

## 异星歧途

打开之后发现最右侧八个按钮下方有一个“微型处理器”，单击之后查看逻辑，为每个按钮控制下方一排中的一个电力源，而整片电力源的输出在左下角那个电力节点，点击那个电力节点，找到前一个依赖的涡轮发电机，而涡轮发电机需要传送带桥上传来的资源，尝试点击上方按钮，发现第三第四个按钮点开后，涡轮发电机依赖的两个传送带桥被激活，但过一会又没电了，点击传送带桥，发现路径上有些缺少电力，一些来自于左边，因此尝试点击第一第二个，发现打开第二个后，稳定激活。第三个传送带桥需要来自右侧的电力，类似尝试后发现为 01110111.

之后来到最左侧，寻找类似的处理器，发现在按钮下方的传送带旁边，点击之后查看逻辑，发现是只要八个按钮满足任意一条就跳过打开的命令，只需让八个按钮都不满足即可，也就是 10100101.

第二组八个按钮，发现是要让八位数和小于 16 的数与 2 做 ^ 运算相同，最初以为是异或，后来发现下方“变量”按钮可以查看内部变量值，而这个实际上是小于 16 的数的平方，同时还要满足第一位和第六位为 1，因此是 11000100.

第三组八个按钮，发现需要让钍上的溢流门打开，钛上的反向溢流门关闭，钍反应堆打开，脉冲导管关闭，冷冻液混合器打开，抽水机打开，同样按照处理器逻辑即可，为 10001100.

因此答案为 10100101 11000100 10001100 01110111.
