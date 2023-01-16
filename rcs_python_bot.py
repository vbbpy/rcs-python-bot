import telebot
from telebot import types

bot = telebot.TeleBot('5834698775:AAH8TZfNXw8JyhER98DUjsMUAQJXzGhIHNQ')

# Make bot's reaction on word "start" / User can choose from 4 variants

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('GAMES')
    # desktop Games / mobile Games
    btn2 = types.KeyboardButton('MOBILE APP')
    # ANDROID / iOS
    btn3 = types.KeyboardButton('WEB DEVELOPMENT')
    # FRONTEND / BACKEND
    btn4 = types.KeyboardButton('DATA ANALYTICS')
    # Data Science / Machine Learning

    markup.add(btn1, btn2, btn3, btn4)

    send_mess = f"<b>Hello {message.from_user.first_name}</b>\nWhat direction are you interested in?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


# Make bot reaction on client choices

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'games':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('DESKTOP GAMES')
        btn2 = types.KeyboardButton('MOBILE GAMES')
        markup.add(btn1, btn2)
        final_message = "For games development need you choice. Please enter button"

    elif get_message_bot == 'mobile app':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('ANDROID')
        btn2 = types.KeyboardButton('iOS')
        markup.add(btn1, btn2)
        final_message = "For OS development need you choice. Please enter button"

    elif get_message_bot == 'web development':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('FRONT END')
        btn2 = types.KeyboardButton('BACK END')
        markup.add(btn1, btn2)
        final_message = "Please choose one of two options"

    elif get_message_bot == 'data analytics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('DATA SCIENCE')
        btn2 = types.KeyboardButton('MACHINE LEARNING')
        markup.add(btn1, btn2)
        final_message = "Please choose one of two options"

    elif get_message_bot == 'desktop games' or get_message_bot == 'mobile games' or get_message_bot == 'android' or get_message_bot == 'ios':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('GO TO RCS SCHOOL')
        btn2 = types.KeyboardButton('STUDY BY YOURSELF')
        markup.add(btn1, btn2)
        final_message = "Please enter button"

    elif get_message_bot == 'front end' or get_message_bot == 'back end' or get_message_bot == 'data science' or get_message_bot == 'machine learning':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('GO TO RCS SCHOOL')
        btn2 = types.KeyboardButton('STUDY BY YOURSELF')
        markup.add(btn1, btn2)
        final_message = "Please enter button"

    elif get_message_bot == 'go to rcs school':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('GO TO RCS SCHOOL')
        markup.add(btn1)
        final_message = "RIGHT Choice. Please, visit out web page https://rigacoding.lv"

    elif get_message_bot == 'study by yourself':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('GO TO RCS SCHOOL')
        markup.add(btn1)
        final_message = "NO, NO, NO :)). Get quality education only at RCS. Please, visit out web page https://rigacoding.lv"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('GAMES')
        btn2 = types.KeyboardButton('MOBILE APP')
        btn3 = types.KeyboardButton('WEB DEVELOPMENT')
        btn4 = types.KeyboardButton('DATA ANALYTICS')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = 'Sorry, something wrong. Please, press relevant button once again.'

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)