## JSON ⊂ YAML?

###  JSON ⊄ YAML 1.1

利用的浮点数解析的差异：

```
>>> json.loads('1e13')
10000000000000.0
>>> yaml.safe_load('1e13')
'1e13'
>>> json.loads('Infinity')
inf
>>> yaml.safe_load('Infinity')
'Infinity'
```

### JSON ⊄ YAML 1.2

发现 JSON 和 YAML 库对重复的 key 处理方式不一样：

```
>>> json.loads('{"b": 1, "b": 2}')
{'b': 2}
>>> ruamel.yaml.safe_load('{"b": 1, "b": 2}')
Traceback (most recent call last):
......
found duplicate key "b" with value "2" (original value: "1")
......
```

其实 YAML 1.2 说了新版本的一个目标是“making YAML a strict superset of JSON.”

可 JSON 没有禁止 duplicated keys，标准的用词是“[should be unique](https://stackoverflow.com/questions/21832701/does-json-syntax-allow-duplicate-keys-in-an-object)”。感觉这个例子只是 YAML 懒得兼容一个 JSON 中允许但没有实际意义的行为。