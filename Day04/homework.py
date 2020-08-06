import json, requests
getURL = "http://httpbin.org/get"
postURL = "http://httpbin.org/post"
getResponse = requests.get(getURL)
postResponse = requests.post(postURL)
print('=================This is the response of get=====================')
print(getResponse.text)
print('=================This is the response of post====================')
print(postResponse.text)