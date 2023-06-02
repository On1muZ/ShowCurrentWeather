import googletrans
from pyowm import OWM
from structures import WeatherType, Weather, weather_types, Celsius
from coordinates import get_gps_coordinates
from config import OPEN_WEATHER_API
from datetime import datetime, time


def get_weather() -> Weather:
    return _get_weather()


def _get_weather() -> Weather:
    return _parse_OpenWeather_answer(_get_openWeather_answer())


def _get_openWeather_answer() -> dict:
    coordinates = get_gps_coordinates()
    owm = OWM(OPEN_WEATHER_API)
    mgr = owm.weather_manager()
    data = mgr.weather_at_coords(lat=coordinates.latitude, lon=coordinates.longitude)
    return data.to_dict()


def _parse_OpenWeather_answer(open_weather_data: dict) -> Weather:
    return Weather(
        city=_parse_city(open_weather_data),
        temperature=_parse_temperature(open_weather_data),
        weather_type=_parse_weather_type(open_weather_data),
        sunset=_parse_sunset_time(open_weather_data),
        sunrise=_parse_sunrise_time(open_weather_data)
    )


def _parse_city(open_weather_data: dict) -> str:
    translator = googletrans.Translator()
    result = translator.translate(text=open_weather_data['location']['name'], src='en', dest='ru')
    return result.text


def _parse_temperature(open_weather_data: dict) -> Celsius:
    return round(open_weather_data['weather']["temperature"]['temp'] - 273.15)


def _parse_weather_type(open_weather_data: dict) -> WeatherType:
    return weather_types[str(open_weather_data['weather']['weather_code'])]


def _parse_sunset_time(open_weather_data: dict) -> time:
    return datetime.fromtimestamp(open_weather_data['weather']['sunset_time']).time()


def _parse_sunrise_time(open_weather_data: dict) -> time:
    return datetime.fromtimestamp(open_weather_data['weather']['sunrise_time']).time()


if __name__ == "__main__":
    get_weather()
