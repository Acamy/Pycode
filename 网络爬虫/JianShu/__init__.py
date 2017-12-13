import requests
from bs4 import BeautifulSoup
import MySQLdb
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def crawlArticleByUrl(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find_all('div', class_="article")[0]
    title = article('h1', class_="title")[0].string
    print(title)
    content = str(article('div', class_="show-content")[0])[48:-7]
    return title,content

def writeIntoDB(title,content):
    DBKWARGS = {'db':'myblog','user':'root','passwd':'root',
            'host':'localhost','use_unicode':True,'charset':'utf8'}
    con = MySQLdb.connect(**DBKWARGS)
    cur = con.cursor()
    sql = "insert into article(article_title,article_content) values(%s,%s)"
    lis = (title,content)
    try:
        cur.execute(sql, lis)
    except Exception as e:
        print("Insert Error:", e)
        con.rollback()
    else:
        con.commit()
    cur.close()
    con.close()

def GetArticleList(userId):
    url = "http://www.jianshu.com/u/" + userId
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    num = int(soup.find_all('div', class_="meta-block")[2]('p')[0].string) #获取文章总数
    page = int(num / 9) + 1 #获取页数

    for i in range(page):
        newUrl = url + "?order_by=shared_at&page=" + str(page - i)
        newHtml = getHTMLText(newUrl)
        newSoup = BeautifulSoup(newHtml,"html.parser")
        ul = newSoup.find_all('ul', class_="note-list")[0]
        lis = []
        # 倒序输出
        for li in ul.children:
            if isinstance(li,bs4.element.Tag):
                lis.append(li)
        for li in lis[::-1]:
            articleUrl = "http://www.jianshu.com" + (li("a", class_="title")[0].attrs['href'])
            title, content = crawlArticleByUrl(articleUrl)
            writeIntoDB(title, content)

GetArticleList("9f29e0217f4d")
print("Finish!")