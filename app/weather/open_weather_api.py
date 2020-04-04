"""
weather.open_weather_api
------------------------
Weather API methods to retrieve weather information data from some parameters
Read the docs
https://openweathermap.org/current
"""
import requests

from django.conf import settings

from app.weather.constants import ApiConstants
from app.weather.exceptions import APIRequestException


class OpenWeatherApi:
    """
    Class to handle request to open weather map API
    """
    def __init__(self, city_slug: str, country_slug: str):
        self.base_url = settings.OPEN_WEATHER_API_BASE_URL
        self.city_slug = city_slug
        self.country_slug = country_slug

    def get_country_city_weather_data(self) -> (int, dict):
        """
        Consumes the endpoint
        bas_urñ/weather?q={city name}&appid={your api key}
        :return: Tuple with the status code and  Weather data corresponding to
        the city slug
        """
        api_url = f"{self.base_url}/weather"
        request_params = dict(
            q=f"{self.city_slug},{self.country_slug}",
            appid=settings.OPEN_WEATHER_API_ID_KEY
        )
        response = requests.get(api_url, params=request_params)

        if response.status_code == ApiConstants.OK_STATUS_CODE.value:
            return response.status_code, response.json()

        else:
            exception_message = f"The API response with status code " \
                f"{response.status_code} and data\n {response.json()}"
            raise APIRequestException(exception_message)
