"""
weather.open_weather_utility
----------------------------
Utility file to handle the API call and works as communication layer between
OpenWeatherAPI services and APIViews
"""
from decimal import Decimal

from services.open_weather_api import OpenWeatherApi
from weather.constants import DegreesRanges, WeatherConstants
from weather.exceptions import CityDoesNotExistsException, APIRequestException
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
            city_name=city_name,
            country_slug=country_slug
        )

    def retrieve_weather_data(self):
        """
        Method to connect with the OpenWeatherAPI and retrieve the data for
        the given city
        :return: Dict with the response if it was successful
        """
        try:
            _, open_weather_response = self.open_weather_api.\
                get_country_city_weather_data()

            response_data = self.transform_response_data(open_weather_response)
            return response_data
        except APIRequestException as e:
            return e.message

    def transform_response_data(self, response_data: dict) -> dict:
        """
        Transform the response from OpenWeatherAPI into a more understanding
        response
        :param response_data: response object from OpenWeatherAPI
        :return: Data response dict with the followed structure
        {
            "location_name": "Bogota, CO",
            "temperature": "17 °C",
            "wind": Gentle breeze, 3.6 m/s, west-northwest",
            "cloudines": "Scattered clouds",
            "presure": "1027 hpa",
            "humidity": "63%",
            "sunrise": "06:07",
            "sunset": "18:00",
            "geo_coordinates": "[4.61, -74.08]",
            "requested_time": "2018-01-09 11:57:00"
        }
        """
        pass

    @staticmethod
    def transform_degrees(degrees: Decimal) -> str:
        """
        Get the degrees (meteorological) and it transforms into str coordinates
        :param degrees: Decimal with the values betwee 0 and 360
        :return: str with the coordinate
        """
        degrees = Decimal(str(degrees))

        if degrees in DegreesRanges.NORTH_A.value or \
                degrees in DegreesRanges.NORTH_B.value:

            return WeatherConstants.NORTH.value

        elif degrees in DegreesRanges.NORTH_EAST.value:
            return WeatherConstants.NORTH_EAST.value

        elif degrees in DegreesRanges.NORTH_NORTHEAST.value:
            return WeatherConstants.NORTH_NORTHEAST.value

        elif degrees in DegreesRanges.EAST_NORTHEAST.value:
            return WeatherConstants.EAST_NORTHEAST.value

        elif degrees in DegreesRanges.EAST.value:
            return WeatherConstants.EAST.value

        elif degrees in DegreesRanges.EAST_SOUTHEAST.value:
            return WeatherConstants.EAST_SOUTHEAST.value

        elif degrees in DegreesRanges.SOUTH_EAST.value:
            return WeatherConstants.SOUTH_EAST.value

        elif degrees in DegreesRanges.SOUTH_SOUTHEAST.value:
            return WeatherConstants.SOUTH_SOUTHEAST.value

        elif degrees in DegreesRanges.SOUTH.value:
            return WeatherConstants.SOUTH.value

        elif degrees in DegreesRanges.SOUTH_SOUTHWEST.value:
            return WeatherConstants.SOUTH_SOUTHWEST.value

        elif degrees in DegreesRanges.SOUTH_WEST.value:
            return WeatherConstants.SOUTH_WEST.value

        elif degrees in DegreesRanges.WEST_SOUTHWEST.value:
            return WeatherConstants.WEST_SOUTHWEST.value

        elif degrees in DegreesRanges.WEST.value:
            return WeatherConstants.WEST.value

        elif degrees in DegreesRanges.WEST_NORTHWEST.value:
            return WeatherConstants.WEST_NORTHWEST.value

        elif degrees in DegreesRanges.NORTH_WEST.value:
            return WeatherConstants.NORTH_WEST.value

        elif degrees in DegreesRanges.NORTH_NORTHWEST.value:
            return WeatherConstants.NORTH_NORTHWEST.value
