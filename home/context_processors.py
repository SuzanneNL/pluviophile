from django.conf import settings


def weather(request):
    """Returns open weather map secret key"""
    open_weather_map_key = settings.OPEN_WEATHER_MAP_KEY
    return {'open_weather_map_key': open_weather_map_key}
