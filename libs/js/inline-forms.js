(function ($) {
    'use strict';
    $('.delete-inline-row').click(function () {
        var tableCell = $(this).closest('.delete');
        var deleteLink = tableCell.find('.inline-deletelink');
        if (deleteLink.length) {
            deleteLink.trigger("click");
        } else {
            var checkbox = tableCell.find('input[type=checkbox]');
            if (checkbox.length) {
                checkbox.prop('checked', true);
                $(this).closest('.form-row').hide();
            } else {
                $(this).closest('.form-row').remove();
            }
        }
    });
    $('.tabular.inline-related input:checkbox + span').click(function() {
        var checkbox = $(this).prev();
        checkbox.prop('checked', !checkbox.prop("checked"))
    });
})(django.jQuery);
