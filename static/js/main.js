$(document).ready( function() {
    $('nav.tabs ul li a').on('click', function() {
        $('.content.inner.active').removeClass('active');
        var activeTab = $(this).attr('href');
        var color = $(this).data('color');
        $(activeTab).addClass('active').fadeIn(); 
        console.log(activeTab);
        console.log(color);
        return false;
    }); 
});
