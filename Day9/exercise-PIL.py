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

from PIL import Image
import os
def download_file(url, index):
    dir_name = 'tos_images'
    if dir_name not in os.listdir():
        os.mkdir(dir_name)    

    res = requests.get(url, stream=True)
    image = Image.open(res.raw)    
    extension = '.' + image.format.lower()
    localname = f'[PIL]{str(index)}{extension}'
    image.save(dir_name + '/' + localname)
    return localname

index = 1
for image_url in download_list:
    filename = download_file(image_url, index)
    index += 1
    print('Successful download: ' + filename)
print('Download Complete')