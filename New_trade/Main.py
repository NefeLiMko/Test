import requests
import pandas as pd
import numpy as np
'''
    Some variables we need
'''
secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'
Trades = requests.get('https://market.dota2.net/api/Trades/?key='+secret_key)
GetItemsToGive = requests.get('https://market.dota2.net/api/GetItemsToGive/?key='+secret_key)
InvId = []
InvStat = []
InvInstId = []
InvClassId = []
InvName = []
DB = {}

'''

'''
def GetInv(Inf):
    GetInv = requests.get('https://market.dota2.net/api/GetInv/?key='+secret_key)
    ok = GetInv.json()['ok']
    if ok==False:
        return(0)
    inv = GetInv.json()['data']
    if Inf=='len':
        return(len(inv))
    if Inf=='Id' :
        return(inv[0]['i_classid'])
    if Inf=='Instance' :
        return(inv[0]['i_instanceid'])
    if  Inf=='Name':
        return(inv[0]['i_market_name'])     
    
def Sell(DB,marketname,classid,instanceid,price,tosell):
    for i in range(tosell):
        requests.get('https://market.dota2.net/api/SetPrice/new_' + classid+'_'+instanceid+'/'+str(price)+'/?key='+secret_key)
        numb = DB.get(marketname)[1]
        DB[marketname] = [price,numb+1]
        
    
    np.save('out.npy', DB)

def Trades():
    Trade = requests.get('https://market.dota2.net/api/Trades/?key='+secret_key)
    return(Trade.json())
    
    
    
    
def ConfirmTrade():
    print('hello')
    for i in range(len(Trades())):
        if  Trades()[i]['ui_status'] =='4':
            Bot_id = Trades()[i]['ui_bid']
            Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/out/'+Bot_id+'/?key='+secret_key)
            if Item_Request.json()['success'] == True:
                print('success')
        if Trades()[i]['ui_status']=='2':
            Bot_id = Trades()[i]['ui_bid']
            Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/in/'+Bot_id+'/?key='+secret_key)
            if Item_Request.json()['success'] == True:
                print('sold successfull')           
                
