jq(document).ready(function() {
    var min_width = jq('#responsive-menu').attr('data-min-width');
    if (typeof min_width == 'undefined') {
        min_width = 0;
    }

    var menu_type = 'small-menu';
    if (jq(window).width() >= min_width) {
        menu_type = 'big-menu';
    }
    jq('#responsive-menu').addClass(menu_type);
});
