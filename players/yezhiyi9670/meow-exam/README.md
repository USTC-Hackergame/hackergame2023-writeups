## 2. 猫咪小测

### 尝试与解决

> 关键词：枚举、GitHub 搜索、学术搜索

#### 适合枚举的问题

前两个问题的答案是非负整数。

西区图书馆是一个比较高的楼，但也不是太高，楼层数绝对不会超过 25。因此第一题经过简单枚举即可获得答案 12。

根据对物理常量的经验，第二题的答案也很难超过 120，同样采用枚举获得答案，为 23。

#### 启用 TCP BBR 的内核编译选项

在网上搜索 Linux TCP BBR，很难找到答案。许多搜索结果都是指出在 Linux 发行版中如何启用 TCP BBR，而不是编译时如何启用。即使加入“内核 编译”关键词似乎也无济于事。

这种情况并非无解。一个非常可靠的方法是，直接[前往 GitHub 搜索找到 Linux 内核源代码](https://github.com/torvalds/linux)。在代码仓库内搜索“TCP BBR”，可以找到 `net/ipv4/Makefile` 文件内的线索：

```makefile
obj-$(CONFIG_INET_TCP_DIAG) += tcp_diag.o
obj-$(CONFIG_INET_UDP_DIAG) += udp_diag.o
obj-$(CONFIG_INET_RAW_DIAG) += raw_diag.o
obj-$(CONFIG_TCP_CONG_BBR) += tcp_bbr.o
obj-$(CONFIG_TCP_CONG_BIC) += tcp_bic.o
obj-$(CONFIG_TCP_CONG_CDG) += tcp_cdg.o
obj-$(CONFIG_TCP_CONG_CUBIC) += tcp_cubic.o
```

这里的 `CONFIG_TCP_CONG_BBR` 就很可能是答案了。提交验证，确实是。

#### Python 类型检查死循环问题

寻找这样的论文，一个很好的去处是 Google 学术搜索。根据“Python 类型检查死循环”可以拟定关键词“python type check infinite loop”（注意死循环一般不叫“Dead loop”）。但是，这样找到的结果非常多，相关性也不够强。这里很可能存在的问题是，死循环“Infinite loop”很可能不会出现在论文的标题里。

但是，题面还给出了一句话，“Python 的类型检查和停机问题一样困难”。停机问题是指判断一个一般的图灵机在给定输入下能否停机（即能否运行结束），可以用反证法证明不存在一般的解法。因此，可以将“死循环”关键词换成“图灵完备”，即“Turing complete”。

现在就可以在 Arxiv 上找到一个看起来很像的论文了：[Python Type Hints are Turing Complete](https://arxiv.org/abs/2208.14755)。但是，Arxiv 并没有指出论文在什么学术会议上使用。不妨使用论文的标题再次进行网页搜索，很快就可以找到“ECOOP 2023”字样，看来 ECOOP 就是答案了。

### Flags

```plain
flag{w3lCoM3-7o-@7tEND-7HE-nEk0-EXAM-Z0z3}
```

```plain
flag{R3al-M@S73R-of-The-NekO-3X@M-iN-u$7c}
```
