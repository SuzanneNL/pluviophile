let weatherCodes = ["200", "201", "202", "230", "231", "232", "300", "301", "302", "310", "311", "312", "313", "314", "321", "500", "501", "502", "503", "504", "511", "520", "521", "522", "531"]
var openWeatherMapKey = $('#id_open_weather_map_key').text().slice(1, -1);

$("#getWeather").click(function(){
    let city = $("#city").val();

    $.ajax({
        url: 'https://api.openweathermap.org/data/2.5/weather',
        dataType: 'json',
        type: 'GET',
        data: {q: city, appid: openWeatherMapKey, units: 'metric'},

        success: function(data){

            let weatherid = '';
            let cityname = '';
            let icon = '';
            let temp = '';
            let desc = '';
            $.each(data.weather, function(index, val) {
                weatherid += val.id
                cityname += data.name
                icon += "<img src=" + 'https://openweathermap.org/img/w/' + val.icon + ".png>"
                temp += data.main.temp 
                temprounded = Math.floor(temp) + '&deg;C '
                desc += val.description
            });
            $("#show-city").html(cityname)
            $("#show-icon").html(icon)
            $("#show-temp").html(temprounded)
            $("#show-desc").html(desc)
            if (weatherCodes.includes(weatherid)) {
                $("#isItRaining").html("Yaay, it's raining in")
            }
            else {
                $("#is-it-raining").html("Sorry, it's not raining in")
            }
        }
    })
});
