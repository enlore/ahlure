$(document).ready(function() {
    $('#section1-link').on('click', function() {
        $('section.active').removeClass('active');
        $('#wrapper > section').addClass('hidden');
        $('#section1').addClass('active');
        return false;
    });

    $('#section2-link').on('click', function() {
        $('section.active').removeClass('active');
        $('#wrapper > section').addClass('hidden');
        $('#section2').addClass('active');
        return false;
    });

    $('#section3-link').on('click', function() {
        $('section.active').removeClass('active');
        $('#wrapper > section').addClass('hidden');
        $('#section3').addClass('active');
        return false;
    });
});
