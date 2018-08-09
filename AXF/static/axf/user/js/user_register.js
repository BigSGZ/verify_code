function check_input() {
    var u_name_color=$('#u_name_info').css('color');
    console.log(u_name_color);
    if(u_name_color== 'rgb(255, 0, 0)'){
        console('用户名已存在')
        return false
    }
    var u_password = $('#u_password').val();
    console.log(u_password);
    var u_password_confirm = $('#u_password_confirm').val();
    console.log(u_password_confirm);
    if (u_password === u_password_confirm) {
        return true
    } else {
        return false
    }
}
$(function () {
    //change的作用是 内容改变，且失去焦点才会生效
    $('#u_name').change(function () {
        var username =$(this).val();
        console.log(username);
        $.getJSON('/app/checkuser/',{'u_name':username},function (data) {
            console.log(data);
            if (data['status']==200){
                console.log('用户名可用');
                $('#u_name_info').html('用户名可用').css('color','green');
            }else{
                console.log('用户名已存在');
                $('#u_name_info').html('用户名已存在').css('color','red');
            }
        })
    })
    $('#u_email').change(function () {
        var email=$(this).val()
        console.log(email);
        $.getJSON('/axf/checkemail/',{'u_email':email},function (data) {
            console.log(data);

        })

    })
    $('#u_password_confirm').change(function () {
        var password_confirm=$(this).val();
        var password=$('#u_password').val();
        if (password_confirm===password){
         $('#password_confirm_info').css('color','green').html('密码输入一致');
        }else {
            $('#password_confirm_info').css('color','red').html('密码输入错误');
        }
    })
    $('#u_password').change(function () {
        var password_confirm=$('#u_password_confirm').val();
        var pasword=$('#u_password').val();
        if (password_confirm.length == 0){
            return
        }
        if(password_confirm===pasword){
            $('#password_confirm_info').css('color','green').html('密码输入一致');
        }else{
            $('#password_confirm_info').css('color','red').html('密码错误');
        }
    })
})