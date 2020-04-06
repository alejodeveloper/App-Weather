"""
weather.tests.test_api_call
---------------------------
File to test the request functions with the OpenWeatherMap API
"""
import json
import os

import unittest

from unittest.mock import patch

from django.core.management import call_command

from .test_constants import ApiResponsesData, ApiResponsesCode, \
    HandlerConstants, ExpectedDicts
from weather.open_weather_utils import OpenWeather

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(
    dir_path + '/fixtures/api_call_unauthorized_response.json'
) as json_data_file:
    unauthorized_api_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/api_call_london_response.json'
) as json_data_file:
    london_api_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/api_call_bogota_response.json'
) as json_data_file:
    bogota_api_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/api_call_server_error_response.json'
) as json_data_file:
    server_error_api_response = json.load(json_data_file)


MOCKED_API_RESPONSES = dict(
    unathorized_response=unauthorized_api_response,
    server_error_response=server_error_api_response,
    london_response=london_api_response,
    bogota_response=bogota_api_response,
)


class TestApiFormatter(unittest.TestCase):

    def setUp(self) -> None:
        self.test_handler = OpenWeather
        json_path = os.path.join(
            dir_path, 'fixtures', 'tested_data.json'
        )
        call_command('loaddata', json_path, verbosity=0)

    def test_api_formatter(self):

        test_mocked_data = MOCKED_API_RESPONSES.get(
            ApiResponsesData.BOGOTA_RESPONSE.value
        )
        test_handler = self.test_handler(
            city_name=HandlerConstants.BOGOTA_NAME.value,
            country_slug=HandlerConstants.COLOMBIA_SLUG.value,
            city_slug=HandlerConstants.BOGOTA_SLUG.value,
        )
        test_formatted_data = \
            test_handler.transform_response_data(test_mocked_data)

        self.assertDictEqual(
            ExpectedDicts.BOGOTA_FORMATTED_DICT.value,
            test_formatted_data
        )

    def test_api_formatter_bad(self):

        test_mocked_data = dict()
        test_handler = self.test_handler(
            city_name=HandlerConstants.BOGOTA_NAME.value,
            country_slug=HandlerConstants.COLOMBIA_SLUG.value,
            city_slug=HandlerConstants.BOGOTA_SLUG.value,
        )
        test_formatted_data = \
            test_handler.transform_response_data(test_mocked_data)

        self.assertDictEqual(
            ExpectedDicts.BOGOTA_BAD_FORMATTED_DICT.value,
            test_formatted_data
        )


class TestApiHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.test_handler = OpenWeather
        json_path = os.path.join(
            dir_path, 'fixtures', 'tested_data.json'
        )
        call_command('loaddata', json_path, verbosity=0)

    def test_api_handler(self):
        with patch('weather_app.weather.open_weather_utils.OpenWeatherApi.'
                   'get_country_city_weather_data') as \
                request_mock:
            request_mock.return_value = (
                ApiResponsesCode.OK_RESPONSE_CODE.value,
                MOCKED_API_RESPONSES.get(
                    ApiResponsesData.BOGOTA_RESPONSE.value
                )
            )
            test_handler = self.test_handler(
                city_name=HandlerConstants.BOGOTA_NAME.value,
                country_slug=HandlerConstants.COLOMBIA_SLUG.value,
                city_slug=HandlerConstants.BOGOTA_SLUG.value,
            )
            test_formatted_data = \
                test_handler.retrieve_weather_data()

            self.assertDictEqual(
                ExpectedDicts.BOGOTA_FORMATTED_DICT.value,
                test_formatted_data
            )
