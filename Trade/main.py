import requests
import json
import pandas as pd
from getpass import getpass

df = pd.DataFrame()

secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'
"""GetInv = requests.get('https://market.dota2.net/api/GetInv/?key='+secret_key)
inv = GetInv.json()['tradable']"""
#print(inv) 


FNAME = '1.CSV'
secret_key = '7197wXK98l64P21jj4S6MQQuKWzK057'
r= requests.get('https://market.dota2.net/itemdb/current_570.json')
r.text
new_db = r.json()['db']

item_db = requests.get('https://market.dota2.net/itemdb/'+new_db)
df =  pd.read_csv('https://market.dota2.net/itemdb/'+new_db)
print (df)
print (new_db)
