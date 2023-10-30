import telebot
import logging
import json
import database
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = telebot.TeleBot(token='6584727414:AAESMmFxFCIEVFw0qO5j-WJFXeZjQ1j88vY')


logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def main(message: Message):
    button = [
        [telebot.types.InlineKeyboardButton(text = 'Войти', callback_data ='come')],
        [telebot.types.InlineKeyboardButton(text="Зарегестироваться", callback_data="regisrtation")]
    ]
    keyboard = telebot.types.InlineKeyboardMarkup(keyboard= button)
    bot.send_message(text = "Здравствуйте", chat_id = message.chat.id, reply_markup= keyboard)

@bot.message_handler(content_types=['text'])
@bot.callback_query_handler(func=lambda call: call.data == 'regisrtation' )
def Come(callback: CallbackQuery):
    data = {'key_1':"value_1",'key_2':"value_2",}
    bot.send_message(text='Введите ваше имя', chat_id= callback.message.chat.id)
    bot.send_message(text='Введите вашу фамилию', chat_id=callback.message.chat.id)
    if key == None and value == None:
        for key,value in data.items():
            database.user_insert(key, )
        bot.send_message(text='Вы успешно зарегистрировались', chat_id = callback.message.chat.id)

if __name__ == "__main__":
    bot.infinity_polling(logger_level=logging.DEBUG)
