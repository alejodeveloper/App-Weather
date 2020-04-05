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


class TimestampsConstants(Enum):
    APRIL_FIVE_2020 = 1586083995
    MARCH_TWENTY_TWO_1974 = 133185600


class GeneralTestConstants(Enum):
    CITY_SLUG = "London"
    COUNTRY_SLUG = "gb"


class MockedRequestMethods(Enum):
    WEATHER_API_GET = "weather_app.services.open_weather_api.requests.get"


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