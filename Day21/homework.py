# Step.1 open the browser
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://www.ettoday.net/news/news-list.html'
browser = webdriver.Chrome(executable_path='../tools/chromedriver.exe')
browser.get(url)

# Step.2 Set a timer to roll the page
import time
N = 20
js_scroll = 'window.scrollTo(0,10000);'
for i in range(N):
    time.sleep(1)
    browser.execute_script(js_scroll)

# Step.3 Get the full source
html_source = browser.page_source 
browser.quit()
soup = BeautifulSoup(html_source, features='html.parser')

# Step.4 Get the data
for d in soup.find(class_="part_list_2").find_all('h3'):
    print(d.find(class_="date").text, d.find_all('a')[-1].text)

