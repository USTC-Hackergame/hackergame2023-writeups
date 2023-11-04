# HTTP 集邮册

题解作者：[taoky](https://github.com/taoky)

出题人、验题人、文案设计等：见 [Hackergame 2023 幕后工作人员](https://hack.lug.ustc.edu.cn/credits/)。

## 题目描述

- 题目分类：web

- 题目分值：5 种状态码（150）+ 没有状态……哈？（150）+ 12 种状态码（200）

> 「HTTP 请求一瞬间就得到了响应，但是，HTTP 响应的 status line、header 和 body 都是确实存在的。如果将一个一个 HTTP 状态码收集起来，也许就能变成……变成……变成……」
>
> 「flag？」
>
> 「就能变成 flag！」

---

本题中，你可以向一个 nginx 服务器（对应的容器为**默认配置下的 `nginx:1.25.2-bookworm`**）发送 HTTP 请求。你需要获取到不同的 HTTP 响应状态码以获取 flag，其中：

- 获取第一个 flag 需要收集 5 种状态码；
- 获取第二个 flag 需要让 nginx 返回首行无状态码的响应（不计入收集的状态码中）；
- 获取第三个 flag 需要收集 12 种状态码。

关于无状态码的判断逻辑如下：

```python
crlf = buf.find(b"\r\n")
if buf.strip() != b"":
    try:
        if crlf == -1:
            raise ValueError("No CRLF found")
        status_line = buf[:crlf]
        http_version, status_code, reason_phrase = status_line.split(b" ", 2)
        status_code = int(status_code)
    except ValueError:
        buf += "（无状态码）".encode()
        status_code = None
```

## 题解

@zzh1996 的 idea，还是我负责实现。

本题给了一个 Web 界面，用户可以用这个界面构造请求并向另一个 nginx 容器发送。赛时提供了无状态码的判断和用户输入的解析代码，但是完整的 web 代码没有开源。

因为没有全部包着 `try...except`，并且总的上传大小也有限制，所以这个 web 界面本身可能能触发 500 等错误，但是不算收集到的 HTTP 请求，因为 web 界面本身就负责收集工作，它没法收集自己导致的 HTTP code。

关于收集的状态码，可以去 [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100) 逛一圈，MDN 对每个状态码的解释是很详细的。首先列出 5 个最容易拿到的状态码：

- 200 OK. 点击就送，代表请求成功。
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n\r\n
    ```
- 404 Not Found. 修改路径到一个不存在的文件即可。
    ```
    GET /x HTTP/1.1\r\n
    Host: example.com\r\n\r\n
    ```
- 400 Bad Request. 构造不符合格式的 HTTP 请求即可。
    ```
    GET / aHTTP/1.1\r\n
    Host: example.com\r\n\r\n
    ```
- 505 HTTP Version Not Supported. 修改 HTTP 版本号到一个离谱的值即可。
    ```
    GET / HTTP/11\r\n
    Host: example.com\r\n\r\n
    ```
- 405 Method Not Allowed. 修改请求方法到 `POST` 等即可。
    ```
    POST / HTTP/1.1\r\n
    Host: example.com\r\n\r\n
    ```

接下来是可能需要看文档的部分：

- 100 Continue. 代表服务器希望客户端继续请求或者忽略。需要客户端发送 `Expect: 100-continue`。
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    Expect: 100-continue\r\n\r\n
    ```
- 206 Partial Content. 一个 HTTP 请求可以只请求部分内容，服务器也会返回部分内容。
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    Range: bytes=1-2\r\n\r\n
    ```
- 416 Range Not Satisfiable. 上面的 `Range` 是一个合法的范围，那么不合法的范围呢？就是 416。
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    Range: bytes=114514-1919810\r\n\r\n
    ```
- 304 Not Modified. 代表文件在指定条件下没有修改过，这里用 `If-Modified-Since`：
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    If-Modified-Since: Tue, 15 Aug 2023 17:03:04 GMT\r\n\r\n
    ```
- 412 Precondition Failed. 这个 payload 使用了 ETag + If-Match，ETag 和对应的 web 资源对应，用来区分对应资源不同的版本。客户端可以利用这个信息来节省带宽。这里 [`If-Match`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match) 则在尝试匹配这个 ETag，如果不匹配，那就返回 412。
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    If-Match: "bfc13a64729c4290ef5b2c2730249c88ca92d82d"\r\n\r\n
    ```
- 413 Content Too Large. 不需要真正输入很大的 payload，把 `Content-length` 弄得很大就行：
    ```
    GET / HTTP/1.1\r\n
    Host: example.com\r\n
    Content-length: 1145141919810\r\n\r\n
    ```
- 414 URI Too Long. 大概需要很长的 URI 路径（但是又不能太长，否则 web 界面本体不会允许这样的响应）。内容详见 [414.txt](./414.txt)。

以上就已经集满了 12 个。在验题时还有一个 HTTP code 漏了：

- 501 Not Implemented. 代表服务器不支持此功能。Nginx 源代码中默认配置下唯一可能触发的地方是 <https://github.com/nginx/nginx/blob/a13ed7f5ed5bebdc0b9217ffafb75ab69f835a84/src/http/ngx_http_request.c#L2008>:

    ```c
    } else {
        ngx_log_error(NGX_LOG_INFO, r->connection->log, 0,
                        "client sent unknown \"Transfer-Encoding\": \"%V\"",
                        &r->headers_in.transfer_encoding->value);
        ngx_http_finalize_request(r, NGX_HTTP_NOT_IMPLEMENTED);
        return NGX_ERROR;
    }
    ```

    `else` 上面只允许 `chunked`，所以可以：

    ```
    GET / HTTP/1.1\r\n
    Transfer-Encoding: gzip\r\n
    Host: example.com\r\n\r\n
    ```

    `gzip` 换成除了 `chunked` 以外的任意字符串都行。

最后一个问题：没有状态码是怎么回事？这道题可能可以手工 fuzz 出来，payload 类似于这样：

```
GET /\r\n
```

这里实际发送的是 HTTP/0.9 请求，它只支持 `GET`，然后后面直接接 URL，没有别的。然后响应就直接响应文件内容，也没有状态码之类的东西。
当时做原型的时候，看到这个其实还是挺惊讶的，没想到 nginx 还保留着和 HTTP/0.9 客户端的兼容性。

## 其他

截至比赛中途，状态码收集的统计如下：

```
    156             HTTP/1.1 501 Not Implemented
    563             HTTP/1.1 412 Precondition Failed
    595             HTTP/1.1 304 Not Modified
    616             HTTP/1.1 416 Requested Range Not Satisfiable
    642             HTTP/1.1 414 Request-URI Too Large
    823             HTTP/1.1 413 Request Entity Too Large
   1110             HTTP/1.1 206 Partial Content
   1346             HTTP/1.1 100 Continue
   3081             HTTP/1.1 505 HTTP Version Not Supported
  36830             HTTP/1.1 405 Not Allowed
 156961             HTTP/1.1 400 Bad Request
 272886             HTTP/1.1 200 OK
 628252             HTTP/1.1 404 Not Found
```

另外这道题也玩了 mygo 梗，包括文案 `<hr>` 之前的 quote（其实好像还不止 mygo 的梗），和第二小题的名字（rikki: 哈？）。
