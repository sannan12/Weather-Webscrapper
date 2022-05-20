import bs4
import requests
from bs4 import BeutifulSoap

def parcePrice():
    r =requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soap=bs4.BeutifulSoap(r.txt,"XML")
    price=soap.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

while True:
    print('the current price::'+str(parsePrice()))