import requests
import operator
import urllib
import pandas as pd
import numpy as np
import time
import json
import csv
import tradestart
import sort

SecretKey = '540Ow7mW4PV1839A0u36cAn0C9SHcGo'



'''                 Prodazha                 '''
def Sell(SecretKey):
    df= pd.read_csv('BoughtDb.csv')
    profit = 5
    n=1
    Not_Sold_Cid = []
    Not_Sold_Iid = []
    Not_Sold_Price = []
    for i in range(len(df)):
        print(df.loc[i])
        if df.loc[i]['Status']=='Bought':
            to_sell_price =int( df.loc[i]['Price'])
            to_sell_Iid = df.loc[i]['Iid']
            to_sell_Cid = df.loc[i]['Cid']
            to_sell_price =str( round((to_sell_price + profit)/0.9))
            sell = requests.get('https://market.dota2.net/api/SetPrice/new_' +str(to_sell_Cid) +'_' +str(to_sell_Iid) +'/' + str(to_sell_price) +'/?key=' +SecretKey)
            print('https://market.dota2.net/api/SetPrice/' +str(to_sell_Cid) +'_' +str(to_sell_Iid) +'/' + str(to_sell_price) +'/?key=' +SecretKey)
            sell.text
            if sell.json()['success']==True:
                df.drop(i)
            if sell.json()['success'] != True:
                Not_Sold_Cid.append(to_sell_Cid)
                Not_Sold_Iid.append(to_sell_Iid)
                Not_Sold_Price.append(to_sell_price)
                NotSoldDF = {"price":pd.Series(Not_Sold_Price),
                    "CId": pd.Series(Not_Sold_Cid),
                    "IId": pd.Series(Not_Sold_Iid),
                    "Operation":pd.Series('NotSold')}
                NotSoldDF = pd.DataFrame(NotSoldDF)
                NotSoldDF.to_csv('NotBoughtDb.csv',mode='a', header=False)
    return('done')
df= pd.read_csv('BoughtDb.csv')

print(df)
df.to_csv('Bought.csv',header=True)
