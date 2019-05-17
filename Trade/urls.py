import requests
import pandas as pd
"""
def Buy(classid,instanceid,price):
    req = requests.get('https://market.dota2.net/api/Buy/'+ classid + '_' + instanceid + '/' + price +'/?key='+secret_key)')
    
"""
secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'
InvId = []
InvStat = []
InvInstId = []
InvClassId = []
InvName = []
Money = 0
"""GetInv = requests.get('https://market.dota2.net/api/GetInv/?key='+secret_key)
inv = GetInv.json()['data']

for i in range(8):
    InvId.append(inv[i]['ui_id'])
    InvStat.append(inv[i]['ui_status'])
    InvInstId.append(inv[i]['i_instanceid'])
    InvClassId.append(inv[i]['i_classid'])
    InvName.append(inv[i]['i_market_name'])
print(InvId)     #for SetPrice
print(InvStat)
print(InvInstId)
print(InvClassId)
print(InvName)

x=0
BestSellOffer = requests.get('https://market.dota2.net/api/BestSellOffer/'+InvClassId[x]+'_'+InvInstId[x]+'/?key='+secret_key)
Price = int(BestSellOffer.json()['best_offer'] ) -1
print(Price)




for x in range(8):

    BestSellOffer = requests.get('https://market.dota2.net/api/BestSellOffer/'+InvId[x]+'/?key='+secret_key)
    Price = int(BestSellOffer.json()['best_offer']) - 1
    SetPrice = requests.get('https://market.dota2.net/api/SetPrice/new_'+InvId[x]+'/'+str(Price)+'/?key='+secret_key)


"""
"""
GetMoney = requests.get('https://market.dota2.net/api/GetMoney/?key='+secret_key)
Money = GetMoney.json()['money']
"""
def CheckStats():
    r= requests.get('https://market.dota2.net/itemdb/current_570.json')
    r.text

    db = r.json()['db']
    url = 'https://market.dota2.net/itemdb/'+db

    idb = requests.get(url)
    idb.text

    df = pd.read_csv(url,sep=';',encoding='utf-8')
    df = df.sort_values(by = ['c_popularity'],ascending=False)
    print(df[0:57].sort_values(by = ['c_price'],ascending=True))




