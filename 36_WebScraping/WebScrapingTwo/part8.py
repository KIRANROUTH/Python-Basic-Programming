from bs4 import BeautifulSoup
import requests
import itertools
import csv

csv_file=open("csv_scrape.csv",'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Date','Open','High','Low','Close','Adj_Close','Volume'])

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

Date=[]
Open=[]
High=[]
Low=[]
Close=[]
Adj_Close=[]
Volume=[]
cycle=itertools.cycle([1,2,3,4,5,6])

for article in soup.find_all("td",class_="Py(10px) Ta(start) Pend(10px)"):
	Date.append(str(article.span.text))

for val in soup.find_all("td",class_="Py(10px) Pstart(10px)"):
	cycle_count=next(cycle)
	if cycle_count==1:
		Open.append(str(val.span.text))
	if cycle_count==2:
		High.append(str(val.span.text))
	if cycle_count==3:
		Low.append(str(val.span.text))
	if cycle_count==4:
		Close.append(str(val.span.text))
	if cycle_count==5:
		Adj_Close.append(str(val.span.text))
	if cycle_count==6:
		Volume.append(str(val.span.text))

print(Date)
print()
print(Open)
print()
print(High)
print()
print(Low)
print()
print(Close)
print()
print(Adj_Close)
print()
print(Volume)

for date,Open,high,low,close,adj,vol in zip(Date,Open,High,Low,Close,Adj_Close,Volume):
	csv_writer.writerow([date,Open,high,low,close,adj,vol])

csv_file.close()
