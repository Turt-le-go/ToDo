PATH_TO_DATABASE = "database.db"

exitCommands = ("exit", "quit", "q",)

helpCommands = ("help", "h",)

createTableCommands = ("createTable", )
createTaskCommands = ("createTask","ct", )

listAllCommands = ("listAll","la",)
listOfTablesCommands = ("listOfTables",)
listTableCommands = ("listTable","lt",)

rmTaskCommands = ("rmTask",)
rmTableCommands = ("rmTable",)
rmAllCommands = ("rmAll",)

changeStatusCommands = ("changeStatus",)

helpText = """
Довідка ToDo:

    Перелік команд: 

    exit - для виходу з програми.
    
    help - для отримання цієї довідки.
    
    creataTable <name> - Створити нову дошку.
    creataTask <table ID> <title> <status> <description> - Додати завдання на дошку.
        <table ID> - ID дошки для якої створюється завдання.
        <title> - Заголовок завдання.
        <status> - Статус виконання 1 або 0. За замовчуванням 0. (не обовязновий параметр) 
        <description> - Опис завдання. (не обовязновий параметр)  
    
    listAll - Вивести всі дошки завданнь.
    listOfTables - Вивести список дошок.
    listTable <table ID> - Вивести одну дошку з завданнями.
    
    rmAll - Видалити всі записи.
    rmTable <table ID> - Видалити дошку і завдання на ній.
    rmTask <task ID> - видалити одне завдання.
    
    changeStatus <task ID> - Змінити статус завдання.

    Додаткові налаштування:

    За бажанням можна додати скорчення для команд в файлі config.py.
    Також в ньому можна шлях, або підключити нову базу даних.
"""