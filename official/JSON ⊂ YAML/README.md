# JSON ⊂ YAML?

题解作者：[Hypercube](https://0x01.me/)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：JSON ⊄ YAML 1.1（100）+ JSON ⊄ YAML 1.2（100）

你知道吗？Hackergame 出题时，每道题都需要出题人用 YAML 格式写下题目的关键信息。然而，每年总有一些出题人在编写 YAML 文件时被复杂的语法规则弄得头疼不已。

这天小 Z 又找到小 W 说：「我昨天写 YAML 时，又花了半天研究 YAML 的规范，YAML 好难啊！」

小 W 惊讶道：「怎么会有人不会写 YAML 呢？只要你会写 JSON 就会写 YAML 呀，因为任何合法的 JSON 本身就是合法的 YAML。」

小 Z 听闻这番言论后当场表示怀疑，立刻说出了一个字符串，JSON 和 YAML 解析出的含义存在差异。小 W 研究了一番才发现，这是因为很多主流的 YAML 库仍然是 YAML 1.1 的，它没有这个性质。他不得不承认：「好吧，这个性质只适用于 YAML 1.2。」

小 Z 笑了：「别提 YAML 1.2 了，它遇到合法的 JSON 都有可能报错。」

**[下载题目源代码](files/yaml_vs_json.py)**

你可以通过 `nc 202.38.93.111 10096` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

## 题解

### JSON ⊄ YAML 1.1

输入 `1e2` 可以拿到这个 flag。解题思路可以来自[这个问题](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)中提到的 `12345e999`，或者[这篇文章](https://john-millikin.com/json-is-not-a-yaml-subset)中提到的 `1e2`。

[JSON](https://www.json.org/json-zh.html) 的数字格式很清晰，网页上有一张图，可以翻译为这个正则表达式（为了增加可读性，我加了一些空格，下同）：

```regex
-?  (0|[1-9][0-9]*)  (\.[0-9]+)?  ([eE][-+]?[0-9]+)?
```

可以看出这个规则是比较严格的，不允许使用正号，不允许有前面的零（除非只有一个零），只要有小数点就必须有小数部分。

YAML 1.1 就没这么清晰了，实际上，你翻遍[这个网页](https://yaml.org/spec/1.1/)也不会找到任何关于数字格式的规定。因为 YAML 1.1 并没有规定未标注类型的文字该按什么规则确定类型，而是允许解析器自己实现一系列正则表达式，逐一尝试匹配。[YAML 1.1 tag repository](https://yaml.org/type/index.html) 提供了一些常见的类型，供解析器参考。其中，十进制浮点数的正则表达式是：

```regex
[-+]?  ([0-9][0-9_]*)?  \.  [0-9.]*  ([eE][-+][0-9]+)?
```

这个正则表达式极其宽松，这是一些它能匹配的情况：`.`、`...`、`+0_0_..0..e+0`。但是，它匹配不了 `1e2`，因为小数点是必须的。这么宽松的规则真的能用吗？它岂不是会导致 YAML 文档中的大量包含点的文字都被误认为是浮点数？实际上，PyYAML 库用的确实不是这个。从[它的源代码](https://github.com/perlpunk/pyyaml/blob/ee37f4653c08fc07aecff69cfd92848e6b1a540e/lib3/yaml/resolver.py#L179-L183)中可以看到，它支持两种十进制浮点数（不考虑 60 进制和特殊值）：

```regex
[-+]?  ([0-9][0-9_]*)   \.  [0-9_]*  ([eE][-+][0-9]+)?
                        \.  [0-9_]+  ([eE][-+][0-9]+)?
```

对比 JSON 的规则和上面两条规则，可以发现，总共有两处存在 JSON 能匹配，但上面两条规则不能匹配的情况。一是**没有小数点**，二是**指数部分没有正负号**。

即使选手没有考虑到 PyYAML 用的正则表达式和 YAML 1.1 推荐的不一致，也不会对这道题的解题产生影响，因为 PyYAML 和 YAML 1.1 推荐的正则表达式之间的差异，全部发生在 JSON 不能匹配的情况中。对于 JSON 能匹配的情况，PyYAML 和 YAML 1.1 推荐的正则表达式总是会给出一致的结果。

### JSON ⊄ YAML 1.2

这个 flag 实际上有一个额外的要求，就是输入必须能正常被 YAML 1.1 解析成功。这是故意的，因为能让 YAML 1.1 与 YAML 1.2 同时报错的输入太多了，非常容易找到，例如超长的 key（1024 字符）、`\t0`、`0\t`、`{""\n:0}`、`[0,\t1]`（其中 `\t` 和`\n` 需要分别换成 tab 和换行符）等。显然 YAML 1.2 并不像自己所承诺的那样是“a strict superset of JSON”。

输入 `{"":0,"":0}` 可以拿到这个 flag。解题思路可以来自[这个问题](https://stackoverflow.com/questions/21584985/what-valid-json-files-are-not-valid-yaml-1-1-files)中提到的“with one minor caveat regarding duplicate keys”，或者 [ruamel.yaml 库的文档](https://yaml.readthedocs.io/en/latest/api/)中提到的“Duplicate keys”。

JSON 由两个规范定义：[ECMA-404](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/) 与 [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)，它们明确提到了二者对语法方面的定义应当是完全一致的。ECMA-404 的表述更宽松一些，它说：

> The JSON syntax ... does not require that name strings be unique ...

RFC 8259 的表述更严格一些，它说：

> The names within an object SHOULD be unique.

其中大写的“SHOULD”是 RFC 的一个术语，表示特定情况下可以违反这个规则，但是要考虑到可能会导致的问题。

然而，[YAML 1.2](https://yaml.org/spec/1.2.2/) 说：

> The content of a mapping node is an unordered set of key/value node pairs, with the restriction that each of the keys is unique.

这个规则是绝对的，YAML 1.2 解析器在遇到重复的键时必须报错。

至于如何能用一个输入同时获得两个 flag，出题人认为最短的答案需要 13 个字符：`{"":0,"":1e2}`。

## 花絮

在出题过程中，我发现 YAML 的生态很糟糕。不仅很多库是 YAML 1.1 的，不容易知道每个使用 YAML 的地方是否按 YAML 1.2 解析，而且几乎没有完全符合 YAML 1.2 标准的库。[这个网站](https://matrix.yaml.info/)展示了各种语言的 YAML 库分别能通过多少 YAML 1.2 的测试样例，可以看到错误是很多的。

另外，因为 YAML 1.2 的文档中说自己是 JSON 的超集，所以这个误解在网上随处可见，产生了很多后果。一个我觉得挺搞笑的例子是 [Python 标准库 json 的官方文档](https://docs.python.org/zh-cn/3/library/json.html)中的这段话：

> JSON 是 YAML 1.2 的一个子集。由该模块的默认设置所产生的 JSON（尤其是默认的 separators 值）也是 YAML 1.0 和 1.1 的一个子集。因此该模块也能被用作 YAML 序列化器。

不，JSON 不是 YAML 1.2 的一个子集，而且用这个模块默认设置序列化 1e20 这个数字所产生的 JSON（`json.dumps(1e20)` 结果为 `1e+20`）也不能正确被 YAML 1.1 解析（会解析成字符串而非数字）。两个错误分别存在 [9 年多](https://github.com/simplejson/simplejson/blob/1ddfc5ace82f4fbda2a6a85c62a063ae45c94576/index.rst?plain=1#L127-L130)和 [17 年多](https://github.com/simplejson/simplejson/blob/27ece5964f2da82383ca24b128ecfca962baa93f/docs/index.html#L143-L144)了，simplejson, please fix.

不过，抛开“JSON 的超集”这个谎言不谈，YAML 还是个不错的选择，比较适合用于自己写的程序的配置文件。只要确保你用的是一个 YAML 1.2 的库，很多老生常谈的问题（例如 `country: no` 或 `port: 22:22`）都不会出现。JSON 也确实几乎都是合法的 YAML 1.2，所以不确定 YAML 该怎么写的时候可以用 JSON 的写法写，对于简单的小程序的配置文件这个需求来说够用了。

## 补充

赛后看 QQ 群里的讨论，出题人才意识到输入 `NaN` 或 `Infinity` 也能拿到一个 flag。这和本题想考的知识点完全无关，因为这是 Python 的 `json.loads` 额外支持的非标准的功能，JSON 标准中没有这种东西。明明每次用 `json.dumps` 的时候都记得这回事的（因为它有一个叫 `allow_nan` 的参数控制是否启用这一行为），但用 `json.loads` 的时候就忘了（它文档没说，并且也不好禁用这个行为），好气啊。
