import requests
import pandas as pd

secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'

Trades = requests.get('https://market.dota2.net/api/Trades/?key='+secret_key)

GetItemsToGive = requests.get('https://market.dota2.net/api/GetItemsToGive/?key='+secret_key)


def ConfirmTrade()
    for i in range(Trades.text.count('ui_status')):
        Status = Trades.json()[i] 
         
        if int(Status['ui_status'])==4:
            Bot_id = Status['ui_bid']
            Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/out/'+Bot_id+'/?key='+secret_key)
        if int(Status['ui_status'])==2:
            Bot_id = Status['ui_bid']
            Item_Request = requests.get( 'https://market.dota2.net/api/ItemRequest/out/'+Bot_id+'/?key='+secret_key)


        



    
