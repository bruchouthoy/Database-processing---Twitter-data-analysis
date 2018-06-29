# -*- coding: utf-8 -*-
"""
Brunda Chouthoy
Depaul ID: 1804455
Part 1d
d.Use your locally saved tweet file (created in part-b) to repeat the database population step from part-c.
That is, load 500,000 tweets into the 3-table database using your saved file with tweets (do not use the URL
to read twitter data). How does the runtime compare with part-c?
"""
import json
import time
import sqlite3
import html

conn = sqlite3.connect("Part1d_final.db")
cursor = conn.cursor()

start=time.time()
fd = open('Part1b_final.txt', 'r',encoding='utf8');

def uniqid():
    from time import time
    return hex(int(time()*10000000))[2:]

for i in range(500000):
    #read each tweet one by one    
    allLines = fd.readline().split('TweetEnd')
    for tweet in allLines: 
        try:
            a_tweet = json.loads(tweet)
        except:
            error_msg = "Tweet is corrupted and it threw a ValueError"
            print(error_msg)    
        
        if 'retweeted_status' in a_tweet.keys():
            retweetcount = a_tweet['retweeted_status']['retweet_count']
        else:
            retweetcount = a_tweet['retweet_count']
        userdict = a_tweet['user']
        geodict = a_tweet['geo']
        if(geodict in [None,'',[],'null','NULL']):
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], html.unescape(a_tweet['text']), 
                           a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],None)
        else:
            coordinate_id = uniqid()
            geovalues = (coordinate_id,geodict['coordinates'][0],geodict['coordinates'][1],geodict['type'])
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], html.unescape(a_tweet['text']), 
                      a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],
                      a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],coordinate_id)
        
        
        uservalues = (userdict['id'],userdict['name'],userdict['screen_name'],
                     userdict['description'],userdict['friends_count'])
        
        cursor.execute("INSERT OR IGNORE INTO USER_DATA VALUES(?,?,?,?,?);",uservalues)
        cursor.execute("INSERT OR IGNORE INTO GEO_DATA VALUES(?,?,?,?);",geovalues)
        cursor.execute("INSERT OR IGNORE INTO TWITTER_DATA VALUES(?,?,?,?,?,?,?,?,?,?,?);",tweetvalues)
        
end=time.time()
print ("loadTweets took ", (end-start), ' seconds.')
#loadTweets took  271.4044873714447  seconds.
#User_data - 447304
#Twitter_data - 499776
#Geo_data - 8467

conn.commit()
conn.close()