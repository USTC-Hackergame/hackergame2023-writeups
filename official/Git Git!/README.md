# Git? Git!

题解作者：[PRO-2684](https://github.com/PRO-2684)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：general

- 题目分值：150

> 图片使用 AI 技术生成，与真实人物无关。

![](files/copy.jpg)

「幸亏我发现了……」马老师长吁了一口气。

「马老师，发生甚么事了？」马老师的一位英国研究生问。

「刚刚一不小心，把 flag 提交到本地仓库里了。」马老师回答，「还好我发现了，撤销了这次提交，不然就惨了……」

「这样啊，那太好了。」研究生说。

马老师没想到的是，这位年轻人不讲武德，偷偷把他的本地仓库拷贝到了自己的电脑上，然后带出了实验室，想要一探究竟……

**[打开/下载题目](files/ML-Course-Notes.zip)**

## 题解

下载并解压附件，然后进入 `ML-Course-Notes` 目录。根据题目描述，首先使用 `git reflog` 查看完整的操作历史：

```bash
ubuntu@some-linux:/home/ubuntu/ML-Course-Notes$ git reflog
ea49f0c (HEAD -> main) HEAD@{0}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD~
505e1a3 HEAD@{2}: commit: Trim trailing spaces
15fd0a1 (origin/main, origin/HEAD) HEAD@{3}: clone: from https://github.com/dair-ai/ML-Course-Notes.git
```

可以看到，`clone` 后最近的一次提交 hash 是 `505e1a3`，猜测这就是马老师~~故意~~不小心提交 flag 的 commit。使用 `git reset` 回退到这次提交：

```bash
ubuntu@some-linux:/home/ubuntu/ML-Course-Notes$ git reset --hard 505e1a3
HEAD is now at 505e1a3 Trim trailing spaces
```

查看 `README.md` 文件，发现 flag：

```bash
ubuntu@some-linux:/home/ubuntu/ML-Course-Notes$ cat .\README.md
...
  <!-- flag{TheRe5_@lwAy5_a_R3GreT_pi1l_1n_G1t} -->
...
```
