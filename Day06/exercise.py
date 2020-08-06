import requests
zhihuURL = 'https://www.zhihu.com/api/v4/questions/55493026/answers'
myheader = {'user-agent':'watson/0.0.1'} # originally may be "python-requests/2.18.4"
response = requests.get(zhihuURL, headers=myheader).text

import json
data = json.loads(response)
for d in data['data']:
    print(d['author']['name'] + '---------------'  + d['author']['headline'])
