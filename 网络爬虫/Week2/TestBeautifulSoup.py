from bs4 import BeautifulSoup
import requests

url = "http://www.baidu.com"
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
#print(soup.prettify())
print(soup.title)
print(soup.a.parent.parent.attrs['class'])