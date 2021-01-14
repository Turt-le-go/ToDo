import sqlite3
from utils import getDateNowTimestamp, convertDate
from config import PATH_TO_DATABASE
from Tables import Tables

class Tasks:

    @staticmethod
    def create(tableID, title, status=0, description=""):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            createDate = getDateNowTimestamp()
            cursor.execute("""INSERT INTO tasks(tableID, title, creationDate, changeDate, status, description)     
                            VALUES(?,?,?,?,?,?)""",
                            (tableID,title,createDate,createDate,status,description))
            cursor.execute("""SELECT id FROM tasks  WHERE title LIKE ? ORDER BY id DESC""",(title,))
            id = cursor.fetchall()[0][0]
            db.commit()
            Tables.updateTable(tableID)
        return id

    @staticmethod
    def getTasksFromTable(tableID):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("""SELECT * FROM tasks WHERE tableID = ? ORDER BY status DESC, changeDate""", (tableID,))
            tasks = cursor.fetchall()
            db.commit()
        return tasks