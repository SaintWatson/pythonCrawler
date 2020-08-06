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
def download_file(url, index, my_chunk_size):
    dir_name = 'tos_images'
    if dir_name not in os.listdir():
        os.mkdir(dir_name)
    extension = url[-4:]
    localname = f'[requests]{str(index)}{extension}'

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f'./{dir_name}/{localname}', 'wb') as f:
            for chunk in r.iter_content(chunk_size = my_chunk_size):
                if chunk:
                    f.write(chunk)
    return localname


index = 1
for image_url in download_list:
    filename = download_file(image_url, index, 256)
    index += 1
    print('Successful download: ' + filename)
print('Download Complete')