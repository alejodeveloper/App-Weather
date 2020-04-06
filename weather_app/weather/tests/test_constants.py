from decimal import Decimal
from enum import Enum


class ApiResponsesCode(Enum):
    OK_RESPONSE_CODE = 200
    UNAUTHORIZED_RESPONSE_CODE = 401
    SERVER_ERROR_RESPONSE_CODE = 500


class ApiResponsesData(Enum):
    UNAUTHORIZED_RESPONSE = "unathorized_response"
    SERVER_ERROR_RESPONSE = "server_error_response"
    LONDON_RESPONSE = "london_response"
    BOGOTA_RESPONSE = "bogota_response"


class HandlerConstants(Enum):
    BOGOTA_NAME = "Bogota"
    BOGOTA_SLUG = "bogota"
    COLOMBIA_SLUG = "co"
    LONDON_NAME = "London"
    GB_SLUG = "gb"
    UK_SLUG = "uk"


class ExpectedDicts(Enum):
    BOGOTA_FORMATTED_DICT = dict(
        location_name="Bogota, CO",
        temperature="19 °C",
        wind="broken clouds, 2.1 m/s, north",
        cloudiness="Clouds",
        pressure='1025 hpa',
        humidity='52%',
        sunrise='10:53',
        sunset='23:04',
        geo_coordinates="[4.61 - -74.08]",
        requested_time="2020-04-05 23:30"
    )
    BOGOTA_BAD_FORMATTED_DICT = dict(
        location_name="Bogota, CO",
        temperature="Bad response °C",
        wind="Bad response, Bad response m/s, north",
        cloudiness="Bad response",
        pressure='Bad response hpa',
        humidity='Bad response%',
        sunrise='00:00',
        sunset='00:00',
        geo_coordinates="[Bad response - Bad response]",
        requested_time="1970-01-01 00:00"
    )


class TimestampsConstants(Enum):
    APRIL_FIVE_2020 = 1586083995
    MARCH_TWENTY_TWO_1974 = 133185600


class GeneralTestConstants(Enum):
    CITY_SLUG = "London"
    COUNTRY_SLUG = "gb"


class MockedRequestMethods(Enum):
    WEATHER_API_GET = "weather_app.services.open_weather_api.requests.get"


class MockedHandler(Enum):
    WEATHER_HANDLER = "weather_app.weather.open_weather_utils" \
        ".OpenWeather"


class DegreesConstants(Enum):
    NORTH = Decimal(str(5.11))
    NORTH_NORTHEAST = Decimal(str(25.11))
    NORTH_EAST = Decimal(str(50.11))
    EAST_NORTHEAST = Decimal(str(60.11))
    EAST = Decimal(str(80.11))
    EAST_SOUTHEAST = Decimal(str(110.11))
    SOUTH_EAST = Decimal(str(130.11))
    SOUTH_SOUTHEAST = Decimal(str(150.11))
    SOUTH = Decimal(str(170.11))
    SOUTH_SOUTHWEST = Decimal(str(205.11))
    SOUTH_WEST = Decimal(str(225.11))
    WEST_SOUTHWEST = Decimal(str(245.11))
    WEST = Decimal(str(270.11))
    WEST_NORTHWEST = Decimal(str(290.11))
    NORTH_WEST = Decimal(str(310.11))
    NORTH_NORTHWEST = Decimal(str(330.11))


class DjangoTestEndpointUrls(Enum):
    TEST_WEATHER_APP = "weather_urls"
    TEST_WEATHER_URL = "weather_url"


class TestApiParams(Enum):
    BOGOTA_CITY = "Bogota"
    BOGOTA_COUNTRY = "co"
