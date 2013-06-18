$(document).ready(function() {
    $('#section1-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section1').addClass('active');
        $(this).parent().addClass('active blue');
    });

    $('#section2-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section2').addClass('active');
        $(this).parent().addClass('active red');
    });

    $('#section3-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section3').addClass('active');
        $(this).parent().addClass('active yellow');
    });

    $('#section4-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section4').addClass('active');
        $(this).parent().addClass('active green');
    });
});
