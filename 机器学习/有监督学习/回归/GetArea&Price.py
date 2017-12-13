import requests
from bs4 import BeautifulSoup
import bs4
import os

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getAreaPrice(url,path):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        ul = soup.find_all('ul', class_="sellListContent")[0]
        with open(path,"a") as f:
            for li in ul.children:
                try:
                  if isinstance(li, bs4.element.Tag):
                    area = li('div', class_="houseInfo")[0].text.split('|')[2][:-3]
                    price = li('div', class_="unitPrice")[0].string[2:-4]
                    f.write(str(float(area)).strip() + "," + str(int(price)) + "\n")
                except:
                  continue
    except:
        pass

if __name__ == '__main__':
    list = []
    path = "prices.txt"
    if os.path.exists(path):
        os.remove(path)
    pageNum = 97
    for i in range(pageNum):
        url = "https://wh.lianjia.com/ershoufang/pg" + str(i)
        print("\r房价数据正在下载,当前进度: {:.2f}%".format((i +1) * 100 / pageNum), end="")
        getAreaPrice(url,path)