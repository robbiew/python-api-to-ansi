# -*- coding: utf-8 -*-

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
# (when you run 'python3 bgg-hotness.py), which can be used as a Mystic BBS menu. 
# 
# Make sure you set this new ANSI menu file as the 'Display File' in Mystic's Menu Settings for the Main Menu (or
# whatever menu you are creating).
#  
# The 'bgg-hotness.cfg' file contains the configuration details (like where the menu file will be saved) and the 
# source ANSI files used to build/layer the menu:
#   - blood.ans: background art
#   - header.ans: header art
#   - menu-options: the menu's commands (Mystic Main menu, in this case)
#
# A custom function called "print_there" in the code allows the writing of text to an exact row/column so that 
# you can add text in and around specific places in your templates, esentially creating a kind of "layering" process.
#
# Put the files somewhere Mystic can access them (e.g. /mystic/python/hotness/) and create a Mystic Event and run the 
# python command (e.g. Internaval, 2x per day, every hour, etc.) to build the menu: 'python3 /mystic/python/hotness/bgg-hotness.py'
#
# Testing using Linux 64 (Ubuntu 18.04) with python3.
#
# You can see this in action at cardandclaw.com:8888
#
# -----------------------------------------------

# -----------------------------------------------
# required Python Modules
# -----------------------------------------------

# you'll need to install the BGG API using pip:
# > sudo apt-get install python3-pip
# > pip install boardgamegeek2

import os
from boardgamegeek import BGGClient
import configparser as ConfigParser
import datetime
import inspect

# -----------------------------------------------
# variable declarations
# -----------------------------------------------

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/bgg-hotness.cfg')
applicationAuthor = config.get('BGG Hotness Config', 'applicationAuthor')
outputFileName = config.get('BGG Hotness Config', 'outputFileName')
bgFileName = config.get('BGG Hotness Config', 'bgFileName')
headerFileName = config.get('BGG Hotness Config', 'headerFileName')
menuCmdFileName = config.get('BGG Hotness Config', 'menuCmdFileName')

# -----------------------------------------------
# initialize python3 Boardd Game Geek api // https://github.com/lcosmin/boardgamegeek
# -----------------------------------------------

bgg = BGGClient()

# -----------------------------------------------
# open background .ans file
# -----------------------------------------------

f = open(bgFileName, 'r+', encoding="cp437")
contents = f.read()

# -----------------------------------------------
# define output file format
# -----------------------------------------------

textFile = open(outputFileName, 'w+', encoding='cp437')
textFile.write(contents)

# -----------------------------------------------
# Functio to write to specific X,Y coordinates
# -----------------------------------------------

def print_there(x, y, text):
    textFile.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))

# -----------------------------------------------
# Add header
# -----------------------------------------------

header = open(headerFileName, 'r+', encoding='cp437') 
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

# -----------------------------------------------
# Get Board Game Geek data and save each item to a variable
# -----------------------------------------------

for item in bgg.hot_items("boardgame"):
    info = item.name[:30] + (item.name[30:] and '...')
    # Just the board game name!
    if item.rank == 1:
        a = ("|08" + item.name)
    if item.rank == 2:
        b = ("|08" + item.name)
    if item.rank == 3:
        c = ("|08" + item.name)
    if item.rank == 4:
        d = ("|08" + item.name)
    if item.rank == 5:
        e = ("|08" + item.name)
    if item.rank == 6:
        f = ("|08" + item.name)
    if item.rank == 7:
        g = ("|08" + item.name)
    if item.rank == 8:
        h = ("|08" + item.name)
    if item.rank == 9:
        i = ("|08" + item.name)
    if item.rank == 10:
        j = ("|08" + item.name)

    # Left aligned, tab-spaced, with rank/numbers
    # if item.rank == 1:
    #     a = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 2:
    #     b = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 3:
    #     c = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 4:
    #     d = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 5:
    #     e = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 6:
    #     f = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 7:
    #     g = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 8:
    #     h = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 9:
    #     i = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(4))
    # if item.rank == 10:
    #     j = ("   |05{0}|04.\t|07{1}\r".format(
    #         item.rank, info).expandtabs(1))

# -----------------------------------------------
# Left column BGG Top 10
# -----------------------------------------------

print_there(8, 1,  '       |08·|07·|15· BoardGameGeek Top 10 ·|07·|08·')

# Text centered within X characters
print_there(10, 4, a.center(38))
print_there(11, 4, b.center(38))
print_there(12, 4, c.center(38))
print_there(13, 4, d.center(38))
print_there(14, 4, e.center(38))
print_there(15, 4, f.center(38))
print_there(16, 4, g.center(38))
print_there(17, 4, h.center(38))
print_there(18, 4, i.center(38))
print_there(19, 4, j.center(38))
print_there(21, 4, "|07{:%b %d, %Y}".format(datetime.date.today()).center(38) )

# Text left-aligned
# print_there(10, 1, a)
# print_there(11, 1, b)
# print_there(12, 1, c)
# print_there(13, 1, d)
# print_there(14, 1, e)
# print_there(15, 1, f)
# print_there(16, 1, g)
# print_there(17, 1, h)
# print_there(18, 1, i)
# print_there(19, 1, j)
# print_there(21, 4,  '|08{:%b %d, %Y}'.format(datetime.date.today()) )

# -----------------------------------------------
# Right column 
# -----------------------------------------------

print_there(8, 44,  '         |08·|07·|15· Commands ·|07·|08·')
cmd = open(menuCmdFileName, 'r+', encoding='cp437') 
count = 9

while True: 
    count += 1

    # Get next line from file 
    line = cmd.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print_there(count, 43, line) 

cmd.close() 
textFile.close()


