import random_license_generater as RLG
import sys
def init():
    try:
        data_scale = int(sys.argv[1])
    except:
        data_scale = 1000
        print('no arg')
    RLG.make_data(data_scale)

init()
import re
regex_1 = '[A-Z]{3}-[0-9]{3}\n'
pattern = re.compile(regex_1)

with open('license_data.txt', 'r') as f:
    LL = f.readlines()
    for string in LL:
        if re.match(pattern, string):
            print(string[:-1])
            
