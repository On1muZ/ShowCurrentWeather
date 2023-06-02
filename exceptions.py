class CantGetCoordinates(Exception):
    """Program can't get current gps coordinates"""


class WeatherApiError(Exception):
    """Program can't get current weather with gps coordinates"""
