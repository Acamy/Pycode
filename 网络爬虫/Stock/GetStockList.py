import requests
import time
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


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append((re.findall(r"[s][hz]\d{6}", href)[0])[2:])
        except:
            continue

# http://quotes.money.163.com/service/chddata.html?code=0600016&start=20001219&end=20171207&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP
def getHistoryTradeInfo(stockCode):
    download_url = "http://quotes.money.163.com/service/chddata.html?code=0" + stockCode + "&start=" + getStockStartDate(stockCode) + "&end=" + time.strftime("%Y%m%d") + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    data = requests.get(download_url)
    f = open('histotry/' + stockCode + '.csv', 'wb')
    for chunk in data.iter_content(chunk_size=10000):
        if chunk:
            f.write(chunk)

def getStockStartDate(stockCode):
    html = getHTMLText("http://quotes.money.163.com/f10/gszl_" + stockCode + ".html#01f02")
    soup = BeautifulSoup(html, 'html.parser')
    try:
        a = soup.find_all('table', class_="table_bg001 border_box limit_sale table_details")[1]
    except:
        return time.strftime("%Y%m%d")
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


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    slist = []
    getStockList(slist, stock_list_url)
    count = 0
    for i in slist:
        if(i[0] == "6"):
            getHistoryTradeInfo(i)
        count = count + 1
        print("\r历史数据正在下载,当前进度: {:.2f}%".format(count * 100 / len(slist)), end="")
    print("Success!")

main()