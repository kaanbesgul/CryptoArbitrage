<footer>
    <div class="container-fluid bg-dark text-white text-center">
        <div class="row p-2">
            <div class="col-lg-6">
                For any issue you can mail <a href="#">uslandeli77@outlook.com</a> 
            </div>
            <div class="col-lg-6">
                <small>All prices taken by exchanges api but don't be sure 100% and always check price before the transaction</small>
            </div>
            <div class="col-lg-12">
                Copyright:Kaan Beşgül
            </div>
        </div>
    </div>
</footer>
<script src="scr.js"></script>

<script>
    function hideshow(e){
        $("tbody tr").each(function(){
            $("td:eq("+e+")",this).toggleClass("invisible");
        })
    }
</script>
</body>
</html>