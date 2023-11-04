import socket

# 定义HTTP请求内容
http_request = "POST / HTTP/1.1\r\nHost: 192.168.23.1:18080\r\nContent-Length: 98\r\n\r\n2:MEUCIQC40y4XGGJHH303roxcGXaDxmkE4GJ2yKBAgnkWdSwY+gIgP45PlTy+3eAQsjd1iwdHxPBJwC7sjzwzs3K3ZJ3Z4OY="

# 分割HTTP请求为每3个字符的块
chunk_size = 3
chunks = [http_request[i:i + chunk_size] for i in range(0, len(http_request), chunk_size)]

# 建立TCP连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.connect(("202.38.93.111", 18080))
    s.connect(("192.168.23.1", 18081))

    # 逐个发送块
    for chunk in chunks:
        s.send(chunk.encode())

    # 接收响应
    response = b""
    while True:
        data = s.recv(999999)
        print(data)
        if not data:
            break
        response += data

    # print(response)
    # print(response.decode())
