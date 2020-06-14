/**
 * Created by Javi on 12/06/2020.
 */

$(function () {

    $("#dark-mode").on("click", function () {

        var checked = 0;

        $.post("{% url 'change_theme' %}",
            {
                'csrfmiddlewaretoken': '{{csrf_token}}',
                'checked': checked,
            },

            function (data, status) {
                if (data.result == 'ok') {
                    if ($(this).find("input").prop("checked") == true) {
                        checked = 1;
                    } else {
                        checked = 2;
                    }
                }
                console.log(data.result + "ewset");
                console.log(data);
            }
        )

    });

});