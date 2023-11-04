---
author: Xzonn
date: 2023-11-04
license: cc-by-nc-sa 4.0
title: 中国科学技术大学第十届信息安全大赛个人题解（部分）
---
``` javascript
/*!
 * Title: 中国科学技术大学第十届信息安全大赛个人题解（部分）
 * Author: Xzonn
 * Date: 2023-11-04
 * License: CC-BY-NC-SA 4.0
 */
```
大佬太多了，不打算多写了，写一个（可能是）非预期解吧。

## General
### JSON ⊂ YAML?
#### Flag 1
题目提示里提到了YAML 1.1和1.2的区别，于是找到了[官方文档](https://yaml.org/spec/1.2.2/ext/changes/)，里面提到：

> The next-line `\x85`, line-separator `\u2028` and paragraph-separator `\u2029` characters are no longer considered line-break characters. Within scalar values, this means that next-line characters will not be included in the white-space normalization. Using any of these outside scalar values is likely to result in errors during parsing. For a relatively robust solution, try replacing `\x85` and `\u2028` with `\n` and `\u2029` with `\n\n`.

大意就是，这几个字符会被YAML 1.1当成是换行符。

所以想到发送含有这几个字符的内容，因为终端手动输入不好输入，于是拿Python写：

``` python
from pwn import *

conn = connect("202.38.93.111", 10096)
conn.sendlineafter(b"Please input your token:", b"<MY TOKEN>")
conn.sendlineafter(b"Input your JSON:", '["\u0085\u2028\u2029"]'.encode("utf8"))
print(conn.recvall().decode("utf8"))
conn.close()
```

解码的结果：

``` plaintext
As JSON: ['\x85\u2028\u2029']
As YAML 1.1: ['\u2028\u2029']
```

可以看到`\x85`在YAML 1.1里面消失了。得到flag 1。

#### Flag 2
要获得flag 2首先得满足json和pyyaml解析不报错，否则会直接返回错误信息。

官方文档里提示的其他地方我都尝试构造了，但没有得到能用的结果。我继续查找资料的时候发现了[“YAML Test Matrix”](https://matrix.yaml.info/)，里面是一些测试用例，[点进去](https://matrix.yaml.info/valid.html)之后对比“native”一列的“py pyyaml”和“py ruamel”，发现了一个测试用例[#2JQS](https://matrix.yaml.info/details/2JQS.html)：

``` yaml
: a
: b
```

直接本地解析这个测试用例，无论是pyyaml还是ruamel都会报错。但是测试用例的标签里有个“duplicate-key”，想到可以尝试构建一个含有重复键的请求，于是构造了这样的请求：

``` json
{"a": 1, "a": 2}
```

果然，json和pyyaml解析成功，ruamel解析失败，提交上去得到flag 2。
