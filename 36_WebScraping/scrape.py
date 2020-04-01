#if you run this program you gets cms_scrape.csv file
#open cms_scrape.csv in excel to see the data clearly
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
'''
output:
Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview
In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…
https://youtube.com/watch?v=-nh9rCzPJ20

Visual Studio Code (Mac) – Setting up a Python Development Environment and Complete Overview
In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on MacOS. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…
https://youtube.com/watch?v=06I63_p-2A4

Clarifying the Issues with Mutable Default Arguments
In this Python Programming Tutorial, we will be clarifying the issues with mutable default arguments. We discussed this in my last video titled “5 Common Python Mistakes and How to Fix Them”, but I received many comments from people who were still confused. So we will be doing a deeper dive to explain exactly what is going on here. Let’s get started…
https://youtube.com/watch?v=_JGmemuINww

5 Common Python Mistakes and How to Fix Them
In this Python Programming Tutorial, we will be going over some of the most common mistakes. I get a lot of questions from people every day, and I have seen a lot of people making these same mistakes in their code. So we will investigate each of these common mistakes and also look at the fixes for each other these as well. Here are the timestamps for each topic we will cover… 1) Indentation and Spaces – 0:45 2) Naming Conflicts – 4:12 3) Mutable Default Args – 10:05 4) Exhausting Iterators – 16:35 5) Importing with * – 22:13
https://youtube.com/watch?v=zdJEYhA2AZQ

How I Setup a New Development Machine – Using Scripts to Automate Installs and Save Time
In this video, I’ll be showing how I set up a new development machine. I recently got a new MacBook and wanted to show how I use scripts to automate a lot of this process. It used to take me a lot of time to install all of my software and get everything set up the way I like it. Now I use these automated scripts to do this in minutes. Let’s get started…
https://youtube.com/watch?v=kIdiWut8eD8

How to Write Python Scripts to Analyze JSON APIs and Sort Results
In this Python Programming Tutorial, we will be learning how to grab data from a JSON API, parse out the information we want, and then sort the data using a custom key. The API we will be using is a JSON API for Homebrew Packages and we will be sorting the packages by their popularity. We cover a lot of topics in this tutorial. We will be using the Requests Library, converting to/from JSON, reading and writing to files, writing our own sorting function, and more. Let’s get started…
https://youtube.com/watch?v=1lxrb_ezP-g

Homebrew Tutorial: Simplify Software Installation on Mac Using This Package Manager
In this video, we’ll be learning how to use the Homebrew Package Manager on MacOS. Brew allows us to easily install command-line tools with a simple command. We can also install native applications for Mac using Brew Cask. I often use these commands in scripts to install a lot of new software quickly and easily on new machines. Let’s get started…
https://youtube.com/watch?v=SELYgZvAZbU

Python Tutorial: VENV (Windows) – How to Use Virtual Environments with the Built-In venv Module
In this Python Programming Tutorial, we will be learning how to use virtual environments on the Windows operating systems with the built-in venv module. We will learn how to create them, activate them, remove them, and much more. Let’s get started…
https://youtube.com/watch?v=APOPm01BVrk

Python Tutorial: VENV (Mac & Linux) – How to Use Virtual Environments with the Built-In venv Module
In this Python Programming Tutorial, we will be learning how to use virtual environments on the Mac and Linux operating systems with the built-in venv module. We will learn how to create them, activate them, remove them, and much more. Let’s get started…
https://youtube.com/watch?v=Kg1Yvry_Ydk

10 Python Tips and Tricks For Writing Better Code
In this Python Programming video, we will be going over 10 tips and tricks for writing Pythonic code. Here are the timestamps for each topic we will cover… 1) Ternary Conditionals – 0:34 2) Underscore Placeholders – 2:13 3) Context Managers – 4:25 4) Enumerate – 6:50 5) Zip – 8:52 6) Unpacking – 13:02 7) Setattr/Getattr – 19:08 8) GetPass – 26:24 9) Python dash m – 29:18 10) Help/Dir – 33:17 
https://youtube.com/watch?v=C-gEQdGVXbk


***Repl Closed***
'''