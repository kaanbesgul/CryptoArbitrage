$.ajax({
    url: "spatialArbitrage.json",
    dataType: "json",
    type: "get",
    cache: false,
    success: function (data) {
        var tablehead = document.getElementById("arbitrage-head");
        var tablebody = document.getElementById("arbitrage");
        

        var thead = "<tr class='table-head'><th class='nothing'>COIN/USDT</th>";
        var tbody = "";

        for (var i in data['AAX']){
            i=i.charAt(0).toUpperCase() + i.slice(1);
            thead+="<th class='_"+i+"'>"+i+"</th>"
        }
        for (var i in data){
            var tds=""
            for(var y in data['AAX']){
                y=y.charAt(0).toUpperCase() + y.slice(1);
                tds+="<td class='_"+y+"'></td>"
            }
            tbody+="<tr class='"+i+"'><td class='headcol bg-danger text-white'>"+i+"<button onclick='myFunction(this)' class='but'></button></td>"+tds+"</tr>"
        }
        tbody+="<tr class='profit'><td class='headcol bg-success text-white'>Profit</td>"+tds+"</tr>"
        tablebody.innerHTML = tbody;
        tablehead.innerHTML = thead;

        
    }
})

function run() {
    $.ajax({
        url: "spatialArbitrage.json",
        dataType: "json",
        type: "get",
        cache: false,
        success: function (data) {
            for (var _ in data) {
                for (var i in data[_]) {
                    y=i.charAt(0).toUpperCase() + i.slice(1);
                    var x = document.querySelector("." + _ + " " + "._" + y );
                    if (data[_][i] !=null) {
                        x.innerHTML = data[_][i];
                    } else {
                        x.innerHTML = "-";
                    }
                }
            }  
        }
    })
    $.ajax({
        url:"spatialArbitrage.json",
        dataType:"json",
        type:"get",
        cache: false,
        success: function(data){
            $(document).ready(function(){
                $('#arbitrage-head tr').children().not('.nothing').each(function(){
                    var className = $(this).attr("class");
                    var array=[];
                    $('#arbitrage tr').not('.invisible').not('.profit').each(function(index,element){
                        var x=$('.'+className,element);
                        var y=x.hasClass('invisible');
                        if(x.text() == '-' || y){}
                        else{
                            array.push(parseFloat(x.text()));
                        }
                    })
                    var max = Math.max(...array);
                    var min = Math.min(...array);

                    var profit = ((max - min) * 100) / min;

                    $('#arbitrage .profit .'+className).html("% " + profit.toFixed(3));

                    $('#arbitrage tr').not('.invisible').not('.profit').each(function(){
                        if (parseFloat($(this).find('.'+className).text()) == max) {
                            $(this).find('.'+className).addClass("bg-danger text-white");
                        } else if (parseFloat($(this).find('.'+className).text()) == min) {
                            $(this).find('.'+className).addClass("bg-success text-white");
                        } else {
                            $(this).find('.'+className).removeClass("bg-danger bg-success text-white");
                        }
                    });
                })
            })
        }
    })
    setTimeout(run, 5000);
}
run()
