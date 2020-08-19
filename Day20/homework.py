url = 'https://www.dcard.tw/service/api/v2/forums?nsfw=true'
csvName = 'data.csv'

import requests
import json
response = requests.get(url).text
forums = json.loads(response)
infos = [['名稱','縮寫','訂閱數','創立日期','本月文章數']]
for forum in forums:
    name = forum['name']
    alias = forum['alias']
    subscriptionCount = forum['subscriptionCount']
    createdAt = forum['createdAt'][:10]
    postCount = forum['postCount']['last30Days']
    forum_info = [name, alias, subscriptionCount, createdAt, postCount]
    infos.append(forum_info)

import csv
with open(csvName, mode='w', encoding='Big5', errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(infos)