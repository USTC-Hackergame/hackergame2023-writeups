## 13. 惜字如金 2.0

### 尝试与解决

> 关键词：推理

首先先简单恢复一下程序，

```python
#!/usr/bin/python3

# The size of the file may reduce after XZRJification

def check_equals(left, right):
    # check whether left == right or not
    if left != right: exit(1)

def get_code_dict():
    # prepare the code dict
    code_dict = []
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
    code_dict += ['ct{l-findiehaai{oveatas']
    code_dict += ['ty9kxborszstguyd?!blm-p']
    check_equals(set(len(s) for s in code_dict), {24})
    return ''.join(code_dict)

def decrypt_data(input_codes):
    # retrieve the decrypted data
    code_dict = get_code_dict()
    output_chars = [code_dict[c] for c in input_codes]
    return ''.join(output_chars)

if __name__ == '__main__':
    # check some obvious things
    check_equals('create', 'cre' + 'at')
    check_equals('referrer', 'refer' + 'rer')
    # check the flag
    flag = decrypt_data([53, 41, 85, 109, 75, 1, 33, 48, 77, 90,
                         17, 118, 36, 25, 13, 89, 90, 3, 63, 25,
                         31, 77, 27, 60, 3, 118, 24, 62, 54, 61,
                         25, 63, 77, 36, 5, 32, 60, 67, 113, 28])
    check_equals(flag.index('flag{'), 0)
    check_equals(flag.index('}'), len(flag) - 1)
    # print the flag
    print(flag)
```

这题的核心是还原 `code_dict` 部分，每一行都是 23 个字符，少了个字符。

```python
def get_code_dict():
    # prepare the code dict
    code_dict = []
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
    code_dict += ['ct{l-findiehaai{oveatas']
    code_dict += ['ty9kxborszstguyd?!blm-p']
    check_equals(set(len(s) for s in code_dict), {24})
    return ''.join(code_dict)
```

如果不对 `code_dict` 做更改，flag 的前五个字符 `flag{` 和最后一个字符 `}` 会在这些地方：

```python
    code_dict += ['nymeh1niwemflcir}echaet']
    code_dict += ['a3g7}kidgojernoetlsup?h']
                 #     }            l
    code_dict += ['ulw!f5soadrhwnrsnstnoeq']
                 #      f
    code_dict += ['ct{l-findiehaai{oveatas']
                 #    {         a
    code_dict += ['ty9kxborszstguyd?!blm-p']
                 #              g
```

因此一种可能的还原是（插入的字符用 `#` 标示）：

```python
    code_dict += ['nymeh1niwemflcir}echaet#']
                 #                        #
    code_dict += ['a3g7}kidgojernoetl#sup?h']
                 #     }            l#
    code_dict += ['ulw!#f5soadrhwnrsnstnoeq']
                 #     #f
    code_dict += ['ct#{l-findiehaai{oveatas']
                 #   #{         a
    code_dict += ['ty9kxborszst#guyd?!blm-p']
                 #             #g
```

运行即可得到一个看起来很正常的 flag：

```plain
flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}
```

这个问号让人非常不自信，但是既然已经有一个 flag 了，为何不交呢？

### Flag

```plain
flag{you-ve-r3cover3d-7he-an5w3r-r1ght?}
```

You've recovered the answer right? Yes!
