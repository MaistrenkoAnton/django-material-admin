(function() {
    'use strict';
    window.addEventListener('load', function () {
        var now = document.querySelector('i.now');
        if (now) {
            now.addEventListener('click', function() {
                var myDate = document.querySelector(myDate);
                var today = new Date();
                var input = this.closest('.time-input').querySelector('.timepicker');
                input.value = ('0' + today.getHours()).slice(-2) + ":" + ('0' + today.getMinutes()).slice(-2) + ":" +
                 ('0' + today.getSeconds()).slice(-2);
            });
        }
        var clock = document.querySelector('i.clock');
        if (clock) {
            clock.addEventListener('click', function() {
                var input = this.closest('.time-input').querySelector('.timepicker');
                input.click();
            });
        }
    });
})();