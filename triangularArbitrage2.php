<?php include('header.php') ?>
<table id="table" class="w-100">
    <thead id="arbitrage-head">
        <tr>
            <th class="mx-auto">BTC/BNB arbitrage</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(BTC/Coin)*(Coin/BNB)</th>
            <th class="mx-auto">BNB/BTC</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="BNBBTC-arbitrage"></tbody>
</table>

<table class="w-100 my-5">
    <thead>
        <tr>
            <th class="mx-auto">BTC/ETH arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(BTC/Coin)*(Coin/ETH)</th>
            <th class="mx-auto">BTC/ETH</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="ETHBTC-arbitrage"></tbody>
</table>

<table class="w-100">
    <thead>
        <tr>
            <th class="mx-auto">ETH/BNB arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">(ETH/Coin)*(Coin/BNB)</th>
            <th class="mx-auto">ETH/BNB</th>
            <th class="mx-auto">% Profit</th>
        </tr>
    </thead>
    <tbody id="BNBETH-arbitrage"></tbody>
</table>
<script src="js/triangular.js"></script>