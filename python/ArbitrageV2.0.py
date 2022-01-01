import json
import time
import requests
import threading


def coinmarket(number):
    marketc = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit="+str(number))

    marketcap = json.loads(marketc.content)

    stable = ["USDT", "USDC", "BUSD", "DAI", "UST", "TUSD", "USDP", "FEI", "HUSD", "WBTC", "BTCB"]
    global coins
    coins = {}

    for i in marketcap['data']['cryptoCurrencyList']:
        if i['symbol'] in stable:
            pass
        elif i['symbol'] == "MIOTA":
            coins["IOTA"] =i['slug']
        else:
            coins[i['symbol']] =i['slug']

Bitstampt = ""
Cryptocom = ""
"""Digifinex:https://api.digifinex.com/market
LBank:https://www.lbank.info/request/tick
Indoex:https://masternode.indoex.io/getavailablepairs
Probit:https://www.probit.com/api/exchange/v1/ticker"""

dict = {
    "AAX": "https://api.aax.com/common/v2/market/histTicker?type=spotAll",
    "Binance": "https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true",
    "Bitfinex": "https://api-pub.bitfinex.com/v2/tickers?symbols=ALL",
    "Bithumb": "https://global-api.bithumb.pro/market/data/ticker?symbol=ALL",
    "Bitmart": "https://www.bitmart.com/api/ds/market_trade_mappings_front?local=en_US",
    "Bittrex": "https://api.bittrex.com/v3/markets/tickers",
    "Bybit": "https://api-testnet.bybit.com/v2/public/tickers",
    "Coinbase": "https://www.coinbase.com/api/v2/assets/search?base=USDT&country=TR&filter=all&include_prices=true&limit=50&order=asc&page=1&query=&resolution=day&sort=rank",
    "Coinw": "https://www.coinw.com/open/coinw/trade/partition/quotations/all",
    "Ftx": "https://ftx.com/api/markets",
    "Gate": "https://www.gate.io/json_svr/get_leftbar/?u=128&c=397506",
    "Gokumarket": "https://exchange.gokumarket.com/v3/getActiveExchangeCurrencies",
    "Huobi": "https://api.huobi.pro/market/tickers",
    "Kraken": "https://www.kraken.com/api/internal/cryptowatch/markets/assets?asset=USDT&limit=200&assetName=new",
    "Kucoin": "https://www.kucoin.com/_api/trade-front/market/getSymbol/USDS?lang=tr_TR",
    "Liquid":"https://api.liquid.com/products?with_rate=true",
    "Probit":"https://www.probit.com/api/exchange/v1/ticker",
    "Okex": "https://www.okex.com/priapi/v5/market/mult-cup-tickers?t=1638123712053&ccys=",
    "Wazirx": "https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates"
}

dict2 = {"AAX": {},
         "Binance": {},
         "Bitfinex": {},
         "Bithumb": {},
         "Bitmart": {},
         "Bittrex": {},
         "Bybit": {},
         "Coinbase": {},
         "Coinw": {},
         "Ftx": {},
         "Gate": {},
         "Gokumarket": {},
         "Huobi": {},
         "Kraken": {},
         "Kucoin": {},
         "Liquid": {},
         "Probit": {},
         "Okex": {},
         "Wazirx": {}
         }

dict3 = {
    "BNBBTC": "",
    "BNBETH": "",
    "ETHBTC": "",
    "BTCBNB": {
        "BTC": {},
        "BNB": {}
    },
    "BTCETH": {
        "BTC": {},
        "ETH": {}
    },
    "ETHBNB": {
        "ETH": {},
        "BNB": {}
    }
}


