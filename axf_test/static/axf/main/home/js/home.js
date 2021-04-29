$(function () {
    init_mySwiper1();
    init_mySwiper2();

})
function init_mySwiper1() {
    var mySwiper = new Swiper ('#topSwiper', {
                loop: true, // 循环模式选项
                speed: 300,
                autoplay: 3000,  //间隔时间

                // 如果需要分页器
                pagination : '.swiper-pagination',
                autoplayDisableOnInteraction: false,

        })
}
function init_mySwiper2() {
    var mySwiper = new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })
}