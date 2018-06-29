# -*- coding: utf-8 -*-
"""
Brunda Chouthoy
Depaul ID: 1804455
Part 1-e
e.Re-run the previous step with batching size of 500 (i.e. by inserting 500 rows at a time with executemany). 
You can adapt the posted example code. How does the runtime compare when batching is used?
"""
import time,json,sqlite3

conn = sqlite3.connect("Part1e_final.db")
c = conn.cursor()
c.execute('pragma foreign_keys=ON')

def uniqid():
    from time import time
    return hex(int(time()*10000000))[2:]


fd = open('Part1b_final.txt', 'r',encoding='utf8');

#Counts
batch_count = 0
good_count = 0
bad_count = 0

 # Load the values into the table via batch
batchRows = 500
batchedInsertsTweet = []
batchedInsertsGeo = []
batchedInsertsUser = []

start = time.time()
for i in range(500000):
    #read each tweet one by one    
    allLines = fd.readline().split('ENDOFTWEET')
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
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], a_tweet['text'], 
                           a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],None)
        else:
            coordinate_id = uniqid()
            geovalues = (coordinate_id,geodict['coordinates'][0],geodict['coordinates'][1],geodict['type'])
            tweetvalues = (a_tweet['created_at'], a_tweet['id_str'], a_tweet['text'], 
                      a_tweet['source'],a_tweet['in_reply_to_user_id'], a_tweet['in_reply_to_screen_name'],
                      a_tweet['in_reply_to_status_id'], retweetcount, a_tweet['contributors'],userdict['id'],coordinate_id)
        
        
        uservalues = (userdict['id'],userdict['name'],userdict['screen_name'],
                     userdict['description'],userdict['friends_count'])
    
        #Create Batch Files 
        batchedInsertsTweet.append(tweetvalues)
        batchedInsertsGeo.append(geovalues)
        batchedInsertsUser.append(uservalues)
        
        #Execute batch files if threshold is met
        if len(batchedInsertsGeo) >= batchRows or len(a_tweet) == 0:
            c.executemany('INSERT OR IGNORE INTO GEO_DATA VALUES (?,?,?,?)', batchedInsertsGeo)
            #reset after execution
            batchedInsertsGeo = []
            batch_count+=1
                
        if len(batchedInsertsUser) >= batchRows or len(a_tweet) == 0:
            c.executemany('INSERT OR IGNORE INTO USER_DATA VALUES (?,?,?,?,?)', batchedInsertsUser)
            # reset after execution
            batchedInsertsUser = []
            batch_count+=1
                
        if len(batchedInsertsTweet) >= batchRows or len(a_tweet) == 0:
            c.executemany('INSERT OR IGNORE INTO TWITTER_DATA VALUES (?,?,?,?,?,?,?,?,?,?,?)', batchedInsertsTweet)
            # reset after execution
            batchedInsertsTweet = []
            batch_count+=1  
    
# Calculate Time
end = time.time()

#Print Time
print ("Part 1e-Loading tweets via batch took ", (end-start), "seconds")
print ("Batch Count:",batch_count/3)
#Part 1e-Loading tweets via batch took 215.38358235359192 seconds
#Batch Count: 1000.0
#User_data-447304
#Twitter_data-499776
#Geo_data-6993

conn.commit()
conn.close()