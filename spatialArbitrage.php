<?php include("header.php"); ?>
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

<?php include("footer.php"); ?>