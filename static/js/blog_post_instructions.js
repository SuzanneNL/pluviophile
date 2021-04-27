// This makes instructions visible
$(".show-instructions").click(function() {
	$(".instructions").slideToggle(200);
	ChangeButtonText();
});

// This changes the button text
function ChangeButtonText() {
	if($(".show-instructions").html() === "Show instructions") {
		$(".show-instructions").html("Hide instructions");
	} else {
		$(".show-instructions").html("Show instructions");
	}
}