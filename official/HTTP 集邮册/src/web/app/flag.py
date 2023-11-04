import hashlib

sha256 = lambda x: hashlib.sha256(x.encode()).hexdigest()

def flag1(token: str) -> str:
    return f"5 种状态码：flag{{stacking_up_http_status_codes_is_fun_{sha256('200404etc' + token)[:10]}}}"

def flag2(token: str) -> str:
    return f"没有状态……哈？：flag{{{['d1d you hear the HTTP packet from 1991?', 'great backward compatibility of nginx, R1ght?', 'congratu1ations you discovered someth1ng before http1.0'][int(sha256('http0.9surprise'+token), 16) % 3]}}}"

def flag3(token: str) -> str:
    return f"12 种状态码：flag{{I think that when many such status codes are accumulated {sha256('mygotomorihttp' + token)[:10]} it becomes a lifetime}}"
