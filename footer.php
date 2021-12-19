<footer class="bg-dark border-top pt-4 ">
    <div class="container-fluid  text-white text-center">
        <div class="row py-3">

            <a href="main.php" class="col-lg-2 offset-lg-1 border-right">Home</a>
            <a href="spatialArbitrage.php" class="col-lg-2 border-right">Spatial Arbitrage</a>
            <a href="triangularArbitrage.php" class="col-lg-2 border-right">Triangular Arbitrage</a>
            <a href="donate.php" class="col-lg-2 border-right">Donate and referral links</a>
            <a href="generaltips.php" class="col-lg-2 ">General information</a>
            
        </div>
        <div class="row justify-content-lg-center py-3">
            <a href="" class="col-lg-2 border-right">Privacy Policy</a>
            <a href="" class="col-lg-2 ">Terms Of Use</a>
        </div>

        <div class="row justify-content-lg-center py-3">
            <a href="about-me.php" class="col-lg-12">About Me</a>
        </div>
        
        <div class="row pt-4">
            <div class="col-lg-12 py-2">
                cryptokandela@yahoo.com <br> Copyright:Kaan Beşgül
            </div>
        </div>
    </div>
</footer>
<script>
    var tipButton = document.querySelector('.tip-button')
    tipButton.addEventListener('click', function() {
  if (typeof web3 === 'undefined') {
    return renderMessage('You need to install MetaMask to use this feature.  https://metamask.io')
  }

  var user_address = web3.eth.accounts[0]
  web3.eth.sendTransaction({
    to: 0x5B7bb2F5C81C933dA498a9A55268AEB51158bb89,
    from: user_address,
    value: web3.toWei('0.01', 'ether'),
  }, function (err, transactionHash) {
    if (err) return renderMessage('Oh no!: ' + err.message)

    // If you get a transactionHash, you can assume it was sent,
    // or if you want to guarantee it was received, you can poll
    // for that transaction to be mined first.
    renderMessage('Thanks!')
  })
})
</script>
</body>
</html>