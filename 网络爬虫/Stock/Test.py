
import requests
from bs4 import BeautifulSoup
import re
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockStartDate(stockCode):
    html = getHTMLText("http://quotes.money.163.com/f10/gszl_" + stockCode + ".html#01f01")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('table',class_="table_bg001 border_box limit_sale table_details")[1]
    cnt = 0;
    date = ""
    for tr in a.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            cnt = cnt + 1
            if(cnt ==2):
                date = tds[1].string.replace("-","")
                break;
    return date


#print(getStockStartDate("600016"))

import time
## dd/mm/yyyy格式
print (time.strftime("%Y%m%d"))
