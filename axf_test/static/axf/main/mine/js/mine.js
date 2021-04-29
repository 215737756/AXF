$(function(){
    $('#regis').click(function () {
        // window.open('axfuser/register/',target='_self')
        window.location.href='/axfuser/register/';
    })
    $('#not_login').click(function () {
        window.open('/axfuser/login/',target='_self')
    })
})