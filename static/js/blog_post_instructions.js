$(document).ready(function(){
    $(".show-instructions").click(function(){
        $(".instructions").slideToggle(200);
        ChangeButtonText();
    });
});

function ChangeButtonText() {
if ($(".show-instructions").html() === "Show instructions") {
    $(".show-instructions").html("Hide instructions")}
else {
    $(".show-instructions").html("Show instructions")}
}