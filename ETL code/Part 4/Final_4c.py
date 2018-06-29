# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 4c
c.For the User table file add a column (true/false) that specifies whether “screen_name” or “description” attribute contains 
within it the “name” attribute of the same user. That is, your output file should contain all of the columns from the User
table,plus the new column. You do not have to modify the original User table.
"""

import sqlite3



conn = sqlite3.connect("twitter_data.db")
c = conn.cursor()

output = open('Final_4c_text.txt', 'w',encoding='utf8')
uservalues = c.execute('SELECT * FROM USER_DATA;').fetchall()

result = ''
for eachrow in uservalues:
    name = eachrow[1]
    screen_name = eachrow[2]
    desc = eachrow[3]
    if name in [None,'','null']:
        name='NULL'
    if screen_name in [None,'','null']:
        screen_name='NULL'
    if desc in  [None,'','null']:
        desc='NULL'
        
    boolean=''
    if name in [screen_name,desc]:
        boolean='True'   
    else:
        boolean='False'
    result+= eachrow[0]+'|'+name+'|'+screen_name+'|'+desc+'|'+str(eachrow[4])+'|'+boolean+'|'+'\n'

output.write(result)
output.close()
conn.close()

