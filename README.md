USE AT YOUR OWN RISK. ALWAYS BACKUP FILES, INCLUDING /MYSTIC/THEMES 
---
Example python (python3) scripts showing how to build a [Mystic BBS menu](http://wiki.mysticbbs.com/doku.php?id=menus) file that incorporates data from an external API. 

/bgg-example uses a [Board Game Geek python API](https://github.com/lcosmin/boardgamegeek).

/newsapi-example uses a [NewsAPI python API](https://newsapi.org/). You'll need to sign up for a free developer account to get an API Key (required).

Each scripts grabs data from the API, then builds/writes an ANSI file with the retrieved data when its called:

e.g. 

```python
python3 bgg-hotness.py
```
or
```python
python3 breaking-news.py
```
...the output file (defined in the cfg file) can then be used as a Mystic BBS menu file, bulletin, etc. 
 
To use as a menu file, make sure you set this new ANSI menu file as the 'Display File' in Mystic's Menu Settings for the Main Menu (or in whatever menu you are creating).

The 'bgg-hotness.cfg' file contains the configuration details (like where the menu file will be saved) and the source ANSI files used to build/layer the menu (header, background, etc.)

A custom function called "print_there" in the code allows the writing of text to an exact row/column so that you can add text in and around specific places in your templates.

Put the files somewhere Mystic can access them (e.g. /mystic/python/hotness/) and create a Mystic Event and run the python3 command (e.g. as an Interval, 2x per day, every hour, etc.) to build the menu: 

e.g.

```python 
python3 /mystic/python/hotness/bgg-hotness.py
```

Tested using Linux 64 (Ubuntu 18.04) and Windows 10 with Python3. 

You can see this in action at cardandclaw.com:8888

Refer to bgg-hotness.py inline comments for more detailed info on how it all works.

NOTE:

I'm indebted to all the other Mystic mod-writers out there, whom I cribbed and adapted different techniques and formats: Phenom Productions, XQTR, Netsurge, Gyphon, Darryl Perry -- and many more.

And thanks to g00r00 for making such awesome software.

If you use this scrript on your BBS, please use your own ANSI art!

Alpha - Card & Claw BBS - cardandclaw.com:8888 - alpha@cardandclaw.com
