//This counts the number of posts(threads/comments - on the entire forum)
//created by the commenting user

$(".elements").each(function(ind, val){
    var nTotalPost = $(val).find(".count-this").length;

    //Based on this number, an activity status is created
    if (nTotalPost < 5) {
        $(val).find(".count").html(
            "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>")
    }
    else if (nTotalPost < 10) {
        $(val).find(".count").html(
            "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>")
    }
    else if (nTotalPost < 20) {
        $(val).find(".count").html(
            "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>")
    }
    else if (nTotalPost < 25) {
        $(val).find(".count").html(
            "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>")
    }
    else {
        $(val).find(".count").html(
        "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>"
        + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>")
    }
});
