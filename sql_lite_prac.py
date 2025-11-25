##import sqlite3
##firstName = input("enter first  name: ")
##lastName = input("enter last  name: ")
##age = input("enter age: ")
##personData = (firstName, lastName, age)
##
##with sqlite3.connect('test_database.db') as connection:
    #c = connection.cursor()
    #line = "INSERT INTO People VALUES ('"+ firstName +"','"+ lastName +"', "+str(age) +")"
    #c.execute(line)

    #print (line)

##
##    c = connection.cursor()
##    #c.execute("INSERT INTO People VALUES (?,?,?)", personData)
##    c.execute("UPDATE People SET AGE=? WHERE FirstName=? AND LastNAme=?",
##              (45, 'erica', 'millsn'))
##

##
##import sqlite3
##peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
##
##with sqlite3.connect('test_database.db') as connection:
##    c = connection.cursor()
##    c.execute("DROP TABLE IF EXISTS People")
##    c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT)")
##    c.executemany("INSERT INTO People VALUES(?,?,?)",
##                  peopleValues)
##    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
##    for row in c.fetchall():
##        print(row)


import sqlite3
peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)",
                  peopleValues)
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
