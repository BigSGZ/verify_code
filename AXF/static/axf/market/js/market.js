$(function () {
    $("#all_type").click(function () {
        console.log('全部类型');
        $("#all_type_container").show();
        $(this).find("span").find("span").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
        $("#sort_rule_container").slideUp();
        $("#sort_rule").find("span").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })
    $("#all_type_container").click(function () {
        $(this).slideUp();
        $("#all_type").find("span").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })
    $('#sort_rule').click(function () {
        console.log('排序规则');
        $("#sort_rule_container").show();
        $(this).find("span").find("span").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up")
        $("#all_type_container").slideUp();
        $("#all_type").find("span").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })
    $("#sort_rule_container").click(function () {
        $(this).slideUp();
        $("#sort_rule").find("span").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down")
    })
    $(".addshopping").click(function () {
        //aatr 可以获取任意属性，prop只能获取内置属性
        var $addshopping=$(this);
        // console.log($addshopping.prop('class'));
        // console.log($addshopping.attr('goodsid'));
        var goodsid=$addshopping.attr('goodsid');
        console.log(goodsid);
        $.getJSON('/app/addtocart/',{'goodsid':goodsid},function (data) {
            console.log(data);
            if(data['status']=='200'){
                var goods_num=data['goods_num'];
                $addshopping.prev().html(goods_num)

            }else if(data['status']=='302'){
                window.open('/app/userlogin',target='_self')
            }

        })


    })
    $(".subshopping").click(function () {
        
    })
})
