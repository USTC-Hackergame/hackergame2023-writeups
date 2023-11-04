## 14. 🪐 高频率星球

### 尝试与解决

> 关键词：文本处理、终端控制序列

首先下载 `asciinema_restore.rec`，用文本编辑器打开。很明显，这是一个文本文档。

```plain
{"version": 2, "width": 150, "height": 50, "timestamp": 1697951135, "env": {"SHELL": "/bin/zsh", "TERM": "xterm-256color"}}
[0.032562, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                                                                                                     \r \r"]
[0.033128, "o", "\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jstage % \u001b[K\u001b[?2004h"]
...
```

接下来我们安装 asciinema 来播放这一文件。这一次终端会话先执行了 `sha256sum flag.js`，这一命令的输出可以帮助选手检查自己还原出的 `flag.js` 是否与原文一致。接下来，执行了 `less flag.js`，这一命令的作用是在终端中分页浏览文件，但是文件滚动地非常快，很难看到具体内容。

不难发现文件是一页一页滚动的，通过“盯帧”来重构文件是可能的，但是文件非常长，手动操作肯定要花很长时间，且容易出错；自动化操作相当麻烦。不如来研究一下 `asciinema_restore.rec` 本身。反正这是个文本文件，处理起来肯定相当容易。

观察不难发现，每一行都是包含三个值的三元组。第一个显然是表示时间；第二个永远是 `"o"`，或许表示 `output`；第三个是一个字符串，表示具体内容。不妨尝试把每一行的内容都拼接起来，看看会得到什么。

```js
// === recover-record.js ===
const fs = require('fs')

const content = fs.readFileSync('./asciinema_restore.rec').toString()

const lines = content.split('\n')

let result = ''

for(const line of lines) {
  if(line[0] == '[') {
    const obj = JSON.parse(line)
    if(obj[1] != 'o') {
      throw new Error(`Unknown action ${obj[1]}, line ${line}`)
    }
    result += obj[2]
  }
}

console.log(result)
```

运行并将输出导出到 `dump.txt`。不难发现，`dump.txt` 中包含了几乎完整的 `flag.js` 内容，但是其中每隔一段都有一坨奇怪的字符。这一坨东西其实是终端控制序列，在终端中输出可以用来清空屏幕并打印下一页内容。

```plain
    "W7VdMvffFW",
    "k8kRwmoNWQC",
:[K
[K [KESCESC[K[[[K66[K~~
[K    "W58/WOqNW6i",
    "pSodCKdcGW",
    "W5W2W6frWQi",
```

确实可以写一个程序根据终端控制序列语法来移除它们，但是，不难注意到，`flag.js` 内容中的每一坨控制序列都是完全相同的，除了第一处。不妨把这一段相同的东西复制出来，存为 `strip.txt`，另外写一个程序将这些东西移除。

```js
// === strip.js ===
const fs = require('fs')

let dumpContent = fs.readFileSync('dump.txt').toString()
const stripContent = fs.readFileSync('strip.txt').toString()

while(true) {
  let next = dumpContent.replace(stripContent.trim(), '')
  if(next == dumpContent) {
    break
  }
  dumpContent = next
}

console.log(dumpContent)
```

运行并将输出导向到 `stripped.txt`，然后复制出 `flag.js` 内容并手动删去第一坨控制序列。

```plain
    "W5nepCkkaG",
    "CCoyWQFcPSoe",
[7mflag.js[27m[K
[K [KESCESC[K[[[K66[K~~
[K    "eqtdJYnV",
    "omk+y2JcSq",
    "v8o+ashcKG",
```

将结果另存为 `flag.js`，运行，即得到 flag。

### Flag

```plain
flag{y0u_cAn_ReSTorE_C0de_fr0m_asc11nema_3db2da1063300e5dabf826e40ffd016101458df23a371}
```
