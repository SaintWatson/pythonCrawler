#%%
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
from sys import stdout

# constant data
url = 'https://www.ettoday.net/news/focus/3C%E5%AE%B6%E9%9B%BB/'
option = Options()
option.headless = True
js_scroll = 'window.scrollTo(0,100000);'
scroll_times = 10
sleep_time = 1
#%%
# Step.1 Get the soup
time_s = datetime.now()
browser = Chrome('../tools/chromedriver.exe', options = option)
print('Open the webdriver...')
browser.get(url)
for i in range(scroll_times):
    string = '\rLoading the page: [' + '#' * i + ' ' * (scroll_times-i) +']'
    sleep(sleep_time)
    stdout.write(string)
    stdout.flush()
    browser.execute_script(js_scroll)
soup = BeautifulSoup(browser.page_source, features='lxml')
browser.quit()
time_f = datetime.now()
print(f'\nThe soup is done! (cost {(time_f-time_s).seconds} seconds.)')

#%%

# Step.2 Find the articles
news_list = [['日期', '標題', '網址']]
titles = soup.find_all('h3')
for title in titles:
    single_news = title.find('a', target="_blank")
    if single_news and 'htm' in single_news.get('href'):
        date = single_news.get('href').split('/')[2]
        date = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
        header = single_news.text
        URL = 'https://www.ettoday.net/' + single_news.get('href')
        news_list.append([date, header, URL])
print(f'All {len(news_list)-1} datas are ready!')
#%%
# Step.3 Output to a file
import csv
with open('news-list.csv', 'w', encoding='big5', errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(news_list)
    print('The file is done!')
