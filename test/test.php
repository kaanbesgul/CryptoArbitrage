<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
  </script>
  <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
    integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous">
  </script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
  </script>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"
    integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="test.css">
  <title>Crypto Arbitrage</title>
</head>

<body>
  <nav class="navbar navbar-expand-lg bg-light navbarr">
    <a class="navbar-brand" href="main.php">CRYPTO ARBITRAGE</a>
    <button class="navbar-toggler bg-light" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="mx-lg-5 collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="main.php">HOME <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
            aria-haspopup="true" aria-expanded="false">
            ARBITRAGE
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="spatialArbitrage.php">SPATIAL ARBITRAGE</a>
            <a class="dropdown-item" href="triangularArbitrage2.php">TRIANGULAR ARBITRAGE</a>
          </div>
        <li class="nav-item">
          <a class="nav-link" href="generaltips.php">GENERAL INFORMATION</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="about-me.php">ABOUT ME</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="donate.php">DONATE AND REFERRAL LINKS</a>
        </li>
    </div>
  </nav>
  <div class="myclas">
  </div>


<div class="tableFixHead">
    <table id="table" class="content-table mx-auto table-striped">
        <thead id="arbitrage-head"></thead>
        <tbody id="arbitrage"></tbody>
    </table>
</div>
<script src="js/spatial.js"></script>

<script>
    function hideshow(e) {
        $("tbody tr").each(function () {
            $("td:eq(" + e + ")", this).toggleClass("invisible");
        })
    }
</script>

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
</body>
</html>