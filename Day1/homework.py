# [1]根據需求引入正確的 Library
from urllib.request import urlretrieve
import os

# [2]下載檔案到 Data 資料夾，存成檔名 test.txt
try:
    os.makedirs( './Data', exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/test.txt")
except:
    print('error！')

# [3]檢查 Data 資料夾是否有 test.txt 檔名之檔案
files = os.listdir("./Data")
if 'test.txt' in files :
    print('[O] 檢查 Data 資料夾是否有 test.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 test.txt 檔名之檔案')

# [4]將「Hello World」字串覆寫到 test.txt 檔案
with open('./Data/test.txt','r') as fh:
    lines = fh.readlines()
    for line in lines:
        print(line)