firstName = input("enter first  name: ")
lastName = input("enter last  name: ")
age = input("enter age: ")

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"','"+ lastName +"', "+str(age) +")"
    c.execute(line)


    
