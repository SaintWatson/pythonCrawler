import requests
target = 'https://www.dcard.tw/f'
html_doc = requests.get(target).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, features="html.parser")
a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag.get('href'))
