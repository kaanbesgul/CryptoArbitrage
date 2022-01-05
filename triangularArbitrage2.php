<?php include('header.php') ?>
<div class="my-5">
    <div class="bg-danger text-white my-3 p-4">
        <h2 class="text-center">BE CAREFUL</h2>
        <div>
            <ul>
                <li>All datas refresh in 10 seconds </li>
                <li>Always consider volumes when trading.</li>
                <li>Please think hard before you arbitrage, arbitrage may not be as easy as you think and you may lose money as a result.</li>            </ul>
        </div>
    </div>
</div>
<table id="BTCBNB" class="w-100 table-striped text-center">
    <thead id="arbitrage-head">
        <tr>
            <th class="mx-auto">BTC/BNB arbitrage</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(BNB/Coin)*(Coin/BTC)</th>
            <th class="mx-auto">BNB/BTC</th>
            <th class="mx-auto">% Profit</th>
            <th class="mx-auto">Description</th>
        </tr>
    </thead>
    <tbody id="BNBBTC-arbitrage"></tbody>
</table>

<table id="BTCETH" class="w-100 my-5 table-striped text-center">
    <thead>
        <tr>
            <th class="mx-auto">ETH/BTC arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BTC</th>
            <th class="mx-auto">BTC Volume</th>
            <th class="mx-auto">(ETH/Coin)*(Coin/BTC)</th>
            <th class="mx-auto">ETH/BTC</th>
            <th class="mx-auto">% Profit</th>
            <th class="mx-auto">Description</th>
        </tr>
    </thead>
    <tbody id="ETHBTC-arbitrage"></tbody>
</table>

<table id="ETHBNB" class="w-100 table-striped text-center">
    <thead>
        <tr>
            <th class="mx-auto">BNB/ETH arbitrage</th>
            <th class="mx-auto">Coin/ETH</th>
            <th class="mx-auto">ETH Volume</th>
            <th class="mx-auto">Coin/BNB</th>
            <th class="mx-auto">BNB Volume</th>
            <th class="mx-auto">(BNB/Coin)*(Coin/ETH)</th>
            <th class="mx-auto">BNB/ETH</th>
            <th class="mx-auto">% Profit</th>
            <th class="mx-auto">Description</th>
        </tr>
    </thead>
    <tbody id="BNBETH-arbitrage"></tbody>
</table>
<script src="js/triangular.js"></script>

<script>
    $('#BNBBTC-arbitrage tr').children().each(function(){
        console.log('helloki');
    })
</script>