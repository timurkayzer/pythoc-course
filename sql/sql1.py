import sqlite3

con = sqlite3.connect("database.sqlite3")

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notebook
(name TEXT UNIQUE, phone TEXT, age INTEGER)
""")

try:
    cursor.execute("""
    INSERT INTO notebook VALUES('Vasya','1234567',20)
    """)
except Exception as e:
    print(e)

con.commit()

cursor.execute("SELECT * FROM notebook")
print(cursor.fetchall())

con.close()