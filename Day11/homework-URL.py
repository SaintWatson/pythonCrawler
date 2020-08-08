import requests
aim = 'https://movies.yahoo.com.tw/movietime_result.html/id=9467'
response = requests.get(aim).text

import re
regex = 'href=\"https://.*\.html.*\"'
pattern = re.compile(regex)
hrefs = pattern.finditer(response)
for href in hrefs:
    url = href.group(0).split('"')
    print(url[1])