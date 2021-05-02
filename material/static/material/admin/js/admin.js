(function($) {
    const toasts = ['success', 'warning', 'info', 'error']

    $('#mobile-demo').on('touchstart click touchmove', function() {
        $('.scroll-pane').jScrollPane();
    });

    $('.collapsible-body, .collapsible-header').on('mouseenter', function() {
        $('.scroll-pane').jScrollPane();
    });
    $('#side-bar').on('mouseenter scroll', function() {
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
        var collapsible = document.querySelectorAll('.collapsible:not(.no-autoinit)');
         M.Collapsible.init(collapsible, {
            accordion: false
        });

        var sidenav = document.querySelectorAll('.sidenav:not(.no-autoinit)');
        M.Sidenav.init(sidenav);

        var elems = document.querySelectorAll('.dropdown-trigger:not(.no-autoinit)');
        M.Dropdown.init(elems);

        $('select').not('.empty-form select, .selector-available select, .selector-chosen select, .admin-autocomplete, .no-autoinit')
        .formSelect();

        for(const toast of toasts) {
            const messages = $(`.messagelist > .${toast}`);
            for(let message of messages) {
              M.toast({
                html: message.innerText,
                classes: `rounded ${toast}-toast`,
                displayLength: 10000
              });
            }
        }
        $('img[src$="icon-yes.svg"]').replaceWith('<i class="material-icons green-color medium-icon">check_circle</i>');
        $('img[src$="icon-no.svg"]').replaceWith('<i class="material-icons red-color medium-icon">highlight_off</i>');
        $('img[src$="icon-unknown.svg"]').replaceWith('<i class="material-icons medium-icon">help_outline</i>');
    });
})(jQuery);
