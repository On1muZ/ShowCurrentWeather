from typing import NamedTuple
from datetime import datetime, time
from enum import Enum

Celsius = int


class Coordinates(NamedTuple):
    latitude: float
    longitude: float
    city: str

    def __str__(self):
        return f"City: {self.city}\nLatitude: {self.latitude}\nLongitude: {self.longitude}"


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: time
    sunset: time
    city: str


weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
