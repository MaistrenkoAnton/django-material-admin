document.addEventListener('DOMContentLoaded', function() {
    var datepickers = document.querySelectorAll('.datepicker');
    if (datepickers.length) {
        datepickerOptions['format'] = get_format('DATE_INPUT_FORMATS')[0].replace('%Y', 'yyyy').replace('%m', 'mm').replace('%d', 'dd');
        M.Datepicker.init(datepickers, datepickerOptions);
    }

    var timepickers = document.querySelectorAll('.timepicker');
    if (timepickers.length) {
        M.Timepicker.init(timepickers, timeOptions);
    }
});
