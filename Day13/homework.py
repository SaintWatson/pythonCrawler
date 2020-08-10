import requests
url = 'https://www.ptt.cc/bbs/NBA/index.html'
response = requests.get(url).text
print('Receive the response...')

from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
authors = soup.find_all('div', class_='author')
titles = soup.find_all('div', class_='title')
dates = soup.find_all('div', class_='date')
print('Grasp the target infomation...')

articles = len(authors)
article_list = [['作者','標題','日期']]   
for i in range(articles):
    author = authors[i].text.replace('\n','')
    title = titles[i].text.replace('\n','')
    date = dates[i].text.replace('\n','')
    article_list.append([date, author, title])

import time
curTime = time.ctime().split()
now = f'{curTime[1]}.{curTime[2]} {curTime[3]}'.replace(':','_')

import os
dirname = 'result'
filename = now + '.csv'
if dirname not in os.listdir():
    os.mkdir(dirname)
print('Create the table...')

import csv
fullname = dirname + '/' + filename
with open(fullname, 'w', encoding='Big5') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(article_list)
print(f'Done!!! \nThe file {filename} has saved in the directory {dirname}.')