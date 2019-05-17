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

MinPrice,MinValueClassId,MinValueInstanceId = sort.Sort_DB()
print(MinPrice)
print(MinValueClassId)
print(MinValueInstanceId)
MinPrice = str(MinPrice)
MinValueClassId = str(MinValueClassId)
MinValueInstanceId = str(MinValueInstanceId)
tradestart.CheckTrades(SecretKey)


Bought = tradestart.Buy(MinValueClassId, MinValueInstanceId, MinPrice,  SecretKey)
BoughtSuccess = tradestart.CheckTrades(SecretKey)


Bought.to_csv('BoughtDb.csv',mode='a', header=False)

'''                 Prodazha                 '''
