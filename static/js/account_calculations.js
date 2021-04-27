/* The section below calculates the number of bookmarks.
If there are none, a 'no bookmarks' message is visible. */
let bookmarkscount = document.getElementsByClassName("bookmark").length;
if(bookmarkscount == 0) {
	showNoBookmarksMessage();
}

function showNoBookmarksMessage() {
	document.querySelector('#no-bookmarks').classList.remove('hide');
}

/* The section below calculates the amount donated by the logged in user,
 And displays the amount on the account page. */
let yourDonationCount = document.getElementsByClassName("your-donation-amount").length;
let yourDonationAmount = yourDonationCount * 5;
if(yourDonationCount) {
	showYourDonationAmount();
}

function showYourDonationAmount() {
	document.getElementById("your-amount-donated").innerHTML = yourDonationAmount;
}

/* The section below calculates the amount donated by all users.
And displays the amount on the account page. */
let donationCount = document.getElementsByClassName("donation-amount").length;
let donationAmount = donationCount * 5;
if(donationCount) {
	showDonationAmount();
}

function showDonationAmount() {
	document.getElementById("amount-donated").innerHTML = donationAmount;
}