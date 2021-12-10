<?php include('header.php') ?>
<div class="text-center my-5">
    If (BNB/Coin)*(Coin/BTC) coloumn's value is lower than BNB/BTC coloumn this mean you can buy BNB cheaper. <br>
    You need to buy BNB first,then from Coin/BNB pair buy Coin,after that from Coin/BTC pair sell coin to buy BTC

    <div class="bg-danger my-3">
        <h2>BE CAREFUL</h2>

        <div>
            -All datas refresh in 10 seconds
            -Profit show you the most profitable arbitrage most of time this can't be happen
        </div>
    </div>
    
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