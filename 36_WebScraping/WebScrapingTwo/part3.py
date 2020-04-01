from bs4 import BeautifulSoup
import requests

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

#line 85
#<tr class="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)" data-reactid="49">
article=soup.find("tr",class_="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)")

data_column_one=article.span.text
print(data_column_one)
#output
#Jul 19, 2019