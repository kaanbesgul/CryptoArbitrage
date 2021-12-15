<?php include('header.php') ?>
<div class="text-center my-5">
    <div class="bg-danger my-3 p-2">
        <h2>BE CAREFUL</h2>
        <div>
            -All datas refresh in 10 seconds <br>
            -The profit value in the table is valid for the values in the table, but most of the time, the investor may not be able to trade for this price because these values are full in the order book. Therefore, your profit will decrease accordingly. <br>
            -Always consider volumes when trading <br>
            -The profit rate seems to be very high in coins with a very small value against bitcoin, but it is very difficult to buy these coins at those prices.<br>
            -The arbitrage technique I used is as follows:
I have Bnb in my hand and if I have bitcoin after making the sales, I will look for arbitrage suitable for Bitcoin and I will have converted my money back to BNB by arbitrage and avoid paying extra commissions. <br>
            -Please think hard before you arbitrage, arbitrage may not be as easy as you think and you may lose money as a result. <br>
            -What is written here is only data and a few tips necessary for you not to lose money, and I cannot be held responsible for any loss. For more, visit the Terms of Use page.
        </div>
    </div>
    If (BNB/Coin)*(Coin/BTC) coloumn's value is lower than BNB/BTC coloumn this mean you can buy BNB cheaper. <br>
    You need to buy BNB first,then from Coin/BNB pair buy Coin,after that from Coin/BTC pair sell coin to buy BTC
</div>
<table id="BTCBNB" class="w-100 table-striped">
    <thead id="arbitrage-head">
        <tr class="text-center">
            <th class="mx-auto">BTC/BNB arbitrage</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(BNB/Coin)*(Coin/BTC)</th>
            <th class="mx-auto">BNB/BTC</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="BNBBTC-arbitrage"></tbody>
</table>

<table id="BTCETH" class="w-100 my-5">
    <thead>
        <tr class="text-center">
            <th class="mx-auto">ETH/BTC arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(ETH/Coin)*(Coin/BTC)</th>
            <th class="mx-auto">ETH/BTC</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="ETHBTC-arbitrage"></tbody>
</table>

<table id="ETHBNB" class="w-100">
    <thead>
        <tr class="text-center">
            <th class="mx-auto">BNB/ETH arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">(BNB/Coin)*(Coin/ETH)</th>
            <th class="mx-auto">BNB/ETH</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="BNBETH-arbitrage"></tbody>
</table>
<script src="js/triangular.js"></script>