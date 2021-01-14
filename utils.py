from datetime import datetime

def getDateNowTimestamp():
    return datetime.timestamp(datetime.now())
    
def convertDate(tmstmp):
    return datetime.fromtimestamp(tmstmp).strftime("%Y-%m-%d %H:%M:%S")

def error():
    print("\x1b[31mНеправильно введена команда!\x1b[0m\nДля отримання довідки введіть команду help.")

def hello():
    print("Ласкаво просимо в ToDo, дружній командний менеджер ваших завданнь\nДля отримання довідки введіть команду help.")

def fn(str, sep, max):
    #Функція розділяє рядок на підрядки довжини
    #не більшої ніж max, по сепаратору sep
    
    res = [] 
    while(len(str) > max):
        index = str.rfind(" ",0,max+1) 
        index = max if index  in (-1,0) else index+1
        res.append(str[:index])
        str = str[index:]
    res.append(str)
    return res


def printTable(tableName, tasks):
    table = """
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║{}║
╠════════════════╦══════╦════════╦═════════════════════╦══════════════════════╦═══════════════════════════╣ 
║    Завдання    ║  ID  ║ Статус ║   Дата створення    ║   Дата редагування   ║           Опис            ║""".format(tableName.center(105))

    for task in tasks:
        title = task[2].center(16)
        id = str(task[0]).center(6)
        status = "   ✔    " if int(task[5]) else "   ✘    "
        createDate = convertDate(int(task[3])).center(21)
        changeDate = convertDate(int(task[4])).center(22)

        description = fn(task[6], " ", 25)
        table +="""
╠════════════════╬══════╬════════╬═════════════════════╬══════════════════════╬═══════════════════════════╣
║{}║{}║{}║{}║{}║{}║""".format(title, id, status, createDate, changeDate, (" " + description[0]).ljust(27))
    
        for i in range(1,len(description)):
            table +="""
║                ║      ║        ║                     ║                      ║{}║""".format((" " + description[i]).ljust(27))
    table +="""
╚════════════════╩══════╩════════╩═════════════════════╩══════════════════════╩═══════════════════════════╝\n"""
    print(table)

def printListOfTables(tables):
    pTable = """
╔════════════════════════════════════════════════════════════════════╗
║                              Таблиці                               ║
╠════════════════╦══════╦═════════════════════╦══════════════════════╣ 
║    Таблиця     ║  ID  ║   Дата створення    ║   Дата редагування   ║"""

    for table in tables:
        title = table[1].center(16)
        id = str(table[0]).center(6)
        createDate = convertDate(int(table[2])).center(21)
        changeDate = convertDate(int(table[3])).center(22)

        pTable +="""
╠════════════════╬══════╬═════════════════════╬══════════════════════╣
║{}║{}║{}║{}║""".format(title, id, createDate, changeDate)
    
    pTable +="""
╚════════════════╩══════╩═════════════════════╩══════════════════════╝\n"""
    print(pTable)

