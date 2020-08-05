import requests
zhihuURL = 'https://www.zhihu.com/api/v4/questions/55493026/answers'
myheader = {'user-agent':'watson/0.0.2'} 
response = requests.get(zhihuURL, headers=myheader).text

import json
data = json.loads(response)['data']
for comment in data:
    print(comment['updated_time'])
