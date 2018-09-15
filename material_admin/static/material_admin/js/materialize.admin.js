document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {
        accordion: false
    });
});

$(function()
    {
      $('.scroll-pane').jScrollPane();
    }
);
