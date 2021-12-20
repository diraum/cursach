import sqlite3
import  random

#бд для сложных вопросов 9-10

def creation():# создание и заполнение бд
    conn = sqlite3.connect("difficult_questions.db")
    cursor = conn.cursor()
    # Создание таблицы
    cursor.execute("""CREATE TABLE albums
                      (number,quaction,right)
                   """)

    # Сохраняем изменения
    conn.commit()

    #добавление вопросов
    albums = [('1', 'Как назывался город, в котором проходила подготовка Гагарина?', 'звездный'),
              ('2', 'Число космонавтов побывавших в космосе за все время', '566'),
              ('3', 'Самая холодная из планет, которая вращается, лежа на одном боку', 'уран'),
              ('4','Отец русской косноватики, ученый. Напишите фамилию','циалковский'),
              ('5', 'Сколько минут Гагарин пробыл в космосе?. Напишите число', '108'),
              ('6', 'Какого размера (в см.) был первый спутник? Напишите число', '58'),
              ('7', 'В каком году был запущен первый искусственный спутник?', '1957'),
              ('8', 'Какая из планет третья от Солнца?', 'земля'),
              ('9', 'Сколько планет Солнечной системы можно увидеть невооруженным глазом?', '5'),
              ('10', 'Кто первым предположил, что Земля имеет форму шара?', 'пифагор')]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?)", albums)
    conn.commit()

def adding(): # выборка из бд
        massiv = []
        sqlite_connection = sqlite3.connect('difficult_questions.db')
        cursor = sqlite_connection.cursor()
        listt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

         # генератор рандом
        random1 = random.sample(listt, 2)  # рандомные 8 вопрос
        sqlite_select_query = """SELECT * from albums """
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()



        for e in range(len(random1)):
            massiv.append(list(record[random1[e]]))
        cursor.close()

        return  massiv


#creation()

