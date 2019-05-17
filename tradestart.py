import requests
import operator
import urllib
import pandas as pd
import numpy as np
import json
import csv
import sort
import time
import telebot


token = '443874886:AAGWuXZcJv5pwOcfVagsNsJEt03oOwy-KaQ'
url = "https://api.telegram.org/bot" + token +"/"
bot = telebot.TeleBot(token) 
Chat_Id = '327385749'

def Buy(classid,instanceid,price,secret_key):

    Buy = requests.get('https://market.dota2.net/api/Buy/' + classid + '_' + instanceid + '/' + price + '/'  + '/?key=' + secret_key)
    print('https://market.dota2.net/api/Buy/' + classid + '_' + instanceid + '/' + price   + '/?key=' + secret_key)
    time.sleep(0.3)
    Buy.text
    print(Buy.json()['result'])
        

    return (Buy.json()['result'])

def Sell(SecretKey):
    df= pd.read_csv('BoughtDb.csv')
    df = df.loc[:, ['Price','Cid','Iid','Status']]
    profit = 5
    n=1
    Not_Sold_Cid = []
    Not_Sold_Iid = []
    Not_Sold_Price = []
    for i in range(len(df)):
        print((df.loc[i]['Price']))
        if df.loc[i]['Status']=='Bought':


            
            to_sell_price =int( df.loc[i]['Price'])
            to_sell_Iid = df.loc[i]['Iid']
            to_sell_Cid = df.loc[i]['Cid']
            
            to_sell_price =str( round((to_sell_price + profit)/0.9))
            sell = requests.get('https://market.dota2.net/api/SetPrice/new_' +str(to_sell_Cid) +'_' +str(to_sell_Iid) +'/' + str(to_sell_price) +'/?key=' +SecretKey)
            sell.text
            if sell.json()['success']==True:
                print('ia tut   ' + str(i))
                df = df.drop([i])

                df.to_csv('BoughtDB.csv',header=True)
            
    return('done')


def MyTrades(secret_key):
    Trades = requests.get('https://market.dota2.net/api/Trades/?key=' + secret_key)
    time.sleep(0.3)
    return(Trades.json())

def ConfirmTrade(botid, secret_key,key):
    Success = ''
    if key==1:
        Confirm = requests.get('https://market.dota2.net/api/ItemRequest/out/' + botid + '/?key=' + secret_key)
        Confirm.text
        time.sleep(0.3)
        if Confirm.json()['success']==True:
            Success = 'Bought'
        return(Success)
    if key==2:
        Confirm = requests.get('https://market.dota2.net/api/ItemRequest/in/' + botid + '/?key=' + secret_key)
        Confirm.text
        time.sleep(0.3)
        if Confirm.json()['success']==True:
            Success = 'Sold'
        return(Success)

def CheckTrades(SecretKey):
    Trades = MyTrades(SecretKey)
    BoughtSuccess= ''
    BoughtPrice =[]
    Classid = []
    Instanceid = []
    Operation = []
    k=0
    d = []
    z = 0
    for i in range(len(Trades)):
        if Trades[i]['ui_status'] != '1':
            k=k+1
    if k==0:
        BoughtSuccess ='No active trades'
    
            
    if k!=0 :
        for i in range(len(Trades)):
            if Trades[i]['ui_status'] == '4':
                BotId = Trades[i]['ui_bid']
                BoughtSuccess = ConfirmTrade(BotId,SecretKey,1)
                Ui_price = str(Trades[i]['ui_price'] * 100)
                BoughtPrice.append(Trades[i]['ui_price'])
                Classid.append(Trades[i]['i_classid'])
                Instanceid.append(Trades[i]['i_instanceid'])
                Operation.append('Bought') 
                d = {"price":pd.Series(Ui_price),
                    "CId": pd.Series(Classid),
                    "IId": pd.Series(Instanceid),
                    "Operation":pd.Series(Operation)}
                Id = Trades[i]['ui_id']
                New_Trades = MyTrades(SecretKey)
                while z==0:
                    if New_Trades[i]['ui_id']==Id:
                        New_Trades = MyTrades(SecretKey)
                        bot.send_message(Chat_Id, 'Нужно принять')
                        time.sleep(30)
                    else:
                        z=1    
                df = pd.DataFrame(d)    
                df.to_csv('BoughtDb.csv',mode='a', header=False)        

            if Trades[i]['ui_status'] == '2':
                BotId = Trades[i]['ui_bid']
                Ui_price = str(Trades[i]['ui_price'] * 100)
                BoughtSuccess = ConfirmTrade(BotId,SecretKey,2)  
                BoughtPrice.append(Ui_price)
                Classid.append(Trades[i]['i_classid'])
                Instanceid.append(Trades[i]['i_instanceid']) 
                Operation.append('Sold') 
                d = {"price":pd.Series(Ui_price),
                    "CId": pd.Series(Classid),
                    "IId": pd.Series(Instanceid),
                    "Operation":pd.Series(Operation)}
                Id = Trades[i]['ui_id']
                New_Trades = MyTrades(SecretKey)
                while z==0:
                    if New_Trades[i]['ui_id']==Id:
                        New_Trades = MyTrades(SecretKey)
                        bot.send_message(Chat_Id, 'Нужно принять')
                        time.sleep(25)
                    else:
                        z=1   
                df = pd.DataFrame(d)    
                df.to_csv('BoughtDb.csv',mode='a', header=False)        
    return(BoughtSuccess)
    