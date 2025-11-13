"""
Python script assignment
Requirments:
-Use python 3 sql3 module
-DB requires 2 fields: an auto incrementing primary int and
field with data type "string"
-read from a list and determind files that end in .txt
-script adds only files that end in .txt to database
-script should print qualifying text files to the console

filelist = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')

"""

import sqlite3
#conn is going to hold the connection to the databse.
#once I connect to database, were going to keep a token
# of that connection to the database

#invoking sqlikte3 and using connect method to connect to DB
conn = sqlite3.connect('db_assignment.db')

##while we have an open session through "conn" do the following lines of code
with conn:
#cursor is what is going to be operating on the databse when we do commands.
#accessing the cursor object and giving it the name cur.
    cur = conn.cursor()
#going to call on the execute command
#creating table in DB one col is primary key other is the file name col.
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_filename TEXT \
    )")
#committing changes to the database
    conn.commit()
conn.close()

#invoking sqlikte3 and using connect method to connect to DB
conn = sqlite3.connect('db_assignment.db')

#tuple of files
files_tuple = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the tuple to find the files that end in .txt

for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #The value for each row will be one file of the tuple therefore (x,)
            #will denote a one element tuple for each file ending with .txt.
            cur.execute("Insert into tbl_files (col_filename) values (?)", (x,))
            print(x)
conn.close()


