// Source: YouTube tutorial by 'The Basics of Web Tech', see README file under 'Sources'. 

/* A user enters a city and after submitting, he sees the current weather situation for that city, provided by openweathermap.
Also, based on the weather code for that situation, the user sees a small message about whether or not it's raining */
let weatherCodes = ["200", "201", "202", "230", "231", "232", "300", "301", "302", "310", "311", "312", "313", "314", "321", "500", "501", "502", "503", "504", "511", "520", "521", "522", "531"];
var openWeatherMapKey = $('#id_open_weather_map_key').text().slice(1, -1);

$("#getWeather").click(function() {
	let city = $("#city").val();
	$.ajax({
		url: 'https://api.openweathermap.org/data/2.5/weather',
		dataType: 'json',
		type: 'GET',
		data: {
			q: city,
			appid: openWeatherMapKey,
			units: 'metric'
		},
		success: function(data) {
			let weatherid = '';
			let cityname = '';
			let icon = '';
			let temp = '';
			let temprounded = '';
			let desc = '';
			$.each(data.weather, function(index, val) {
				weatherid += val.id;
				cityname += data.name;
				icon += "<img src=" + 'https://openweathermap.org/img/w/' + val.icon + ".png>";
				temp += data.main.temp;
				temprounded = Math.floor(temp) + '&deg;C ';
				desc += val.description;
            });
            $("#error").html("");
			$("#show-city").html(cityname);
			$("#show-icon").html(icon);
			$("#show-temp").html(temprounded);
			$("#show-desc").html(desc);
			if(weatherCodes.includes(weatherid)) {
				$("#is-it-raining").html("Yaay, it's raining in");
			} else {
				$("#is-it-raining").html("Sorry, no rain in");
			}
        },
        error: function(){
            $("#is-it-raining").html("");
            $("#show-city").html("");
            $("#show-icon").html("");
            $("#show-temp").html("");
            $("#show-desc").html("");
            $("#error").html("Oops, something went wrong.<br><br>Did you spell the city name correctly? If so, perhaps the service is unavailable. Please, try again later.")
        }
	});
});