import telebot
token = 'токен'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start_message(message):
  
  bot.send_message(message.chat.id,"Привет ✌️ ")


bot.polling(none_stop=True, interval=0)
