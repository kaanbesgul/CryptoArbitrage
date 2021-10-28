<?php include("header.php"); ?>
<table id="table" class="content-table mx-auto">
    <thead id="arbitrage-head"></thead>
    <tbody id="arbitrage"></tbody>
</table>
<script src="spatial.js"></script>

<script>
    function hideshow(e){
        $("tbody tr").each(function(){
            $("td:eq("+e+")",this).toggleClass("invisible");
        })
    }
</script>
<?php include("footer.php"); ?>