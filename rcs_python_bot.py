@bot.message_handler(commands=['webdev'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "webdev":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("FRONT END")
        btn2 = types.KeyboardButton("BACK END")
        markup.add(btn1, btn2)
        last_message = "Please choose one of two options"


    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('GAMES')
        btn2 = types.KeyboardButton('MOBILE APP')
        btn3 = types.KeyboardButton('WEB DEV')
        btn4 = types.KeyboardButton('DATA ANALYTICS')
        markup.add(btn1, btn2, btn3, btn4, )
        last_message = "Choose one of the options"
    bot.send_message(message.chat.id, last_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['analytics'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "analytics":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("DATA SCIENCE")
        btn2 = types.KeyboardButton("MACHINE LEARNING")
        markup.add(btn1, btn2)
        last_message = "Please choose one of two options"
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('GAMES')
        btn2 = types.KeyboardButton('MOBILE APP')
        btn3 = types.KeyboardButton('WEB DEV')
        btn4 = types.KeyboardButton('DATA ANALYTICS')
        markup.add(btn1, btn2, btn3, btn4, )
        last_message = "Please choose one of the options"
    bot.send_message(message.chat.id, last_message, parse_mode='html', reply_markup=markup)

# https: // www.w3schools.com / howto / howto_blog_become_frontenddev.asp
# https://learntocodewith.me/posts/backend-development/

# https://www.edx.org/learn/data-science
# https://www.coursera.org/learn/machine-learning

# start bot
bot.polling(none_stop=True)
