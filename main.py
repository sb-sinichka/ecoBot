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
    words = message.text.split()
    if words >= 2:
        word = words[1]
        if word in sorting_guide:
            bot.reply_to(message, sorting_guide[word])
        else:
            bot.reply_to(message, 'мы не знаем,как сортировать этот предмет')