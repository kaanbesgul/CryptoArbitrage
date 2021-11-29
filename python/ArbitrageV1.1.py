import json
import requests
import threading
from collections import OrderedDict

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
coinmarket(50)


keyorder = []
for i in coins.values():
    keyorder.append(i)

binance = []
bitfinex = []
bithumb = []
bitstampt=[]
bittrex=[]
bybit=[]
cryptocom=[]
coinbase = []
ftx=[]
gateio=[]
huobi = []
kucoin = []
mexc=[]
okex=[]
wazirx=[]

# add coins without coinbase to arrays
for i in coins.keys():
    bin = i + "USDT"
    bitf = "t" + i + "USD"
    bithkuco = i + "-USDT"
    cryptocomm=i+"_USDT"
    ftxi=i+"/USDT"
    gate=i.lower()+"_usdt"
    huobkrak = i.lower() + "usdt"

    binance.append(bin)
    bitfinex.append(bitf)
    bithumb.append(bithkuco)
    bitstampt.append(huobkrak)
    bittrex.append(bithkuco)
    bybit.append(bin)
    cryptocom.append(cryptocomm)
    ftx.append(ftxi)
    gateio.append(gate)
    huobi.append(huobkrak)
    kucoin.append(bithkuco)
    mexc.append(cryptocomm)
    okex.append(bithkuco)
    wazirx.append(huobkrak)

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
    "bittrex":
        {"url":"https://global.bittrex.com/v3/markets/{}/orderbook?depth=1",
         "currency":bittrex},
    "bybit":
        {"url":"https://api2.bybit.com/spot/api/quote/v1/multi/kline?symbol={}&exchangeId=301&interval=1h&limit=1",
         "currency":bybit},
    "cryptocom":
        {"url":"https://api.crypto.com/v2/public/get-ticker?instrument_name={}",
         "currency":cryptocom},
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
         "currency": kucoin},
    "mexc":
        {"url":"https://www.mexc.com/api/platform/spot/market/symbol?symbol={}",
         "currency":mexc},
    "okex":
        {"url":"https://www.okex.com/priapi/v5/market//mult-tickers?t=1635659891209&instIds={}",
         "currency":okex},
    "wazirx":
        {"url":"https://x.wazirx.com/api/v2/trades?market={}&limit=1",
         "currency":wazirx}}

binanceS = {}
bitfinexS = {}
bithumbS = {}
bitstamptS={}
bittrexS={}
bybitS={}
cryptocomS={}
coinbaseS = {}
ftxS={}
gateS={}
huobiS = {}
kucoinS = {}
mexcS={}
okexS={}
wazirxS={}

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
            bitstamptS[currency]=float(site_json['data']['latest']['price'])
        else:
            bitstamptS[currency] = None
    elif url == exchanges['bittrex']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'bid' in site_json:
                bittrexS[currency] = float(site_json['bid'][0]['rate'])
            else:
                bittrexS[currency] = None
        else:
            bittrexS[currency] = None
    elif url == exchanges['bybit']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']) > 0 :
                if len(site_json['result'][currency]) > 0 :
                    bybitS[currency] = float(site_json['result'][currency][0]['c'])
                else:
                    bybitS[currency] = None
            else:
                bybitS[currency] = None
        else:
            bybitS[currency] = None
    elif url == exchanges['cryptocom']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['result']['data']) !=0:
                cryptocomS[currency] = float(site_json['result']['data']['b'])
            else:
                cryptocomS[currency] = None
        else:
            cryptocomS[currency] = None
    elif url == exchanges['coinbase']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'errors' in site_json:
                coinbaseS[currency] = None
            else:
                coinbaseS[currency] = round(float(site_json['data']['prices']['latest']), 7)

        else:
            coinbaseS[currency] = None
    elif url == exchanges['ftx']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['success'] == True:
                ftxS[currency] = round(float(site_json['result']['bids'][0][0]), 7)
            else:
                ftxS[currency] = None
        else:
            ftxS[currency] = None
    elif url == exchanges['gate']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'last' in site_json:
                gateS[currency] = round(float(site_json['last']), 7)
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
            kucoinS[currency] = None
    elif url == exchanges['mexc']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if 'data' in site_json:
                mexcS[currency] = site_json['data']['c']
            else:
                mexcS[currency] = None
        else:
            mexcS[currency] = None
    elif url == exchanges['okex']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if len(site_json['data']) !=0:
                okexS[currency] = float(site_json['data'][0]['last'])
            else:
                okexS[currency] = None
        else:
            okexS[currency] = None
    elif url == exchanges['wazirx']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if type(site_json) is list:
                wazirxS[currency] = float(site_json[0]['price'])
            else:
                wazirxS[currency] = None
        else:
            wazirxS[currency] = None
    else:
        print("wrong url")


def threadd(exchange):
    threads = []
    for i in exchange:
        for _ in exchange[i]['currency']:
            t = threading.Thread(target=checkprice, args=[exchange[i]['url'],_])
            t.start()
            threads.append(t)

    for thread in threads:
        thread.join()


def readd():
    with open("../price.json", "r") as f:
        t = f.read()
        print(t)


def run(exchange):
    threadd(exchange)
    prices['binance'] = binanceS
    prices['bitfinex'] = bitfinexS
    prices['bithumb'] = bithumbS
    prices['bitstampt']=bitstamptS
    prices['bittrex']=bittrexS
    prices['bybit'] = bybitS
    prices['cryptocom']=cryptocomS
    prices['coinbase'] = coinbaseS
    prices['ftx']=ftxS
    prices['gate']=gateS
    prices['huobi'] = huobiS
    prices['kucoin'] = kucoinS
    prices['mexc']=mexcS
    prices['okex']=okexS
    prices['wazirx']=wazirxS

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
    with open("../price.json", "w+") as f:
        f.write(j)
    readd()
    run(exchange)

run(exchanges)