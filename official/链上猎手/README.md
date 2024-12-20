# 链上猎手

题解作者：[zzh1996](https://github.com/zzh1996)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](../../credits.pdf)。

## 题目描述

- 题目分类：general

- 题目分值：The Maximal Extractable Value（200）+ The Dark Forest（250）+ Death's End（250）

你最近研究了一下如何在区块链上开发一个 MEV Bot，而小 Z 跟你说：「区块链就像是一个黑暗森林，到处都是带枪的猎人。」

### The Maximal Extractable Value

「我新写的 MEV Bot，是不是很安全？」

### The Dark Forest

「Gas fee 好贵！听别人说节约 gas 的一个好方法就是把能在链下检查的逻辑都从智能合约挪到链下去检查。」

### Death's End

「每次更新代码都重新部署智能合约也太贵了，我这次一定要写一个通用的 MEV Bot 合约！」

---

注：题目环境未启用 EVM 的 Shanghai 升级，不支持 `PUSH0` 指令，与 Solidity 0.8.20 及以上版本的默认编译选项不兼容，请注意选择正确的 EVM 版本。

**[下载题目源代码](files/链上猎手.zip)**

你可以通过 `nc 202.38.93.111 10222` 来连接，或者点击下面的「打开/下载题目」按钮通过网页终端与远程交互。

> 如果你不知道 `nc` 是什么，或者在使用上面的命令时遇到了困难，可以参考我们编写的 [萌新入门手册：如何使用 nc/ncat？](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/)

## 题解

**警告：本题解仅作为技术研究，所有内容均不构成投资建议。在与任何公开区块链进行交互时，请遵守您所在地的相关法律法规**

本题考察了 MEV Bot（区块链上的套利机器人）所用智能合约的安全性问题。

以下介绍一些基本概念，如果已经了解可以直接跳过：

- 区块链（Blockchain）：一种去中心化的账本，将交易分块打包，用密码学方法保证账本的历史不可篡改。
- 智能合约（Smart Contract）：区块链上面的一类特殊账户，这类账户的行为由预先设定好的程序来控制，可以在用户触发时执行有条件的、复杂的交易（例如：如果 A 的余额大于 5 个代币，则给 B 转账 3 个代币，并且修改变量 x 的值为 1）。智能合约的执行不由特定的人控制（除非在代码里写明）。智能合约可以跟普通用户一样与其他智能合约进行交互，智能合约也可以创建新的智能合约。
- 以太坊（Ethereum）：第一个较好支持智能合约的公共区块链，是当今区块链生态中最重要的区块链之一。智能合约底层运行的是 EVM 指令集，智能合约通常用 Solidity 语言编写。以太坊区块链的原生代币是 ETH，可以用来支付交易的手续费。
- Gas：用来测量 EVM 指令执行过程中消耗的计算资源，例如说一次加法会消耗 3 个 gas，一次乘法会消耗 5 个 gas，创建一个新的智能合约要消耗至少几万个 gas。以太坊的手续费是按照每 gas 来收取的。
- ERC-20：一种在以太坊区块链上创建新代币（Token）的规范，定义了查询余额、转账等接口。如果一个智能合约符合这种规范，那么这个智能合约就可以作为一个 ERC-20 代币来使用。以太坊上常见的 ERC-20 代币包括 USDT 等。
- WETH（Wrapped ETH）：由于以太坊的原生代币 ETH 并非由智能合约实现，不满足 ERC-20 标准，不方便与其他 ERC-20 代币一样使用，所以可以通过把 ETH 包装起来的方法实现一种与 ETH 等价的 ERC-20 代币，这个新代币就是 Wrapped ETH。
- DeFi（Decentralized Finance，去中心化金融）：在区块链上通过智能合约的形式来实现很多传统金融业务，例如不同代币间的兑换、抵押借贷、衍生品交易等。如今已经形成了一个庞大且复杂的生态。用户在交易时只需要信任智能合约的源代码，而无需信任任何中心化机构。
- DEX（Decentralized Exchange，去中心化交易所）：在区块链上提供代币之间兑换功能的智能合约。以太坊上知名的 DEX 有 Uniswap、Curve 等。
- Uniswap：一个知名的去中心化交易所，实现了一个所谓“自动做市商”的机制：一些用户可以把自己的代币存入 Uniswap 的智能合约中，用来给其他用户兑换，可以赚取手续费（通常称作提供流动性）；而另一些用户可以通过 Uniswap 的智能合约来随时兑换代币，需要付一些手续费。Uniswap V2 的兑换计算很简单，在不考虑手续费的情况下，就是保持智能合约中两种代币余额的乘积不变，即 $x\cdot y=k$。Uniswap V2 的智能合约包含一个唯一的 factory 合约，然后任何用户都可以通过它创建出来任意两种代币之间的兑换合约（即交易对，pair）。
- Flashloan：由于区块链上的交易是有原子性的，所以可以实现一种有趣的机制：在一个交易执行的过程中，你可以跟某个智能合约借来一笔巨款，并且随意使用，然后你需要在当前交易结束之前归还这笔借款。如果没有归还，那么智能合约会让整个交易回滚，所以这种借款可以随意进行而无需信任，但仅限单笔交易内部可用。为了让交易结束前智能合约可以检查你是否还了钱，通常来说 Flashloan 的流程都是：你调用某个智能合约要求借钱，智能合约借你钱后回调（callback）到你自己的智能合约里面，你做完想做的事情之后返回，就会回到提供 Flashloan 服务的智能合约中，此时它可以检查你是否已经还钱。
- 套利：如果区块链上的两个去中心化交易所之间同种代币的价格不同，那么可以通过低买高卖的方式来赚取差价。例如你用 100 块钱在 A 市场购买 100 个苹果，然后在 B 市场把 100 个苹果卖成 110 块钱，这样你就净赚了 10 块钱。在区块链上，进行这样的套利操作可以在一个交易内进行，所以具有原子性（不用担心买了 100 个苹果之后 B 市场的价格下跌导致亏钱）。链上的套利操作通常会使用 Flashloan 来提供初始资金，而 Uniswap 本身支持所谓的“Flash Swap”，即你想把 A 换成 B 的时候，可以先把你要的 B 直接拿走，之后把 A 还上就行。随手可以找到一个以太坊区块链上的套利交易：[套利交易例子](https://cn.etherscan.com/tx/0x765392d2a7ef3b1e90de93d1955bbc0aa9d3e9d9a4dbb25102962a41e83d0dec)，注意看 Transaction Action 右边的两个 Swap 操作。
- MEV（Maximal Extractable Value 或 Miner Extractable Value）：指任何在链上可以“凭空”赚的钱，例如去中心化交易所之间的套利、借贷的清算等等。
- MEV Bot：自动化在区块链上通过 MEV 赚钱的程序，通常分为链上智能合约和链下程序两部分。链下程序会计算赚钱的机会，然后发送交易调用链上的智能合约来执行相应操作。区块链上通常有很多 MEV 相关的交易，也有很多地址被一些区块链查看器网站标为 [MEV Bot](https://cn.etherscan.com/accounts/label/mev-bot)，它们的智能合约通常是不开源的，并且每天发送大量的交易。

本题的程序先是启动了以太坊区块链节点软件 Geth，运行了一条私有区块链，然后在这条链上部署了两份 Uniswap V2 的 factory 智能合约（源代码与 Uniswap [官方 GitHub 仓库](https://github.com/Uniswap/v2-core)完全一样，未经修改），然后创建了 WETH 和“Token”两个 ERC-20 代币，并且在两份 Uniswap 中分别创建了 WETH-Token 代币的交易对（pair），然后在这两个交易对中添加了不同的流动性，其中一个是 1:1，另一个是 1:2，导致两边的价格不同，从而产生了套利机会。

然后，题目程序部署了一个 MEV Bot 套利程序所使用的智能合约，这个智能合约的功能就是帮助套利程序原子性地执行两个交易所间的套利操作。然后，题目启动了 MEV Bot 的主程序 `bot.py`，并让它在后台一直运行。这个主程序的功能是，对于每一个新的区块，都获取这两个 Uniswap 的所有交易对，然后筛选出来两边都有的交易对，并且按照 WETH -> X -> WETH 的路径来模拟计算套利交易的过程，找到赚的 WETH 最多的输入数额，并且发送真正的套利交易。

启动这个 Bot 后，题目给了 3 种交互方式：

1. 获取一些免费的 ETH
2. 发送一个 raw transaction（已经签名的交易）
3. 获取 flag，条件是 MEV Bot 的智能合约 WETH 余额为 0。

按理来说，MEV Bot 的智能合约有一些初始的 WETH，并且套利的时候只会赚钱而不会亏钱，余额不可能减少。如果 MEV Bot 的智能合约里面的余额减少（排除提现的情况），意味着它有安全漏洞，里面的钱可以被偷走。

### The Maximal Extractable Value

「我新写的 MEV Bot，是不是很安全？」

这一小问的智能合约有 3 个入口函数，其中 `arbitrage` 和 `withdraw` 都验证了交易的 sender 地址，所以我们无法调用。剩下的 `uniswapV2Call` 是给 Uniswap V2 的 pair 合约来作为 callback 调用的，但是它怎么确保调用者是真的 Uniswap V2 pair 呢？可以看到检查条件为：

```solidity
require(IUniswapV2Pair(msg.sender).factory() == FACTORY1 || IUniswapV2Pair(msg.sender).factory() == FACTORY2);
require(sender == address(this));
```

就是说只要调用者“声称”自己的 factory 是 Uniswap 的 factory 即可，`sender` 参数也只是一个普通的函数参数而已，调用者都可以控制。这样我们就可以写出来一个假的合约来骗过这个检查，然后通过指定参数把所有 WETH 转走即可。后面有一个 `pair1.swap` 的函数调用，我们只要让 `pair1` 是我们写的合约，并且啥都不做就行了。

解题代码见 [exp1.py](exp1.py) 和 [hack1.sol](hack1.sol)。

### The Dark Forest

「Gas fee 好贵！听别人说节约 gas 的一个好方法就是把能在链下检查的逻辑都从智能合约挪到链下去检查。」

与第一问对比一下，我们可以发现，`uniswapV2Call` 的检查方式变成了 `require(tx.origin == owner)`，也就是要求整个交易的发起者是 MEV Bot 的控制者地址，那我们就无法直接去调用这个函数了。但是，我们可以构造恶意的 Token，并且创建交易对、添加流动性来创造套利机会，吸引这个 Bot 上钩来主动发交易。这个 Bot 主动发的交易执行过程中，当然 `tx.origin` 就是 Bot 的控制者地址了。

这题的套利交易发出前，Python 代码会使用智能合约的 `simulate` 函数来提前模拟执行一下，只有执行成功的情况下才会发送真正的交易。而成功的条件就是 Bot 合约的 WETH 余额不会减少，那我们还怎么偷走这些 WETH？答案就是让模拟执行的时候余额不减少，但是真正执行的时候余额减少。所以我们应该想办法找到模拟执行和真正执行的时候的细微差异，并且用这种差异来决定是否偷走 WETH 余额。

实际上，本题故意设置得比较简单。本题的模拟执行底层是使用 `eth_call` 接口进行的，区块高度（block number）就是最新的区块（latest）。而交易真正执行的时候，区块高度是下一个区块。所以使用 block number 就可以判断当前是在模拟执行还是真正执行。本题的环境非常确定，所以区块高度也是每次都不会变的，比较容易写出来。

解题代码见 [exp2.py](exp2.py) 和 [hack2.sol](hack2.sol)。

如果你好奇解题脚本里面的常数是怎么算出来的，那当然就是先写成 1，然后看看最后 MEV Bot 合约里面剩下多少 WETH，再修改成对应的数值，就可以掏空到 0 了。

除了区块高度之外，其实两个不同的函数消耗的 gas 也可能有一些细微区别，我们还可以用区块的哈希、时间戳等等很多信息来区分。实在不行，你甚至可以创建足够多的交易对，让 MEV Bot 的 Python 代码执行缓慢，然后在模拟和真正上链之间插入自己的交易的方式来创造区别。

在真正的 MEV 场景中，套利者通常不会用 `eth_call` 接口来模拟执行交易，而是使用 MEV-Geth 的 `eth_callBundle` 接口或者自己编写的接口来实现模拟执行。即使是这样，仍然不能保证链下模拟的结果和链上执行会完全相同，因为很多因素是无法预测的，你的交易前面也可能被插入其他交易。

### Death's End

「每次更新代码都重新部署智能合约也太贵了，我这次一定要写一个通用的 MEV Bot 合约！」

与上一小问对比，智能合约的 `arbitrage` 函数会确保 WETH 余额不减少，而 `uniswapV2Call` 函数要求交易的发起者是 Bot 的控制者地址。根据 Python 代码，这个地址会发出的交易只有 `arbitrage` 函数，那岂不是无解？

这一小问还有一个修改，就是 `uniswapV2Call` 写成了一个非常通用的形式，可以调用任何智能合约的任何函数。此时我们想偷走 WETH，还不希望 WETH 余额减少，就有了一种迂回的办法：先在 `uniswapV2Call` 里面调用 WETH 的 `approve` 函数把代币授权给我们自己控制的地址，这样套利交易执行过程中 WETH 余额不会减少。但是等套利交易结束后，我们就可以用自己的地址发出交易，来把它授权的代币通过 WETH 的 `transferFrom` 转移出来。

解题代码见 [exp3.py](exp3.py) 和 [hack3.sol](hack3.sol)。

### 结语

[区块链就是一个黑暗森林](https://www.paradigm.xyz/2020/08/ethereum-is-a-dark-forest)。如果你经常看一些 MEV Searcher（套利者）聚集的社交平台，比如 Flashbots 的 Discord，你会发现经常有人 MEV Bot 的智能合约被黑。对于题目这种原子性的套利操作，其实还好，因为收益总是可以及时取出来。但是对于一些做三明治或者 DEX-CEX 套利的人来说，智能合约里面通常需要放很多的资金，被黑就会损失惨重。但是区块链上只有知名的项目被黑时，才会有相关的新闻报道，MEV Bot 被黑这种事情通常吸引不到任何人的关注（何况这种智能合约都是不开源的）。我之前研究过一些 MEV Bot 智能合约被黑的例子，很多都是由于 callback 函数没写好导致的，并且本地的模拟执行结果告诉你余额不减少也不一定有用。

这道题可以让大家亲身体会一下 MEV Bot 是如何运作的，但是题目的代码还远远不够在真正的区块链上运行（连手续费都没算呢，而且性能很差）。即使你真的跑起来，对于这种 Uniswap V2 的套利，大家也都已经把手续费卷到了收益的 99.9% 以上。通常来说对于这种赚钱的东西，有一定经验的玩家是不愿意分享相关技术的，学术圈的相关研究也和真正的 MEV 生态脱钩比较严重。希望这道题给大家带来了一些不一样的视角，有问题也欢迎通过各种渠道与我交流。
