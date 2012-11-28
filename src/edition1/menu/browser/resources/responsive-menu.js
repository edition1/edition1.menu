function resetSmallMenu() {
    // Reset the small menu so all items are 'collapsed'.
    jq('.small-menu .has-children').removeClass('children-visible')
                                   .addClass('children-hidden');
    jq('.big-menu .children-hidden').removeClass('children-hidden');
    jq('.small-menu .has-children').unbind();
    jq('.small-menu .has-children').toggle(function(event) {
        event.preventDefault();
        event.stopImmediatePropagation();
        jq(this).removeClass('children-hidden').addClass('children-visible');
        jq(this).unbind();
    }, function () {
        // Don't do anything, let the browser handle the click on the link.
        return true;
    });

    // Open/close of the small menu
    jq('.small-menu .tabtitle')
        .unbind()
        .removeClass('children-visible')
        .addClass('children-hidden')
        .toggle(function() {
            jq(this).removeClass('children-hidden').addClass('children-visible');
        }, function () {
            jq(this).removeClass('children-visible').addClass('children-hidden');
        });
}

function setMenuSize() {
    // Set a class on the menu which determines if the small or big menu
    // should be shown.
    var menu = jq('#responsive-menu');
    var forced_small_flag = menu.attr('data-force-small');
    var min_width = menu.attr('data-min-width');
    if (typeof min_width == 'undefined') {
        min_width = 0;
    }

    var newMenuType = 'big-menu';
    var oldMenuType = 'small-menu';
    if (forced_small_flag == 'True' || jq(window).width() < min_width) {
        newMenuType = 'small-menu';
        oldMenuType = 'big-menu';
    }
    menu.addClass(newMenuType).removeClass(oldMenuType);
    resetSmallMenu();
}

jq(window).resize(function() {
    setMenuSize();
});
