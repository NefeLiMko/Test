import requests
import pandas as pd
import time

def Sort_DB():
    '''Poluchaem last DB na servere i gruzim ee na ustroistvo'''
    Current = requests.get('https://market.dota2.net/itemdb/current_570.json')
    Current.text
    time.sleep(1)
    Current_DB = Current.json()['db']
    time.sleep(1)
    '''                                                      '''
    '''Sozdaem dataframe dlia sortirovki po populiarnosti'''
    '''with open('e:/Workspace/trader/Db.csv', 'wb') as f:  
        f.write(Item_db.content)
    '''
    df = pd.read_csv('https://market.dota2.net/itemdb/'+Current_DB,sep=';', comment='#')
    
    Popular = df.sort_values(by=['c_popularity'], ascending=False)
    '''                                                  '''
    '''Otbiraem pervuiu stranicu populiarnih i sortiruem po cene'''
    Cheapest =Popular[0:55] 
    Cheapest = Cheapest.sort_values(by=['c_price'], ascending=True)
    '''                                                         '''
    '''Vivodim'''
    MinPrice = Cheapest['c_price'][:1].values[0]
    ValueClassId = Cheapest['c_classid'][:1].values[0]
    ValueInstanceId = Cheapest['c_instanceid'][:1].values[0]
    return(MinPrice, ValueClassId, ValueInstanceId)

