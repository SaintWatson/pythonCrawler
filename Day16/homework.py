import requests
from bs4 import BeautifulSoup
url='https://zh.wikipedia.org/zh-tw/%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91'
response = requests.get(url).text
soup = BeautifulSoup(response, features='html.parser')
paragraphs = soup.find_all('p')[3:78]

checklist = []
href = []
for paragraph in paragraphs:
    tags = paragraph.find_all('a')
    for tag in tags:
        title = tag.text
        url = tag.get('href')
        if '[' not in title and url not in checklist:
            checklist.append(url)
            href.append([title, url])
href.sort()
href.insert(0,['標題', '網址'])


import csv
with open('links.csv', encoding='Big5', mode='w', errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(href)