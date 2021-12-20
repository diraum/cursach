import sqlite3

#РЕГИСТРАЦИЯ
def creation():
    conn = sqlite3.connect("database_users.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    #Создание таблицы
    cursor.execute("""CREATE TABLE albums
                      (time,login, parol)
                   """)
    conn.commit()

def add(time,login1, parol):
    massiv = []
    conn = sqlite3.connect("database_users.db")
    cursor = conn.cursor()


    # проверка, существует ли такой логин уже или нет

    chek = conn.execute("SELECT login  FROM albums WHERE login=?", (login1,)).fetchone()
    if chek is None:
        sqlite_insert_with_param = """INSERT INTO  albums (time,login, parol)
                                          VALUES (?, ?, ?);"""

        data_tuple = (time, login1, parol)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        sqlite_select_query = """SELECT * from albums """
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()

        for e in range(len(record)):
            massiv.append(list(record[e]))
            print(massiv[e])

        if conn:
            conn.close()
        return massiv

    else:
        error = "Такой логин уже существует! Придумайте другой"
        print(error)

        return error


#creation()


