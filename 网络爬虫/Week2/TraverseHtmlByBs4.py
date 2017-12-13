import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

print(soup.head)

print(soup.head.contents)

print(soup.body.contents)

print(len(soup.body.contents))

for child in soup.body.children:
    print(child)