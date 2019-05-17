import requests
import pandas as pd
import telebot
import time
import threading
import urls

secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'
Sold = []
SoldId = []
SoldInstId = []
InvId = []
InvStat = []
InvInstId = []
InvClassId = []
InvName = []
ItemsToGive = []
Stat = []
Timer = 0
BSO = ''
SolId = ''
Sol = ''
St = ''
SolInstId = ''
chat_id = '327385749'
bot = telebot.TeleBot('443874886:AAGWuXZcJv5pwOcfVagsNsJEt03oOwy-KaQ')


@bot.message_handler(commands=['sell'])
def sell(message):
    Counter = 0
    Prc=0
    _, inp = message.text.split()
    for i in range(int(inp)):
        Counter = SellInv(i)
    bot.send_message(message.chat.id, str(Counter) + 'prodano')

@bot.message_handler(commands=['confirm'])
def confirm(message):
    _, inp = message.text.split()
    for i in range(int(inp)):
        St,SolInstId,SolId,Sol = ConfirmTrade(i)
        SoldInstId.append(SolInstId)
        SoldId.append(SolId)
        Sold.append(Sol)
        Stat.append(St)
    bot.send_message(message.chat.id, 'done')
	
@bot.message_handler(commands=['check'])
def check(message):
    SoIn = 0
    SoOut = 0
    SoOut,SoIn = CheckConfirmation()
    bot.send_message(message.chat.id,'out = ' + str(SoOut) + ', in = ' + str(SoIn) )

def SellInv(Num):
    num = int(Num)
    Counter = 0
    GetInv = requests.get('https://market.dota2.net/api/GetInv/?key='+secret_key)
    inv = GetInv.json()['data']
    InvId.append(inv[i]['ui_id'])
    InvStat.append(inv[i]['ui_status'])
    InvInstId.append(inv[i]['i_instanceid'])
    InvClassId.append(inv[i]['i_classid'])
    InvName.append(inv[i]['i_market_name'])
    BestSellOffer = requests.get('https://market.dota2.net/api/BestSellOffer/'+InvClassId[i]+'_'+InvInstId[i]+'/?key='+secret_key)
    if BestSellOffer.json()['success'] == True:
        Price = BestSellOffer.json()['best_offer']
        SetPrice = requests.get('https://market.dota2.net/api/SetPrice/new_'+InvClassId[i]+'_'+InvInstId[i]+'/'+Price+'/?key='+secret_key)
        Counter+=1
    elif BestSellOffer.json()['success'] == False: 
        print('noope')
    return(Counter)
    
def ConfirmTrade(Num):
    Status = ''
    Ret = ''
    IdN = ''
    Inst = ''
    i = Num
    Status = Trades.json()[i] 
    print(Status)
    if int(Status['ui_status'])==4:
        print('4')
        Bot_id = Status['ui_bid']
        print(Bot_id)
        Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/out/'+Bot_id+'/?key='+secret_key)
        print(Item_Request)
        if Item_Request.json()['success'] == True:
            Ret = Status['ui_price']
            IdN = Status['i_classid']
            Inst = Status['i_instanceid']
    if int(Status['ui_status'])==2:
        print('2')
        Bot_id = Status['ui_bid']
        Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/in/'+Bot_id+'/?key='+secret_key)
        print(Item_Request)
        Ret = Status['ui_price']
        IdN = Status['i_classid']
        Inst = Status['i_instanceid']
    return (Status['ui_status'],Inst,IdN,Ret)

def CheckConfirmation():
    SomeOut=0
    SomeIn=0
    for i in range(Trades.text.count('ui_status')):
        Status = Trades.json()[i]
        if int(Status['ui_status'])==4:
            SomeOut += 1 
        if int(Status['ui_status'])==2:
            SomeIn += 1
    return(SomeOut,SomeIn)    

def pol():
    bot.polling(none_stop=True)

#def FindCheap():


def main(S):
    Mess = ' Нужно подтвердить '
    Timer=S
    Timer+=1
    time.sleep(1)
    #print(Stat)
    if Timer % 60 == 0:
        if len(SoldId) > 0 :
            for i in range(len(SoldId)):
                BSO = requests.get('https://market.dota2.net/api/BestSellOffer/'+SoldId[i]+'_'+SoldInstId[i]+'/?key='+secret_key)
                print(Stat[i])
                if BSO.json()['success'] == True:
                    if Stat[i] == '4':
                        Price = int(Sold[i]) * 1000 / 8
                        print(Price)
                        SetPrice = requests.get('https://market.dota2.net/api/SetPrice/new_'+SoldId[i]+'_'+SoldInstId[i]+'/'+str(Price)+'/?key='+secret_key)
                        SoldInstId.pop(i)
                        SoldId.pop(i)
                        Stat.pop(i)
                    elif Stat[i] == '2':
                        if int(BSO.json()['best_offer'])<=int(Sold[i]):
                            SetPrice = requests.get('https://market.dota2.net/api/SetPrice/new_'+SoldId[i]+'_'+SoldInstId[i]+'/'+str(Price)+'/?key='+secret_key)
                            SoldInstId.pop(i)
                            SoldId.pop(i)
                            Stat.pop(i)
    if Timer % 900 == 0:
        SOut,SIn = CheckConfirmation()
        if (SOut != 0) or (SIn != 0):
            bot.send_message(chat_id, text = 'READY')
    if Timer % 180 == 0:
        PingPong = requests.get( 'https://market.dota2.net/api/PingPong/?key='+secret_key)
        if Timer % 900 == 0:
            Timer = 0         
    return(Timer)

# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=pol)
t2 = threading.Thread(target=main)

# start threads
t1.start()
t2.start()

e1.set() # initiate the first event



while True:
    Trades = requests.get( 'https://market.dota2.net/api/Trades/?key='+secret_key)
    GetItemsToGive = requests.get( 'https://market.dota2.net/api/GetItemsToGive/?key='+secret_key)

    Timer = main(Timer)
    

######CHECK TO BUY