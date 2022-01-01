<?php include("header.php"); ?>
<div class="tableFixHead my-3">
    <table id="table" class="text-center content-table mx-auto table-striped">
        <thead id="arbitrage-head"></thead>
        <tbody id="arbitrage"></tbody>
    </table>
</div>
<script src="js/spatialv2.js"></script>

<script>
    function myFunction(e) {
        var x=$(e).parent().siblings().each(function(){
            $(this).toggleClass("invisible");
        })
        

        /*
        $("tbody tr").each(function () {
            $("td:eq(" + e + ")", this).toggleClass("invisible");
        })*/
    }
</script>

<?php include("footer.php"); ?>