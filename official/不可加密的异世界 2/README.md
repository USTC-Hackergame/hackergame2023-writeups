# 不可加密的异世界 2

题解作者：[tl2cents](https://github.com/tl2cents)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：math

- 题目分值：希尔混淆（250）+ 希尔之核（200）+ 希尔之秘（300）


时隔一年，你在异世界误入了一个名为希尔的秘境，只有破解希尔之核（Hill's Kernel）的秘密，才能破局。当然，在牢固数理基础下，基于矩阵的加密简直小菜一碟，来让它失效吧。

### 希尔混淆

虽然希尔加密很简单，但是希尔秘境中笼罩着一层迷雾，使你无法直接接收希尔 Oracle 返回的输出，可是聪明的你发现通过某个固定的角度观察，希尔混淆的作用似乎是非常简单的。



### 希尔之核

终于你走出迷雾，到达了希尔秘境的核心，这里你只需要让希尔加密失效。

“咦？这不是有个开关吗，简直是送分题，太好了。”



### 希尔之秘

虽然你让希尔加密失效了，也顺利走出了希尔秘境。可是构造的输入都是乱七八糟的，简单 print 之后是一堆乱码，作为强迫症的出题人，看着非常别扭。于是只要你的输入足够好看，能够打印出来，就可以再拿一个白嫖的 flag。




### 题目信息

- [题目附件下载](./files/unencryptable_world2.sage)
- 你可以通过 `nc 202.38.93.111 22000` 来连接题目，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

### 附录

本题解提供了[修复了 `decrypt()` 的附件下载](./files/unencryptable_world2_fixed.sage)，该修改不影响做题。

## 题解

题目逻辑其实很简单，生成一个在有限域 $\mathbf{GF}(257)$ 上 $128 \times 128$ 的特殊矩阵 $M$ 作为希尔加密的密钥，不想直接给出矩阵 $M$ , 于是借鉴了 2023 LACTF 的 [hill-hard](https://b6a.black/posts/2023-02-26-lactf/#hill-hard-31-solves) 稍微增加了一点难度，弄成了第一问。本题提供两个 oracle，首先检查给定的消息加密后是否等于本身，否则会和填充后 flag1 异或后加密再输出密文。

$$
c =  M \cdot p \\
\stackrel{c \ne p}{\implies} c^\prime  = M \cdot (p \oplus flag_1)
$$

Exp ： [exp.sage](./exp.sage)



### 希尔混淆（密钥恢复）

首先不考虑混淆的影响，希尔加密是纯线性的，每次选择明文加密理论上都可以拿 128 组方程，交互 128 次，就可以把整个 $128 \times 128$  的矩阵密钥完全恢复，一个最简单的选择是每次输入明文 

$$
\vec{p_i} = (x_1,\cdots, x_{128}), \quad  x_i = 1, x_j = 0, \forall j \ne i
$$

即每次获取密钥矩阵的第 i 列。



在加入混淆之后直接加密的明文不可控了，但是明文差分在多次选择明文的场景下仍然是可控的，考虑从明文差分入手。此时如果两次明文的差分只在单个字节的单个比特上，比如 $\Delta_p = x \oplus flag_1 \oplus y \oplus flag_1 = x \oplus y = (1,0,\cdots,0)$ ，则：

$$
\Delta_c = C_x - C_y = M\cdot (x \oplus flag_1) - M \cdot (y \oplus flag_1)
$$

$$
=\begin{array}{lr}
M \cdot (1,0,\cdots,0) & flag_1[0]\oplus x[0] \text{ lsb is 1}\\
-M \cdot (1,0,\cdots,0) & flag_1[0]\oplus x[0] \text{ lsb is 0}
\end{array}
$$

此时对于我们构造的**输入差分**，根据返回的**密文差值**，存在两组可能的方程，这时候如果单纯靠穷举，需要解 $2^{128}$ 次方程组。因此我们需要一些确定的比特来构建方程或者某种方法确定正确的方程组。


预期解：由于 $flag_1$ 都是 ascii，则 $flag_1$ 转换成字节向量，每个维度的值都在 0~127 之间，即 flag 的最高比特位都是 0。因此，构造差分输入 $\Delta_{p_1}, \Delta_{p_2}, \cdots , \Delta_{p_{128}} = 128 \vec p_1, 128 \vec p_2, \cdots, 128 \vec p_{128}$ ，然后解方程组即可。



#### Remarks

除了上述核心思路，还需要注意的点是加解密中会把 256 强制转换成 0，因此我们每次获取到的密文中可能存在字节等于 0，这个时候我们无法确定其精确值。假设在完全随机的情况下，密文中不出现 0 字节的可能性为：

$$
p = (\frac{255}{257})^{128} \approx 0.36787757002747357
$$

因此，要获取 128 组完全可以确定差分方程组的明文输入，需要获取的密文次数为：

$$
n = \frac{128}{p} \approx 348
$$

这在题目最大 oracle 次数为 400 的情况下是完全可行的。

除此之外，**我们需要保证每次输入的差分与已有的差分方程组是线性无关的**，因为这样的输入对求解密钥矩阵没有任何帮助，还会浪费 oracle 的次数，实现细节参考 [exp](./exp.sage#L65) 的代码。 



### 希尔之核

此时我们已经恢复 $128 \times 128$ 的密钥矩阵 $M$ ，让希尔加密失效，数学化的表达就是，求  $\mathbf{GF}(257)$ 上 128 维的向量 $\vec v$ 使得：

$$
M \cdot \vec v = \vec v
$$

其实就是寻找特征值为 1 的特征向量 $\vec v$ ，上述式子化简一下就是：

$$
\underbrace{(M - I)}_{M^\prime} \cdot \vec v = 0
$$

对于一般的矩阵 $M$ ， $M^\prime$ 大概率是是满秩的，也就意味着上式只有唯一解零向量 $\vec 0$ 。但是本题中矩阵生成方式如下：

``` python
def random_square_matrix_with_fixed_rank(ring, nrows, rank):
    M = random_matrix(ring, rank, nrows)
    result = [list(row) for row in M]
    for i in range(nrows - rank):
        row = random_vector(ring, rank) * M
        result.append(row)
    random.shuffle(result)
    result_matrix = matrix(ring, result)
    assert M.rank() == rank, "bad matrix"
    return result_matrix

def random_square_matrix_with_full_rank(ring, nrows):
    result_matrix = random_square_matrix_with_fixed_rank(ring, nrows, nrows//2) + 1
    return result_matrix
```



也就是说密钥矩阵对应  $128 \times 128$ 的 $M^\prime$ 的秩为 64，这意味着 $M ^ \prime \cdot \vec v = 0$  存在非零解。解方程即可，或者直接计算矩阵 $M^\prime$ 的右核空间。



#### Remarks

这题就是纯粹的解方程，感觉第一问预期解做出了，这一问应该完全没难度。



### 希尔之秘

我们考虑：

$$
\underbrace{(M - I)}_{M^\prime} \cdot \vec v = 0
$$


$M^\prime$ 的秩为 64，也就意味 $M^\prime$ 的右核空间（Right-Kernel）的秩为 $128 - 64 = 64$ ，记右核空间为

$$
M_r = \mathcal{Ker}(M^\prime) = (\vec v_1, \vec v_2, \cdots, \vec v_{64})
$$

则 $(\vec v_1, \vec v_2, \cdots, \vec v_{64})$ 的任意线性组合 $\vec v = \sum_{i} a_i \vec x_i$ 都满足 $M^{\prime} \cdot \vec v = \vec 0$ 。



我们要找到一组系数 $a_1,a_2,\cdots a_{64}$ 恰好使得 $\vec v$ 转换成字节后都在可打印字符 0x20 ~ 0x7e 集合内。这是典型的格上搜索场景，可以考虑将其转换为最近向量问题 CVP（[Closest Vector Problem](https://en.wikipedia.org/wiki/Lattice_problem#Closest_vector_problem_(CVP))）求解。



构造格：

$$
B = \begin{bmatrix}
M_r \\
257 \cdot I
\end{bmatrix}
$$

可打印字符的中值为 79，因此我们想要在 $\mathcal{L}(B)$ 上寻找一个尽量接近目标向量 $\vec t = (79,79,\cdots,79)$  的格点 $\vec v$ 。这里用 BKZ 规约到一组好的基后，直接使用 [Babai](http://www.noahsd.com/mini_lattices/05__babai.pdf) 最近平面算法即可。 