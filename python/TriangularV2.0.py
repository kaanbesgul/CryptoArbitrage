import requests
import json
import time

url = "https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true"

dict={
    "BNBBTC":"",
    "BNBETH":"",
    "ETHBTC":"",

    "BTCBNB":{
        "BTC":{},
        "BNB":{}
    },
    "BTCETH":{
        "BTC":{},
        "ETH":{}
    },
    "ETHBNB":{
        "ETH":{},
        "BNB":{}
    }
}
def run():
    
    r = requests.get(url)
    site_json = json.loads(r.content)

    for i in site_json['data']:
        for y in site_json['data']:
            if i['q'] == "BTC" and y['q'] == "BNB" and i['b'] == y['b']:
                dict['BTCBNB'][i['q']][i['b']]={}
                dict['BTCBNB'][i['q']][i['b']]['price']=float(i['c'])
                dict['BTCBNB'][i['q']][i['b']]['volume']=float(i['qv'])
                dict['BTCBNB'][y['q']][y['b']]= {}
                dict['BTCBNB'][y['q']][y['b']]['price']=float(y['c'])
                dict['BTCBNB'][y['q']][y['b']]['volume']=float(y['qv'])
            elif i['q'] == "ETH" and y['q'] == "BNB" and i['b'] == y['b']:
                dict['ETHBNB'][i['q']][i['b']] = {}
                dict['ETHBNB'][i['q']][i['b']]['price'] = float(i['c'])
                dict['ETHBNB'][i['q']][i['b']]['volume'] = float(i['qv'])
                dict['ETHBNB'][y['q']][y['b']] = {}
                dict['ETHBNB'][y['q']][y['b']]['price'] = float(y['c'])
                dict['ETHBNB'][y['q']][y['b']]['volume'] = float(y['qv'])
            elif i['q'] == "BTC" and y['q'] == "ETH" and i['b'] == y['b']:
                dict['BTCETH'][i['q']][i['b']] = {}
                dict['BTCETH'][i['q']][i['b']]['price'] = float(i['c'])
                dict['BTCETH'][i['q']][i['b']]['volume'] = float(i['qv'])
                dict['BTCETH'][y['q']][y['b']] = {}
                dict['BTCETH'][y['q']][y['b']]['price'] = float(y['c'])
                dict['BTCETH'][y['q']][y['b']]['volume'] = float(y['qv'])
            elif i['s'] == "BNBBTC":
                dict['BNBBTC']=float(i['c'])
            elif i['s'] == "ETHBTC":
                dict['ETHBTC']=float(i['c'])
            elif i['s'] == "BNBETH":
                dict['BNBETH'] =float(i['c'])

    j = json.dumps(dict)
    with open("../triangulararbitrage.json", "w+") as f:
        f.write(j)
        time.sleep(7)
    run()
run()