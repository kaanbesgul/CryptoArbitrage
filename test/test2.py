import requests
import json
r = requests.get("https://ftx.com/api/markets/BTC/USDT/orderbook?depth=1")
if r.status_code == 200:
    site_json = json.loads(r.content)
    if site_json["success"] == True:
        print(round(float(site_json['result']['bids'][0][0]), 5))
else:
    print("olmadı")




