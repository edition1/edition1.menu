function resetSmallMenu() {
    // Reset the small menu so all items are 'collapsed'.
    jq('.small-menu .has-children').removeClass('children-visible')
                                   .addClass('children-hidden');
    jq('.small-menu .has-children').toggle(function(event) {
        event.preventDefault();
        event.stopImmediatePropagation();
        jq(this).removeClass('children-hidden').addClass('children-visible');
        jq(this).unbind();
    }, function () {
        // Don't do anything, let the browser handle the click on the link.
        return true;
    });
}

function setMenuSize() {
    // Set a class on the menu which determines if the small or big menu
    // should be shown.
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
    resetSmallMenu();
}

jq(window).resize(function() {
    setMenuSize();
});

jq(document).ready(function() {
    setMenuSize();
});
