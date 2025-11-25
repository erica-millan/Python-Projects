import sqlite3
connection = sqlite3.connect("C:/Users/erica/Documents/Python-Projects/python-projects/test_database.db")
#need a way to communicate across the connection.
#instantiate a cursor object
#cursor is a control structure that enables operations on a database)
c = connection.cursor()
c.execute("create table People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("insert into People values('Ron', 'Obvious', 42)")
connection.commit()
