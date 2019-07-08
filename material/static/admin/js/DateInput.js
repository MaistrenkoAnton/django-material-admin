(function() {
    'use strict';
    window.addEventListener('load', function () {
        var today = document.querySelector('i.today');
        if (today) {
            today.addEventListener('click', function() {
                var myDate = document.querySelector(myDate);
                var today = new Date();
                var input = this.closest('.date-input').querySelector('.datepicker');
                input.value = today.toISOString().substr(0, 10);
            });
        }
        var calendar = document.querySelector('i.calendar');
        if (calendar) {
            calendar.addEventListener('click', function() {
                var input = this.closest('.date-input').querySelector('.datepicker');
                input.click();
            });
        }
    });
})();