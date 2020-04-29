import telebot

TOKEN = '1064285952:AAHBigGaEeWMwR6mRjH4yUVWpoQk9-A2Wo8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def download(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
