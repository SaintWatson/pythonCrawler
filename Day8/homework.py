import requests
url = 'https://www.zhihu.com/explore'
myheader = {'user-agent':'watson/0.0.1'}
response = requests.get(url, headers=myheader).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag.text)