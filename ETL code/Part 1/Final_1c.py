# -*- coding: utf-8 -*-
"""
c.Repeat what you did in part-b, but instead of saving tweets to the file, populate the 3-table schema that you created
in SQLite. Be sure to execute commit and verify that the data has been successfully loaded (report row counts for each
of the 3 tables).
If you use the posted example code be sure to turn off batching for this part. (i.e., batchRows set to 1). 
How long did this step take?
"""

import urllib.request as urllib
import json
import sqlite3
import time

conn = sqlite3.connect("Part1c_Final.db")
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

start=time.time()
webFD=urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")

#Function to get the first 500000 tweets from the weburl
def getLines(webFD):
    res = []
    i = 0
    while i < 500000:
        res.append(webFD.readline().decode("utf-8"))
        i+=1
    return res

allTweets = getLines(webFD)

def uniqid():
    from time import time
    return hex(int(time()*10000000))[2:]
 

for tweet in allTweets: 
        try:
            a_tweet = json.loads(tweet) 
        except:
            print("Tweet is corrupted and it threw a ValueError")
        
        userdict = a_tweet['user']
        geodict = a_tweet['geo']
        if 'retweeted_status' in a_tweet.keys():
            retweetcount = a_tweet['retweeted_status']['retweet_count']
        else:
            retweetcount = a_tweet['retweet_count']
        
        if(geodict in [None,'',[],'null']):
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], a_tweet['text'], 
                           a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],
                           a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],None)
        else:
            coordinate_id = uniqid()
            geovalues = (coordinate_id,geodict['coordinates'][0],geodict['coordinates'][1],geodict['type'])
            #Insert values to Geo table 
            cursor.execute("INSERT OR IGNORE INTO GEO_DATA VALUES(?,?,?,?);",geovalues)
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], a_tweet['text'], 
                      a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],
                      a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],coordinate_id)
        
        
        uservalues = (userdict['id'],userdict['name'],userdict['screen_name'],
                     userdict['description'],userdict['friends_count'])
                     
        cursor.execute("INSERT OR IGNORE INTO USER_DATA VALUES(?,?,?,?,?);",uservalues) 
        cursor.execute("INSERT OR IGNORE INTO TWITTER_DATA VALUES(?,?,?,?,?,?,?,?,?,?,?);",tweetvalues)
   
    
end=time.time()
print ("loadTweets took ", (end-start), ' seconds.')
#loadTweets took  5829.0454025268555  seconds - 90+ mins.
#Geo table - 11787
#Twitter table  - 499776
#User table - 447304
conn.commit()
conn.close()