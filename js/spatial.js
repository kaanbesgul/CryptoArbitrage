$.ajax(
    {
        url:"price.json",
        dataType:"json",
        type:"get",
        cache:false,success:function(data){
            var tablehead=document.getElementById("arbitrage-head");
            var tablebody=document.getElementById("arbitrage");
            
            var thead="<tr class='table-head'><th>All pairs in USDT</th>";
            var tbody="";
            var counter=1;
            for(var i in data){
                var i = i.toUpperCase();
                thead+="<th><span>"+i+"</span><button onclick='hideshow("+counter+")'>Hide/Show</button></th>";
                counter++;
            }
            thead+="<th><span>% Profit</span></th></tr>";
            for(var i in data['AAX']){
                var i2 = i.charAt(0).toUpperCase() + i.slice(1);
                tbody+="<tr class='"+i+"'><td class='coin'>"+i2+"</td>";

                for(ii in data){
                    tbody+="<td class='"+ii+"'></td>";
                }
                tbody+="<td class='profit'></td></tr>";                    
            }
            tablebody.innerHTML=tbody;
            tablehead.innerHTML=thead;
        }
    }
)
        
function run(){
    $.ajax(
{
    url:"price.json",
    dataType:"json",
    type:"get",
    cache:false,
    success:function(data){
        for(var _ in data){
            for(var i in data[_]){
                var x=document.querySelector("."+i+" "+"."+_);
                if(data[_][i]){
                    x.innerHTML=data[_][i]
                }else{
                    x.innerHTML="-";
                }                         
            }     
        }
    }       
})

$(document).ready(function(){
    $("tr").not(".table-head").each(function(index,element){
    var array=[];    
    $("td",element).not(".profit").not(".coin").not(".invisible").each(function(){
        var x =$(this).text();
        if(x== "-"){

        }else{
            array.push(parseFloat(x))    
        }   
    });
    var max =Math.max(...array);
    console.log(array.indexOf(max))
    var min =Math.min(...array);
    var profit=((max-min)*100)/min;
    $(element).find(".profit").html("% "+profit.toFixed(3));     
})})
setTimeout(run,2000);
}
run();            