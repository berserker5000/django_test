$(document).ready(function(){
   var form=$('#ordering');
    //console.log(form);
    form.on('submit',function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id= submit_btn.data("product_id");
        var product_name=submit_btn.data("product_name");
        var product_price=submit_btn.data("product_price");
        var product_discount = submit_btn.data("product_discount");

        var data={};
        data.product_id=product_id;
        data.nmb=nmb;
        var csrf_token=$('#ordering [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url=form.attr('action');

        console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success:function(data){
                console.log("OK");
                console.log(data.products_total_number);
                if (data.products_total_number){
                    $("#basket_total_nmb").text("("+data.products_total_number+")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products,function(k,v){
                        $('.basket-items ul').append('<li>'+ v.item_product_name+" * "+ v.number+" pcs = "+ v.price_per_item* v.number+" $ "+'</li>');
                        })
                }
            },
            error:function(){
                console.log("error");
            }


        });






    });

    function showBasket(){
         $('.basket-items').toggleClass('hidden');
    }


    $(".basket").on('click',function(e){
        e.preventDefault();
        showBasket()
    });

    $(".basket").mouseover(function(e){
        e.preventDefault();
        showBasket()
    });
    $(".basket").mouseout(function(e){
        e.preventDefault();
        showBasket()
    });

    $(document).on('click','.delete-item',function(){
        $(this).closest('li').remove();
    })
});