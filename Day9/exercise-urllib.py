from urllib.request import urlretrieve
import requests
url = 'https://www.ptt.cc/bbs/ToS/M.1596592091.A.510.html'
response = requests.get(url).text
print('Receive the response...')


from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
image_tags = soup.find_all('a')
download_list = []
for image in image_tags:
    href = image.get('href')
    if 'i.imgur' in href:
        download_list.append(href)
print('Get the target urls...')


import os
dir_name = 'tos_images'
if dir_name not in os.listdir():
    os.mkdir(dir_name)
index = 1
for image_url in download_list:
    filename = '[urllib]' + str(index) + image_url[-4:]
    urlretrieve(image_url, './'+dir_name+'/' + filename)
    index += 1
    print('Successful download: ' + filename)
print('Download Complete')