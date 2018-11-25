$(function(){
//隐藏二级菜单
	function second(lar,sma){

		lar.mouseenter(function(){
			sma.animate({opacity: 'show'});
		})
//		sma.mouseenter(function(){
//			sma.animate({opacity: 'show'});
//		})
		sma.mouseleave(function(){
			sma.animate({opacity: 'hide'});
		})
//		lar.mouseleave(function(){
//			sma.animate({opacity: 'hide'});
//		})
	}
	function second1(lar,sma){
		
		lar.mouseenter(function(){
			sma.animate({opacity: 'show'});
		})
//		sma.mouseenter(function(){
//			sma.animate({opacity: 'show'});
//		})
		sma.mouseleave(function(){
			sma.animate({opacity: 'hide'});
		})
//		lar.mouseleave(function(){
//			sma.css({"display":"none"});
//		})
	}
//扫码
	second($("#saoma11"),$("#headerApp_m"));

	//购物袋
	second1( $("#shop"),$("#headershop"));


//版心图:鼠标移入,动态左移
	$("#box1_btn li").hover(function(){
			$(this).addClass("relative");
			$(this).find("img").addClass("absolute").stop(true).animate({"left":"20"},200);
		},
		function(){
			$(this).find("img").addClass("absolute").stop(true).animate({"left":"0"},200);
		}
	)

    // total()

	//计算购物车商品数量和总金额
    // function total(){
	//     var $priceall = 0
    //     var $numall = 0
	//     $('#product2_li .product2').each(function () {
    //         var $num = parseFloat($(this).find('p').attr('num'))
    //         var $price = parseFloat($(this).find('p').attr('price'))
    //         $priceall += $num * $price
    //         $numall += $num
    //   })
	//
    //     if ($priceall > 0){
    //         $priceall = $priceall.toFixed(2)
    //     }
	//
    //     $('#total_num').html($numall)
    //     $('#headershop .car_b .totalprice').html($priceall)
	//
    //     if($priceall > 0){
    //         // $("#headershop").css({"display":"block"});
	// 		$("#headershop .kong").css({"display":"none"});
	// 		$("#headershop .cart_out").css({"display":"block"});
	// 	}
	// 	else{
	// 	    // $("#headershop").css({"display":"block"});
	// 		$("#headershop .kong").css({"display":"block"});
	// 		$("#headershop .cart_out").css({"display":"none"});
	// 	}
	//
    // }

    // 轮播数据
	$.get('/api/v1/getlunbo/',function (response) {
        if (response.status == 200){
            var $wheels = response['data']
            for (var i=0;i < $wheels.length; i++){
                var $temp = response['data'][i].img
                var $name = response['data'][i].name
                if (i == 0){
                    var $img = $('<img>').attr('src',$temp)
                    var $div = $('<div class="carousel-caption"></div>').html($name)
                    $('<div class="item active"></div>').append($img).append($div).appendTo('.carousel-inner')
                }else {
                    var $img = $('<img>').attr('src',$temp)
                    var $div = $('<div class="carousel-caption"></div>').html($name)
                    $('<div class="item"></div>').append($img).append($div).appendTo('.carousel-inner')
                }
            }
        } else {
            console.log('获取数据失败')
        }

    })

    // 商品展示
    $.get('/api/v1/goods/',function (response) {
        if (response.status == 200){
            var $goods = response['data'];
            for (var i=0;i < $goods.length;i++){
                var $id = $goods[i].id;
                var $icon = $goods[i].icon;
                var $name = $goods[i].name;
                var $detail = $goods[i].detail;
                var $price = $goods[i].price;
                var $img = $('<img>').attr('src',$icon)
                var $h3 = $('<h3></h3>').html($name)
                var $p = $('<p></p>').html($detail)
                var $p1 = $('<p style="color: red"></p>').html($price)
                var $p2 = $('<p></p>')
                var $a1 = $('<a class="btn btn-default" role="button"></a>').html('详情')
                var $a2 = $('<a href="#" class="btn btn-primary" role="button">加入购物车</a>').attr('gooid',$id)
                $p2.append($a1).append($a2)
                var $caption = $('<div class="caption"></div>').append($h3).append($p).append($p1).append($p2)
                var $thumbnail = $('<div class="thumbnail"></div>').append($img).append($caption)
                var $col = $('<div class="col-sm-6 col-md-4"></div>').append($thumbnail).appendTo('.goodlist')

            }
        }else {
            console.log(response)
        }
    })

    var $token = $.cookie('mycookie')
    if ($token.length <= 0 || isNaN($token)){
        $('#login').html('登录')
        $('#register').html('注册').attr('href','register.html').attr('title','注册')
    } else{
        $('#login').html('欢迎【' + $token + '】')
        $('#register').html('退出').attr('href','index.html').attr('title','退出')
        $.get('/api/v1/filename/',{'telephone':$token},function (response) {
            if (response.status == 200){
                var $file = response.data.icon
                $('#topimg').attr('src',$file)
            }
        })
    }
    $('#register').on('click',function () {
        var $html = $(this).html()
        if ($html == '退出') {
            $.cookie('mycookie', null);
            window.open('index.html',target='_self')
        }
    })
})



