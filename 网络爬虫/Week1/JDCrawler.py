import requests
r = requests.get("https://item.jd.com/1593516.html")
print(r.headers)
print(r.text[:2000])