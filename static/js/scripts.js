$(document).ready(function () {
    var form = $('#ordering');
    form.on('submit', function (e) {
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price");
        var product_discount = submit_btn.data("product_discount");

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#ordering [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                if (data.products_total_number) {
                    $("#basket_total_nmb").text("(" + data.products_total_number + ")");
                    //console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li>' + v.item_product_name + " * " + v.number + " pcs = " + v.price_per_item * v.number + " $ " + '</li>');
                    })
                }
            },
            error: function () {
                console.log("error");
            }


        });


    });


    document.getElementsByClassName('product_in_basket_number','form-control').onkeypress=function(e){
        return !(/[А-Яа-яA-Za-z ]/.test(String.fromCharCode(e.charCode)));
    };

    function showBasket() {
        $('.basket-items').toggleClass('hidden');
    }


    //$(".basket").on('click',function(e){
    //    e.preventDefault();
    //    showBasket()
    //});

    $(".basket").mouseover(function (e) {
        e.preventDefault();
        showBasket()
    });
    $(".basket").mouseout(function (e) {
        e.preventDefault();
        showBasket()
    });

    $(document).on('click', '.delete-item', function () {
        $(this).closest('li').remove();
    })

//total_order_amount
    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total_product_amount_in_basket').each(function () {
            total_order_amount =total_order_amount+ parseFloat($(this).text());
        });
       $("#total_order_amount").text(total_order_amount.toFixed(2) + " $");
    };

    $(document).on('change', '.product_in_basket_number', function(){
       var current_number=$(this).val();

        var current_tr=$(this).closest('tr');
        var current_price=parseFloat(current_tr.find('.product_price').text()).toFixed(2);
        var total_amount=parseFloat(current_number*current_price).toFixed(2);
        current_tr.find('.total_product_amount_in_basket').text(parseFloat(total_amount).toFixed(2) + " $");
        calculatingBasketAmount();
    });

    calculatingBasketAmount();



    //slider
   var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}
    x[myIndex-1].style.display = "block";
    setTimeout(carousel, 3600);
}



});