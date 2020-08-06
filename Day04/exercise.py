import requests
r = requests.get("https://github.com/timeline.json")
response = r.text
print(response)
