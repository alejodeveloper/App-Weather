"""
weather.open_weather_utility
----------------------------
Utility file to handle the API call and works as communication layer between
OpenWeatherAPI services and APIViews
"""
from decimal import Decimal

from services.open_weather_api import OpenWeatherApi
from weather.constants import DegreesRanges, WeatherConstants, DeafultConstants, \
    TimeFormat
from weather.exceptions import CityDoesNotExistsException, APIRequestException
from weather.models import CityWeather
from weather.utils import transform_number_date


class OpenWeather:
    """
    OpenWeather Singleton to handle and transforms data from  OpenWeatherAPI
    """
    def __init__(
            self,
            city_name: str,
            country_slug: str,
            city_slug: str = None
    ):
        self.city_name = city_name
        self.country_slug = country_slug.upper()
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
            "cloudiness": "Scattered clouds",
            "pressure": "1027 hpa",
            "humidity": "63%",
            "sunrise": "06:07",
            "sunset": "18:00",
            "geo_coordinates": "[4.61, -74.08]",
            "requested_time": "2018-01-09 11:57:00"
        }
        """

        weather = response_data.get(
            "weather", DeafultConstants.DEFAULT_WEATHER_DICT.value
        )[0]
        main = response_data.get(
            "main", DeafultConstants.DEFAULT_MAIN_DICT.value
        )
        wind = response_data.get(
            "wind", DeafultConstants.DEFAULT_WIND_DICT.value
        )
        degree_transformed = self.transform_degrees(
            Decimal(str(wind.get("deg")))
        )
        sys_data = response_data.get(
            "sys", DeafultConstants.DEFAULT_SYS_DICT.value
        )
        coordinates_data = response_data.get(
            "coord", DeafultConstants.DEFAULT_COORD_DICT.value
        )

        sunrise = transform_number_date(sys_data.get("sunrise")).strftime(
            TimeFormat.hours_minutes.value
        )
        sunset = transform_number_date(sys_data.get("sunrise")).strftime(
            TimeFormat.hours_minutes.value
        )
        requested_time = transform_number_date(
            response_data.get("dt")
        ).strftime(TimeFormat.datetime.value)

        wind_speed = wind.get("speed")
        humidity = main.get("humidity")
        pressure = main.get("pressure")
        temperature = main.get("temp")
        latitude = coordinates_data.get("lat")
        longitude = coordinates_data.get("lon")

        wind_description = weather.get("description")
        cloudiness = weather.get("main")

        data_response = dict(
            location_name=f"{self.city_name}, {self.country_slug}",
            temperature=f"{temperature} °C",
            wind=f"{wind_description}, {wind_speed} m/s, {degree_transformed}",
            cloudiness=f"{cloudiness}",
            pressure=f"{pressure} hpa",
            humidity=f"{humidity}%",
            sunrise=f"{sunrise}",
            sunset=f"{sunset}",
            geo_coordinates=f"[{latitude} - {longitude}]",
            requested_time=requested_time,
        )

        return data_response

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
