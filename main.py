import telebot 


TOKEN = "2115217076:AAFvroyog-t29iY8Sg9bnm_pU_niMTor8r0"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, ползователь! Вот список моих команд:\n\nПривет\nКак дела?\nЧем занимаешься?\nЧто такое хоккей?\nКак в него играть?\nПравила хоккея\nПопулярные хоккеисты\nСпасибо")



@bot.message_handler(content_types=["text"])
def main(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет!")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Замечательно, а у вас?")
    elif message.text.lower() == "чем занимаешься?":
        bot.send_message(message.chat.id, "Помогаю вам узнать аспекты про данный вид спорта.")
    elif message.text.lower() == "что такое хоккей?":
        bot.send_message(message.chat.id, "Это спортивная командная игра на льду, целью в которой является забросить шайбу в ворота соперника большее число раз, чем это сделает команда соперника в установленное время.")
    elif message.text.lower() == "как в него играть?":
        bot.send_message(message.chat.id, "Первым на лед ставит клюшку: в центральной точке — гость, в зоне защиты — игрок защищающей команды. При вбрасывании шайба сначала должна коснуться льда и только потом разрешается хоккеистам вводить ее в игру. Серия бросков. Назначается после дополнительного периода при ничейном результате для определения победителя матча. Каждая команда делает 6 бросков. Очередность их выполнения определяется жеребьевкой с помощью монеты.")
    elif message.text.lower() == "правила хоккея":
        bot.send_message(message.chat.id, "Обычная игра должна состоять из трех периодов, каждый из которых длиться 20 минут чистого времени и двух 15-минутных перерывов. Команды должны меняться воротами после каждого периода. - Время игры должно включаться в момент вбрасывания шайбы и останавливаться, когда звучит свисток.")
    elif message.text.lower() == "популярные хоккеисты":
        bot.send_message(message.chat.id, "Сергей Фёдоров, Евгений Малкин , Александр Овечкин")
    elif message.text.lower() == "спасибо":
        bot.send_message(message.chat.id, "Всего хорошего, надеюсь помог вам)")
    else:
        bot.send_message(message.chat.id, "Не знаю, что ответить(")


bot.polling(none_stop=True)