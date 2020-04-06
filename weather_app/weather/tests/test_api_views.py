"""
weather.tests.test_api_views
---------------------------
File to test the request functions with the OpenWeatherMap API
"""
import json
import os

import unittest

from unittest.mock import patch

from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .test_constants import DjangoTestEndpointUrls, TestApiParams, \
    ExpectedDicts, MockedRequestMethods, ApiResponsesData, ApiResponsesCode
from .utils import MockResponse
from weather.views import WeatherAPI

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(
    dir_path + '/fixtures/bad_request_response.json'
) as json_data_file:
    api_bad_request_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/error_request_response.json'
) as json_data_file:
    api_error_request_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/london_response.json'
) as json_data_file:
    api_london_response = json.load(json_data_file)

with open(
    dir_path + '/fixtures/bogota_response.json'
) as json_data_file:
    api_bogota_response = json.load(json_data_file)

MOCKED_API_RESPONSES = dict(
    unathorized_response=api_bad_request_response,
    server_error_response=api_error_request_response,
    london_response=api_london_response,
    bogota_response=api_bogota_response,
)


class TestWeatherApiViews(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = WeatherAPI.as_view()
        self.maxDiff = None

        json_path = os.path.join(
            dir_path, 'fixtures', 'tested_data.json'
        )
        call_command('loaddata', json_path, verbosity=0)

    def test_200_response(self):
            test_url = reverse(
                f'{DjangoTestEndpointUrls.TEST_WEATHER_APP.value}:'
                f'{DjangoTestEndpointUrls.TEST_WEATHER_URL.value}'
            )
            params = dict(
                city=TestApiParams.BOGOTA_CITY.value,
                country=TestApiParams.BOGOTA_COUNTRY.value,
            )

            test_request = self.factory.get(test_url, params)
            test_response = self.view(test_request)
            self.assertTrue(test_response.status_code == status.HTTP_200_OK)
