$(function() {
	var swiper = new Swiper('.swiper-container', {
		pagination: '.swiper-pagination',
		paginationClickable: true,
		nextButton: '.swiper-button-next',
		prevButton: '.swiper-button-prev',
		spaceBetween: 30,
		effect: 'fade'
	});

	// 轮播数据
	$.get('/api/v1/getlunbo/',function (response) {
        if (response.status == 200){
            var $wheels = response['data']
            for (var i=0;i < $wheels.length; i++){
                var $temp = response['data'][i].image
				var $img = $('<img>').attr('src',$temp)
				if (i==0){
					$('<div class="swiper-slide swiper-slide-active"></div>').append($img).appendTo('.swiper-wrapper')
				} else {
					$('<div class="swiper-slide"></div>').append($img).appendTo('.swiper-wrapper')
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
                var $postid = $goods[i].postid;
                var $title = $goods[i].title;
                var $wx_small_app_title = $goods[i].wx_small_app_title;
                var $image = $goods[i].image;
                var $likenum = $goods[i].like_num;
                var $duration = $goods[i].duration;
                var $durations = formatSeconds($duration)
                // 左边
                var $span = $('<span class="film-time"></span>').html($durations)
                var $bottom = $('<div class="bottom-cover"></div>').append($span)
                var $img = $('<img>').attr('src',$image)
                var $href = 'https://www.vmovier.com/'+ $postid + '?qingapp=app_new'
                var $a1 = $('<a target="_blank"></a>').attr('href',$href).attr('title',$title).append($img).append($bottom)
                var $movie_list_left = $('<div class="movie_list_left"></div>').append($a1)

                // 右边
                var $span1 = $('<span></span>').html($title)
                var $a2 = $('<a target="_blank"></a>').attr('href',$href).attr('title',$title).append($span1)
                var $h2 = $('<h2></h2>').append($a2)
                var $movie = $('<div class="movie-intro"></div>').html($wx_small_app_title)
                var $span2 = $('<span class="glyphicon glyphicon-heart" style="color: black;"></span>').attr('postid',$postid)
                var $span3 = $('<span></span>').html($likenum)
                var $movielike = $('<div class="movie-like"></div>').append($span2).append($span3)
                var $movie_list_right = $('<div class="movie_list_right"></div>').append($h2).append($movie).append($movielike)

                var $li = $('<li></li>').append($movie_list_left).append($movie_list_right).appendTo('.movie_list')
            }

            //添加收藏或修改收藏状态或显示状态
            $('.glyphicon-heart').each(function () {
                $(this).click(function () {
                    var $postid = $(this).attr('postid')
                    var $token = $.cookie('mycookie')
                    if ($token.length <= 0 || isNaN($token)){
                        window.open('login.html',target='_self')
                    }else {
                        var $that = $(this)
                        $.get('/api/v1/savegoods/'+$token+'/'+$postid+'/' ,function (response) {
                            console.log(response)
                            if (response.status == 200){
                                var $num = response.num
                                var $flag = response.flag
                                if ($flag == 1){
                                    $that.css('color','red')
                                } else{
                                    $that.css('color','black')
                                }

                                $that.next().html($num)
                            }else {
                                console.log(response)
                            }
                        })
                    }

                })
                var $postid = $(this).attr('postid')
                var $token = $.cookie('mycookie')
                console.log($postid)
                if ($token.length <= 0 || isNaN($token)){
                }else {
                    var $that = $(this)
                    $.get('/api/v1/checksave/'+$token+'/'+$postid+'/',function (response) {
                        console.log(response)
                        if (response.status == 200){
                            $that.css('color','red')
                        }else {
                            $that.css('color','black')
                        }
                    })
                }
            })

        }else {
            console.log(response)
        }
    })

    //秒转成时分秒格式
       function formatSeconds(value) {
        var secondTime = parseInt(value);// 秒
        var minuteTime = 0;// 分
        var hourTime = 0;// 小时
        if(secondTime > 60) {//如果秒数大于60，将秒数转换成整数
            //获取分钟，除以60取整数，得到整数分钟
            minuteTime = parseInt(secondTime / 60);
            //获取秒数，秒数取佘，得到整数秒数
            secondTime = parseInt(secondTime % 60);
            //如果分钟大于60，将分钟转换成小时
            if(minuteTime > 60) {
                //获取小时，获取分钟除以60，得到整数小时
                hourTime = parseInt(minuteTime / 60);
                //获取小时后取佘的分，获取分钟除以60取佘的分
                minuteTime = parseInt(minuteTime % 60);
            }
        }
        var result = "" + parseInt(secondTime) ;

        if(minuteTime > 0) {
            result = "" + parseInt(minuteTime) + ":" + result;
        }
        if(hourTime > 0) {
            result = "" + parseInt(hourTime) + ":" + result;
        }
        return result;}

	var $token = $.cookie('mycookie')
    if ($token.length <= 0 || isNaN($token)){
        $('#login').html('登录')
        $('#register').html('注册').attr('href','register.html').attr('title','注册')
    } else{
        $('#login').html('欢迎【' + $token + '】')
        $('#register').html('退出').attr('href','home.html').attr('title','退出')
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
            window.open('home.html',target='_self')
        }
    })

})