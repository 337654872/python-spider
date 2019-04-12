from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import datetime

# chrome浏览器，用于全页面爬取
class ChromeOptions():

    def __init__(self, chromePath, driverPath):
        chrome_options = Options()
        # 无头模式
        chrome_options.add_argument("--headless")
        print('开启无头模式。。。，关闭无头，请输出参数')
        # 谷歌文档说加上这个避免bug
        chrome_options.add_argument("--disable-gpu")
        # 禁用图片
        chrome_options.add_argument("blink-settings=imagesEnabled=false")
        print('禁用图片')
        # 定义chrome的安装目录，加入文件目录，避免默认路径没有导致报错
        chrome_options.binary_location = chromePath
        # driver 目录
        chrome_driver_binary = driverPath
        # 启动浏览器
        self.__browser = webdriver.Chrome(chrome_driver_binary, chrome_options=chrome_options)

    def getHtml(self, url):
        self.browser.get(url)

    def getBrowser(self):
        return self.__browser

class a(object):
    pass