import json
import requests
import threading
from collections import OrderedDict

# add coin here symbol:name
coins = {
    "BTC":"bitcoin",
    "ETH":"ethereum"

}

keyorder = []
for i in coins.values():
    keyorder.append(i)


ftx=[]


# add coins without coinbase to arrays
for i in coins.keys():
    ftxi=i+"/USDT"


    ftx.append(ftxi)


exchanges = {
    "ftx":
        {"url":"https://ftx.com/api/markets/{}/orderbook?depth=1",
         "currency": ftx}
    }

ftxS={}


prices = {}


def checkprice(url, currency):
    if url == exchanges['ftx']['url']:
        r = requests.get(url.format(currency))
        if r.status_code == 200:
            site_json = json.loads(r.content)
            if site_json['success']== True:
                ftxS[currency] = round(float(site_json['result']['bids'][0][0]), 5)
            else:
                ftxS[currency]=None
        else:
            ftxS[currency] = None
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

    prices['ftx'] = ftxS

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