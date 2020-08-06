import os
filename = "example.xml"
if filename not in os.listdir():
    from urllib.request import urlretrieve
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    urlretrieve(url, filename)

import xmltodict
with open(filename) as fd:
    doc = dict(xmltodict.parse(fd.read()))
    locations = doc['cwbopendata']['dataset']['locations']['location']
    for location in locations:
        locationName = location['locationName']
        geocode = location['geocode']
        lat = location['lat']
        lon = location['lon']
        print(f'{locationName}{geocode}\tlat:{lat}\tlon:{lon}')