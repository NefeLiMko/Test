import start
import telebot


k=0
bot = telebot.TeleBot('443874886:AAGWuXZcJv5pwOcfVagsNsJEt03oOwy-KaQ')

@bot.message_handler(commands=['sell'])
def sell(message):
	bot.send_message(message.chat.id, 'skolko prodat?')

@bot.message_handler(commands=['confirm'])
def sell(message):
	start.ConfirmTrade()
	bot.send_message(message.chat.id, 'done')
	


@bot.message_handler(func=lambda message: True, content_types=['text'])
def add_answer(message):

	start.SellInv()
	bot.send_message(message.chat.id,'sold')
	return False

bot.polling(none_stop=True)