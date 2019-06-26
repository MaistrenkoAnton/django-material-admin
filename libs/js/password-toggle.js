(function () {
    var input = document.getElementById("password-input");
    var visibleOff = document.getElementById("visible-off");
    var visibleOn = document.getElementById("visible-on");

    function passwordShow () {
      input.type = "text";
      visibleOn.classList.add("hide");
      visibleOff.classList.remove("hide");
    }

    function passwordHide () {
      input.type = "password";
      visibleOff.classList.add("hide");
      visibleOn.classList.remove("hide");
    }
})();
