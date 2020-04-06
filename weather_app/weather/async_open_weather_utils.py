"""
weather.async_open_weather_utils
--------------------------------
Async helper of the app
"""
from weather.tasks import schedule_api_call


class AsyncOpenWeather:
    def __init__(self, city_name: str, country_slug: str, city_slug: str = ""):
        self.city_name = city_name
        self.country_slug = country_slug.upper()
        self.city_slug = country_slug.upper()

    def set_asycn_task(self):
        """
        Send to execute celery async task for
        """
        schedule_api_call(self.city_name, self.country_slug)
