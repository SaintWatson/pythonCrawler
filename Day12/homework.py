import requests
ettoday_url = 'https://www.ettoday.net/news/news-list.htm'
response = requests.get(ettoday_url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
h3_tags = soup.find_all('h3')

index = 0
for tag in h3_tags:
    a_tag = tag.findChildren('a') # the title is in the <a> tag under the <h3> tag
    if len(a_tag) != 0:
        print(f'#{str(index)}: {a_tag[0].text}')
        index += 1