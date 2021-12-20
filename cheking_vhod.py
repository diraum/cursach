import sqlite3
massiv2 =[]

### проверка на ввод данных пользователя при входе
def cheking(time,login1, parol1):
    massiv = []

    database_users = sqlite3.connect("database_users.db")
    cursor = database_users.cursor()



    # проверка, существует ли такой логин уже или нет

    chek = database_users.execute("SELECT parol  FROM albums WHERE login=?", (login1,)).fetchone()
    print(chek)

    #print(correct_pwd)
    if chek==None:
        error = "Пользователь не существует с таким логином. Пожалуйста, проверьте логин или зарегистрируйтесь."
        print(error)
        return error


    else:
        correct_pwd=chek[0]
        if parol1 != correct_pwd:
            error_par = "Пароль неверен!"
            print(error_par)

            return error_par
    return " "


def create(): # бд для отслеживания входа пользователя в игру
    entries = sqlite3.connect("entries.db")  # или :memory: чтобы сохранить в RAM
    cursor = entries.cursor()
    # Создание таблицы
    cursor.execute("""CREATE TABLE albums
                          (entry_number,login, number_of_correct_answers)
                       """)
    entries.commit()

#create()
#cheking(1,"diana","chacha")