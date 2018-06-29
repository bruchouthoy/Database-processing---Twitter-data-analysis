# -*- coding: utf-8 -*-
"""
Name:Brunda Chouthoy
Depaul ID: 1804455
Part 2-b
b.	Write python code that is going to read the locally saved tweet data file from 1-b 
and perform the equivalent computation for parts 2-i and 2-ii only. How does the runtime 
compare to the SQL queries?
i.	Find tweets where tweet id_str contains “44” or “77” anywhere in the column

ii.	Find how many unique values are there in the “in_reply_to_user_id” column

"""
import time
import json

fd = open('Part1b_final.txt', 'r',encoding='utf8');

#Function to get the first 500000 tweets from the weburl
def getLines(fd):
    res = []
    i = 0

    while i < 500000:
        res.append(fd.readline())
        i+=1

    return res
allTweets = getLines(fd)

#Part2b-i
start=time.time()
for tweet in allTweets: 
    try:
        a_tweet = json.loads(tweet)
    except:
        print("Tweet is corrupted and it threw a ValueError")
    id_str=a_tweet['id_str']
    if '44' in id_str or '77' in id_str:
        res = tweet
end=time.time()
print ("Part2b-i took ", (end-start), ' seconds.')

#Part 2b-ii
start=time.time()
uniquelist=[]
list_count=0
for tweet in allTweets: 
    try:
        a_tweet = json.loads(tweet)
    except:
        print("Tweet is corrupted and it threw a ValueError")
    text = a_tweet['in_reply_to_user_id']
    if text==None:
        text='NULL'
    if text not in uniquelist:
        uniquelist.append(text)
        list_count+=1
print("Count of unique values",list_count)
end=time.time()
print ("Part 2b-ii took ", (end-start), ' seconds.')

fd.close()
    
        
        