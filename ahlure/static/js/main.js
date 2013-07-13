$(document).ready( function() {
    $('nav.tabs ul li a').on('click', function() {
        $('nav.tabs ul li.active').removeClass('active');
        $('.content.inner.active').removeClass('active');
        var activeTab = $(this).attr('href');
        $(this).parent().addClass('active');
        $(activeTab).addClass('active'); 
        return false;
    }); 
});
