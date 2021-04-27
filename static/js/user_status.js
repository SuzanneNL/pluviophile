/* This counts the number of posts(threads/comments - on the entire forum) created by a user
Based on that number, an activity status is created in the form of blue and grey drops */
$(".elements").each(function(ind, val) {
	var nTotalPost = $(val).find(".count-this").length; 
	if(nTotalPost < 5) {
		$(val).find(".count").html("<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>");
	} else if(nTotalPost < 10) {
		$(val).find(".count").html("<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>");
	} else if(nTotalPost < 20) {
		$(val).find(".count").html("<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>");
	} else if(nTotalPost < 25) {
		$(val).find(".count").html("<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint grey-drop' aria-hidden='true'></i>");
	} else {
		$(val).find(".count").html("<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>" + "<i class='fa fa-tint blue-drop' aria-hidden='true'></i>");
	}
});