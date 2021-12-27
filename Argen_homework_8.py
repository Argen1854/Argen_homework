import sqlite3

database = sqlite3.connect("mywork.sqlite3")
sql = database.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS myworks (
    namework TEXT,
    description TEXT
    )
    """
)

database.commit()

def reqister_work(): # функция что бы добавить дело в список
    namework = input("Work name: ")
    description = input("Description: ")

    sql.execute(f"SELECT namework FROM myworks WHERE namework = '{namework}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO myworks VALUES {(namework, description)}")
        database.commit()
        print("Work add")
        view_list()
    else:
        print("Work was added earlier")
        view_list()

def delete_work(): # что бы удалить
    namework = input("Work name: ")
    sql.execute(f"SELECT namework FROM myworks WHERE namework = '{namework}'")
    if sql.fetchone() is None:
        print("There is no such work")
        view_list()
    else:
        sql.execute(f"DELETE FROM myworks WHERE namework ='{namework}'")
        print("Work was delete")
        database.commit()
        view_list()
    
def view_list(): # что бы просмотреть мой список дел
    print("==================================")
    print("My list:")
    for i, k in sql.execute("SELECT * FROM myworks"):
        print(f"{i} - {k}")
    print("==================================")
    database.commit()

view_list() # смотрит список
answer = input("You want delete or add new work?: ") # спрашивает хочешь добавить или удалить
if answer == "add": # добавляем
    reqister_work()
elif answer == "delete": # удаляем
    delete_work()
else:
    print("Enter delete or add") # если написали что то кроме add и delete

