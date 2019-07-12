(function ($) {

    var sideBar = $('#side-bar');
    var container = $('#container');
    var navBarIcon = $('.tray-nav-bar.material-icons');
    var navBarCookie = 'tray-nav-bar';

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

    function navMinimize () {
        sideBar.hide();
        container.removeClass('indent');
        navBarIcon.removeClass('minimized');
    }

    $('.nav-bar.minimize').on('click', function () {
        navMinimize();
        createCookie(navBarCookie, true, 30);
    });

    navBarIcon.on('click', function () {
        sideBar.show();
        container.addClass('indent');
        $(this).addClass('minimized');
        eraseCookie(navBarCookie)
    });


})(jQuery);
