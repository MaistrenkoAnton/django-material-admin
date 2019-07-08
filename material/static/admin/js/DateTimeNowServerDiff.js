(function() {
    'use strict';
    var DateTimeShortcuts = {
        warn: function () {
            var body = document.getElementsByTagName('body')[0];
            var serverOffset = body.getAttribute('data-admin-utc-offset');
            if (serverOffset) {
                var localOffset = new Date().getTimezoneOffset() * -60;
                DateTimeShortcuts.timezoneOffset = localOffset - serverOffset;
            }
            var inputs = document.getElementsByTagName('input');
            var warningClass = DateTimeShortcuts.timezoneWarningClass;
            var timezoneOffset = DateTimeShortcuts.timezoneOffset / 3600;
            if (!timezoneOffset) {
                return;
            }
            var message;
            if (timezoneOffset > 0) {
                message = ngettext(
                    'Note: You are %s hour ahead of server time.',
                    'Note: You are %s hours ahead of server time.',
                    timezoneOffset
                );
            }
            else {
                timezoneOffset *= -1;
                message = ngettext(
                    'Note: You are %s hour behind server time.',
                    'Note: You are %s hours behind server time.',
                    timezoneOffset
                );
            }
            message = interpolate(message, [timezoneOffset]);
            var warnItems = document.getElementsByClassName('time-difference');
            for (let elem of warnItems) {
                elem.innerText = message;
            }
        }
        _today: function () {
          var myDate = document.querySelector(myDate);
          var today = new Date();
          myDate.value = today.toISOString().substr(0, 10);
        },

        console.log(document.querySelector('i.calendar'))

    }



    window.addEventListener('load', DateTimeShortcuts.warn);
})();