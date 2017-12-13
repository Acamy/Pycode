import re
#1. 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
match = re.search(r'[1-9]\d{5}','430074 BIT 100081 430074')
if match:
    print("search:" + match.group(0))

#2. 从一个字符串的开始位置起匹配正则表达式，返回match对象
match = re.match(r'[1-9]\d{5}','430074 BIT 100081')
if match:
    print("match:" + match.group(0))

#3. 搜索字符串，以列表类型返回全部能匹配的子串
list= re.findall(r'[1-9]\d{5}','430074 BIT 100081')
print("findall:" + str(list))

#4. 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
list= re.split(r'[1-9]\d{5}','TSU 430074 BIT 100081END 430008 kk',maxsplit=2)
print("split:" + str(list))

#5. 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
for m in re.finditer(r'[1-9]\d{5}','430074 BIT 100081'):
    if m:
        print("finditer:" + m.group(0))

#6. 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
str = re.sub(r'[1-9]\d{5}','INSTEADED','430074 BIT 100081')
print("sub:" + str)