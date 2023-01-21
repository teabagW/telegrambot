import telebot
from telebot import types
from config import token



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Физика")
    btn2 = types.KeyboardButton("Информатика")
    btn3 = types.KeyboardButton("Профильная математика")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помогу тебе с подготовкой к ЕГЭ! Какой предмет тебя интересует?".format(
                         message.from_user),
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def subject(message):
    if (message.text == "Физика"):
        bot.send_message(message.chat.id, text="Напиши номер задания")
    elif (message.text == "Информатика"):
        bot.send_message(message.chat.id, text="Напиши номер задания")
    elif (message.text == "Профильная математика"):
        bot.send_message(message.chat.id, text="Напиши номер задания")
    else:
        bot.send_message(message.chat.id, text="К такому предмету у меня нет материалов(")

bot.polling(none_stop=True)

