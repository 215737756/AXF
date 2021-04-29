$(function () {
    // 用户名
    var name = $('#username_input').blur(function () {
        var name = $(this).val();

        var reg = /^[a-z].{2,8}$/;

        var b = reg.test(name)
        if (b) {
            $('#nameinfo').html('').css('color', 'green')
            name = $.getJSON(
                '/axfuser/checkname',
                {'name': name},
                function (data) {
                    if (data['status'] != 200) {
                        $('#nameinfo').html(data['message']).css('color', 'green')
                    }
                })


        } else {
            $('#nameinfo').html('请输入以字母开头3-8位字符').css('color', 'red')

        }

    })
    // 输入密码
    var password = $('#exampleInputPassword').blur(function () {
        var password = $('#exampleInputPassword').val()

        var reg = /^.{6,10}$/
        var b = reg.test(password)
        // console.log(password)
        // console.log(b)

        if (b) {
            $('#password_alert').html('').css('color', 'green')

        } else {
            $('#password_alert').html('请输入密码6-10位').css('color', 'red')
        }


    })
    // 重复密码
    var password1 = $('#exampleInputPassword1').blur(function () {
        var password1 = $('#exampleInputPassword1').val()
        var reg = /^.{6,10}$/
        var b = reg.test(password1)
        if (b) {
            $.getJSON(
                ''
            )
            $('#password_alert1').html('').css('color', 'green')
        } else {
            $('#password_alert1').html('请输入密码6-10位').css('color', 'red')
        }
    })


})