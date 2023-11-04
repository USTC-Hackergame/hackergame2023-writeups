# 小 Z 的谜题

题解作者：[mingliangz](https://github.com/mlzeng)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：math

- 题目分值：Easy（200）+ Medium（200）+ Hard（300）

方程之中

变量如锁链相扣

约束交织成网

组合间蕴藏古老的秘密

在变量的森林中追寻

足迹遍历每一个角落

在约束的花丛中舞蹈

影子覆盖每一寸土地

和谐之美指引着方向

我们终将找到自己的答案

**[下载题目源代码](files/puzzle_of_z.py)**

你可以通过 `nc 202.38.93.111 10098` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

## 题解

这道题 idea 是 @zzh1996 的，我负责 implementation。

首先阅读源代码理解谜题的逻辑，发现本质是一个三维积木问题：

```python
import itertools

# 可以摆放积木的三维空间的每一维的长度
bound = 5
# 每一种积木的形状（每一维的长度）
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
# 每一种积木的数量
count = [3, 4, 2, 2, 2, 3]
# 积木的总数量（16）
num_constraints = sum(count)
# 问题的维度（3）
num_dims = len(constraints[0])
# 存储积木的摆放方式（离原点最近与最远的两个顶点的坐标）
# arrange[i][j][k] 代表第 i 个积木的第 k 个顶点（k=0,1）的第 j 维度（j=0,1,2）的坐标值
# k=2 时值一定是 -1
arrange = [[[0 for k in range(3)] for j in range(num_dims)] for i in range(num_constraints)]
print('Input a string:')
# 读取积木的摆放方式并检查积木在三维空间边界内
s = (c for c in input().strip())
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(3):
            if k == 2:
                arrange[i][j][k] = -1
            else:
                number = int(next(s))
                assert 0 <= number <= bound
                arrange[i][j][k] = number
print('Stage 0 passed')
# 检查积木是否按照顶点坐标排序
assert arrange == list(sorted(arrange))
print('Stage 1 passed')
# 检查积木摆放是否存在重叠部分（枚举积木对并使用计算几何长方体相交判定方法）
for i in range(num_constraints):
    for j in range(num_constraints):
        if i == j:
            continue
        assert any((arrange[i][k][1] <= arrange[j][k][0] or arrange[j][k][1] <= arrange[i][k][0]) for k in range(num_dims))
print('Stage 2 passed')
# 统计每个积木的类型以确保每个积木都已经被使用了
# 注意需要考虑积木是可以旋转的
for i in range(num_constraints):
    for t in range(len(constraints)):
        if tuple(sorted([arrange[i][j][1] - arrange[i][j][0] for j in range(num_dims)])) == constraints[t]:
            count[t] -= 1
            break
assert not any(count)
print('Stage 3 passed')
# 统计所有积木的顶点以及其多个方向的投影总共占用的格点数量作为分数
score = len(set((x, y, z) for i in range(num_constraints) for x, y, z in itertools.product(*arrange[i])))
# 根据分数所在的范围提供 flag
if score >= 157:
    print(open('/flag3').read())
elif score <= 136:
    print(open('/flag2').read())
else:
    print(open('/flag1').read())
```

通过查找三维积木问题相关资料，可以知道这个谜题是 conway puzzle 的变体。Stage 1 的约束在求解时可以忽略，得到解之后再进行排序就可以通过检查。把网络上搜到的解答简单做一下变形就可以得到 flag1，而 flag2 和 flag3 有比较严格的 score 范围限制，通过尝试可以发现手动构造是很难达到的，需要使用搜索算法来找到符合要求的解。

flag2 可以使用简单的搜索算法（例如 DFS）来得到。考虑到 score 很低，可以尝试把一些小方块合并成大方块来减少搜索量。

flag3 不能通过合并方块来减少搜索量。通过计算体积之和可以发现所有积木刚好可以覆盖全部空间，于是可以把问题转化为精确覆盖问题。把空间的每个单元格以及每个积木作为一个元素，元素被选取代表对应的单元格被占有或者该积木被使用。一个积木及其覆盖的单元格就构成了一个元素的集合，枚举每个积木及其所有摆放方法就可以得到一系列集合，那么目标就是从这一系列集合中选出一部分集合，使得它们互不相交，并且它们的并集包含了所有元素，也就是精确覆盖。精确覆盖意味着每个积木都被（不重复）使用而且每个格点都被（不重复）占有，对应了积木问题的一个解。

如果阅读过 conway puzzle 的求解方法，可以知道有一个 parity 约束可以非常有效地加速问题求解，这个约束也可以被转化为精确覆盖问题的形式。

精确覆盖问题可以使用 Donald Knuth 发明的 Dancing Links X 算法高效求解。

编写 Python 代码把积木问题转化为精确覆盖问题，然后调用 SageMath 的 DLX 算法求解即可。

```python
import itertools
import math
from sage.combinat.dlx import *

blocks = ((1, 1, 3),) * 3 + ((1, 2, 2),) * 4 + ((1, 2, 4),) * 2 + ((1, 4, 4),) * 2 + ((2, 2, 2),) * 2 + ((3, 2, 2),) * 3
target = (5, 5, 5)
assert sum(math.prod(i) for i in blocks) == math.prod(target)
matrix = []
table = []
for block_idx, block_size in enumerate(blocks):
    for p in set(itertools.permutations(sorted(block_size))):
        for x0 in range(target[0]):
            for y0 in range(target[1]):
                for z0 in range(target[2]):
                    if not (x0 + p[0] <= target[0] and y0 + p[1] <= target[1] and z0 + p[2] <= target[2]):
                        continue
                    table.append(((x0, x0 + p[0]), (y0, y0 + p[1]), (z0, z0 + p[2])))
                    matrix.append([len(matrix), []])
                    # block should be used
                    matrix[-1][-1].append(block_idx + 1)
                    # space should be occupied
                    for x in range(x0, x0 + p[0]):
                        for y in range(y0, y0 + p[1]):
                            for z in range(z0, z0 + p[2]):
                                offset = x * target[1] * target[2] + y * target[2] + z
                                matrix[-1][-1].append(len(blocks) + offset + 1)
                    # parity trick
                    if math.prod(p) == 3:
                        tmp = []
                        for x in range(x0, x0 + p[0]):
                            for y in range(y0, y0 + p[1]):
                                for z in range(z0, z0 + p[2]):
                                    tmp.append(x)
                                    tmp.append(y + target[0])
                                    tmp.append(z + target[0] + target[1])
                        tmp = list(set(tmp))
                        assert len(tmp) == 5
                        for offset in tmp:
                            matrix[-1][-1].append(len(blocks) + math.prod(target) + offset + 1)

DLXM = DLXMatrix(matrix)
flag1 = False
flag2 = False
flag3 = False
for C in DLXM:
    arrange = [[[table[C[i]][j][k] if k <= 1 else -1 for k in range(3)] for j in range(len(blocks[0]))] for i in range(len(blocks))]
    arrange = list(sorted(arrange))
    score = len(set((x, y, z) for i in range(len(blocks)) for x, y, z in itertools.product(*arrange[i])))
    flag = ''
    if 136 < score < 157 and not flag1:
        flag1 = True
        flag = 'flag1'
    if score <= 136 and not flag2:
        flag2 = True
        flag = 'flag2'
    if score >= 157 and not flag3:
        flag3 = True
        flag = 'flag3'
    if flag:
        print(flag, ''.join([str(arrange[i][j][k]) for i in range(len(blocks)) for j in range(len(blocks[0])) for k in range(2)]))
        if flag1 and flag2 and flag3:
            break
```

运行示例：

```
$ time python3 dlx.py 
flag1 010103010235012435021303023503024535121434130445150104231504254545350445351202351324352502353524
flag3 010103011504020135021545121434130201130212132502150423154524240235252435254545350302353502450235
flag2 010103011504020135021545121434130102130223131202132403154504230435254545350203350235352403352435

real    2m29.550s
user    2m29.542s
sys     0m0.004s
```

直接使用 Z3 Theorem Prover 求解也是可以的。需要灵活地将得分约束（`len(set(xxx))>=xxx`）和积木放置方式约束（`tuple(sorted(xxx))=...`）这样的 Python 运算转化为精简的逻辑表达式形式，求解运行时间会和逻辑表达式的写法有关系。得到 flag2 和 flag3 一般需要比较长的运行时间，有时候把 `score>=xxx` 写成 `score==xxx` 会更容易得到结果。

```python
import itertools
from z3 import *

bound = 5
constraints = ((1, 1, 3), (1, 2, 2), (1, 2, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3))
count = [3, 4, 2, 2, 2, 3]
num_constraints = sum(count)
num_dims = len(constraints[0])
arrange = [[[Int('x_{}_{}_{}'.format(k, j, i)) for i in range(3)] for j in range(num_dims)] for k in range(num_constraints)]
solver = Solver()

# Stage 0 constraints
for i in range(num_constraints):
    for j in range(num_dims):
        for k in range(3):
            if k == 2:
                solver.add(arrange[i][j][k] == -1)
            else:
                solver.add(0 <= arrange[i][j][k])
                solver.add(arrange[i][j][k] <= bound)

# Stage 1 constraints are skipped

# Stage 2 constraints
for i in range(num_constraints):
    for j in range(num_constraints):
        if i == j:
            continue
        solver.add(Or(*[(Or(arrange[i][k][1] <= arrange[j][k][0], arrange[j][k][1] <= arrange[i][k][0])) for k in range(num_dims)]))

# Stage 3 constraints
for t in range(len(constraints)):
    solver.add(Sum([If(Or(*[And(*[arrange[i][j][1] - arrange[i][j][0] == perm[j] for j in range(num_dims)]) for perm in set(itertools.permutations(constraints[t]))]), 1, 0) for i in range(num_constraints)]) == count[t])

# Score constraint
score = Sum([If(Or(*[And(x0 == x1, y0 == y1, z0 == z1) for i in range(num_constraints) for x1, y1, z1 in itertools.product(*arrange[i])]), 1, 0) for x0, y0, z0 in itertools.product(*([list(range(-1, bound + 1))] * 3))])
solver.add(score >= 157)  # modify this constraint

print('solving')
if solver.check() == z3.sat:
    ans = solver.model()
    for i in range(num_constraints):
        for j in range(num_dims):
            for k in range(3):
                arrange[i][j][k] = ans[arrange[i][j][k]].as_long()
    arrange.sort()
    print(''.join([str(arrange[i][j][k]) for i in range(num_constraints) for j in range(num_dims) for k in range(2)]))
else:
    print('no solution')
```

运行示例：

```
$ time python3 z3.py
solving
013502020224020302022524030145041545123502230404244504341434350135350203352401352413451535454503

real    33m14.577s
user    33m12.361s
sys     0m2.144s
```