function run(){
    $.ajax(
        {
            url:"triangulArarbitrage.json",
            dataType:"json",
            type:"get",
            cache:false,
            success:function(data){
                var BNBBTCtablebody=document.getElementById("BNBBTC-arbitrage");
                var BNBETHtablebody=document.getElementById("BNBETH-arbitrage");
                var ETHBTCtablebody=document.getElementById("ETHBTC-arbitrage");
                var text="";
    
                for(var i in data['BTCBNB']['BTC']){
                    var myarr=[]
                    myarr.push(parseFloat(((data['BTCBNB']['BTC'][i]['price'])*1/(data['BTCBNB']['BNB'][i]['price'])).toFixed(6)))
                    myarr.push(data['BNBBTC'])
    
                    var minn=Math.min(...myarr);
                    var maxx=Math.max(...myarr);
                    
                    var profit=(((maxx-minn)/minn)*100).toFixed(3)

                    var text2='';
                    if(data['BNBBTC'] > parseFloat(((data['BTCBNB']['BTC'][i]['price'])*1/(data['BTCBNB']['BNB'][i]['price'])).toFixed(6))){
                        text2+="BTC -> "+i+" -> BNB";
                    }
                    else{
                        text2+="BNB -> "+i+" -> BTC";
                    }

                    text+="<tr><td>"+i+"</td><td>"+data['BTCBNB']['BNB'][i]['price']+"</td><td>"+data['BTCBNB']['BNB'][i]['volume']+"</td><td>"+data['BTCBNB']['BTC'][i]['price']+"</td><td>"+data['BTCBNB']['BTC'][i]['volume']+"</td><td>"+((data['BTCBNB']['BTC'][i]['price'])*1/(data['BTCBNB']['BNB'][i]['price'])).toFixed(6)+"</td><td>"+data['BNBBTC']+"</td><td>"+profit+"</td><td>"+text2+"</td></tr>"
                }
                BNBBTCtablebody.innerHTML=text;
    
                
    
                var text="";
    
                for(var i in data['BTCETH']['BTC']){
                    var myarr=[]
                    myarr.push(parseFloat(((data['BTCETH']['BTC'][i]['price'])*1/(data['BTCETH']['ETH'][i]['price'])).toFixed(6)))
                    myarr.push(data['ETHBTC'])
    
                    var minn=Math.min(...myarr);
                    var maxx=Math.max(...myarr);
                    
                    var profit=(((maxx-minn)/minn)*100).toFixed(3)

                    var text2='';
                    if(data['ETHBTC'] > parseFloat(((data['BTCETH']['BTC'][i]['price'])*1/(data['BTCETH']['ETH'][i]['price'])).toFixed(6))){
                        text2+="BTC -> "+i+" -> ETH";
                    }
                    else{
                        text2+="ETH -> "+i+" -> BTC";
                    }
                    
                    text+="<tr><td>"+i+"</td><td>"+data['BTCETH']['ETH'][i]['price']+"</td><td>"+data['BTCETH']['ETH'][i]['volume']+"</td><td>"+data['BTCETH']['BTC'][i]['price']+"</td><td>"+data['BTCETH']['BTC'][i]['volume']+"</td><td>"+((data['BTCETH']['BTC'][i]['price'])*1/(data['BTCETH']['ETH'][i]['price'])).toFixed(6)+"</td><td>"+data['ETHBTC']+"</td><td>"+profit+"</td><td>"+text2+"</td></tr>";
                }
                ETHBTCtablebody.innerHTML=text;

                var text="";
    
                for(var i in data['ETHBNB']['ETH']){
                    var myarr=[]
                    myarr.push(parseFloat(((data['ETHBNB']['ETH'][i]['price'])*1/(data['ETHBNB']['BNB'][i]['price'])).toFixed(6)))
                    myarr.push(data['BNBETH'])
    
                    var minn=Math.min(...myarr);
                    var maxx=Math.max(...myarr);
                    
                    var profit=(((maxx-minn)/minn)*100).toFixed(3)

                    var text2='';
                    if(data['BNBETH'] > parseFloat(((data['ETHBNB']['ETH'][i]['price'])*1/(data['ETHBNB']['BNB'][i]['price'])).toFixed(6))){
                        text2+="ETH -> "+i+" -> BNB";
                    }
                    else{
                        text2+="BNB -> "+i+" -> ETH";
                    }
                    text+="<tr><td>"+i+"</td><td>"+data['ETHBNB']['ETH'][i]['price']+"</td><td>"+data['ETHBNB']['ETH'][i]['volume']+"</td><td>"+data['ETHBNB']['BNB'][i]['price']+"</td><td>"+data['ETHBNB']['BNB'][i]['volume']+"</td><td>"+((data['ETHBNB']['ETH'][i]['price'])*1/(data['ETHBNB']['BNB'][i]['price'])).toFixed(6)+"</td><td>"+data['BNBETH']+"</td><td>"+profit+"</td><td>"+text2+"</td></tr>";
                }
                BNBETHtablebody.innerHTML=text;
            }
            
        }
    )
    setTimeout(run,5000);       
}
run()