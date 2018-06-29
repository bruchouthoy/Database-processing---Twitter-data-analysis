# -*- coding: utf-8 -*-
"""
Name:Brunda Chouthoy
Depaul ID: 1804455
Part 2-c
c.	Extra-credit: Perform the python equivalent for 2-iii
iii.	Find the tweet(s) with the longest text message

"""

import time
import json

start=time.time()
fd = open('Part1b_final.txt', 'r',encoding='utf8');

currTextLength=0
maxTextLength=0
max_tweet={}

for i in range(500):
    allLines = fd.readline().split('ENDOFTWEET')
    for tweet in allLines:
        try:
            a_tweet = json.loads(tweet)
        except:
            print("Error tweet")
        text = a_tweet['text']
        id_str=a_tweet['id_str']
        if maxTextLength < len(a_tweet['text']):
            maxTextLength = len(a_tweet['text'])
            max_tweet = {}
            max_tweet.update(a_tweet)
        elif maxTextLength == len(a_tweet['text']):
            max_tweet.update(a_tweet)
    
print(maxTextLength)
print(max_tweet)
fd.close()
        
        
        
    