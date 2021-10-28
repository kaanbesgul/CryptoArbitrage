import json
import requests
import threading
from collections import OrderedDict


# add coin here symbol:name
coins = {
    "BTC":"bitcoin",
    "ETH":"ethereum",
    "BNB":"binancecoin",
    "ADA":"cardano",
    "SOL":"solana",
    "XRP":"ripple",
    "DOT":"polkadot",
    "DOGE":"dogecoin",
    "SHIB":"shibainu",
    "LUNA":"terra",
    "UNI":"uniswap",
    "AVAX":"avalanche",    
    "LINK":"chainlink",
    "LTC":"litecoin",
    "ALGO":"algorand",
    "MATIC":"polygon",
    "BCH":"bitcoincash",
    "VET":"vechain",
    "XLM":"stellar",
    "ATOM":"cosmos",
    "ICP":"internetcomputer",
    "FTM":"fantom",
    "AXS":"axieinfinity",
    "FTT":"ftxtoken",
    "FIL":"filecoin",
    "TRX":"tron",
    "THETA":"theta",
    "ETC":"ethereumclassic",
    "NEAR":"nearprotocol",
    "HBAR":"hedera",
    "XTZ":"tezos",
    "EGLD":"elrond",
    "XMR":"monero",
    "GRT":"thegraph",
    "CAKE":"pancakeswap",
    "EOS":"eos",
    "AAVE":"aave",
    "KLAY":"klayton",
    "FLOW":"flow",
    "IOTA":"iota",
    "QNT":"quant"
}

keyorder = []
for i in coins.values():
    keyorder.append(i)

binance = []
bitfinex = []
bithumb = []
coinbase = []
ftx=[]
gateio=[]
huobi = []
kucoin = []

# add coins without coinbase to arrays
for i in coins.keys():
    bin = i + "USDT"
    bitf = "t" + i + "USD"
    bithkuco = i + "-USDT"
    ftxi=i+"/USDT"
    gate=i.lower()+"_usdt"
    huobkrak = i.lower() + "usdt"

    binance.append(bin)
    bitfinex.append(bitf)
    bithumb.append(bithkuco)
    ftx.append(ftxi)
    gateio.append(gate)
    huobi.append(huobkrak)
    kucoin.append(bithkuco)

# add coins to coinbase
for i in coins.values():
    coinbase.append(i)

exchanges = {
    "binance":
        {"url": "https://www.binance.com/api/v3/depth?symbol={}&limit=1",
         "currency": binance},
    "bitfinex":
        {"url": "https://api-pub.bitfinex.com/v2/tickers?symbols={}",
         "currency": bitfinex},
    "bithumb":
        {"url": "https://global-api.bithumb.pro/market/data/ticker?symbol={}&type=CUSTOM&limit=1&sort=DESC",
         "currency": bithumb},
    "coinbase":
        {"url": "https://www.coinbase.com/api/v2/assets/prices/{}?base=USDT",
         "currency": coinbase},
    "ftx":
        {"url":"https://ftx.com/api/markets/{}/orderbook?depth=1",
         "currency": ftx},
    "gate":
        {"url":"https://data.gateapi.io/api2/1/ticker/{}",
         "currency": gateio},
    "huobi":
        {"url": "https://api.huobi.pro/market/depth?symbol={}&type=step1",
         "currency": huobi},
    "kucoin":
        {"url": "https://trade.kucoin.com/_api/order-book/orderbook/level2?symbol={}&limit=1&lang=tr_TR",
         "currency": kucoin}}

binanceS = {}
bitfinexS = {}
bithumbS = {}
coinbaseS = {}
ftxS={}
gateS={}
huobiS = {}
kucoinS = {}

prices = {}


def checkprice(url, currency):
    if url == exchanges['binance']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json:
                binanceS[currency] = float(site_json['bids'][0][0])
            else:
                binanceS[currency] = None
        else:
            binanceS[currency] = None
    elif url == exchanges['bitfinex']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json:
                bitfinexS[currency] = float(site_json[0][1])

            else:
                bitfinexS[currency] = None
        else:
            bitfinexS[currency] = None
    elif url == exchanges['bithumb']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['info']:
                bithumbS[currency] = float(site_json['info'][0]['c'])
            else:
                bithumbS[currency] = None
        else:
            bithumbS[currency] = None
    elif url == exchanges['coinbase']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json:
                coinbaseS[currency] = round(float(site_json['data']['prices']['latest']), 5)
            else:
                coinbaseS[currency] = None
        else:
            coinbaseS[currency] = None
    elif url == exchanges['ftx']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['success'] == True:
                ftxS[currency] = round(float(site_json['result']['bids'][0][0]), 5)
            else:
                ftxS[currency] = None
        else:
            ftxS[currency] = None
    elif url == exchanges['gate']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['last']:
                gateS[currency] = round(float(site_json['last']), 5)
            else:
                gateS[currency]=None
        else:
            gateS[currency] = None
    elif url == exchanges['huobi']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['status'] == 'ok':
                huobiS[currency] = float(site_json['tick']['bids'][0][0])
            else:
                huobiS[currency] = None
        else:
            huobiS[currency] = None
    elif url == exchanges['kucoin']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['data']['bids'] == None:
                kucoinS[currency] = None
            else:
                kucoinS[currency] = float(site_json['data']['bids'][0][0])
    else:
        print("wrong url")


def threadd(url, list):
    threads = []
    for _ in range(len(list)):
        t = threading.Thread(target=checkprice, args=[url, list[_]])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def readd():
    with open("price.json", "r") as f:
        t = f.read()
        print(t)


def run(exchange):
    for _ in exchange:
        threadd(exchange[_]['url'], exchange[_]['currency'])
    prices['binance'] = binanceS
    prices['bitfinex'] = bitfinexS
    prices['bithumb'] = bithumbS
    prices['coinbase'] = coinbaseS
    prices['ftx']=ftxS
    prices['gate']=gateS
    prices['huobi'] = huobiS
    prices['kucoin'] = kucoinS

    for i in prices:
        for y in list(prices[i]):
            for z in coins.keys():
                if z in y.upper() and i != "coinbase":
                    prices[i][coins[z]] = prices[i][y]
                    del prices[i][y]

    dict2 = {}

    for y in prices:
        dene = sorted(prices[y].items(), key=lambda i: keyorder.index(i[0]))
        odict = OrderedDict(dene)
        dict2[y] = odict

    j = json.dumps(dict2)
    with open("price.json", "w+") as f:
        f.write(j)
    readd()
    run(exchange)

run(exchanges)