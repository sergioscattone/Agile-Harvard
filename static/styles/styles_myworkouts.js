$(document).ready(function() {
    $('.toggleButton').click(function() {
        var target = $(this).data('target');
        $(target).toggle();
    });
});

