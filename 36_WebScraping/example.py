from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.guru99.com/excel-vs-csv.html").text
soup=BeautifulSoup(response,'lxml')

Heading=[]
for tableH in soup.find_all('strong'):
	for column in tableH.find_all("center"):
		Heading.append(column.text)

content=[]

for row in soup.find_all("tbody",valign="top"):
	excelval=row.text 
	content=excelval.split("    ")

import csv
'''
with open("difference.csv",'w') as wf:
	writer=csv.writer(wf)
	writer.writerow(Heading)'''

import itertools 

cycle=itertools.cycle([1,2])

excelcontent=[]
csvcontent=[]

for values in content:
	val=next(cycle)
	if val==1:
		excelcontent.append(str(values))

	if val==2:
		csvcontent.append(str(values))

print(len(excelcontent),len(csvcontent))

with open("sample.csv",'w') as wf:
	for columnA,columnB in zip(excelcontent,csvcontent):
		writer=csv.writer(wf)
		writer.writerow([columnA,columnB])