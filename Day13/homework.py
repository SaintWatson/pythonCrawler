import requests
url = 'https://www.ptt.cc/bbs/PC_Shopping/index.html'
response = requests.get(url).text

import re
regex = '/bbs/PC_Shopping/M\.\d{10}.A.\w{3}\.html'
rule = re.compile(regex)
def is_article(url):
    if url is None:
        return False
    if rule.match(url):
        return True
    else:
        return False

from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
authors = soup.find_all('div', class_='author')
titles = soup.find_all('div', class_='title')
dates = soup.find_all('div', class_='date')

articles = len(authors)    
for i in range(articles):
    author = authors[i].text
    title = titles[i].text
    date = dates[i].text
    print(f'{title[:-1]}---{date}: {author}')