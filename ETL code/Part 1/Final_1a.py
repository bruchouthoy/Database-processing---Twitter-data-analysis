# -*- coding: utf-8 -*-
"""
Name: Brunda Chouthoy
Depaul ID: 1804455
Part 1a
a.	Create a 3rd table incorporating the Geo table (in addition to tweet and user tables that you already have)
 and extend your schema accordingly.You will need to generate an ID for the Geo table primary key (you may use 
any value or combination of values as long as it is unique) for that table and link it to the Tweet table 
(foreign key should be in the Tweet table because there can be multiple tweets sent from the same location). 
In addition to the primary key column, the geo table should have “type”, “longitude” and “latitude” columns.

"""

import sqlite3


TWITTER_DATA = '''CREATE TABLE TWITTER_DATA
(
  created_at DATE,
  id_str VARCHAR(30) NOT NULL,
  text VARCHAR(70) NOT NULL,
  source VARCHAR(40) NOT NULL,
  in_reply_to_user_id VARCHAR(30),
  in_reply_to_screen_name VARCHAR(30),
  in_reply_to_status_id VARCHAR(30),
  retweet_count INTEGER,
  contributors VARCHAR(30),
  user_id VARCHAR(30) NOT NULL,
  coordinate_id varchar(50),
  CONSTRAINT twitter_data_pk PRIMARY KEY(id_str),
  CONSTRAINT twitter_data_fk1 FOREIGN KEY(user_id) references USER_DATA(id)
  CONSTRAINT twitter_data_fk2 FOREIGN KEY(coordinate_id) references GEO_DATA(coordinate_id)
);'''

USER_DATA = '''CREATE TABLE USER_DATA
( 
    id VARCHAR(30) NOT NULL,
    name VARCHAR(40),
    screen_name VARCHAR(20),
    description VARCHAR(100),
    friends_count INTEGER,
    CONSTRAINT USER_DATA_PK PRIMARY KEY(id)
);'''

#'geo': {'coordinates': [42.136671, -75.957731], 'type': 'Point'}
GEO_DATA = '''CREATE TABLE GEO_DATA
(
    coordinate_id varchar(50),
    longitude REAL,
    latitude REAL,
    type varchar(20),
    CONSTRAINT GEO_DATA_PK PRIMARY KEY(coordinate_id)
);'''

# Open a connection to database
conn = sqlite3.connect("twitter_data.db")

# Request a cursor from the database
cursor = conn.cursor()
cursor.execute('pragma foreign_keys=ON')

cursor.execute("DROP TABLE IF EXISTS TWITTER_DATA")
cursor.execute("DROP TABLE IF EXISTS USER_DATA")
cursor.execute("DROP TABLE IF EXISTS GEO_DATA");

# Create the table
cursor.execute(USER_DATA)
cursor.execute(GEO_DATA)
cursor.execute(TWITTER_DATA)


# Finalize and close the connection to the database
conn.commit()
conn.close()
