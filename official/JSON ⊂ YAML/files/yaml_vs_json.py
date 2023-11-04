# pip install PyYAML==6.0.1 ruamel.yaml==0.17.40 ruamel.yaml.clib==0.2.8
import json
import yaml
import ruamel.yaml

s = input('Input your JSON: ')

# 作为 JSON 读取
as_json = json.loads(s)
print('As JSON:', repr(as_json))

# 作为 YAML 1.1 读取，如果和作为 JSON 读取的结果不同，即可获得 flag1
as_yaml_1_1 = yaml.safe_load(s)
print('As YAML 1.1:', repr(as_yaml_1_1))

if as_json != as_yaml_1_1:
    print('Flag1:', open('flag1').read())
else:
    print('No flag1')

# 作为 YAML 1.2 读取，如果出现异常，即可获得 flag2
try:
    ruamel.yaml.safe_load(s)
except Exception:
    print('Flag2:', open('flag2').read())
else:
    print('No flag2')
