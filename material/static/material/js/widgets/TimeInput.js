(function() {
    'use strict';
    window.addEventListener('load', function () {
        var nowIcons = document.querySelectorAll('i.now');
        if (nowIcons.length) {
            for(var nowIcon of nowIcons) {
                nowIcon.addEventListener('click', function() {
                    var myDate = document.querySelector(myDate);
                    var today = new Date();
                    let input = this.closest('.time-input').querySelector('.timepicker');
                    input.value = ('0' + today.getHours()).slice(-2) + ":" + ('0' + today.getMinutes()).slice(-2) + ":" +
                     ('0' + today.getSeconds()).slice(-2);
                });
            }
        }
        var clockIcons = document.querySelectorAll('i.clock');
        if (clockIcons.length) {
            for(var clockIcon of clockIcons) {
                clockIcon.addEventListener('click', function() {
                    let input = this.closest('.time-input').querySelector('.timepicker');
                    input.click();
                });
            }
        }
        var timePickers = document.querySelectorAll('.timepicker');
        var re = /^([01]?[0-9]|2[0-3]):[0-5][0-9]$/;
        if (timePickers.length) {
            for(var timePicker of timePickers) {
                timePicker.addEventListener('change', function() {
                    if (this.value.match(re)) {
                        this.value += ':00';
                    }
                });
            }
        }
    });
})();
