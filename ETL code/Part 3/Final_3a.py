# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 3a
a.	Export the contents of the User table from a SQLite table into a sequence of INSERT statements within a file. 
This is very similar to what you did in Assignment 4. However, you have to add a unique ID column which has to be a
 string (you cannot use any numbers). 
Hint: one possibility is to replace digits with letters, e.g., chr(ord('a')+1) gives you a 'b' and chr(ord('a')+2) 
returns a 'c'
"""
import sqlite3,time

conn = sqlite3.connect("twitter_data.db")
c = conn.cursor()

start = time.time()
query = c.execute('SELECT * FROM USER_DATA;').fetchall()
output = open('Final_3a.txt', 'w',encoding='utf8')

for eachrow in query:
    user_id = eachrow[0]
    name=eachrow[1]
    screen_name=eachrow[2]
    desc = eachrow[3]
    friends_count = eachrow[4]
    
    #Converting numeric id to alphabets
    alpha_id = ''
    for digit in str(user_id):
        char = chr(ord('a')+int(digit))
        alpha_id += char
  
    uservalues = (user_id,name,screen_name,desc,friends_count,alpha_id)

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
print("Part 3a took",(end-start),"seconds")
#Part 3a took 73.54536151885986 seconds
c.close()
conn.close()
