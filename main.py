from sys import exc_info
from Tables import Tables
from Tasks import Tasks
from init import initDB
from config import *
from utils import *

if __name__ == "__main__":

    initDB()

    hello()

    while True:
        cmd = input("> ").split(" ")

        if cmd[0] in exitCommands:
            quit()

        elif cmd[0] in helpCommands:
            print(helpText)

        elif cmd[0] in createTableCommands:
            try:
                id = Tables.create(cmd[1])
                print("Table \"{}\" created. ID = {}".format(cmd[1], id))
            except:
                error()
                
        elif cmd[0] in createTaskCommands:
            try:
                
                id = Tasks.create(*cmd[1:4:]," ".join(cmd[4::]))
                print("Task \"{}\" created. ID = {}".format(cmd[2], id))
            except:
                error()

        elif cmd[0] in listTableCommands:
            try:
                tableName = Tables.list()[int(cmd[1])-1][1]
                tasks = Tasks.getTasksFromTable(cmd[1])
                printTable(tableName, tasks)
            except:
                error()

        elif cmd[0] in listAllCommands:
            try:    
                tablesID = [table[0] for table in Tables.list()]
                for id in tablesID:
                    tableName = Tables.list()[int(id)-1][1]
                    tasks = Tasks.getTasksFromTable(id)
                    printTable(tableName, tasks)
            except:
                error()
        elif cmd[0] in listOfTablesCommands:
            printListOfTables(Tables.list())
        else:
            error()
