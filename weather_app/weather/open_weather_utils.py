"""
weather.open_weather_utility
----------------------------
Utility file to handle the API call and works as communication layer between
OpenWeatherAPI services and APIViews
"""
from services.open_weather_api import OpenWeatherApi
from weather.exceptions import CityDoesNotExistsException
from weather.models import CityWeather


class OpenWeather:
    def __init__(self, city_name: str, country_slug: str, city_slug: str = None):
        try:
            self.city = CityWeather.get_city(
                city_name=city_name,
                country_slug=country_slug
            )
        except CityDoesNotExistsException:
            self.city = CityWeather.create_city(
                city_slug=city_slug,
                country_slug=country_slug,
                city_name=city_name
            )
        self.open_weather_api = OpenWeatherApi(
            city_slug=city_slug,
            country_slug=country_slug
        )

    def retrieve_weather_data(self):
        """
        Method to connect with the OpenWeatherAPI and retrieve the data for
        the given city
        :return: Dict with the response if it was successful
        """

