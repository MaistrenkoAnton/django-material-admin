(function ($) {

    var navBarIcon = $('.tray-nav-bar.material-icons');
    var additionalSubmitLineIcon = $('.tray-additional-submit-row.material-icons');
    var toolsIcon = $('.tray-object-tools.material-icons');
    var navBarCookie = 'tray-nav-bar';
    var additionalSubmitLineCookie = 'additional-submit-line';
    var toolsCookie = 'object-tools';

    function createCookie(name, value, days) {
        var expires;

        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
    }

    function readCookie(name) {
        var nameEQ = encodeURIComponent(name) + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ')
                c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0)
                return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
        return null;
    }

    function eraseCookie(name) {
        createCookie(name, "", -1);
    }

    function manageCookies(name) {
        readCookie(name)
            ? eraseCookie(name)
            : createCookie(name, true, 1000);
        location.reload();
    }

    navBarIcon.on('click', function () {
        manageCookies(navBarCookie);
    });
    $('.nav-bar.minimize').on('click', function () {
        manageCookies(navBarCookie);
    });

    toolsIcon.on('click', function () {
        manageCookies(toolsCookie);
    });
     $('.tools.minimize').on('click', function () {
        manageCookies(toolsCookie);
    });

    additionalSubmitLineIcon.on('click', function () {
        manageCookies(additionalSubmitLineCookie);
    });
    $('.submit-line.minimize').on('click', function () {
        manageCookies(additionalSubmitLineCookie);
    });

})(jQuery);
