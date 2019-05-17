import requests
import New_trade.Main as ma

if __name__ == '__main__':
    for i in range(len(ma.Trades())):
        print(ma.Trades()[i]['ui_status'])