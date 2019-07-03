(function($) {
    const toasts = ['success', 'warning']

    $('#mobile-demo').on('touchstart click touchmove',
        function() {
        $('.scroll-pane').jScrollPane();
    })
    $('#side-bar').on('mouseenter scroll',
        function() {
        $('.scroll-pane').jScrollPane();
    }).mouseleave(
        function() {
            const jsp = $('.scroll-pane').data('jsp')
            if (jsp) {
                jsp.destroy();
            }
        }
    );
    $('.collapsible-body > .active').closest('.scrollspy').addClass('active');

    window.addEventListener('load', function() {
        var collapsible = document.querySelectorAll('.collapsible');
         M.Collapsible.init(collapsible, {
            accordion: false
        });

        var sidenav = document.querySelectorAll('.sidenav');
        M.Sidenav.init(sidenav);

        var elems = document.querySelectorAll('.dropdown-trigger');
        M.Dropdown.init(elems);
        $('select').not('.empty-form select, .selector-available select, .selector-chosen select').formSelect();

        for(const toast of toasts) {
            const messages = $(`.messagelist > .${toast}`);
            for(let message of messages) {
                M.toast({html: message.innerText, classes: `rounded ${toast}-toast`});
            }
        }

    });
})(jQuery);
