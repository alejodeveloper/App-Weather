"""
weather.open_weather_utils
--------------------------
Utility file to handle the API call and works as communication layer between
OpenWeatherAPI services and APIViews
"""
import json
from datetime import datetime, timezone
from decimal import Decimal

from services.open_weather_api import OpenWeatherApi
from weather.constants import DegreesRanges, WeatherConstants, DeafultConstants, \
    TimeFormat
from weather.exceptions import CityDoesNotExistsException, APIRequestException
from weather.models import CityWeather, CityWeatherLog
from weather.utils import transform_number_date, decimal_range


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

    def retrieve_weather_data(self) -> dict:
        """
        Method to connect with the OpenWeatherAPI and retrieve the data for
        the given city
        :return: Dict with the response if it was successful
        """
        try:
            no_data, open_weather_response = self.verify_logged_data()
            if no_data:
                status_code_response, open_weather_response = \
                    self.open_weather_api.get_country_city_weather_data()

                CityWeatherLog.create_city_weather_log(
                    city=self.city,
                    status_code=status_code_response,
                    response_data=open_weather_response
                )

            response_data = self.transform_response_data(
                open_weather_response
            )
            return response_data
        except APIRequestException as e:
            import traceback
            return dict(error_message=traceback.format_exc(), exception=e)

    def verify_logged_data(self) -> (bool, dict):
        """
        Method to verify previously the logged data
        If the previous data doesn't exists or its difference is bigger than
        300 seconds return false, otherwise the log instance
        :return: A tuple with a boolean that indicates if is necessaty or not to
        make an another request to the API and a dict with the logged data or
        empty
        """
        previous_data = CityWeatherLog.get_city_log(self.city)

        if previous_data is None:
            return True, {}

        time_now = datetime.now(timezone.utc)
        time_delta = time_now - previous_data.created_at

        if time_delta.seconds > DeafultConstants.TIME_BETWEEN_LOGS.value:
            return True, {}

        response_return = previous_data.response_log.response
        if isinstance(response_return, str):
            response_return = json.loads(response_return)
        return False, response_return

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
            Decimal(str(wind.get(
                "deg",
                DeafultConstants.DEFAULT_DEGREES.value
            )))
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
        sunset = transform_number_date(sys_data.get("sunset")).strftime(
            TimeFormat.hours_minutes.value
        )
        requested_time = transform_number_date(
            response_data.get("dt", DeafultConstants.DEFAULT_TIMESTAMP.value)
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

        if degrees in decimal_range(
                start=DegreesRanges.NORTH_A_START.value,
                stop=DegreesRanges.NORTH_A_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ) or degrees in decimal_range(
                start=DegreesRanges.NORTH_B_START.value,
                stop=DegreesRanges.NORTH_B_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):

            return WeatherConstants.NORTH.value

        elif degrees in decimal_range(
                start=DegreesRanges.NORTH_EAST_START.value,
                stop=DegreesRanges.NORTH_EAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.NORTH_EAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.NORTH_NORTHEAST_START.value,
                stop=DegreesRanges.NORTH_NORTHEAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.NORTH_NORTHEAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.EAST_NORTHEAST_START.value,
                stop=DegreesRanges.EAST_NORTHEAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.EAST_NORTHEAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.EAST_START.value,
                stop=DegreesRanges.EAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.EAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.EAST_SOUTHEAST_START.value,
                stop=DegreesRanges.EAST_SOUTHEAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.EAST_SOUTHEAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.SOUTH_EAST_START.value,
                stop=DegreesRanges.SOUTH_EAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.SOUTH_EAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.SOUTH_SOUTHEAST_START.value,
                stop=DegreesRanges.SOUTH_SOUTHEAST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.SOUTH_SOUTHEAST.value

        elif degrees in decimal_range(
                start=DegreesRanges.SOUTH_START.value,
                stop=DegreesRanges.SOUTH_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.SOUTH.value

        elif degrees in decimal_range(
                start=DegreesRanges.SOUTH_SOUTHWEST_START.value,
                stop=DegreesRanges.SOUTH_SOUTHWEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.SOUTH_SOUTHWEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.SOUTH_WEST_START.value,
                stop=DegreesRanges.SOUTH_WEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.SOUTH_WEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.WEST_SOUTHWEST_START.value,
                stop=DegreesRanges.WEST_SOUTHWEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.WEST_SOUTHWEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.WEST_START.value,
                stop=DegreesRanges.WEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.WEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.WEST_NORTHWEST_START.value,
                stop=DegreesRanges.WEST_NORTHWEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.WEST_NORTHWEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.NORTH_WEST_START.value,
                stop=DegreesRanges.NORTH_WEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.NORTH_WEST.value

        elif degrees in decimal_range(
                start=DegreesRanges.NORTH_NORTHWEST_START.value,
                stop=DegreesRanges.NORTH_NORTHWEST_STOP.value,
                step=DegreesRanges.DEFAULT_STEP.value
        ):
            return WeatherConstants.NORTH_NORTHWEST.value
