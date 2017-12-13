import requests

r = requests.get("http://www.baidu.com")

r.encoding = 'utf-8'

print(r.status_code)

print(type(r))

print(r.headers)

print(r.text)