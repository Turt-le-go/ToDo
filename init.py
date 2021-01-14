import sqlite3
from config import PATH_TO_DATABASE

def initDB():
    with sqlite3.connect(PATH_TO_DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            creationDate INTEGER,
            changeDate INTEGER
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tableID INTEGER,
            title TEXT,
            creationDate INTEGER,
            changeDate INTEGER,
            status INTEGER,
            description TEXT
        )""")
        db.commit()