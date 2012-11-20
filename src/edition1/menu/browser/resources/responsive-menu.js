function setMenuSize() {
    var menu = jq('#responsive-menu');
    var min_width = menu.attr('data-min-width');
    if (typeof min_width == 'undefined') {
        min_width = 0;
    }
    var newMenuType = 'small-menu';
    var oldMenuType = 'big-menu';
    if (jq(window).width() >= min_width) {
        newMenuType = 'big-menu';
        oldMenuType = 'small-menu';
    }
    menu.addClass(newMenuType).removeClass(oldMenuType);
}

jq(window).resize(function() {
    setMenuSize();
});


jq(document).ready(function() {
    setMenuSize();
});
