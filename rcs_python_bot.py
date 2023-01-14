import telebot
from telebot import types

bot = telebot.TeleBot('')

# Make bot's reaction on word "start" / User can choose from 6 variants

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('GAMES')
    btn2 = types.KeyboardButton('MOBILE APP')
    btn3 = types.KeyboardButton('WEB DEV')
    btn4 = types.KeyboardButton('SOFT')
    btn5 = types.KeyboardButton('DATA ANALYTICS')
    btn6 = types.KeyboardButton('AI')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    send_mess = f"<b>Hello {message.from_user.first_name}</b>\nWhat direction are you interested in?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


# start bot
bot.polling(none_stop=True)