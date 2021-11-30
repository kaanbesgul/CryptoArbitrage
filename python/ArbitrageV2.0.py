import json
import requests
import threading

def coinmarket(number):
    marketc = requests.get(
        "https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,untracked&exchangeAux=is_active,status&cryptoAux=is_active,status&start=1&limit=10000")

    marketcap = json.loads(marketc.content)

    stable = ["USDT", "USDC", "BUSD", "DAI", "UST", "TUSD", "USDP", "FEI", "HUSD", "WBTC", "BTCB"]
    global coins
    coins={}

    for i in range(0, number):
        if marketcap['data']['cryptoCurrencyMap'][i]['symbol'] in stable:
            pass
        elif marketcap['data']['cryptoCurrencyMap'][i]['symbol'] == "MIOTA":
            coins["IOTA"] = marketcap['data']['cryptoCurrencyMap'][i]['slug']
        else:
            coins[marketcap['data']['cryptoCurrencyMap'][i]['symbol']] = marketcap['data']['cryptoCurrencyMap'][i]['slug']
    return coins


Bitstampt=""
Cryptocom=""
"""Digifinex:https://api.digifinex.com/market
Indoex:https://masternode.indoex.io/getavailablepairs"""

dict={
    "AAX":"https://api.aax.com/common/v2/market/histTicker?type=spotAll",
    "Binance":"https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true",
    "Bitfinex":"https://api-pub.bitfinex.com/v2/tickers?symbols=ALL",
    "Bithumb":"https://global-api.bithumb.pro/market/data/ticker?symbol=ALL",
    "Bitmart":"https://www.bitmart.com/api/ds/market_trade_mappings_front?local=en_US",
    "Bittrex":"https://api.bittrex.com/v3/markets/tickers",
    "Bybit":"https://api-testnet.bybit.com/v2/public/tickers",
    "Coinbase":"https://www.coinbase.com/api/v2/assets/search?base=USDT&country=TR&filter=all&include_prices=true&limit=50&order=asc&page=1&query=&resolution=day&sort=rank",
    "Coinw":"https://www.coinw.com/open/coinw/trade/partition/quotations/all",
    "Ftx":"https://ftx.com/api/markets",
    "Gate":"https://www.gate.io/json_svr/get_leftbar/?u=128&c=397506",
    "Gokumarket":"https://exchange.gokumarket.com/v3/getActiveExchangeCurrencies",
    "Huobi":"https://api.huobi.pro/market/tickers",
    "Kraken":"https://www.kraken.com/api/internal/cryptowatch/markets/assets?asset=USDT&limit=200&assetName=new",
    "Kucoin":"https://www.kucoin.com/_api/trade-front/market/getSymbol/USDS?lang=tr_TR",
    "Mexc":"https://www.mexc.com/_next/data/_iEGdZSD6HVuBsPNvRhYS/tr-TR/markets.json",
    "Okex":"https://www.okex.com/priapi/v5/market/mult-cup-tickers?t=1638123712053&ccys=",
    "Wazirx":"https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates"
}

dict2={"AAX":{},
       "Binance":{},
       "Bitfinex":{},
       "Bithumb":{},
       "Bitmart":{},
       "Bittrex":{},
       "Bybit":{},
       "Coinbase":{},
       "Coinw":{},
       "Ftx":{},
       "Gate":{},
       "Gokumarket":{},
       "Huobi":{},
       "Kraken":{},
       "Kucoin":{},
       "Mexc":{},
       "Okex":{},
       "Wazirx":{}
       }



def threadd(exchangedict,coinsdict):
    threads = []
    for i in exchangedict.keys():
        t = threading.Thread(target=checkprice, args=[exchangedict[i],coinsdict])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

