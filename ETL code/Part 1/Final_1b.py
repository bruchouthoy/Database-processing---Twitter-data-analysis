# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 1b

b.Use python to download from the web and save to a local text file (not into database yet) at least 500,000 lines
worth of tweets. Test your code with fewer rows first – you can reduce the number of tweets if your computer is 
running too slow to handle 500K tweets in a reasonable time. How long did it take to save?
NOTE: Do NOT call read() or readlines() without any parameters. That command will attempt to read the entire file
and you only need 500K rows.
"""

import urllib.request as urllib
import time



webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")

start=time.time()
output = open('Part1b_final.txt', 'w',encoding='utf8');
for i in range(500000):
    #read each tweet one by one    
    allTweets = webFD.readline().decode("utf-8")
    for tweet in allTweets: 
        try:  
            output.write(tweet)
        except:
            error_msg = "For tweet # Tweet is corrupted and it threw a ValueError"
            error_msg += "\n"
output.close()
end=time.time()
print ("loadTweets for part1-b took ", (end-start), ' seconds.')
#loadTweets for part1-b took  3134.432579278946  seconds. ~87 mins
#500000 tweets or rows

