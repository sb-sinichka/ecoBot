import telebot

bot = telebot.TeleBot('')


sorting_guide = {
    'пакет': 'пластик',
    'пластиковая бутылка': 'пластик',
    'стаканчик из-под йогурта': 'пластик',
    'стеклянная банка': 'стекло',
    'винная бутылка': 'стекло',
    'жестяная банка': 'металл',
    'алюминиевая банка': 'металл',
    'крышка от банки': 'металл',
    'газета': 'бумага',
    'картонная коробка': 'бумага'
}


@bot.message_handler(commands = ['sorts'])
def sorts(message):
    obj = message.text[7:]
    if len(obj) > 0:
        if obj in sorting_guide:
            bot.reply_to(message, sorting_guide[obj])
        else:
            bot.reply_to(message, 'мы не знаем,как сортировать этот предмет')

    else:
        bot.reply_to(message,'нужно указать предмет')



@bot.message_handler(commands = ['quiz'])
def quiz(message):
    bot.send_poll(message.chat.id, 'сколько будет 2 на 2?', ['42', '67', '4', '92'], correct_option_id= 2, type= 'quiz', explanation= 'в калькулятор зайди посчитай')



bot.polling()