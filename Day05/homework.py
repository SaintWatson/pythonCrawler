titleLength = 15
def formatize(word,length):
    if '\n' in word:
        word = word.replace('\n','')
    if len(word) > length:
        word = word[:length]
    return word
def processData(data, printing):
    bigDict = dict()
    totalLike = 0
    totalComment = 0
    for d in data:
        title = d['title']
        time = d['createdAt']
        comment = d['commentCount']
        like = d['likeCount']
        title = formatize(title,titleLength)
        totalLike += like
        totalComment += comment
        if printing:
            print(f'{time}\t{comment}\t{like}\t{title}')
        newDict = dict()
        newDict.setdefault('title',title)
        newDict.setdefault('time', time)
        newDict.setdefault('comment', comment)
        newDict.setdefault('like',like)
        bigDict.setdefault(d['id'],newDict)
    bigDict.setdefault('totalLike',totalLike)
    bigDict.setdefault('totalComment',totalComment)
    return bigDict
    
        
import requests, json
apiPop = 'https://www.dcard.tw/_api/forums/pet/posts?popular=true'
apiNpop = 'https://www.dcard.tw/_api/forums/pet/posts?popular=false'
hotResponse = requests.get(apiPop).text
nohotResponse = requests.get(apiNpop).text
hotdata = json.loads(hotResponse)
nohotdata = json.loads(nohotResponse)
hotDATA = processData(hotdata,printing=False)
nohotDATA = processData(nohotdata,printing=False)
hotLike = hotDATA['totalLike'] // 30
nohotLike = nohotDATA['totalLike'] // 30
hotComment = hotDATA['totalComment'] // 30
nohotComment = nohotDATA['totalComment'] // 30
print(f'  熱門--- 平均喜歡:{hotLike}\t平均留言:{hotComment}')
print(f'非熱門--- 平均喜歡:{nohotLike}\t平均留言:{nohotComment}')
