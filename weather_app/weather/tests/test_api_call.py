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
    GeneralTestConstants, MockedRequestMethods
from .utils import MockResponse

from services.open_weather_api import OpenWeatherApi

from weather.exceptions import APIRequestException
from weather.models import LogResponse

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
    dir_path + '/fixtures/api_call_server_error_response.json'
) as json_data_file:
    server_error_api_response = json.load(json_data_file)


MOCKED_API_RESPONSES = dict(
    unathorized_response=unauthorized_api_response,
    server_error_response=server_error_api_response,
    london_response=london_api_response,
)


class TestApiCalls(unittest.TestCase):

    def setUp(self) -> None:
        self.test_api = OpenWeatherApi

    def test_api_ok_response(self):
        with patch('weather_app.services.open_weather_api.requests.get') as \
                request_mock:
            request_mock.return_value = MockResponse(
                MOCKED_API_RESPONSES.get(
                    ApiResponsesData.LONDON_RESPONSE.value
                ),
                ApiResponsesCode.OK_RESPONSE_CODE.value
            )
            test_api = self.test_api(
                GeneralTestConstants.CITY_SLUG.value,
                GeneralTestConstants.COUNTRY_SLUG.value
            )

            test_status_code, _ = \
                test_api.get_country_city_weather_data()

            self.assertEqual(
                ApiResponsesCode.OK_RESPONSE_CODE.value,
                test_status_code
            )

    def test_unathorized_response(self):
        with patch(MockedRequestMethods.WEATHER_API_GET.value) as request_mock:
            request_mock.return_value = MockResponse(
                MOCKED_API_RESPONSES.get(
                    ApiResponsesData.UNAUTHORIZED_RESPONSE.value
                ),
                ApiResponsesCode.UNAUTHORIZED_RESPONSE_CODE.value
            )
            test_api = self.test_api(
                GeneralTestConstants.CITY_SLUG.value,
                GeneralTestConstants.COUNTRY_SLUG.value
            )

            try:
                test_api.get_country_city_weather_data()
            except Exception as e:

                unauthorized_log_response = LogResponse.objects.filter(
                    status_response=ApiResponsesCode.UNAUTHORIZED_RESPONSE_CODE.value,
                )
                self.assertIsInstance(e, APIRequestException)
                self.assertTrue(unauthorized_log_response.exists())

    def test_server_error_response(self):
        with patch(MockedRequestMethods.WEATHER_API_GET.value) as request_mock:
            request_mock.return_value = MockResponse(
                MOCKED_API_RESPONSES.get(
                    ApiResponsesData.SERVER_ERROR_RESPONSE.value
                ),
                ApiResponsesCode.SERVER_ERROR_RESPONSE_CODE.value
            )

            test_api = self.test_api(
                GeneralTestConstants.CITY_SLUG.value,
                GeneralTestConstants.COUNTRY_SLUG.value
            )

            try:
                test_api.get_country_city_weather_data()
            except Exception as e:

                server_error_log_response = LogResponse.objects.filter(
                    status_response=ApiResponsesCode.SERVER_ERROR_RESPONSE_CODE.value,
                )
                self.assertIsInstance(e, APIRequestException)
                self.assertTrue(server_error_log_response.exists())
