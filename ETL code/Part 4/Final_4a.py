# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 4a
4.	Export all three tables (Tweet, User and Geo tables) from the database into a |-separated text file. In this part, 
you do not have to modify the table within the database, just output file data 
(do not generate INSERT statements, just raw data)
a.	For the Geo table, create a single default entry for the ‘Unknown’ location and round longitude and 
latitude to a maximum of 4 digits after the decimal.
"""
import sqlite3
import time


start=time.time()
conn = sqlite3.connect("twitter_data.db")
c = conn.cursor()

output = open('Final_4a_text.txt', 'w',encoding='utf8')
geovalues = c.execute('SELECT * FROM GEO_DATA;').fetchall()

#Creating single default entry for the ‘Unknown’ location 
result = 'Unknown'+'|'+'0'+'|'+'0'+'|'+'No Location'+'|'+'\n'
for eachrow in geovalues: 
    coordinate_id = eachrow[0]
    #Rounding longitude and latitude to a maximum of 4 digits after the decimal
    longitude = str(round(eachrow[1],4))
    latitude= str(round(eachrow[2],4))
    loc_type = eachrow[3]
    
    result += coordinate_id+'|'+longitude+'|'+ latitude+'|'+ loc_type+'|'+'\n'
    
#print(result)
output.write(result)
    
output.close()
conn.close()


