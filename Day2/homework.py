from  urllib.request import urlretrieve
import os, csv
L = os.listdir()
inName = 'infile.csv'
outName = 'outfile.csv'
if inName not in L:
    res = "https://data.taipei/api/getDatasetInfo/downloadResource?id=b1398491-07fe-40da-bb5a-ae73f4e45984&rid=7bcd8da2-06a8-4f22-8ff0-324a1369c106"
    urlretrieve(res, inName)
    infile = open(inName, mode='r', encoding='Big5')
    outfile = open(outName, mode='w', encoding='utf-8')
    content = infile.read()
    outfile.write(content)
    infile.close()
    outfile.close()
with open(outName,newline='',encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile)
    for line in lines:
        print(line)