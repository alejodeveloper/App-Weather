"""
weather.tests.test_open_weather_utilities
----------------------------
Test the utils file from weather.open_weather_utility
"""
import unittest
from datetime import date, datetime

from weather.constants import WeatherConstants
from weather.open_weather_utils import OpenWeather
from weather.tests.test_constants import DegreesConstants, TimestampsConstants
from weather.utils import transform_number_date


class TestOpenWeatherUtils(unittest.TestCase):

    def test_transform_degrees_north(self):
        open_weather = OpenWeather
        test_north = open_weather.transform_degrees(
            DegreesConstants.NORTH.value
        )

        self.assertTrue(test_north == WeatherConstants.NORTH.value)

    def test_transform_degrees_north_northeast(self):
        open_weather = OpenWeather
        test_north_northeast = open_weather.transform_degrees(
            DegreesConstants.NORTH_NORTHEAST.value
        )

        self.assertTrue(
            test_north_northeast == WeatherConstants.NORTH_NORTHEAST.value
        )

    def test_transform_degrees_north_east(self):
        open_weather = OpenWeather
        test_north_east = open_weather.transform_degrees(
            DegreesConstants.NORTH_EAST.value
        )

        self.assertTrue(test_north_east == WeatherConstants.NORTH_EAST.value)

    def test_transform_degrees_test_east_southeast(self):
        open_weather = OpenWeather
        test_east_southeast = open_weather.transform_degrees(
            DegreesConstants.EAST_SOUTHEAST.value
        )

        self.assertTrue(
            test_east_southeast == WeatherConstants.EAST_SOUTHEAST.value
        )

    def test_transform_degrees_test_south_southwest(self):
        open_weather = OpenWeather
        test_south_southwest = open_weather.transform_degrees(
            DegreesConstants.SOUTH_SOUTHWEST.value
        )

        self.assertTrue(
            test_south_southwest == WeatherConstants.SOUTH_SOUTHWEST.value
        )


class TestConvertTimestamp(unittest.TestCase):

    def test_convert_timestamp(self):
        april_5_2020 = date(month=4, day=5, year=2020)
        march_22_1974 = date(month=3, day=22, year=1974)

        test_april = transform_number_date(
            TimestampsConstants.APRIL_FIVE_2020.value
        )
        test_march = transform_number_date(
            TimestampsConstants.MARCH_TWENTY_TWO_1974.value
        )

        self.assertIsInstance(test_april, datetime)
        self.assertIsInstance(test_march, datetime)

        self.assertTrue(test_april.date() == april_5_2020)
        self.assertTrue(test_march.date() == march_22_1974)