

$(function(){

    var $token = $.cookie('mycookie')
    $('#ipt1').val($token)
    $.get('/api/v1/filename/',{'telephone':$token},function (response) {
            if (response.status == 200){
                var $file = response.data.icon
                $('#topimg').attr('src',$file)
            }
        })


    $(      //页面加载完执行
        $("#ajaxForm").on("submit",function () {    //表单提交时监听提交事件
            $(this).ajaxSubmit(options);    //当前表单执行异步提交，optons 是配置提交时、提交后的相关选项
            return false;   //  必须返回false，才能跳到想要的页面
        })
    )
    //配置 options 选项
    var options = {
        url: "/api/v1/changinfo/",       //提交地址：默认是form的action,如果申明,则会覆盖
        type: "post",           //默认是form的method（get or post），如果申明，则会覆盖
        success: successFun,    //提交成功后的回调函数，即成功后可以定页面跳到哪里
        dataType: "json",       //接受服务端返回的类型
        clearForm: true,        //成功提交后，清除所有表单元素的值
        resetForm: true,        //成功提交后，重置所有表单元素的值
        timeout: 3000           //设置请求时间，超过该时间后，自动退出请求，单位(毫秒)
    }
    //设置提交成功后返回的页面
    function successFun(data,status) {
        console.log(data)
        if (data.status == 200){
            var $token = data.data.telephone
            console.log($token)
            // 状态保持
            $.cookie('mycookie', $token)
            window.open('home.html',target='_self')
        } else {
            $('#msg').html(data.err)
        }
    }
})

