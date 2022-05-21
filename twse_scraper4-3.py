import requests
import json

url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220520&selectType=25&_=1653121065994'
res = requests.get(url)
print(res.json()['data'])