import requests, sys, math, csv, time, os, pandas
from bs4 import BeautifulSoup

def page_Field():
    HomePage = 'https://movies.yahoo.com.tw/movie_intheaters.html'
    response = requests.get(HomePage).text
    soup = BeautifulSoup(response, features='html.parser')
    p_tags = soup.find_all('p')
    for tag in p_tags:
        if '目前顯示' in tag.text:
            try:
                return int(tag.text.split('，')[0][1:-1]), math.ceil(int(tag.text.split('，')[0][1:-1])/10)
            except:
                print('Failed')
                exit()
def progressing(cur, total, slow=False):
    if cur % 10 != 1 and slow:
        time.sleep(0.2)
    dots = 6
    figure = '.' * (cur%dots+1) + ' ' * (dots-cur%dots-1)
    sys.stdout.write(f'\rProcessing{figure} ({cur}/{total})')
    sys.stdout.flush()
def score2star(score):
    if score >= 85:
        return '★★★★★'
    elif score >= 75:
        return '★★★★☆'
    elif score >= 65:
        return '★★★☆☆'
    elif score >= 55:
        return '★★☆☆☆'
    elif score >= 45:
        return '★☆☆☆☆'
    else:
        return '☆☆☆☆☆'

movieN, pageN = page_Field()
print(f'There are {movieN} movies need to handle...')
finished = 0
slow = True

movie_list = [['中文名稱', '英文名稱', '期待度', '滿意度', '總分', '上映時間']]
for i in range(pageN):
    url = 'https://movies.yahoo.com.tw/movie_intheaters.html?page=' + str(i+1)
    soup = BeautifulSoup(requests.get(url).text, features='html.parser')
    tags = soup.find_all('div', class_='release_info_text')

    for tag in tags:
        names = tag.find_all(class_='gabtn')
        zh_name = names[0].text.strip('\t\n ')
        en_name = names[1].text.strip('\t\n ')

        leveltexts = tag.find_all(class_='leveltext')
        expectation = leveltexts[0].findChild().text
        satisfaction = leveltexts[1].findChild().get('data-num')

        score = (eval(satisfaction) * 20 + int(expectation[:-1])) // 2
        star = score2star(score)

        release_time = tag.findChild(class_='release_movie_time').text[-10:]

        movie_list.append([zh_name, en_name, expectation, satisfaction, star ,release_time])

        finished += 1
        progressing(finished, movieN, slow)

curTime = time.ctime().split()
now = f'{curTime[1]}.{curTime[2]}-{curTime[3]}'.replace(':','_')
filename = now + '.csv'
dirname = 'result'
if dirname not in os.listdir():
    os.mkdir(dirname)
with open(dirname + '/' + filename, mode='w', encoding='big5') as f:
    writer = csv.writer(f)
    writer.writerows(movie_list)
    print(f'\nThe file {filename} has been saved successfully!!')