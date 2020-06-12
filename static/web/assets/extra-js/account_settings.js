/**
 * Created by Javi on 12/06/2020.
 */

$(function() {

    $(".switchery-demo").on("click", function () {
        console.log("prueba")
        console.log(this.checked)
        console.log($(this).find("input"))
        console.log($(this).find("input").val())
        if($(this).find("input").val() == "on") {
            $(this).find("input").val("off")
        }else {
            $(this).find("input").val("on")
        }
    });

});