def checkprice(url,coinsdict):
    if url==dict['AAX']:
        r=requests.get(url)
        if r.status_code==200:
            site_json=json.loads(r.content)
            if site_json['data']['histTickers'] != None:
                for i in coinsdict.items():
                    newcur= i[0]+"USDT"
                    for y in site_json['data']['histTickers']:
                        if newcur == y['symbol']:
                            dict2['AAX'][i[1]]=float(y['close'])
                            break
                        else:
                            pass
            else:
                print("Wrong URL")
        else:
            print("Wrong Url")
    elif url==dict['Binance']:
        r=requests.get(url)
        if r.status_code==200:
            site_json=json.loads(r.content)
            if site_json['data'] != None:
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if i[0] == y['b'] and y['q'] =="USDT":
                            dict2['Binance'][i[1]]=float(y['c'])
                            break
                        else:
                            pass
            else:
                print("Wrong URL")
        else:
            print("Wrong Url")
    elif url==dict['Bitfinex']:
        r=requests.get(url)
        if r.status_code==200:
            site_json=json.loads(r.content)
            if len(site_json) != 0:
                for i in coinsdict.items():
                    newcur="t"+i[0]+"USD"
                    for y in site_json:
                        if y[0]==newcur:
                            dict2['Bitfinex'][i[1]] = float(y[3])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong Url")
    elif url == dict['Bithumb']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['info']) !=0:
                for i in coinsdict.items():
                    newcur=i[0]+"-USDT"
                    for y in site_json['info']:
                        if newcur == y['s']:
                            dict2['Bithumb'][i[1]] = float(y['c'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url!")
        else:
            print("Wrong Url")
    elif url == dict['Bitmart']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    newcur=i[0]+"/USDT"
                    for y in site_json['data']['result'][0]['mappingList']:
                        if newcur == y['name']:
                            dict2['Bitmart'][i[1]] = float(y['c'])
                            break
                        else:
                            continue
            else:
                print("Wrong url")
        else:
            print("Wrong url")
    elif url == dict['Bittrex']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'code' in site_json:
                print("Wrong Url")
            else:
                for i in coinsdict.items():
                    newcur=i[0]+"-USDT"
                    for y in site_json:
                        if newcur == y['symbol']:
                            dict2['Bittrex'][i[1]] = float(y['lastTradeRate'])
                            break
                        else:
                            continue
        else:
            print("Wrong url")
    elif url == dict['Bybit']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) > 0:
                for i in coinsdict.items():
                    newcur=i[0]+"USDT"
                    for y in site_json['result']:
                        if y['symbol'] == newcur:
                            dict2['Bybit'][i[1]] = float(y['last_price'])
                            break
                        else:
                            continue
        else:
            print("Wrong url")
    elif url == dict['Coinbase']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if y['base'] == i[0]:
                            dict2['Coinbase'][i[1]] = float(y['latest'])
                            break
                        else:
                            continue
            else:
                print("Wrong url")

        else:
            print("Wrong url")
    elif url == dict['Coinw']:
        r = requests.post(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if y['leftCoinName'] == i[0]:
                            dict2['Coinw'][i[1]] = float(y['price'])
                            break
                        else:
                            continue
            else:
                print("Wrong url")
        else:
            print("Wrong url")
    elif url == dict['Ftx']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'result' in site_json:
                for i in coinsdict.items():
                    newcur=i[0]+"/USDT"
                    for y in site_json['result']:
                        if newcur == y['name']:
                            dict2['Ftx'][i[1]] = float(y['last'])
                            break
                        else:
                            continue
            else:
                print("Wrong url")
        else:
            print("Wrong url")
    elif url == dict['Gate']:
        r = requests.post(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['USDT']) >0:
                for i in coinsdict.items():
                    newcur=i[0].lower()+"_usdt"
                    for y in site_json['USDT']:
                        if y == newcur:
                            dict2['Gate'][i[1]] = float(site_json['USDT'][y]['rate'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Gokumarket']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) >0:
                for i in coinsdict.items():
                    newcur=i[0]+"_USDT"
                    for y in site_json['data']:
                        if y['currency_pair'] == newcur:
                            dict2['Gokumarket'][i[1]] = float(y['currentPrice'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Huobi']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) >0:
                for i in coinsdict.items():
                    newcur=i[0].lower()+"usdt"
                    for y in site_json['data']:
                        if y['symbol'] == newcur:
                            dict2['Huobi'][i[1]] = float(y['close'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Kraken']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) >0:
                for i in coinsdict.items():
                    for y in site_json['result']:
                        if y['asset'] == i[0]:
                            dict2['Kraken'][i[1]] = float(y['price'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Kucoin']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) >0:
                for i in coinsdict.items():
                    newcur=i[0]+"-USDT"
                    for y in site_json['data']:
                        if newcur == y['symbol']:
                            dict2['Kucoin'][i[1]] = float(y['lastTradedPrice'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Mexc']:
        r = requests.post(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['pageProps']) > 0:
                for i in coinsdict.items():
                    for y in site_json['pageProps']['spotMarkets']['USDT']:
                        if i[0] == y['currency']:
                            dict2['Mexc'][i[1]] = float(y['c'])
                            break
                        else:
                            continue
            else:
                print("Wrong Url")
        else:
            print("WRONG URL")
    elif url == dict['Okex']:
        for i in coinsdict.items():
            url+=i[0]+","
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if y['ccy'] == i[0]:
                            dict2['Okex'][i[1]] = float(y['last'])
                            break
                        else:
                            continue
            else:
                print("wrong url")

        else:
            print("WRONG URL")
    elif url == dict['Wazirx']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            for i in coinsdict.items():
                for y in site_json:
                    if i[0].lower() == y:
                        dict2['Wazirx'][i[1]] = float(site_json[y]['usdt'])
                        break
                    else:
                        continue

        else:
            print("WRONG URL")

dict3={"AAX":{},
       "Binance":{},
       "Bitfinex":{},
       "Bithumb":{},
       "Bitmart":{},
       "Bittrex":{},
       "Bybit":{},
       "Coinbase":{},
       "Coinw":{},
       "Ftx":{},
       "Gate":{},
       "Gokumarket":{},
       "Huobi":{},
       "Kraken":{},
       "Kucoin":{},
       "Mexc":{},
       "Okex":{},
       "Wazirx":{}
       }

def run():
    coinmarket(50)
    threadd(dict,coins)

    for i in coins.items():
        for y in dict2.keys():
            if i[1] in dict2[y]:
                dict3[y][i[1]] = dict2[y][i[1]]
            else:
                dict3[y][i[1]] = None
    j = json.dumps(dict3)
    with open("../price.json", "w+") as f:
        f.write(j)
run()