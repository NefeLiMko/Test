import requests
import numpy as np
import pandas as pd
import telebot
import time
import threading
import New_trade.Main as ma

Timer=0
chat_id = '327385749'
bot = telebot.TeleBot('443874886:AAGWuXZcJv5pwOcfVagsNsJEt03oOwy-KaQ')
Data = np.load('out.npy').item() 
@bot.message_handler(commands=['sell'])
def sell(message):
    Counter = 0
    Prc=0
    _, inp = message.text.split()
    n=3
    for i in range(int(inp)):
        Counter = ma.Sell(Data, ma.GetInv('Name'),ma.GetInv('Id'), ma.GetInv('Instance'), 188, n)
    bot.send_message(message.chat.id, str(Counter) + 'prodano')

@bot.message_handler(commands=['confirm'])
def confirm(message):
    _, inp = message.text.split()
    ma.ConfirmTrade()
    bot.send_message(message.chat.id, 'done')
    
'''@bot.message_handler(commands=['check'])
def check(message):
    SoIn = 0
    SoOut = 0
    SoOut,SoIn = CheckConfirmation()
    bot.send_message(message.chat.id,'out = ' + str(SoOut) + ', in = ' + str(SoIn) )'''

def pol():
    bot.polling(none_stop=True)

def main(S):
    Mess = ' Нужно подтвердить '
    Timer=S
    Timer+=1
    time.sleep(1)
    print(Timer)
    #print(Stat)
    if Timer % 60 == 0:
        print(60)
    if Timer % 900 == 0:
        print(900)
    if Timer % 180 == 0:
        if Timer % 900 == 0:
            Timer = 0         
    return(Timer)

while True:
    Timer = main(Timer)
    
    