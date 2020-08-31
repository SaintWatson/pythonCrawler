from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from datetime import datetime

url = 'https://hahow.in/courses?page='
time1 = datetime.now()

options = Options()
options.headless = True

table = [] 
for i in range(1,23):
    try:
        browser = webdriver.Chrome('../tools/chromedriver.exe', options=options)
        browser.get(url + str(i))
        time.sleep(1)
        soup = BeautifulSoup(browser.page_source, features='html.parser')
        browser.close()
        tags = soup.find_all('h4')
        for tag in tags:
            temp = [tag.text]
            table.append(temp)
    except:
        browser.close()
browser.quit()

import csv
with open('list.csv','w', encoding='big5', errors='ignore') as file:
    writer = csv.writer(file)
    writer.writerows(table)
    