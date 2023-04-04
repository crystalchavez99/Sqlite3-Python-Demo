import sqlite3

DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
    print(conn) # <sqlite3.Connection object at 0x102bddc60>
    # a database cursor is a mechanism that enables traversal over the records in a database.
    curs = conn.cursor()
    curs.execute("SELECT 'Hello World!'")
    result = curs.fetchone()
    print(result) # ('Hello World!',)
    curs.execute('SELECT manu_year, make, model FROM cars;')
    cars = curs.fetchall()
    for car in cars:
        print(car)
