import requests
from bs4 import BeautifulSoup

# class NovelList:
home_page = 'http://www.360doc.com/content/18/0314/11/79186_736878186.shtml'
#设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}

#获得小说首页，查询排名小说的href
def getNovelList(url):
    html = requests.get(url, headers = header)
    soup = BeautifulSoup(html.text, 'html.parser')
    tag = soup.select("div[class=hotbox] ul li a")
    hotNovelList = []
    for a in tag:
        hotNovelList.append(a["href"])
        # print(a)
    print(hotNovelList)
    return hotNovelList

def downloadNovel(hotNovelList, FilePath):
    for href in hotNovelList:
        pass

getNovelList(test_url)

#
# #根据图片src 执行下载
# def everpage(imgSrc):
#     html = getHtml(imgSrc)
#     nowtime = datetime.datetime.now().microsecond
#     f = open("D:/xkl/个人/"+str(nowtime)+'.jpg', 'wb')
#     f.write(html.content)
#     f.flush()
#     f.close()
