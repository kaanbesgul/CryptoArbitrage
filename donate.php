<?php include("header.php") ?>
    <div class="container-fluid">
        <div class="row text-center donate">
        <div class="col-lg-12 my-2">
            <h1>For Donate</h1>
                <span>Bep20 and Erc20 Network</span>
                <span style="color:white" id="bep20">0x060450100cb6126d349a853ffb74c6fc0ae6ea04</span>
                <button class="float-right" onclick="myFunction('bep20')"><i class="fas fa-copy"></i></button>
            </div>
            <div class="col-lg-12 my-2">
                <span>Trc20 Network</span>
                <span style="color:white" id="trc">TVbBgmycHEJc8JgrYFsf1e2pHF9iLRMzQ7</span>
                <button class="float-right" onclick="myFunction('trc')"><i class="fas fa-copy"></i></button>
            </div>
            <div class="col-lg-12 my-2">
                <span>Solana Network</span>
                <span style="color:white" id="sol">E9jhYaEFi4UtzdJDFWx7BoV4THs97RxJFLieYQgjWnoH</span>
                <button class="float-right" onclick="myFunction('sol')"><i class="fas fa-copy"></i></button>
            </div>
            <div class="col-lg-12 my-2">
                <span>My Favourite Coin Iota Network</span>
                <span style="color:white" id="iota">iota1qpr8ryyn8ed7jwtnds8t4qgg8mrsd5yw385vykjqw5kfnu7qxxkkwrw8g4j</span>
                <button class="float-right" onclick="myFunction('iota')"><i class="fas fa-copy"></i></button>
            </div>
        </div>
        
        <div class="row ref">
            <div class="col-12 my-2 text-center">
                <img src="images/binance.png" alt=""> 
                <span>BINANCE</span>
                <a href="https://accounts.binance.com/tr/register?ref=52456728">https://accounts.binance.com/tr/register?ref=52456728</a>
            </div>
            <div class="col-12 my-2 text-center">
                <img src="images/coinbase.png" alt=""> 
                <span>COINBASE</span>
                <a href="https://coinbase.com/join/6Z8D8E?src=ios-link">https://coinbase.com/join/6Z8D8E?src=ios-link</a>
            </div>
            <div class="col-12 my-2 text-center">
                <img src="images/ftx.png" alt=""> 
                <span>FTX</span>
                <a href="https://ftx.com/#a=16311301">https://ftx.com/#a=16311301</a>
            </div>
            <div class="col-12 my-2 text-center">
                <img src="images/gate.png" alt=""> 
                <span>GATE</span>
                <a href="https://www.gate.io/signup/6702905">https://www.gate.io/signup/6702905</a>
            </div>
            <div class="col-12 my-2 text-center">
                <img src="images/huobi.png" alt=""> 
                <span>HUOBI</span>
                <a href="https://www.huobi.ge/tr-tr/topic/double-reward/?invite_code=tqd73223&t=1634505692681">https://www.huobi.ge/tr-tr/topic/double-reward/?invite_code=tqd73223&t=1634505692681</a>
            </div>
        </div>
    </div>

    <script>
        function myFunction(e) {
            const copyText = document.getElementById(e).textContent;
            navigator.clipboard.writeText(copyText);

        }
</script>
<?php include("footer.php") ?>