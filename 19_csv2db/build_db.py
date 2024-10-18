#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#=========================================================
#c.execute("CREATE TABLE amunals (name TEXT, id INTEGER PRIMARY KEY);")
SELECT * FROM amunals;

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CREATE TABLE amunals (name TEXT, id INTEGER PRIMARY KEY);
INSERT INTO amunals VALUES ("whose-it", 2);
INSERT INTO amunals VALUES ("whats-it", 1);
INSERT INTO amunals VALUES ("blurb", 0);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
