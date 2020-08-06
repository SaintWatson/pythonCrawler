import os
filename = "example.xml"
if filename not in os.listdir():
    from urllib.request import urlretrieve
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    urlretrieve(url, filename)

import xml.etree.ElementTree as ET
tree = ET.parse(filename)
locations = tree.getroot()[8].getchildren()[1].getchildren() #用樹狀的結構一層層移動到指定層

for location in locations:
    locationAttr = location.getchildren()
    L = []
    for attr in locationAttr:
        data = (attr.tag+attr.text).replace("{urn:cwb:gov:tw:cwbcommon:0.1}","")
        L.append(data)
    print(L)
  