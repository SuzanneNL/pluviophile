var openWeatherMapKey = $('#id_open_weather_map_key').text().slice(1, -1);

$("#getWeather").click(function(){
    let city = $("#city").val();

    $.ajax({
        url: 'https://api.openweathermap.org/data/2.5/weather',
        dataType: 'json',
        type: 'GET',
        data: {q: city, appid: openWeatherMapKey, units: 'metric'},

        success: function(data){
            let wf = '';
            let weatherid = '';
            $.each(data.weather, function(index, val) {
                wf += '<p><b>' + data.name + "</b><img src=" + 'https://openweathermap.org/img/w/' + val.icon + ".png></p>"+
                '<p>' + data.main.temp + '&deg;C ' + ' </p><p> ' + val.main + ", " +
                val.description + '</p>'
            });
            $("#showWeather").html(wf)
        }
    })
});