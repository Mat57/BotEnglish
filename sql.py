import sqlite3
import os

path = os.getcwd()


# Обращение к БД
class db_connection:
    db_memory = sqlite3.connect(path + '/EnglishBot.db', check_same_thread=False)
    cursor_memory = db_memory.cursor()


# Проверка на наличие пользователя с таким id в базе
def check_user_in_bd(message):
    db = db_connection
    try:
        sql = '''Select username from Users where id=?'''
        data_tuple = (str(message.from_user.id),)
        db.cursor_memory.execute(sql, data_tuple)
        user_name = db.cursor_memory.fetchall()
        if len(user_name) != 0:
            print('Пользователь ' + str(message.from_user.username) + ' начал работу с ботом')
        else:
            sql = '''INSERT INTO Users (id, username) VALUES(?,?);'''
            data_tuple = (str(message.from_user.id), message.from_user.username,)
            db.cursor_memory.execute(sql, data_tuple)
            db.db_memory.commit()
            print('Пользователь ' + str(message.from_user.username) + ' зарегестрировался в боте и приступил к работе')
    except sqlite3.Error as e:
        print(e)


# Получаем список тем, изучаемых пользователем
def check_users_thems(id):
    db = db_connection
    sql = '''SELECT themes FROM ID_Themes where id=?'''
    data_tuple = (str(id),)
    db.cursor_memory.execute(sql, data_tuple)
    thems = db.cursor_memory.fetchall()
    if thems is not None:
        return thems
    else:
        return 0
