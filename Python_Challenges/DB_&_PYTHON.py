import sqlite3

conn = sqlite3.connect('my1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster(\
                Name TEXT, Species TEXT, IQ INT\
                )")
    conn.commit()

conn.close()
conn = sqlite3.connect('my1.db')
with conn:
    cur = conn.cursor()
####    cur.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?,?,?)", \
####                ('Jean-Baptiste Zorg', 'Human', 122))
####    cur.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?,?,?)", \
####                ('Korben Dallas', 'Meat Popsicle', 100))
####    cur.execute("INSERT INTO Roster(Name, Species, IQ) VALUES (?,?,?)", \
####                ('Ak\'not', 'Mangalore', 100))
####    cur.execute("UPDATE Roster SET Species='Human' WHERE Name  = 'Korben Dallas'")

    cur.execute("select * from Roster")
    for row in cur.fetchall():
        print(row)
    


conn.close()

