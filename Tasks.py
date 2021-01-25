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
            print(status)
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

    @staticmethod
    def rmTask(id):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("""SELECT tableID, title FROM tasks WHERE id=?""", (id,))
            task = cursor.fetchall()[0]
            cursor.execute("""DELETE FROM tasks WHERE id=?""", (id,))
            db.commit()            
            Tables.updateTable(task[0])
        return task[1]

    @staticmethod
    def rmTasksFromTable(id):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("""DELETE FROM tasks WHERE tableID=?""", (id,))
            db.commit()            

    @staticmethod
    def changeStatus(id):
        with sqlite3.connect(PATH_TO_DATABASE) as db:
            cursor = db.cursor()
            createDate = getDateNowTimestamp()
            cursor.execute("""SELECT tableID, status FROM tasks WHERE id=?""", (id,))
            task = cursor.fetchall()[0]
            status = 0 if int(task[1]) else 1
            cursor.execute("""UPDATE tasks SET changeDate = ?, status = ? WHERE id = ?""", (createDate,status,id))
            Tables.updateTable(task[0])
            db.commit()