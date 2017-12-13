import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockInfo(url, fpath):
    html = getHTMLText(url)
    try:
        infoDict = {}
        soup = BeautifulSoup(html, 'html.parser')
        stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

        name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
        infoDict.update({'股票名称': name.text.split()[0]})

        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')
        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val

        with open(fpath, 'a', encoding='utf-8') as f:
            f.write(str(infoDict) + '\n')
    except:
        traceback.print_exc()


def main():
    stock_info_url = 'https://gupiao.baidu.com/stock/sz300205.html'
    output_file = 'D:/BaiduStockInfo.txt'
    slist = []
    getStockInfo(stock_info_url, output_file)
    print("success")


main()