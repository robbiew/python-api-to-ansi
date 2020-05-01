# coding: utf-8

# -----------------------------------------------
# utility: BGG HOTNESS
# author: Robbie Whiting  (aka Alpha)
# contact email: alpha@cardandclaw.com
# bbs: cardandclaw.com:8888
#
# This is an example script showing how to build a Mystic menu file that incorporates data from an API. I'm using
# Board Game Geek python API, but you could use anything.
#
# The script grabs 'Hotness' data from BGG, then builds/writes a mainmenu.ans file with the data 
# (when you run 'python3 bgg-hotness.py), which can then be used as a Mystic BBS menu. 
# 
# Make sure you set this new output file as the 'Display File' in Mystic's Menu Settings for the Main Menu (or
# whatever menu you are creating).
#  
# The 'bgg-hotness.cfg' file contains the configuration details (like where the menu file will be saved) and the 
# source ANSI files used to build/layer the menu.
#
# A custom function called "print_there" in the code allows the writing of text to an exact row/column so that 
# you can add text in and around specific places in your templates, esentially creating a kind of "layering" process.
#
# Put the files somewhere Mystic can access them (e.g. /mystic/python/hotness/) and create a Mystic Event and run the 
# python command (e.g. as an Interval, 2x per day, every hour, etc.) to build the menu: 'python3 /mystic/python/hotness/bgg-hotness.py'
#
# Testing using Linux 64 (Ubuntu 18.04, 20.04) with python3 only.
#
# You can see this in action at cardandclaw.com:8888
#
# -----------------------------------------------

# -----------------------------------------------
# required Python Modules
# -----------------------------------------------

# You'll need to install the BGG API using pip, e.g.:
#   'sudo apt-get install python3-pip'
#   'pip install boardgamegeek2'

import os
from boardgamegeek import BGGClient
import configparser as ConfigParser
import datetime
import inspect
import sys
import codecs

# -----------------------------------------------
# variable declarations
# -----------------------------------------------

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/bgg-hotness.cfg')
applicationAuthor = config.get('BGG Hotness Config', 'applicationAuthor')
outputFileName = config.get('BGG Hotness Config', 'outputFileName')
bgFileName = config.get('BGG Hotness Config', 'bgFileName')

# -----------------------------------------------
# initialize python3 Boardd Game Geek api // https://github.com/lcosmin/boardgamegeek
# -----------------------------------------------

bgg = BGGClient()

# -----------------------------------------------
# open background .ans file as codepage 437
# -----------------------------------------------

f = open(bgFileName, 'r', encoding='cp437')
contents = f.read()

# -----------------------------------------------
# define output file format
# -----------------------------------------------

textFile = open(outputFileName, 'w', encoding='cp437', errors='replace')
textFile.write(contents)

# -----------------------------------------------
# Function to write text to specific X,Y coordinates
# -----------------------------------------------

def print_there(x, y, text):
    textFile.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
textFile.write(contents)
  
# -----------------------------------------------
# Get Board Game Geek data and write out top 10
# -----------------------------------------------

list = bgg.hot_items("boardgame")
# only want first 10 results from API
length = 10
i = 0
count = 10
# after the first 10, we are done
while i > length:
    break
while i < length:
    # add som Mystic pipe color codes
    # set max width to truncate after 35 characters
    # add an elipse '...' for text longer than 35 characters
    # center it all
    print_there(count, 4, (("|08" + list[i].name)[:35] + (list[i].name[35:] and '...')).center(38))
    i += 1
    count += 1
    
# -----------------------------------------------
# Left column Header and Footer
# -----------------------------------------------

print_there(8, 1,  '       |08.|07.|15. BoardGameGeek Top 10 .|07.|08.')
print_there(21, 4, "|07{:%b %d, %Y}".format(datetime.date.today()).center(38) )

# -----------------------------------------------
# Right column BGG Top 10
# -----------------------------------------------

print_there(8, 40,  '             |08.|07.|15. Commands .|07.|08.')

textFile.close()

