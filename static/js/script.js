let callTicker
$(document).ready(function () {
    callTicker = function () {
        let ticker = $('#ticker').val()
        myFunction(ticker, true);
    }

    function myFunction(ticker, bool) {
        // let url_ = "https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=b6c4d69c188b8fda260bb4cc5b2474f8"
        let url_ = "https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=demo"
        $.ajax({
            url: url_,
            dataType: 'json',
            success: function (result) {
                if (bool) {
                    console.log(result);
                    console.log(result[0].symbol, result[0].price)
                    $("#ticker-result").text("Price:" + result[0].price)
                    $("#ticker-result-logo").attr("src", result[0].image).height(20)
                } else {
                    console.log(result);
                    console.log(result[0].symbol, result[0].price)
                    $("#stock-name").text(result[0].symbol)
                    $("#stock-price").text(result[0].price)
                    $("#stock-image").attr("src", result[0].image).height(20)
                    $("#stock-description").text(result[0].description)
                }


            }
        })
    }

    myFunction('AAPL', false);

    // function myFunction() {
    //     $('.difference').each(function (i, obj) {
    //
    //         if (parseInt(this.text(), 10) < 0) {
    //             console.log(this.text())
    //             this.style.color = "red";
    //         } else {
    //             console.log(this.text())
    //             this.style.color = "green";
    //         }
    //     });
    // }
});