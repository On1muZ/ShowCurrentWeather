from weather_api_service import get_weather
from rich.console import Console
from output import print_weather
from exceptions import WeatherApiError

console = Console()

console.clear()

console.set_window_title("Weather")

with console.status("[white on #262626]Ожидание ответа от сервера...[/]", spinner="dots"):
    try:
        weather = get_weather()
    except Exception:
        raise WeatherApiError


print_weather(weather)
