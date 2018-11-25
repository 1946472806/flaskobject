
	
$(function(){
    var code
    var verifyCode
    //检测用户是否合法,是否已经存在
    $('#ipt1').blur(function () {
        var reg = /^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/;
		var val = $(this).val();

		if (reg.test(val)) {
			 $.get('/api/v1/verifyuser/',{'telephone':val},function (data) {
			     console.log(data)
                if (data['status'] == '0'){
                    $('#telephone i').html(data['msg'])
                    $('#telephone').removeClass('has-success').addClass('has-error')
                    $('#telephone span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                } else {
                    $('#telephone i').html('')
                    $('#telephone').removeClass('has-error').addClass('has-success')
                    $('#telephone span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                }
            })
		}
		else {
            $('#telephone i').html('手机号不合法')
            $('#telephone').removeClass('has-error').addClass('has-success')
            $('#telephone span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
		}

    })

	//验证码
	verifyCode = new GVerify("v_container");
    code = verifyCode.options.code.toUpperCase()
	console.log(code)
	$("#ipt2").blur(function(e){
		e.preventDefault();
		if ($("#ipt2").val().toUpperCase() == code){
		    $('#yanid i').html('')
            $('#yanid').removeClass('has-error').addClass('has-success')
            $('#yanid span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
		}
		else {
		    $('#yanid i').html('验证码不正确')
            $('#yanid').removeClass('has-success').addClass('has-error')
            $('#yanid span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
		}
	})

    $('#fresh').click(function () {
        verifyCode = new GVerify("v_container");
        code = verifyCode.options.code.toUpperCase()
        console.log(code)
    })

	//密码
	$("#ipt4").blur(function(){
		//验证密码， 数字字母下划线，且第一个不能为数字， 长度在6~20位
		var reg =/^([a-zA-Z_]{1,})\w{5,19}$/;
//		var reg = /^.{8,16}$/;
		var val = $(this).val();
		
		if (reg.test(val)) {
		    $('#passid i').html('')
            $('#passid').removeClass('has-error').addClass('has-success')
            $('#passid span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
		}
		else {
		    $('#passid i').html('密码包括数字字母下划线，且第一个不能为数字，长度在6~20位!')
            $('#passid').removeClass('has-success').addClass('has-error')
            $('#passid span').removeClass('glyphicon-ok').addClass('glyphicon-remove')

		}
	})
	
	//重复密码
	$("#ipt5").blur(function(){
		var value = $(this).val();

		if (value == $("#ipt4").val()){
		    $('#passchid i').html('')
            $('#passchid').removeClass('has-error').addClass('has-success')
            $('#passchid span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
		}
		else {
		    $('#passchid i').html('重复密码不一致!')
            $('#passchid').removeClass('has-success').addClass('has-error')
            $('#passchid span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
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
        url: "/api/v1/register/",       //提交地址：默认是form的action,如果申明,则会覆盖
        type: "post",           //默认是form的method（get or post），如果申明，则会覆盖
        success: successFun,    //提交成功后的回调函数，即成功后可以定页面跳到哪里
        dataType: "json",       //接受服务端返回的类型
        clearForm: true,        //成功提交后，清除所有表单元素的值
        resetForm: true,        //成功提交后，重置所有表单元素的值
        timeout: 3000           //设置请求时间，超过该时间后，自动退出请求，单位(毫秒)
    }
    //设置提交成功后返回的页面
    function successFun(data,status) {
        if (data.status == 200){
            $('#msg').html('注册成功！')
            window.open('login.html',target='_branch')
        } else {
            $('#msg').html(data.err)
        }
    }
})
	
