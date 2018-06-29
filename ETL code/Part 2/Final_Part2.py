# -*- coding: utf-8 -*-
"""
Name:Brunda Chouthoy
Depaul ID: 1804455
Part 2-a
i.	Find tweets where tweet id_str contains “44” or “77” anywhere in the column

ii.	Find how many unique values are there in the “in_reply_to_user_id” column

iii.	Find the tweet(s) with the longest text message

iv.	Find the average longitude and latitude value for each user name.

v.	Re-execute the query in part iv) 10 times and 100 times and measure the total runtime
 (just re-run the same exact query using a for-loop). Does the runtime scale linearly? 
 (i.e., does it take 10X and 100X as much time?)
"""

import sqlite3
import time

conn = sqlite3.connect("twitter_data.db")
c = conn.cursor()

start=time.time()        
query2a = c.execute("SELECT * FROM TWITTER_DATA WHERE id_str like '%44%' or id_str like '%77%';").fetchall()
end=time.time()
print ("Query 2-i took ", (end-start), ' seconds.')

start=time.time()
query2b = c.execute("select count(distinct in_reply_to_user_id) from twitter_data;").fetchall()
end=time.time()
print ("Query 2-ii took ", (end-start), ' seconds.')

start=time.time()
query2c = c.execute("select * from twitter_data where length(text) = (select max(length(text)) from twitter_data);").fetchall()
end=time.time()
print ("Query 2-iii took ", (end-start), ' seconds.')

start=time.time()
query2d = c.execute("select u.name,avg(latitude),avg(longitude) from twitter_data t, user_data u,geo_data g where t.coordinate_id = g.coordinate_id and t.user_id = u.id group by u.name;").fetchall()
end=time.time()
print ("Query 2-iv took ", (end-start), ' seconds.')

start=time.time()
for i in range(10):
    query2e = c.execute("select u.name,avg(latitude),avg(longitude) from twitter_data t, user_data u,geo_data g where t.coordinate_id = g.coordinate_id and t.user_id = u.id group by u.name").fetchall()
end=time.time()
print ("Query 2-v-a took ", (end-start), ' seconds.')

start=time.time()
for i in range(100):
    query2e = c.execute("select u.name,avg(latitude),avg(longitude) from twitter_data t, user_data u,geo_data g where t.coordinate_id = g.coordinate_id and t.user_id = u.id group by u.name").fetchall()
end=time.time()
print ("Query 2-v-b took ", (end-start), ' seconds.')

conn.close()