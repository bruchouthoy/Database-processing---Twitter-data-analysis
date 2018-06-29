# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 3b
b.	Create a similar collection of INSERT for the User table by reading/parsing data from the local tweet file 
that you have saved earlier. How do these compare in runtime? Which method was faster?
"""

import json
import time


start=time.time()
input_file = open('Part1b_final.txt', 'r',encoding='utf8')
output = open('Final_3b.txt', 'w')

for i in range(500000):
    #read each tweet one by one    
    allLines = input_file.readline().split('ENDOFTWEET')
    for tweet in allLines: 
        try:
            a_tweet = json.loads(tweet)
        except:
            print("Tweet is corrupted and it threw a ValueError")
    
        userdict = a_tweet['user']
        user_id = userdict['id']
        #Converting numeric id to alphabets
        alpha_id = ''
        for digit in str(user_id):
            char = chr(ord('a')+int(digit))
            alpha_id += char
  
        uservalues = (user_id,userdict['name'],userdict['screen_name'],
                     userdict['description'],userdict['friends_count'],alpha_id)

        insert = 'INSERT INTO USER_DATA VALUES ('
        for attr in uservalues:
            # Convert None to NULL
            if attr == None: 
                insert = insert + 'NULL' + ', '
            else:
                if isinstance(attr, (int, float)):
                    value = str(attr)
                else: 
                    # Escape all single quotes in the string
                    value = "'" + str(attr.encode('utf8')).replace("'", "''") + "'"
                insert = insert + value + ', '
        insert = insert[:-2] + '); \n'
        output.write(insert)
output.close()
end=time.time()
print ("Part 3-b took ", (end-start), ' seconds.')
#Part 3-b took  159.92888593673706  seconds.


