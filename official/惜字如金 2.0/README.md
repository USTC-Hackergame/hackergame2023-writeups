# 惜字如金 2.0

题解作者：[zzzz](https://github.com/ustc-zzzz)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

* 题目分类：math

* 题目分值：200

<!-- markdownlint-disable first-line-heading -->
惜字如金一向是程序开发的优良传统。无论是「[creat](https://stackoverflow.com/questions/8390979/why-create-system-call-is-called-creat)」还是「[referer](https://stackoverflow.com/questions/8226075/why-http-referer-is-single-r-not-http-referrer)」，都无不闪耀着程序员「节约每句话中的每一个字母」的优秀品质。上一届信息安全大赛组委会在去年推出「惜字如金化」（XZRJification）标准规范后，受到了广大程序开发人员的好评。现将该标准辑录如下。

### 惜字如金化标准

惜字如金化指的是将一串文本中的部分字符删除，从而形成另一串文本的过程。该标准针对的是文本中所有由 52 个拉丁字母连续排布形成的序列，在下文中统称为「单词」。一个单词中除「`AEIOUaeiou`」外的 42 个字母被称作「辅音字母」。整个惜字如金化的过程按照以下两条原则对文本中的每个单词进行操作：

* 第一原则（又称 creat 原则）：如单词最后一个字母为「`e`」或「`E`」，且该字母的上一个字母为辅音字母，则该字母予以删除。
* 第二原则（又称 referer 原则）：如单词中存在一串全部由完全相同（忽略大小写）的辅音字母组成的子串，则该子串仅保留第一个字母。

容易证明惜字如金化操作是幂等的：惜字如金化多次和惜字如金化一次的结果相同。

### 你的任务

附件包括了一个用于打印本题目 flag 的程序，且已经经过惜字如金化处理。你需要做的就是得到程序的执行结果。

### 附注

本文已经过惜字如金化处理。解答本题不需要任何往届比赛的相关知识。

---

XIZIRUJIN has always been a good tradition of programing. Whether it is "[creat](https://stackoverflow.com/questions/8390979/why-create-system-call-is-called-creat)" or "[referer](https://stackoverflow.com/questions/8226075/why-http-referer-is-single-r-not-http-referrer)", they al shin with th great virtu of a programer which saves every leter in every sentens. Th Hackergam 2022 Comitee launched th "XZRJification" standard last year, which has been highly aclaimed by a wid rang of programers. Her w past th standard as folows.

### XZRJification Standard

XZRJification refers to th proces of deleting som characters in a text which forms another text. Th standard aims at al th continuous sequences of 52 Latin leters named as "word"s in a text. Th 42 leters in a word except "`AEIOUaeiou`" ar caled "consonant"s. Th XZRJification proces operates on each word in th text acording to th folowing two principles:

* Th first principl (also known as creat principl): If th last leter of th word is "`e`" or "`E`", and th previous leter of this leter is a consonant, th leter wil b deleted.
* Th second principl (also known as referer principl): If ther is a substring of th sam consonant (ignoring cas) in a word, only th first leter of th substring wil b reserved.

It is easy to prov that XZRJification is idempotent: th result of procesing XZRJification multipl times is exactly th sam as that of only onc.

### Your Task

A program for printing th flag of this chaleng has been procesed through XZRJification and packed into th atachment. Al you need to do is to retriev th program output.

### Notes

This articl has been procesed through XZRJification. Any knowledg related to previous competitions is not required to get th answer to this chaleng.

**[打开/下载题目](src/print_flag.py)**

## 题解

这道题有两种不同的预期解法，一种基于穷举，一种基于推理。

首先观察题目给出的「源代码」（[`print_flag.py`](src/print_flag.py)），不难注意到以下五行：

```python
cod_dict += ['nymeh1niwemflcir}echaet']
cod_dict += ['a3g7}kidgojernoetlsup?h']
cod_dict += ['ulw!f5soadrhwnrsnstnoeq']
cod_dict += ['ct{l-findiehaai{oveatas']
cod_dict += ['ty9kxborszstguyd?!blm-p']
```

`cod_dict`（实为 `code_dict`，以下简称「码表」）的每个元素都看起来有 23 个字符，但后面的代码提醒我们实际上有 24 个：

```python
check_equals(set(len(s) for s in cod_dict), {24})
```

说明码表的每个元素都有一个字符被惜字如金化去掉了。根据惜字如金化的规则，我们可以得知被去掉的字符一定位于辅音字母后面，并按照两条原则分别得知：

* 第一原则：如果后面不再是字母，则该辅音字母后面可能是 `e` 或者 `E`。
* 第二原则：该辅音字母后面可能是其本身的小写或大写形式。

我们需要做的就是找到被去掉的字符，以及它所在的位置。事实证明，位置其实比字符本身是什么更关键。

### 解法一：穷举

确定了每一个可能被被去掉的字符及其位置后，我们就可以通过穷举找到结果：

```python
#!/usr/bin/python3

from itertools import product

consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
letters = consonants + 'aeiouAEIOU'


def recover(chars):
    results = []
    for i in range(0, len(chars)):
        if chars[i] in consonants:
            results.append(chars[:i] + chars[i].lower() + chars[i:])
            results.append(chars[:i] + chars[i].upper() + chars[i:])
            if i == len(chars) - 1 or chars[i + 1] not in letters:
                results.append(chars[:i] + 'e' + chars[i:])
                results.append(chars[:i] + 'E' + chars[i:])
    return results


flag_collection = set([])
choice_indexes = [53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                  17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                  31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                  25, 63, 77, 36, 5, 32, 60, 67, 113, 28]

for choice in product(recover('nymeh1niwemflcir}echaet'),
                      recover('a3g7}kidgojernoetlsup?h'),
                      recover('ulw!f5soadrhwnrsnstnoeq'),
                      recover('ct{l-findiehaai{oveatas'),
                      recover('ty9kxborszstguyd?!blm-p')):
    chars = [choice[c // 24][c % 24] for c in choice_indexes]
    if chars[:5] == ['f', 'l', 'a', 'g', '{'] and chars[-1] == '}':
        if '}' not in chars[5:-1]: flag_collection.add(''.join(chars))

for flag in flag_collection: print(flag)
```

在命题人的笔记本电脑（Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz）上，得到结果大约需要 2 分钟时间。

注意第二个判断的条件：它不仅要求最后一个字符是 `}`，还要求了这个字符只出现一次。

### 解法二：推理

那是否有办法不通过编写计算机程序得到结果呢？答案是肯定的。

总的来说，输出一共 40 个字符，满足条件的输出共有三个要求：

* 输出字符 0-4 分别是 `flag{`
* 字符 5-38 不出现 `}`
* 字符 39 是 `}`

我们先从输出字符 0 开始。在定义码表的五个元素中，输出字符 0 对应码表第三个元素的字符 5（`53`）。然而，第三个元素惜字如金化后的字符 5 是 `5`，字符 4 才是 `f`，这说明被惜字如金化的字符在字符 4 前——这样才能把 `f` 顺延到惜字如金化前的字符 5 的位置。这样做带来了一个确定的事情，就是：惜字如金化前 `f` 及之后的字符已经全部确定了，我们简记为：

```plain
*****f5soadrhwnrsnstnoeq
```

然后是输出字符 1，它对应码表第二个元素的字符 17（`41`）。第二个元素惜字如金化后的字符 17 正是 `l`，这说明被惜字如金化的字符在字符 17 后——惜字如金化前第二个元素我们确定如下：

```plain
a3g7}kidgojernoetl******
```

对输出字符 2-4 及 39 能够得到以下的结果：

```plain
************************
a3g7}kidgojernoetl******
*****f5soadrhwnrsnstnoeq
***{l-findiehaai{oveatas
*************guyd?!blm-p
```

还有大量的字符我们仍然没有头绪。但实质上第一行仍然可以确定很多字符——这是由输出字符 10 确定的，它对应码表第一个元素的字符 17（`17`）。我们注意到第一个元素惜字如金化后的字符 17 是 `e`，但字符 16 是 `}`：这说明被惜字如金化的字符绝不可能在 `}` 之前，否则字符 17 将顺延到 `}`，从而使得输出包含不止一个 `}` 字符。现在我们把推断得出的结果整理如下：

```plain
nymeh1niwemflcir}*******
a3g7}kidgojernoetl******
*****f5soadrhwnrsnstnoeq
***{l-findiehaai{oveatas
*************guyd?!blm-p
```

此时只剩下输出字符 7 和输出字符 10 没有解开。输出字符 10 对应的是码表第一个元素 `}` 后，说明它不可能是被惜字如金化的字符（`}` 不是辅音字母），那自然就是它的下一个字符 `e`，而输出字符 7 对应的是码表第三个元素的开头，而一个单词的开头不可能被惜字如金化，那么它就直接对应字符 `u`。最后逐个代入，得到的输出就是我们的 flag：

```plain
flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}
```

以上推理也证实了 flag 是唯一的。

### 惜字如金化前的程序

[`print_flag_original.py`](src/print_flag_original.py) 是惜字如金化前的程序，仅供参考——符合条件的情况有很多。
