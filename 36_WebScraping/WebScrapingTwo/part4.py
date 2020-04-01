from bs4 import BeautifulSoup
import requests

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

for article in soup.find_all("tr",class_="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"):

	data_column_one=article.span.text
	print(data_column_one)
'''
output:
Jul 19, 2019
Jul 18, 2019
Jul 17, 2019
Jul 16, 2019
Jul 15, 2019
Jul 12, 2019
Jul 11, 2019
Jul 10, 2019
Jul 09, 2019
Jul 08, 2019
Jul 05, 2019
Jul 03, 2019
Jul 02, 2019
Jul 01, 2019
Jun 28, 2019
Jun 27, 2019
Jun 26, 2019
Jun 25, 2019
Jun 24, 2019
Jun 21, 2019
Jun 20, 2019
Jun 19, 2019
Jun 18, 2019
Jun 17, 2019
Jun 14, 2019
Jun 13, 2019
Jun 12, 2019
Jun 11, 2019
Jun 10, 2019
Jun 07, 2019
Jun 06, 2019
Jun 05, 2019
Jun 04, 2019
Jun 03, 2019
May 31, 2019
May 30, 2019
May 29, 2019
May 28, 2019
May 24, 2019
May 23, 2019
May 22, 2019
May 21, 2019
May 20, 2019
May 17, 2019
May 16, 2019
May 15, 2019
May 14, 2019
May 13, 2019
May 10, 2019
May 09, 2019
May 08, 2019
May 07, 2019
May 06, 2019
May 03, 2019
May 02, 2019
May 01, 2019
Apr 30, 2019
Apr 29, 2019
Apr 26, 2019
Apr 25, 2019
Apr 24, 2019
Apr 23, 2019
Apr 22, 2019
Apr 18, 2019
Apr 17, 2019
Apr 16, 2019
Apr 15, 2019
Apr 12, 2019
Apr 11, 2019
Apr 10, 2019
Apr 09, 2019
Apr 08, 2019
Apr 05, 2019
Apr 04, 2019
Apr 03, 2019
Apr 02, 2019
Apr 01, 2019
Mar 29, 2019
Mar 28, 2019
Mar 27, 2019
Mar 26, 2019
Mar 25, 2019
Mar 22, 2019
Mar 21, 2019
Mar 20, 2019
Mar 19, 2019
Mar 18, 2019
Mar 15, 2019
Mar 14, 2019
Mar 13, 2019
Mar 12, 2019
Mar 11, 2019
Mar 08, 2019
Mar 07, 2019
Mar 06, 2019
Mar 05, 2019
Mar 04, 2019
Mar 01, 2019
Feb 28, 2019
Feb 27, 2019

***Repl Closed***
'''