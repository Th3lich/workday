/**
 * Created by Javi on 12/06/2020.
 */

$(function () {

    // $(".switchery-demo").on("click", function () {
    //
    //
    //
    //     // if($(this).find("input").prop("checked") == true) {
    //     //     $("body").toggleClass("left-side-menu-dark");
    //     // }else {
    //     //     $("body").toggleClass("left-side-menu-dark");
    //     // }
    //
    //     console.log($(this).find("input").val())
    //     console.log(window.location.hostname)
    //     console.log(window.location.port)
    //
    //     $.ajax({
    //         type: 'GET',
    //         url: window.location.hostname + ":" + window.location.port + $(this).find("input").val(),
    //         success: function (response) {
    //             console.log(response)
    //         }
    //     });
    //
    // });

    $("#dark-mode").on("click", function () {

        console.log("entra 1")

        var checked = 0;

        if ($(this).find("input").prop("checked") == true) {
            checked = 1;
        } else {
            checked = 2;
        }

        console.log(checked);

        $.post("{% url 'change_theme' %}",
            {
                'csrfmiddlewaretoken': '{{csrf_token}}',
                'checked': checked,
            },

            function (data, status) {
                if (data.result == 'ok') {
                    alert(data.result);
                }
                console.log(data.result + "ewset");
                console.log(data);
            }
        )

    });

});