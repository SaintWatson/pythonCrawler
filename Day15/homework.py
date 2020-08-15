import requests
from bs4 import BeautifulSoup
url = 'https://rate.bot.com.tw/xrt/quote/2020-07/USD'
response = requests.get(url).text
soup = BeautifulSoup(response, features='html.parser')
tr_tags = soup.find_all('tbody')[0].find_all('tr')

all_days = [['時間','本行買入','本行賣出','即期買入','即期賣出']]
for tag in tr_tags:
    data = tag.text
    info = data.split('\n')[1:-1]
    info.pop(1)
    all_days.insert(1,info)

import csv
filename = 'rate.csv'
with open(filename, encoding='Big5', mode='w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_days)
