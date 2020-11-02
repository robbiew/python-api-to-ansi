# -------------------------------------------------------------------------------------------
# This example uses the NewsAPI python3 library to grab Top Headlines and write to an ANSI
# file.
#
# 'apt-get install python3-pip' -- pip module installer for python3
# 'pip3 install newsapi-python' -- https://github.com/mattlisiv/newsapi-python
# 'pip3 install colorama' -- ANSI color helper https://github.com/tartley/colorama
# 'pip3 install pytz' -- set timezone for timestamp
#
# You'll need to create a NewsAPI developer account and use your own API key below:
# get your API key at https://newsapi.org/
#
# Edit the .cfg file and add your custom paths/file names.
# ------------------------------------------------------------------------------------------

import os
import configparser as ConfigParser
from newsapi import NewsApiClient
from colorama import Fore, Back, Style, init
from colorama import init
from pytz import timezone
from datetime import datetime
import textwrap
import re


# Edit the .cfg file and add your custom paths/file names.

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/breaking-news.cfg')
applicationAuthor = config.get('BreakingNews Config', 'applicationAuthor')
outputFileName = config.get('BreakingNews Config', 'outputFileName')

# grab headlines from newsapi

newsApiKey = config.get('BreakingNews Config', 'newsApiKey')
newsapi = NewsApiClient(api_key=newsApiKey)
data = newsapi.get_top_headlines(country='us')

# Open our output file

textFile = open(outputFileName, 'w+', encoding='cp437', errors='replace')

textFile.write("\n")

# get the data we need from the data object, loop through, remove non-renderable characters,
# and then store in a viarable for later use (I'm using 6 headlines here)

articles = data["articles"]

a = articles[0]["title"]
for k in a.split("\n"):
    a_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

b = articles[1]["title"]
for k in b.split("\n"):
    b_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

c = articles[2]["title"]
for k in c.split("\n"):
    c_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

d = articles[3]["title"]
for k in d.split("\n"):
    d_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

e = articles[4]["title"]
for k in e.split("\n"):
    e_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

f = articles[5]["title"]
for k in f.split("\n"):
    f_safe = " ".join(re.findall(r"[a-zA-Z0-9-'^-]+", k))

# add a header to the file, center the text

# colorama options:
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

preheader = "=-=-=-=-="
header = "BREAKING NEWS"
textFile.write(Fore.RED+preheader.center(80) + Style.BRIGHT+header.center(80))

# Get current data/time and convert it into something usable

now = datetime.now(timezone('US/Pacific'))
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%m/%d/%Y, %I:%M %p")
textFile.write(Style.RESET_ALL+Fore.YELLOW+date_time.center(80))

textFile.write("\n")

# this sets headline area width

width = 60

# write out each headline, line by line, and center it

for line in textwrap.wrap(a_safe, width=width):
    textFile.write(Fore.CYAN+line.center(80))
    if not line:
        break

textFile.write("\n")

for line in textwrap.wrap(b_safe, width=width):
    textFile.write(Style.BRIGHT+line.center(80))
    if not line:
        break

textFile.write("\n")

for line in textwrap.wrap(c_safe, width=width):
    textFile.write(Style.RESET_ALL+Fore.CYAN+line.center(80))
    if not line:
        break

textFile.write("\n")

for line in textwrap.wrap(d_safe, width=width):
    textFile.write(Style.BRIGHT+line.center(80))
    if not line:
        break

textFile.write("\n")

for line in textwrap.wrap(e_safe, width=width):
    textFile.write(Style.RESET_ALL+Fore.CYAN+line.center(80))
    if not line:
        break

textFile.write("\n")

for line in textwrap.wrap(f_safe, width=width):
    textFile.write(Style.BRIGHT+line.center(80))
    if not line:
        break

textFile.write("\n")

# All done!

textFile.close()
