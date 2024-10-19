"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K19 - Creating databases with SQL
2024-10-18
time spent: 1.0
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This code is very static, and relies on changing many aspects for new tables

c.execute('CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)') # Command creates a table called courses with the columns code, mark, and id

with open('courses.csv', 'r') as file: # Opens the courses.csv file to read it
    reader = csv.DictReader(file) # Sets variable named reader to DictReader, which will allow the iteration of the csv file as dictionaries for each row
    for _ in reader: # NOTE: The DictReader object automatically uses the first line of the CSV to generate the keys (the columns), so it does not need to be skipped
        c.execute('INSERT INTO courses VALUES (?, ?, ?);', (_.get('code'), _.get('mark'), _.get('id'))) # Inserts the values from each dictionary returned from the reader into the table

# Same process as above, but for the students.csv file
c.execute('CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)')

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for _ in reader:
        c.execute('INSERT INTO students VALUES (?, ?, ?);', (_.get('name'), _.get('age'), _.get('id')))

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#==========================================================

db.commit() #save changes
db.close()  #close database
