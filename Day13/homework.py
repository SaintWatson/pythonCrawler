import requests
url = 'https://www.ptt.cc/bbs/PC_Shopping/index.html'
response = requests.get(url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
authors = soup.find_all('div', class_='author')
titles = soup.find_all('div', class_='title')
dates = soup.find_all('div', class_='date')

articles = len(authors)
article_list = [['作者','標題','日期']]    
for i in range(articles):
    author = authors[i].text.replace('\n','')
    title = titles[i].text.replace('\n','')
    date = dates[i].text.replace('\n','')
    article_list.append([date, author, title])

import csv
filename = 'ptt.csv'
with open(filename, 'w', encoding='Big5') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(article_list)