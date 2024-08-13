# { Python: Быстрый старт, Тема: Базы данных }

import sqlite3


def get_connection():
    con = sqlite3.connect('notebook.sqlite3')
    return con
    
def insert_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO notebook VALUES(?, ?, ?)',(name,phone,age))
    con.commit()
    print("Успешно добавлено")
    pass

def init_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notebook
    (name TEXT UNIQUE, phone TEXT, age INTEGER)
    """)
    con.commit()
    pass

def show_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notebook")
    data = cursor.fetchall()
    print("Список контактов")
    for note in data:
        print('Имя:{} Телефон:{} Возраст:{}'.format(note[0],note[1],note[2]))    

def delete_by_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM notebook WHERE name = ?", (name,))
    connection.commit()
    print("Данные успешно удалены")


if __name__ == "__main__":
    print("Добро пожаловать в записную книжку!")

    action = None

    while action != 'exit':
        con = get_connection()
        init_table(con)
        action = input("Выберите действие [add, read, delete]\n")

        if action == 'add':
            try:
                name, phone, age = input("Введите данные (name phone age): ").split(" ")
            except ValueError:
                print("Неверно введены данные")
            else:
                insert_data(con, name, phone, age)
        elif action == 'read':
            show_data(con)
        elif action == 'delete':
            name_to_delete = input("Введите имя контакта на удаление: ")
            delete_by_name(con, name_to_delete)
        else:
            con.close()
            print("Пока, пока")
            exit(0)
