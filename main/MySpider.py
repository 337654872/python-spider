from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import datetime

urlhead = "http://www.xxx.com"
test_url="http://www.xxx.com/xiaoshuo/index.html"
home_page = 'http://www.xxx.com/xiaoshuo/index.html'
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

def download(text,filepath):
    f = open(filepath,'wb')
    f.write(text.encode())
    f.flush()
    f.close()



chrome_options = Options()
# 无头模式
chrome_options.add_argument("--headless")
# 谷歌文档说加上这个避免bug
chrome_options.add_argument("--disable-gpu")
# 禁用图片
chrome_options.add_argument("blink-settings=imagesEnabled=false")
# 定义chrome的安装目录，加入文件目录，避免默认路径没有导致报错
chrome_options.binary_location = "C:\\Users\\yanfa\\AppData\\Local\Google\\Chrome\\Application\\chrome.exe"
# driver 目录
chrome_driver_binary = "D:\ProgramData\Anaconda3\Scripts\chromedriver.exe"
# 启动浏览器
browser = webdriver.Chrome(chrome_driver_binary,chrome_options=chrome_options)
noves = getNovelList(test_url)
try:
    for href in noves:
        noveurl = urlhead+href
        print(noveurl)
        browser.get(noveurl)
        inputs = browser.find_element_by_class_name("artbody")
        nowtime = datetime.datetime.now().microsecond
        filepath = "G:/xklPersonal/个人文件/novel/novel"+str(nowtime)+".txt"
        print(inputs.text)
        download(inputs.text,filepath)
        time.sleep(1)
finally:
    browser.close()
