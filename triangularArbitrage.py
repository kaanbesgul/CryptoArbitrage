import requests
import json
import threading

currencys={
    "USDT":1,
    "AUDUSDT":"",
    "USDTBIDR":"",
    "USDTBRL":"",
    "EURUSDT":"",
    "GBPUSDT":"",
    "USDTRUB":"",
    "USDTTRY":""
}
newcurrency={
    "AUD":["BTC","ETH","SOL","BNB","ADA","XRP","LUNA","DOGE","DOT","SHIB","MATIC","LINK","SXP","RUNE","AXS","AVAX","CAKE","UNI"],
    "BIDR":["BTC","ETH","BNB","SOL","DOT","ADA","AVAX","DOGE","AXS","MATIC","XRP","SXP"],
    "BRL":["BTC","ETH","ADA","SOL","BNB","SHIB","AXS","XRP","DOT","DOGE","LTC","ENJ","CHZ","LINK","BTT","MATIC","CAKE","AVAX"],
    "EUR":["BTC","ETH","SHIB","SOL","LUNA","ADA","BNB","DOT","XRP","DOGE","VET","LTC","MATIC","LINK","SXP","ENJ","AVAX","HOT","BTT","CHZ","RUNE","GRT","ETC","UNI"],
    "GBP":["BTC","ETH","SOL","ADA","XRP","BNB","DOT","DOGE","LINK","VET","ENJ","LTC","MATIC","SXP","CAKE","RUNE","CHZ","ETC"],
    "RUB":["BTC","ETH","BNB","ADA","XRP","LTC","DOGE","SOL","DOT","ARPA","MATIC"],
    "TRY":["BTC","ETH","SHIB","ARPA","SOL","AVAX","DOGE","HOT","ADA","GRT","CHZ","BTT","DOT","BNB","SXP","XRP","VET"]
}
allcurrency=list(set(newcurrency['AUD']+newcurrency['BIDR']+newcurrency['BRL']+newcurrency['EUR']+newcurrency['GBP']+newcurrency['RUB']+newcurrency['TRY']))
url = "https://www.binance.com/api/v3/depth?symbol={}&limit=1"

def checkprice(url,asset,dict):
    x=requests.get(url.format(asset))
    site_json3=json.loads(x.content)
    if "code" in site_json3:
        dict[asset] = None
    else:
        dict[asset] = float(site_json3['bids'][0][0])


def threadds(dict):
    threads=[]

    for i in currencys.keys():
        if i != "USDT":
            t = threading.Thread(target=checkprice, args=[url,i,dict])
            t.start()
            threads.append(t)
        else:
            pass

    for thread in threads:
        thread.join()

threadds(currencys)
#-------------------------------------------------------------------------------------------------
dict3={"AUD":{},
       "BIDR":{},
       "BRL":{},
       "EUR":{},
       "GBP":{},
       "RUB":{},
       "TRY":{}}

dict2={"AUD":{},
       "BIDR":{},
       "BRL":{},
       "EUR":{},
       "GBP":{},
       "RUB":{},
       "TRY":{}}

def checkprice2(url,asset,asset2,dict):
    x=requests.get(url.format(asset+asset2))
    site_json3=json.loads(x.content)
    if "code" in site_json3:
        dict[asset2][asset] = None
    else:
        dict[asset2][asset] = float(site_json3['bids'][0][0])

def threadds2(dict):
    threads=[]

    for i in newcurrency:
        for y in newcurrency[i]:
            t = threading.Thread(target=checkprice2, args=[url,y,i,dict])
            t.start()
            threads.append(t)
        else:
            pass

    for thread in threads:
        thread.join()
        

def run():
    threadds2(dict2)

    for i in dict2:
        for y in dict2[i].items():
            if i =="AUD":
                dict3[i][y[0]] = y[1] * currencys["AUDUSDT"]
            elif i =="BIDR":
                dict3[i][y[0]] = y[1] / currencys["USDTBIDR"]
            elif i =="BRL":
                dict3[i][y[0]] = y[1] / currencys["USDTBRL"]
            elif i =="EUR":
                dict3[i][y[0]] = y[1] * currencys["EURUSDT"]
            elif i =="GBP":
                dict3[i][y[0]] = y[1] * currencys["GBPUSDT"]
            elif i =="RUB":
                dict3[i][y[0]] = y[1] / currencys["USDTRUB"]
            elif i =="TRY":
                dict3[i][y[0]] = y[1] / currencys["USDTTRY"]

    for i in allcurrency:
        for y in dict3:
            if i in dict3[y]:
                pass
            else:
                dict3[y][i]=None
    j = json.dumps(dict3)
    with open("arbitrage.json", "w+") as f:
        f.write(j)
    run()
run()
