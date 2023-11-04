## 7. 组委会模拟器

### 尝试与解决

> 关键词：UserScript

这种手速游戏，最简单的处理方法就是浏览器脚本（UserScript）。具体细节不赘述。

```js
// ==UserScript==
// @name        HackerGame 2023 组委会模拟器
// @namespace   Violentmonkey Scripts
// @match       http://202.38.93.111:10021/*
// @grant       none
// @version     1.0
// @author      -
// @description 2023/10/28 13:37:36
// @require     https://cdn.jsdelivr.net/npm/jquery@3.6.4/dist/jquery.min.js
// ==/UserScript==

setInterval(() => {
  $('.fakeqq-message__bubble').each(function() {
    const text = $(this).text()
    if(/hack\[(.*?)\]/.test(text)) {
      $(this).click()
    }
  })
}, 50)
```

### Flag

```plain
flag{Web_pr0gra_mm1ng_907024aba2_15fun}
```

Web programming is fun!

### 其他做法

#### 自动化请求

通过自动化请求肯定也可以解决这个问题，但是相比于网页脚本，这实在过于麻烦了。
