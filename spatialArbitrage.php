<?php include("header.php"); ?>
<div class="tableFixHead my-3">
    <table id="table" class="text-center content-table mx-auto table-striped">
        <thead id="arbitrage-head"></thead>
        <tbody id="arbitrage"></tbody>
    </table>
</div>
<script src="js/spatial.js"></script>

<script>
    function myFunction(e) {
        $(e).toggleClass('bg-dark');

        var x=$(e).parent().siblings().each(function(){
            $(this).toggleClass("invisible");
        })
    }
</script>

<?php include("footer.php"); ?>