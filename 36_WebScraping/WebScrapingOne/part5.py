from bs4 import BeautifulSoup
import requests

source=requests.get("http://coreyms.com").text

soup=BeautifulSoup(source,'lxml')

article=soup.find('article')

#print(article.prettify())

vid_src=article.find("iframe",class_="youtube-player")

'''
output for print(vid_src):
<iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe>'''

vid_src=article.find("iframe",class_="youtube-player")['src']

'''
output for print(vid_src):
https://www.youtube.com/embed/-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent'''

vid_sr=vid_src.split('/')

'''
output for print(vid_sr):
['https:', '', 'www.youtube.com', 'embed', '-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']'''

vid_src=vid_src.split('/')[4]

'''
output for print(vid_src):
-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent'''

vid_sr=vid_src.split("?")

'''
output for print(vid_sr):
['-nh9rCzPJ20', 'version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']'''


vid_sr=vid_src.split("?")[0]

'''
output for print(vid_sr):
-nh9rCzPJ20'''

yt_link=f"https://www.youtube.com/watch?v={vid_sr}"

'''
output for print(yt_link):
https://www.youtube.com/watch?v=-nh9rCzPJ20'''