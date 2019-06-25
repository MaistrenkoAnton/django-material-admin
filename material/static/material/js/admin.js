const toasts = ['success', 'warning']

$('#side-bar, #mobile-demo').mouseenter(
    function() {
    $('.scroll-pane').jScrollPane();
}
).mouseleave(
    function() {
        const jsp = $('.scroll-pane').data('jsp')
        if (jsp) {
            jsp.destroy();
        }
    }
);
$('.collapsible-body > .active').closest('.scrollspy').addClass('active');

document.addEventListener('DOMContentLoaded', function() {
    var collapsible = document.querySelectorAll('.collapsible');
     M.Collapsible.init(collapsible, {
        accordion: false
    });

    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var elems = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(elems);

    $('select').formSelect();

    for(const toast of toasts) {
        const messages = $(`.messagelist > .${toast}`);
        for(let message of messages) {
            M.toast({html: message.innerText, classes: `rounded ${toast}-toast`});
        }
    }

});
