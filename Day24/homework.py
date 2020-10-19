from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from sys import stdout
options = Options()
options.headless = True
# options.add_argument('--start-maximized')
url ='https://www.104.com.tw/cust/list/index/?page=1&order=4&mode=s&jobsource=checkc&area=6001001000&indcat=1001000000'

def handler(company):
    title = company.findChild('h1').findChild('a').text

    location = company.find_all('p')[0].find('span').text

    info = company.find_all('p')[1].text.replace('"', '').replace('\n','')
    capital = info.split('，')[0].replace('資本額：', '').replace('萬元','0000').replace('暫不提供', '0')
    if capital[-1:] == '億':
        capital = capital.replace('億','00000000')
    else:
        capital = capital.replace('億','')

    staff = info.split('，')[1].replace('員工人數：', '').replace('人','').replace('暫不提供', '0')

    needs = '0'
    other = company.find('div', class_='jobs')
    if not other is None:
        other = other.text.replace('"', '').replace('\n','')
        if other != '':
            needs = other.replace('工作機會 (', '').replace(')', '')
    return [title, location, capital, staff, needs]

browser = Chrome('../tools/chromedriver.exe', options=options)
browser.get(url)
company_list = [['公司名稱','地區','資本額','公司人數','招募人數']]
time_s = datetime.now()
index = 0
while True:
    sleep(2)
    index += 1

    soup = BeautifulSoup(browser.page_source, features='lxml')
    total = int(soup.find('div', class_='page-total').text[1:-1].strip())
    
    string = f'\rLoading:[{"#" * (index//(total//100 + 1))}{" " * ((total-index)//(total//100 + 1))}]'
    stdout.write(string)
    stdout.flush()

    companies = soup.find_all('div',class_='info')
    for company in companies:
        company_list.append(handler(company))
        
    while True:
        try:
            btn = browser.find_element_by_partial_link_text('下一頁')
            btn.click()
            break
        except:
           sleep(1)   

    if index == total:
        browser.quit()
        break
time_f = datetime.now()
print(f'\nThe soup is done! (cost {(time_f-time_s).seconds} seconds.)')

import csv
with open('company_list.csv','w', encoding='big5', errors='ignore') as f:
    writer = csv.writer(f)
    writer.writerows(company_list)
    print('The result is done!')