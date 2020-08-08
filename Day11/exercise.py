import myRandomGenerator as RLG
import sys
def init():
    try:
        data_scale = int(sys.argv[1])
    except:
        data_scale = 1000
    RLG.make_data(data_scale)

init()
import re
rule1 = '[A-Z]{3}-\d{3}\n'
rule2 = '[A-Z]{2}-\d{4}\n'
pattern1 = re.compile(rule1)
pattern2 = re.compile(rule2)


with open('license_data.txt', 'r') as f:
    LL = f.readlines()
    AC1 = list()
    AC2 = list()
    for string in LL:
        if re.match(rule1, string):
            AC1.append(string)
        elif re.match(rule2, string):
            AC2.append(string)

    for i, bike in enumerate(AC1):
        print(f'[bike] #{i+1}: {bike}', end='')
    for i, car in enumerate(AC2):
        print(f'[car] #{i+1}: {car}', end='')             
    print(f'Totally {len(AC1)} bikes, {len(AC2)} cars.')
