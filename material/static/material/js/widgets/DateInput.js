(function() {
    'use strict';
    window.addEventListener('load', function () {
        var todayIcons = document.querySelectorAll('i.today');
        if (todayIcons.length) {
            for (let todayIcon of todayIcons) {
                var myDate = document.querySelector(myDate);
                var today = new Date();
                todayIcon.addEventListener('click', function() {
                    let input = this.closest('.date-input').querySelector('.datepicker');
                    input.value = today.toISOString().substr(0, 10);
                });
            }
        }
        var calendars = document.querySelectorAll('i.calendar');
        if (calendars.length) {
            for (var calendar of calendars) {
                calendar.addEventListener('click', function() {
                    let input = this.closest('.date-input').querySelector('.datepicker');
                    input.click();
                });
            }
        }
    });
})();
