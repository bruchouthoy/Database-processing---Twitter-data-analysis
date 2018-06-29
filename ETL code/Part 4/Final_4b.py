# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 4b
b.	For the Tweet table, replace NULLs by a reference to ‘Unknown’ entry (i.e., the foreign key column that references 
Geo table should refer to the “Unknown” entry you created in part-a. Report how many known/unknown locations there were 
in total (e.g., 10,000 known, 490,000 unknown,  2% locations are available)

"""

import sqlite3
import time


start=time.time()
conn = sqlite3.connect("twitter_data_1e.db")
c = conn.cursor()

output = open('Final_4b_text.txt', 'w',encoding='utf8')
twittervalues = c.execute('SELECT * FROM TWITTER_DATA;').fetchall()

known_count=0
unknown_count=0
total_count=0


result=''

for eachrow in twittervalues:
   total_count+=0
   coordinate_id = eachrow[10]
   #Replacing NULL locations with Unknown
   if(coordinate_id==None):
       coordinate_id='Unknown'
       unknown_count+=1
   else:
       known_count+=1
   
   #Replacing None to NULL 
   created_at=eachrow[0]
   in_reply_to_user_id = eachrow[4]
   in_reply_to_screen_name = eachrow[5]
   in_reply_to_status_id = eachrow[6] 
   retweet_count = eachrow[7]
   contributors=eachrow[8]
   user_id = eachrow[9]
   if created_at==None:
       created_at='NULL'
   if in_reply_to_user_id in [None,'null',' ']:
        in_reply_to_user_id='NULL'
   if in_reply_to_screen_name in [None,'null',' ']:
        in_reply_to_screen_name='NULL'
   if in_reply_to_status_id in [None,'null',' ']:
        in_reply_to_status_id='NULL'
   if retweet_count in [None,'null',' ']:
        retweet_count='NULL'
   if contributors in [None,'null',' ']:
        contributors='NULL'
   if user_id in [None,'null',' ']:
        user_id='NULL'
 
   #Writing output to '|' separated file
   result+=created_at+'|'+eachrow[1]+'|'+eachrow[2]+'|'+eachrow[3]+'|'+in_reply_to_user_id+'|'+in_reply_to_screen_name+'|'+in_reply_to_status_id+'|'+str(retweet_count)+'|'+contributors+'|'+user_id+'|'+coordinate_id +'|'+'\n'
   

print("Known locations- ",known_count)
print("Unknown locations-",unknown_count)
    
output.write(result)
output.close()

conn.close()

