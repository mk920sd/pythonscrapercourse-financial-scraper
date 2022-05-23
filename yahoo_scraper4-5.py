from webbrowser import get
import requests
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
dt = soup.find('time').get('datatime')
# print(dt)
rows = soup.find_all('div', {'class':'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})
result = []
for row in rows:
    company = row.find('div', {'class': 'Lh(20px) Fw(600) Fz(16px) Ell'}).getText()
    price = row.find('div', {'class': 'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'}).getText()
    status_element = row.find_all('div', {'class', 'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0]
    status_class = status_element.find('span').get('class')
    status = ''
    if 'C($c-trend-down)' in status_class:
        ico = '▼'
        status = ico + status_element.getText()
    elif 'C($c-trend-up)' in status_class:
        ico = '▲'
        status = ico + status_element.getText()
    else:
        ico = '■'
        status = ico + status_element.getText()
    
    percenttage_element = row.find_all('div', {'class', 'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1]
    percenttage = ico + percenttage_element.getText()

    result.append([dt, company, price, status, percenttage])
print(result)


# 漲：Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-up)
# 跌：Fw(600) Jc(fe) D(f) Ai(c) C($c-trend-down)
# 平：Fw(600) Jc(fe) D(f) Ai(c)