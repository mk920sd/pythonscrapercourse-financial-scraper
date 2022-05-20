import requests
import json

url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220519&selectType=30&_=1653011779435'
res = requests.get(url)
print(res.json()['data'])