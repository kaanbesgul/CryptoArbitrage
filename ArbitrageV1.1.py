import json
import requests
import threading
from collections import OrderedDict


"""Bittrex=https://global.bittrex.com/v3/markets/BTC-USDT/orderbook?depth=1
   Crypto.com=https://api.crypto.com/v2/public/get-ticker?instrument_name=BTC_USDT
   Okex=https://www.okex.com/priapi/v5/market//mult-tickers?t=1635659891209&instIds=BTC-USDT
   Wazirx=https://x.wazirx.com/api/v2/trades?market=btcusdt&limit=1
   Mexc=https://www.mexc.com/api/platform/spot/market/symbol?symbol=BTC_USDT"""

def coinmarket(number):
    marketc = requests.get(
        "https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,untracked&exchangeAux=is_active,status&cryptoAux=is_active,status&start=1&limit=10000")

    marketcap = json.loads(marketc.content)

    stable = ["USDT", "USDC", "BUSD", "DAI", "UST", "TUSD", "USDP", "FEI", "HUSD", "WBTC", "BTCB", ]
    global coins
    coins={}

    for i in range(0, number):
        if marketcap['data']['cryptoCurrencyMap'][i]['symbol'] in stable:
            pass
        else:
            coins[marketcap['data']['cryptoCurrencyMap'][i]['symbol']] = marketcap['data']['cryptoCurrencyMap'][i]['slug']
    return coins
coinmarket(5)


keyorder = []
for i in coins.values():
    keyorder.append(i)

binance = []
bitfinex = []
bithumb = []
bitstampt=[]
bybit=[]
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
    bitstampt.append(huobkrak)
    bybit.append(bin)
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
    "bitstampt":
        {"url":"https://www.bitstamp.net/api-internal/price-history/{}",
         "currency":bitstampt},
    "bybit":
        {"url":"https://api2.bybit.com/spot/api/quote/v1/multi/kline?symbol={}&exchangeId=301&interval=1h&limit=1",
         "currency":bybit},
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
bitstamptS={}
bybitS={}
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
            if 'bids' in site_json:
                binanceS[currency] = float(site_json['bids'][0][0])
            else:
                binanceS[currency] = None
        else:
            binanceS[currency] = None
    elif url == exchanges['bitfinex']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json) !=0:
                bitfinexS[currency] = float(site_json[0][1])

            else:
                bitfinexS[currency] = None
        else:
            bitfinexS[currency] = None
    elif url == exchanges['bithumb']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['info']) > 0:
                bithumbS[currency] = float(site_json['info'][0]['c'])
            else:
                bithumbS[currency] = None
        else:
            bithumbS[currency] = None
    elif url == exchanges['bitstampt']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            bitstamptS[currency]=site_json['data']['latest']['price']
        else:
            bitstamptS[currency] = None
    elif url == exchanges['bybit']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) !=0:
                bybitS[currency] = float(site_json['result'][currency][0]['c'])
            else:
                bybitS[currency] = None
        else:
            bybitS[currency] = None
    elif url == exchanges['coinbase']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'errors' in site_json:
                coinbaseS[currency] = None
            else:
                coinbaseS[currency] = round(float(site_json['data']['prices']['latest']), 5)

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
            if 'last' in site_json:
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
    coinmarket(50)
    for _ in exchange:
        threadd(exchange[_]['url'], exchange[_]['currency'])
    prices['binance'] = binanceS
    prices['bitfinex'] = bitfinexS
    prices['bithumb'] = bithumbS
    prices['bitstampt']=bitstamptS
    prices['bybit'] = bybitS
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