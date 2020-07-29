import requests
schoolName =  input('school:')
url = 'https://www.dcard.tw/_api/forums/' + schoolName + '/posts'
r = requests.get(url)
response = r.text

import json
data = json.loads(response)
male = 0
female = 0
for d in data:
    gender = d['gender']
    if gender == 'F':
        female += 1
    else:
        male += 1
print(data[0]['school'])
print(f'male:{male}  female:{female}')
