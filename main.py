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
    obj = message.text[8:]
    if len(obj) > 0:
        if obj in sorting_guide:
            bot.reply_to(message, sorting_guide[obj])
        else:
            bot.reply_to(message, 'мы не знаем,как сортировать этот предмет')

    else:
        bot.reply_to(message,'нужно указать предмет')


bot.polling()