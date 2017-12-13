import requests
url = "http://www.ip138.com/ips138.asp?ip="
r = requests.get(url + "113.57.228.242")
r.encoding = r.apparent_encoding
print(r.text[-2000:])