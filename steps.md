# Connect to the SQLite3 RDBMS
* All you need to do is import it into any file you wish to use SQLite3 in.
```
import sqlite3

DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
    print(conn) # <sqlite3.Connection object at 0x102bddc60>
```
* code above connects to db, then type `pipenv run python sqlite3_demo.py`
