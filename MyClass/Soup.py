import requests
from bs4 import BeautifulSoup

class Soup(object):

    def __init__(self, url, header):
        self.__url = url
        self.__header = header

    def print(self):
        print('%s: %s' %(self.url, self.header))

    def getUrl(self):
        return self.__url

    def getHeader(self):
        return self.__header

    def setUrl(self, url):
        self.__url = url

    def setHeader(self, header):
        self.__header = header

    def getSoup(self):
        html = requests.get(self.getUrl(), headers = self.getHeader())
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup

    def findElementsByRegx(self, regx, soup):
        tag = soup.select(regx)
        return tag
