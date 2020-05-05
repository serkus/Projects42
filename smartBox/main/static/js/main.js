$(document).ready(() => {
    $('.collapse').click(() => {
        $('.page > .header > .logo').css('border-right', 'none');
        $('.page > .header').css('padding-left', '20px');
        $('.sidebar').css('flex', '0 1 70px').css('padding-right', '10px');
        $('.menu__item span').css('display', 'none');
        $('.raport').css('display', 'none');
        $('.controls').css('display', 'none');
        $('.menu__item svg').css('padding-left', '20px');
    })
})
