from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import datetime


url = "https://ssxd.mediav.com/s?type=2&r=20&mv_ref=blog%2Ecsdn%2Enet&enup=CAABq9RzQAgAAkBz1KsA&mvid=NDQwMTc1MDgzMjY1NDE0MDcwODAwMTg&bid=12883ea6069cac53&price=AAAAAFt1SJgAAAAAAAl5WGZw/HkrKfSDVzMTKg==&finfo=DAABCAABAAABaAgAAgAAAI4EAAM/V85LMuPfjgAIAAIAAAADCgADVRjEqoGgKr8IAAQAAAD4BgAGLbcIAAgANu6ACgAJAAAAAAACEBQGAAoAAAA&ugi=FcTgigEVyNtrTBUCFeIDFegDFQAAFY+f76gDJcgBAA&uai=FZb2lQIlAhUEFrDy65jV5N2YqgEV8ggl/Nakrw8UAhUAFRoA&ubi=FZTKRRXy/KMCFeSr8hUVrKDIVRUEFRwWxt666BYWsPKAgN+q4piqATQCFqjAECUGFc/mj+UOFb4FFQA2puXG8pWepbo9AA&clickid=0&cpx=__OFFSET_X__&cpy=__OFFSET_Y__&cs=__EVENT_TIME_START__&ce=__EVENT_TIME_END__&csign=ae758a17b72085a1&url=http%3A%2F%2F1%2Ebqfbg%2Etop"

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
num = 1;


while num < 100000:
    html = requests.get(url, headers=header)
    num = num+1
    print(num)
    time.sleep(0.1)


