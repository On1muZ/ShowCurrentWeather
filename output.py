from datetime import time, datetime
from time import time as time_now
from rich.console import Console
from structures import Weather, WeatherType, Celsius

console = Console()


def print_weather(weather: Weather) -> None:
    _print_weather(weather)


def _print_weather(weather: Weather) -> None:
    console.clear()
    print_tittle()
    print_city(weather.city)
    print_temperature(weather.temperature)
    print_weather_type(weather.weather_type)
    print_sunset_time(weather.sunset)
    print_sunrise_time(weather.sunrise)


def print_tittle() -> None:
    console.rule(title=f"Погода на {str(datetime.fromtimestamp(time_now()).time())[:8]}")


def print_city(city: str) -> None:
    console.print(f"[bold #4fe3aa]Город: {city}[/]", justify="center")


def print_temperature(temperature: Celsius) -> None:
    console.print(f"[bold white]Температура[/]: [white]{temperature}°С[/]", justify="center")


def print_weather_type(weather_type: WeatherType) -> None:
    if weather_type == WeatherType.THUNDERSTORM or weather_type == WeatherType.RAIN:
        console.print(f"[bold #2c3038]Погода:[/] [#2c3038]{weather_type.value}[/]", justify="center")
    elif weather_type == WeatherType.DRIZZLE or weather_type == WeatherType.SNOW or weather_type == WeatherType.FOG or weather_type == WeatherType.CLOUDS:
        console.print(f"[bold #86949e]Погода:[/] [#86949e]{weather_type.value}[/]", justify="center")
    else:
        console.print(f"[bold #40a9d6]Погода:[/] [#40a9d6]{weather_type.value}[/]", justify="center")


def print_sunset_time(sunset: time) -> None:
    console.print(f"[bold #e86a09]Время заката:[/] [#e86a09]{sunset}[/]", justify='center')


def print_sunrise_time(sunrise: time) -> None:
    console.print(f"[bold #f7ed6f]Время рассвета:[/] [#f7ed6f]{sunrise}[/]", justify='center')