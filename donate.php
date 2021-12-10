<?php include("header.php") ?>
<div class="container-fluid">
    <div class="row text-center donate">
        <div class="col-lg-12 my-2">
            <h1>For Donate</h1>
            <span>Bep20 and Erc20 Network</span>
            <span style="color:white" id="bep20">0x060450100cb6126d349a853ffb74c6fc0ae6ea04</span>
            <div class="tooltips">
                <span class="tooltiptext">Copy to clipboard</span>
                <button onclick="javascript:myfunc(this)" onmouseout="javascript:outFunc(this)"><i class="fas fa-copy"></i></button>
            </div>

        </div>
        <div class="col-lg-12 my-2">
            <span>Trc20 Network</span>
            <span style="color:white" id="trc">TVbBgmycHEJc8JgrYFsf1e2pHF9iLRMzQ7</span>
            <div class="tooltips">
                <span class="tooltiptext">Copy to clipboard</span>
                <button onclick="javascript:myfunc(this)" onmouseout="javascript:outFunc(this)"><i class="fas fa-copy"></i></button>
            </div>
        </div>
        <div class="col-lg-12 my-2">
            <span>Solana Network</span>
            <span style="color:white" id="sol">E9jhYaEFi4UtzdJDFWx7BoV4THs97RxJFLieYQgjWnoH</span>
            <div class="tooltips">
                <span class="tooltiptext">Copy to clipboard</span>
                <button onclick="javascript:myfunc(this)" onmouseout="javascript:outFunc(this)"><i class="fas fa-copy"></i></button>
            </div>
        </div>
        <div class="col-lg-12 my-2">
            <span>My Favourite Coin Iota Network</span>
            <span style="color:white" id="iota">iota1qpr8ryyn8ed7jwtnds8t4qgg8mrsd5yw385vykjqw5kfnu7qxxkkwrw8g4j</span>
            <div class="tooltips">
                <span class="tooltiptext">Copy to clipboard</span>
                <button onclick="javascript:myfunc(this)" onmouseout="javascript:outFunc(this)"><i class="fas fa-copy"></i></button>
            </div>
        </div>
    </div>

    <div class="row ref">
        <div class="col-12 my-5 py-5 text-center">
            <img src="images/binance.png" alt="">
            <span>BINANCE</span>
            <a
                href="https://accounts.binance.com/tr/register?ref=52456728">https://accounts.binance.com/tr/register?ref=52456728</a>
        </div>
    </div>
</div>

<script>
    function myfunc(e) {
            var copyElement= e.parentElement.previousElementSibling.innerHTML;
            navigator.clipboard.writeText(copyElement);
            e.previousElementSibling.innerHTML="Copied";
        }

        function outFunc(e){
            e.previousElementSibling.innerHTML="Copy to clipboard";
        }

    
</script>
<?php include("footer.php") ?>