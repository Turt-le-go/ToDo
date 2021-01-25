import sqlite3
from utils import getDateNowTimestamp, convertDate
from config import PATH_TO_DATABASE


class Tables:
    
    @staticmethod
    def create(name):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            createDate = getDateNowTimestamp()
            cursor.execute("""INSERT INTO tables(name, creationDate, changeDate) VALUES(?,?,?)""",(name,createDate,createDate))
            cursor.execute("""SELECT id FROM tables  WHERE name LIKE ? ORDER BY id DESC""",(name,))
            id = cursor.fetchone()[0]
            db.commit()
        return id

    @staticmethod
    def updateTable(tableID):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            createDate = getDateNowTimestamp()
            cursor.execute("""UPDATE tables SET changeDate = ? WHERE id = ?""", (createDate,tableID))
            db.commit()
            

    @staticmethod
    def list():
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("""SELECT * FROM tables""")
            tables = cursor.fetchall()
            db.commit()
        return tables

    @staticmethod
    def rmTable(id):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("""SELECT name FROM tables WHERE id=?""", (id,))
            table = cursor.fetchall()[0][0]
            cursor.execute("""DELETE FROM tables WHERE id=?""", (id,))
            db.commit()
        return table