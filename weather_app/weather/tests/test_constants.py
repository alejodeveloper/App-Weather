from enum import Enum


class ApiResponsesCode(Enum):
    OK_RESPONSE_CODE = 200
    UNAUTHORIZED_RESPONSE_CODE = 401
    SERVER_ERROR_RESPONSE_CODE = 500


class ApiResponsesData(Enum):
    UNAUTHORIZED_RESPONSE = "unathorized_response"
    SERVER_ERROR_RESPONSE = "server_error_response"
    LONDON_RESPONSE = "london_response"


class GeneralTestConstants(Enum):
    CITY_SLUG = "London"
    COUNTRY_SLUG = "gb"


class MockedRequestMethods(Enum):
    WEATHER_API_GET = "weather_app.services.open_weather_api.requests.get"
