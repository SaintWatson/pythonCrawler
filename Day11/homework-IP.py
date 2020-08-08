import requests
url = 'https://zh.wikipedia.org/wiki/IP%E5%9C%B0%E5%9D%80'
response = requests.get(url).text


import re
# IP address has four range: 0-99, 100-199, 200-249, 250-255
# '\d{1,2}$|1\d\d|2[0-4][0-9]|25[0-5]' means a 0-255 number and it has 4 with seperated by period.
byte = '(\d{1,2}|1\d\d|2[0-4][0-9]|25[0-5])'
regex = f'{byte}\.{byte}\.{byte}\.{byte}'
pattern = re.compile(regex)

ips = pattern.finditer(response)
n = 0
for ip in ips:
    print(ip.group(0))
    n += 1
print(f'Totally {n} ips.')