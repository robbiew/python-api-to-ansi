#-------------------------------------------------------------------------------------------
# This example uses the NewsAPI python library to grab Top Headlines and write to an ANSI
# file with a header ANSI.
#
# 'pip install newsapi-python' -- https://github.com/mattlisiv/newsapi-python
#
# You'll need to create a NewsAPI developer account and use your own API key below.
#
# Edit the .cfg file and add your custom paths/file names.
#------------------------------------------------------------------------------------------

import os
import configparser as ConfigParser
from newsapi import NewsApiClient
import datetime
import textwrap 
import re

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/breaking-news.cfg')
applicationAuthor = config.get('BreakingNews Config', 'applicationAuthor')
outputFileName = config.get('BreakingNews Config', 'outputFileName')
headerFileName = config.get('BreakingNews Config', 'headerFileName')
newsApiKey = config.get('BreakingNews Config', 'newsApiKey')

newsapi = NewsApiClient(api_key=newsApiKey)
data = newsapi.get_top_headlines(country='us')

header = open(headerFileName, 'r+', encoding="cp437")
contents = header.read()

count = 0

while True: 
    count += 1

    # Get next line from file 
    line = header.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print_there(count, 1,  line) 

header.close() 

textFile = open(outputFileName, 'w+', encoding="cp437")
textFile.write(contents)

def print_there(x, y, text):
    textFile.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))

articles = data["articles"]

a = articles[0]["title"]
for k in a.split("\n"):
    a_safe = " ".join(re.findall(r"[a-zA-Z0-9^-]+", k))

b = articles[1]["title"]
for k in b.split("\n"):
    b_safe = " ".join(re.findall(r"[a-zA-Z0-9^-]+", k))

c = articles[2]["title"]
for k in c.split("\n"):
    c_safe = " ".join(re.findall(r"[a-zA-Z0-9^-]+", k))

d = articles[3]["title"]
for k in d.split("\n"):
    d_safe = " ".join(re.findall(r"[a-zA-Z0-9^-]+", k))

e = articles[4]["title"]
for k in e.split("\n"):
    e_safe = " ".join(re.findall(r"[a-zA-Z0-9^-]+", k))

textFile.write("\n\n\n")

width = 60

for line in textwrap.wrap(a_safe, width=width):
    textFile.write("|03"+line.center(80))
    if not line: 
        break

textFile.write('\n')

for line in textwrap.wrap(b_safe, width=width):
    textFile.write("|11"+line.center(80))
    if not line: 
        break

textFile.write('\n')

for line in textwrap.wrap(c_safe, width=width):
    textFile.write("|03"+line.center(80))
    if not line: 
        break

textFile.write('\n')

for line in textwrap.wrap(d_safe, width=width):
    textFile.write("|11"+line.center(80))
    if not line: 
        break

textFile.write('\n')

for line in textwrap.wrap(e_safe, width=width):
    textFile.write("|03"+line.center(80))
    if not line: 
        break

print_there(4, 24, "|07{:%b %d, %Y}".format(datetime.date.today()).center(38) )

print_there(22,27, "|07. |08Python News Mod by Alpha |07.")
print_there(41,1, "|PA")
textFile.close()