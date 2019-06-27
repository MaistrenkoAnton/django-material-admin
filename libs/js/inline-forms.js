(function ($) {
    'use strict';
    $('.delete-inline-row').click(function () {
        var tableCell = $(this).closest('.delete');
        var deleteLink = tableCell.find('.inline-deletelink');
        if (deleteLink.length) {
            deleteLink.trigger("click");
        } else {
            tableCell.find('input[type=checkbox]').prop('checked', true );
            $(this).closest('.form-row').hide();
        }
    });
})(django.jQuery);
