$(document).ready(function() {
    $('#section1-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section1').addClass('active');
    });

    $('#section2-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section2').addClass('active');
    });

    $('#section3-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section3').addClass('active');
    });
});
