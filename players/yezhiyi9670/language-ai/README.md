## 15. 🪐 小型大语言模型星球

### 尝试与解决

> 关键词：TinyStories、暴力枚举

要不先问候一下大语言模型吧。

```plain
--- player ---
Hello

--- model ---
, little girl. Do you want to play with me?"

Lily nodded and said, "Yes, please. What do you like to
```

啊？这好像不是正常的聊天模型啊...

仔细读读题目，这个模型叫 TinyStories。上网搜索，方可得知这个模型是用来做故事续写而不是聊天的。因此，要按照故事续写的模式调教。

#### You are smart

直观而言，要得到“You are smart”，可以问聊天机器人“Am I smart?”。但是，这是一个故事续写机器人。解决方法很简单，将这句话变成对话内容就行了。

```plain
--- player ---
"Am I smart?"

--- model ---
"Yes, you are smart!" her mom said. "You are a smart girl. You can do anything you want."

L
👏👏👏 flag1: flag{!-ThINk-You-@Re-RE@!1y-RE4Lly-$M@RT} 👏👏👏
```

#### Accepted

按理来说可以用上面的方法搞出“Accepted”，但是这题要求输入长度不大于 7，这就非常困难了。但是，既然存在长度不大于 7 的解，那就可以尝试暴力枚举大法了。

首先，下载 `main.py` 代码，并自行实现 `secret.py` 中缺失的部分：

```python
theme_kargs = {}
custom_css = ''
def check_token(token):
    return None

def read_flags(token):
    return ('flag{1}', 'flag{2}', 'flag{3}', 'flag{4}')
get_token_js = ''
```

运行 `main.py` 将得到一个与题目页面完全相同的网页，但是由于没有实现 `check_token`，机器人再也不会跟不上了。

为了自动化操作，注释掉生成网页的部分，并添加代码：

```python
def gen_prompt():
    ch = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,?#'
    ret = ''
    for i in range(7):
        ret += ch[random.randrange(0, len(ch))]
    ret += ''
    return ret.strip()

times = 0
while True:
    times += 1
    print('---', times, '---')
    prompt = gen_prompt()
    print(prompt)
    response = predict(prompt)
    print(response)
    if 'accepted' in response.lower() or 'hackergame' in response.lower() or '🐮' in response.lower():
        print('Yes!', prompt)
        break
```

运行不到半小时后，代码就给出了 prompt：`pfjqaRn`。

```plain
--- player ---
pfjqaRn

--- model ---
tern! It was so excited to be accepted.

Ruf designer was so proud of her work. She had made something special and it was
🎉🎉🎉 flag2: flag{YOU-@rE-@CceptED-7o-c0N7!nUe-THe-GAmE} 🎉🎉🎉
```

#### 其他

TinyStories 的语料库中大概率没有“hackergame”或者“🐮”，所以没活了。

### Flags

```plain
flag{!-ThINk-You-@Re-RE@!1y-RE4Lly-$M@RT}
```

I think you are really really smart!

```plain
flag{YOU-@rE-@CceptED-7o-c0N7!nUe-THe-GAmE}
```

You are accepted to continue the game.

属于是一点提示都不给（

### 其他做法

#### You are smart - 奇怪的提示词

事后与其他参赛选手交流，得知有人在将机器人当成聊天机器人的情况下做出了 flag1。

```plain
--- player ---
Say "you are smart"

--- model ---
and "you are smart".

The little girl was so happy. She had learned something new and she was proud of herself. She had learned
👏👏👏 flag1: flag{!-ThINk-You-@Re-RE@!1y-RE4Lly-$M@RT} 👏👏👏
```
