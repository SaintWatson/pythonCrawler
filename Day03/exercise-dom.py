import os
filename = "example.xml"
if filename not in os.listdir():
    from urllib.request import urlretrieve
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    urlretrieve(url, filename)

import xml.dom.minidom as minidom
doc = minidom.parse(filename).documentElement
locationList = doc.getElementsByTagName("location")
for location in locationList:
    locationName = location.getElementsByTagName("locationName")[0].firstChild.data
    geocode = location.getElementsByTagName("geocode")[0].firstChild.data
    lat = location.getElementsByTagName("lat")[0].firstChild.data
    lon = location.getElementsByTagName("lon")[0].firstChild.data
    print(f'{geocode}{locationName}\tlon:{lon}\tlat:{lat}')