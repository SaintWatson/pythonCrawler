from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
with open('keyword.txt', 'r', encoding='big5') as f:
    keywords = f.readlines()

options = Options()
# options.headless = True
options.add_argument('--start-maximized')
url = 'https://www.google.com.tw/maps/dir///@25.0123641,121.5491398,15.96z'
browser = Chrome('../tools/chromedriver.exe', options=options)
browser.get(url)
sleep(1)
boxes = browser.find_elements_by_class_name('searchbox ')
print(len(boxes))
with open('distance.txt', 'w', encoding='utf8') as f:
    for keyword in keywords:
        for box in boxes:
            box.send_key('666')
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        sleep(1)

browser.quit()