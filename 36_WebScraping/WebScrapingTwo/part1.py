from bs4 import BeautifulSoup
import requests

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

print(soup.prettify())