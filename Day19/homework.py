url = 'https://hahow.in/courses'

# Part.1 static crawl
import requests
from bs4 import BeautifulSoup
response = requests.get(url).text
soup = BeautifulSoup(response, features='lxml')
with open('static.html', 'w') as fd:
    fd.write(str(soup.prettify()))
    print('static way only get partial response')

# Part.2 dynamic crawl
from selenium import webdriver
browser = webdriver.Chrome(executable_path='../tools/chromedriver.exe')
browser.get(url)
content = browser.page_source
browser.close() # only close the window, the driver is still work. 
browser.quit() # close all the windows and also the driver.
soup = BeautifulSoup(content, features='lxml')
with open('dynamic.html', 'w') as fd:
    fd.write(str(soup.prettify()))
    print('dynamic way get the full response')


