document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    M.Datepicker.init(elems, datepickerOptions);
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.timepicker');
    M.Timepicker.init(elems, timeOptions);
});
