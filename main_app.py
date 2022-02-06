import configparser
from settings import TOKEN
import telebot
from telebot import types
from sql import *

bot = telebot.TeleBot(TOKEN)


# Начало работы
# Добавление пользователя в базу. Вывод тем пользователя.
@bot.message_handler(commands=['start'])
def start(message):
    check_user_in_bd(message)
    themes = check_users_thems(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if len(themes) != 0:
        for theme in themes:
            markup.add(types.KeyboardButton(theme[0]))
        bot.send_message(message.chat.id, 'Выберите необходимую тему',
                         reply_markup=markup)
    else:
        markup.add(types.KeyboardButton('Стоп'))
        bot.send_message(message.chat.id, 'Тем не найдено. Загрузите файл для начала работы.',
                         reply_markup=markup)


bot.infinity_polling()
