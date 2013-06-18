$(document).ready(function() {
    $('#section1-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section1').addClass('active blue');
        $(this).parent().addClass('active blue');
    });

    $('#section2-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section2').addClass('active red');
        $(this).parent().addClass('active red');
    });

    $('#section3-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section3').addClass('active yellow');
        $(this).parent().addClass('active yellow');
    });

    $('#section4-link').on('click', function() {
        $('.active').removeClass('active');
        $('#section4').addClass('active green');
        $(this).parent().addClass('active green');
    });
});
