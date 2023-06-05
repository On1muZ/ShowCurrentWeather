from typing import NamedTuple
from datetime import time
from enum import Enum

Celsius = float
Fahrenheit = float


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
    temperature_celsius: Celsius
    temperature_fahrenheit: Fahrenheit
    weather_type: WeatherType
    sunrise: time
    sunset: time
    city: str