def threadd(exchangedict, coinsdict):
    threads = []
    for i in exchangedict.keys():
        t = threading.Thread(target=checkprice, args=[exchangedict[i], coinsdict])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def checkprice(url, coinsdict):
    if url == dict['AAX']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['data']['histTickers'] != None:
                for i in coinsdict.items():
                    newcur = i[0] + "USDT"
                    for y in site_json['data']['histTickers']:
                        if newcur == y['symbol']:
                            dict2['AAX'][i[1]] = float(y['close'])
                            break
                        else:
                            dict2['AAX'][i[1]] = None
            else:
                print("Wrong URL")
        else:
            print("Wrong Url")
    elif url == dict['Binance']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['data'] != None:
                for i in site_json['data']:
                    for y in site_json['data']:
                        if i['q'] == "BTC" and y['q'] == "BNB" and i['b'] == y['b']:
                            dict3['BTCBNB'][i['q']][i['b']] = {}
                            dict3['BTCBNB'][i['q']][i['b']]['price'] = float(i['c'])
                            dict3['BTCBNB'][i['q']][i['b']]['volume'] = float(i['qv'])
                            dict3['BTCBNB'][y['q']][y['b']] = {}
                            dict3['BTCBNB'][y['q']][y['b']]['price'] = float(y['c'])
                            dict3['BTCBNB'][y['q']][y['b']]['volume'] = float(y['qv'])
                        elif i['q'] == "ETH" and y['q'] == "BNB" and i['b'] == y['b']:
                            dict3['ETHBNB'][i['q']][i['b']] = {}
                            dict3['ETHBNB'][i['q']][i['b']]['price'] = float(i['c'])
                            dict3['ETHBNB'][i['q']][i['b']]['volume'] = float(i['qv'])
                            dict3['ETHBNB'][y['q']][y['b']] = {}
                            dict3['ETHBNB'][y['q']][y['b']]['price'] = float(y['c'])
                            dict3['ETHBNB'][y['q']][y['b']]['volume'] = float(y['qv'])
                        elif i['q'] == "BTC" and y['q'] == "ETH" and i['b'] == y['b']:
                            dict3['BTCETH'][i['q']][i['b']] = {}
                            dict3['BTCETH'][i['q']][i['b']]['price'] = float(i['c'])
                            dict3['BTCETH'][i['q']][i['b']]['volume'] = float(i['qv'])
                            dict3['BTCETH'][y['q']][y['b']] = {}
                            dict3['BTCETH'][y['q']][y['b']]['price'] = float(y['c'])
                            dict3['BTCETH'][y['q']][y['b']]['volume'] = float(y['qv'])
                        elif i['s'] == "BNBBTC":
                            dict3['BNBBTC'] = float(i['c'])
                        elif i['s'] == "ETHBTC":
                            dict3['ETHBTC'] = float(i['c'])
                        elif i['s'] == "BNBETH":
                            dict3['BNBETH'] = float(i['c'])
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if i[0] == y['b'] and y['q'] == "USDT":
                            dict2['Binance'][i[1]] = float(y['c'])
                            break
                        else:
                            dict2['Binance'][i[1]] = None
            else:
                print("Wrong URL")
        else:
            print("Wrong Url")
    elif url == dict['Bitfinex']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json) != 0:
                for i in coinsdict.items():
                    newcur = "t" + i[0] + "USD"
                    for y in site_json:
                        if y[0] == newcur:
                            dict2['Bitfinex'][i[1]] = float(y[3])
                            break
                        else:
                            dict2['Bitfinex'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong Url")
    elif url == dict['Bithumb']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['info']) != 0:
                for i in coinsdict.items():
                    newcur = i[0] + "-USDT"
                    for y in site_json['info']:
                        if newcur == y['s']:
                            dict2['Bithumb'][i[1]] = float(y['c'])
                            break
                        else:
                            dict2['Bithumb'][i[1]] = None
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
                    newcur = i[0] + "/USDT"
                    for y in site_json['data']['result'][0]['mappingList']:
                        if newcur == y['name']:
                            dict2['Bitmart'][i[1]] = float(y['c'])
                            break
                        else:
                            dict2['Bitmart'][i[1]] = None
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
                    newcur = i[0] + "-USDT"
                    for y in site_json:
                        if newcur == y['symbol']:
                            dict2['Bittrex'][i[1]] = round(float(y['lastTradeRate']), 7)
                            break
                        else:
                            dict2['Bittrex'][i[1]] = None
        else:
            print("Wrong url")
    elif url == dict['Bybit']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) > 0:
                for i in coinsdict.items():
                    newcur = i[0] + "USDT"
                    for y in site_json['result']:
                        if y['symbol'] == newcur:
                            dict2['Bybit'][i[1]] = float(y['last_price'])
                            break
                        else:
                            dict2['Bybit'][i[1]] = None
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
                            dict2['Coinbase'][i[1]] = round(float(y['latest']), 7)
                            break
                        else:
                            dict2['Coinbase'][i[1]] = None
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
                            dict2['Coinw'][i[1]] = None
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
                    newcur = i[0] + "/USDT"
                    for y in site_json['result']:
                        if newcur == y['name']:
                            dict2['Ftx'][i[1]] = float(y['last'])
                            break
                        else:
                            dict2['Ftx'][i[1]] = None
            else:
                print("Wrong url")
        else:
            print("Wrong url")
    elif url == dict['Gate']:
        r = requests.post(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['USDT']) > 0:
                for i in coinsdict.items():
                    newcur = i[0].lower() + "_usdt"
                    for y in site_json['USDT']:
                        if y == newcur:
                            dict2['Gate'][i[1]] = float(site_json['USDT'][y]['rate'])
                            break
                        else:
                            dict2['Gate'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Gokumarket']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    newcur = i[0] + "_USDT"
                    for y in site_json['data']:
                        if y['currency_pair'] == newcur:
                            dict2['Gokumarket'][i[1]] = float(y['currentPrice'])
                            break
                        else:
                            dict2['Gokumarket'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Huobi']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    newcur = i[0].lower() + "usdt"
                    for y in site_json['data']:
                        if y['symbol'] == newcur:
                            dict2['Huobi'][i[1]] = float(y['close'])
                            break
                        else:
                            dict2['Huobi'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Kraken']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) > 0:
                for i in coinsdict.items():
                    for y in site_json['result']:
                        if y['asset'] == i[0]:
                            dict2['Kraken'][i[1]] = float(y['price'])
                            break
                        else:
                            dict2['Kraken'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Kucoin']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    newcur = i[0] + "-USDT"
                    for y in site_json['data']:
                        if newcur == y['symbol']:
                            dict2['Kucoin'][i[1]] = float(y['lastTradedPrice'])
                            break
                        else:
                            dict2['Kucoin'][i[1]] = None
            else:
                print("Wrong Url")
        else:
            print("Wrong url")
    elif url == dict['Liquid']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json) > 0:
                for i in coinsdict.items():
                    for y in site_json:
                        if y['quoted_currency'] == "USDT" and i[0] ==y['base_currency']:
                            try:
                                dict2['Liquid'][i[1]] = float(y['average_price'])
                                break
                            except TypeError:
                                dict2['Liquid'][i[1]] = None
                        else:
                            dict2['Liquid'][i[1]] = None
            else:
                print("Wrong URL")
        else:
            print("Wrong Url")
    elif url == dict['Probit']:
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'data' in site_json:
                for i in coinsdict.items():
                    newcur = i[0] + "-USDT"
                    for y in site_json['data']:
                        if y['market_id'] == newcur:
                            dict2['Probit'][i[1]] = float(y['last'])
                            break
                        else:
                            dict2['Probit'][i[1]] = None
        else:
            print("Wrong url")
    elif url == dict['Okex']:
        for i in coinsdict.items():
            url += i[0] + ","
        r = requests.get(url)
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) > 0:
                for i in coinsdict.items():
                    for y in site_json['data']:
                        if y['ccy'] == i[0] and i[0] != "BNB":
                            dict2['Okex'][i[1]] = float(y['last'])
                            break
                        else:
                            dict2['Okex'][i[1]] = None
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
                        try:
                            dict2['Wazirx'][i[1]] = round(float(site_json[y]['usdt']), 7)
                            break
                        except KeyError:
                            dict2['Wazirx'][i[1]] = None
                    else:
                        dict2['Wazirx'][i[1]] = None
        else:
            print("WRONG URL")
    else:
        print("Url doesn't match")


def run():
    coinmarket(100)
    threadd(dict, coins)
    j = json.dumps(dict2)
    with open("../spatialArbitrage.json", "w+") as f:
        f.write(j)
    j=json.dumps(dict3)
    with open("../triangulArarbitrage.json","w+") as f:
        f.write(j)
    time.sleep(7)
    run()
run()