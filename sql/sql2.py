import sqlite3

con = sqlite3.connect('database.sqlite3')



with con:
    con.execute("INSERT INTO notebook VALUES('Maria','1244122121',50)")
    con.execute("INSERT INTO notebook VALUES('Maria2','(124)4122121',50)")


con.close()

