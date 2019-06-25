var options = {
    format: 'yyyy-mm-dd'
};
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    M.Datepicker.init(elems, options);
});

var timeOptions = {
    twelveHour: false,
};

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.timepicker');
    M.Timepicker.init(elems, timeOptions);
});
