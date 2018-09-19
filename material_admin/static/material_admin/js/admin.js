document.addEventListener('DOMContentLoaded', function() {
    var collapsible = document.querySelectorAll('.collapsible');
     M.Collapsible.init(collapsible, {
        accordion: false
    });

    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    var elems = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(elems);

    $(document).ready(function(){
    $('select').formSelect();
  });

});

$('#side-bar, #mobile-demo').mouseenter(
    function() {
        $('.scroll-pane').jScrollPane();
    }
).mouseleave(
    function() {
        $('.scroll-pane').data('jsp').destroy();
    }
);

$('.collapsible-body > .active').closest('.scrollspy').addClass('active');
