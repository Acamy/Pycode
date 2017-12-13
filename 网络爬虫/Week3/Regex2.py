import re

#python 默认是贪婪匹配
match = re.search(r'PY.*N','PYANBNCNDN')
if match:
    print(match.group(0))

#加?最小匹配
match = re.search(r'PY.*?N','PYANBNCNDN')
if match:
    print(match.group(0))