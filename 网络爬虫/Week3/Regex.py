import re

#函数式用法：一次性操作
match = re.search(r'[1‐9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

#面向对象用法：编译后的多次操作
pat = re.compile(r'[1‐9]\d{5}')
match = pat.search('BIT 100081')
if match:
    print(match.group(0))

match = pat.search('100082 BIT 100081')
if match:
    print(match.group(0))