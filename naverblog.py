
#naverblog->mongo
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db=client.saka
import os
import sys
import urllib.request
import json
#f=open('_todel3.txt','a')
client_id = "vsrM591ulJUhsKcxxv3y"
client_secret = "cJYnlSX77K"
encText = urllib.parse.quote("¿À»çÄ«")
display = '100'
start='1'
sort='sim'
_maxIter=1000
_iter=1
while _iter<_maxIter:
    url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText
    url+="&display="+display+'&start='+start+'&sort='+sort
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    _iter+=1
    start=str(_iter)
    if(rescode==200):
        response_body = response.read()
        jd = json.loads(response_body.decode('utf-8'))
        db.saka.insert_one(jd)
        print(len(response_body.decode('utf-8')))
    else:
        print("Error Code:" + rescode)

#mongo->txt
import pymongo
import codecs
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db=client.saka
empCol = db.saka.find()
f=codecs.open('p1.txt','w', 'utf-8')
for emp in empCol:
    for i in range(1,100):
        f.write(emp['items'][i]['description'])
f.close()

