import requests
aim = 'https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html'
over18 = {'over18' : '1'}
response = requests.get(aim, cookies = over18).text
print('Receive the response...')


from bs4 import BeautifulSoup
soup = BeautifulSoup(response, features='html.parser')
image_tags = soup.find_all('a')
download_list = []
for href in image_tags:
    url = href.get('href')
    if 'https://imgur.com/' in url:
        download_list.append(url)
print('Deal with the download list...')


import os
from PIL import Image
if 'yui' not in os.listdir():
    os.mkdir('yui')
    
index = 1 
for url in download_list:
    # we don't know the actual format of these images, .gif is just a temp extension
    raw_image = requests.get(url+'.gif', stream=True).raw
    image = Image.open(raw_image)
    extension = '.' + image.format.lower()
    localname = 'yui-' + str(index) + extension
    image.save('./yui/' + localname)
    print(f'Successfully download {localname}')
    index += 1
print('All downloadings are finished')