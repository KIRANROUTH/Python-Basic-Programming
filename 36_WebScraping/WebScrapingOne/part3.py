from bs4 import BeautifulSoup
import requests

source=requests.get("http://coreyms.com").text

soup=BeautifulSoup(source,'lxml')

article=soup.find('article')

#print(article.prettify())

'''
<article class="post-1642 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope="" itemtype="https://schema.org/CreativeWork">
 <header class="entry-header">
  <h2 class="entry-title" itemprop="headline">
   <a class="entry-title-link" href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview" rel="bookmark">
    Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview
   </a>'''

headline=article.h2.a.text
print(headline)
#output:
#Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview