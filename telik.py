import requests
import time
import telebot
import tradestart 
import sort
import threading

token = '443874886:AAGWuXZcJv5pwOcfVagsNsJEt03oOwy-KaQ'
url = "https://api.telegram.org/bot" + token +"/"
bot = telebot.TeleBot(token) 
Chat_Id = '327385749'
SecretKey = '540Ow7mW4PV1839A0u36cAn0C9SHcGo'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Начинаю операцию')
    MinPrice,MinValueClassId,MinValueInstanceId = sort.Sort_DB()
    print(MinPrice)
    print(MinValueClassId)
    print(MinValueInstanceId)
    MinPrice = str(MinPrice)
    MinValueClassId = str(MinValueClassId)
    MinValueInstanceId = str(MinValueInstanceId)
    State = tradestart.Buy(MinValueClassId, MinValueInstanceId, MinPrice,  SecretKey)
    if State == 'К сожалению, предложение устарело. Обновите страницу':
        while State == 'К сожалению, предложение устарело. Обновите страницу' :
            MinPrice,MinValueClassId,MinValueInstanceId = sort.Sort_DB()
            MinPrice = str(MinPrice)
            MinValueClassId = str(MinValueClassId)
            MinValueInstanceId = str(MinValueInstanceId)
            State = tradestart.Buy(MinValueClassId, MinValueInstanceId, MinPrice,  SecretKey)
            print('again')
    
    bot.send_message(message.chat.id, 'Операция выполнена')


@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, 'Начинаю Чекать')
    out = tradestart.CheckTrades(SecretKey)
    bot.send_message(message.chat.id, out)

@bot.message_handler(commands=['sell'])
def sell(message):
    bot.send_message(message.chat.id, 'Начинаю продавать')
    out = tradestart.Sell(SecretKey)
    bot.send_message(message.chat.id, out)

def pol():
    while True:
        print('lul')
        bot.polling()   
 

t = threading.Thread(target=pol)
t.start()
while True:
    mes = tradestart.CheckTrades(SecretKey)
    time.sleep(60)
    pingpong = requests.get('https://market.dota2.net/api/PingPong/?key=' + SecretKey)

