"""
weather.constants
-----------------
Constants file composed majority by enumerators
"""
from decimal import Decimal
from enum import Enum

from django.conf import settings


class ApiConstants(Enum):
    OK_STATUS_CODE = 200
    UNITS = "metric"


class TimeFormat(Enum):
    regular_date = "%Y-%m-%d"
    hours_minutes = "%H:%M"
    datetime = "%Y-%m-%d %H:%M"


class DeafultConstants(Enum):
    DEFAULT_WEATHER_DICT = [
        dict(
            main="Bad response",
            description="Bad response",
        )
    ]
    DEFAULT_MAIN_DICT = dict(
        temp="Bad response",
        humidity="Bad response",
        pressure="Bad response",
    )
    DEFAULT_WIND_DICT = dict(
        speed="Bad response",
        deg=0,
    )
    DEFAULT_COORD_DICT = dict(
        lon="Bad response",
        lat="Bad response",
    )
    DEFAULT_SYS_DICT = dict(
        sunrise=1,
        sunset=1,
    )
    DEFAULT_TIMESTAMP = 1
    DEFAULT_DEGREES = 0
    TIME_BETWEEN_LOGS = settings.TIME_BETWEEN_SECS


class WeatherConstants(Enum):
    NORTH = "north"
    NORTH_EAST = "north-east"
    NORTH_NORTHEAST = "north-northeast"
    EAST_NORTHEAST = "east-northeast"
    EAST = "east"
    EAST_SOUTHEAST = "east-southeast"
    SOUTH_EAST = "south-east"
    SOUTH_SOUTHEAST = "south-southeast"
    SOUTH = "south"
    SOUTH_SOUTHWEST = "south-southwest"
    SOUTH_WEST = "south-west"
    WEST_SOUTHWEST = "west-southwest"
    WEST = "west"
    WEST_NORTHWEST = "west-northwest"
    NORTH_WEST = "north-west"
    NORTH_NORTHWEST = "north-northwest"


class DegreesRanges(Enum):
    DEFAULT_STEP = Decimal(str(0.01))
    NORTH_A_START = Decimal(str(348.75))
    NORTH_A_STOP = Decimal(str(360))
    NORTH_B_START = Decimal(str(0))
    NORTH_B_STOP = Decimal(str(11.25))
    NORTH_NORTHEAST_START = Decimal(str(11.25))
    NORTH_NORTHEAST_STOP = Decimal(str(33.75))
    NORTH_EAST_START = Decimal(str(33.75))
    NORTH_EAST_STOP = Decimal(str(56.25))
    EAST_NORTHEAST_START = Decimal(str(56.25))
    EAST_NORTHEAST_STOP = Decimal(str(78.75))
    EAST_START = Decimal(str(78.75))
    EAST_STOP = Decimal(str(101.25))
    EAST_SOUTHEAST_START = Decimal(str(101.25))
    EAST_SOUTHEAST_STOP = Decimal(str(123.75))
    SOUTH_EAST_START = Decimal(str(123.75))
    SOUTH_EAST_STOP = Decimal(str(146.25))
    SOUTH_SOUTHEAST_START = Decimal(str(146.25))
    SOUTH_SOUTHEAST_STOP = Decimal(str(168.75))
    SOUTH_START = Decimal(str(168.75))
    SOUTH_STOP = Decimal(str(191.25))
    SOUTH_SOUTHWEST_START = Decimal(str(191.25))
    SOUTH_SOUTHWEST_STOP = Decimal(str(213.75))
    SOUTH_WEST_START = Decimal(str(213.75))
    SOUTH_WEST_STOP = Decimal(str(236.25))
    WEST_SOUTHWEST_START = Decimal(str(236.25))
    WEST_SOUTHWEST_STOP = Decimal(str(258.75))
    WEST_START = Decimal(str(258.75))
    WEST_STOP = Decimal(str(281.25))
    WEST_NORTHWEST_START = Decimal(str(281.25))
    WEST_NORTHWEST_STOP = Decimal(str(303.75))
    NORTH_WEST_START = Decimal(str(303.75))
    NORTH_WEST_STOP = Decimal(str(326.25))
    NORTH_NORTHWEST_START = Decimal(str(326.25))
    NORTH_NORTHWEST_STOP = Decimal(str(348.75))


class ApiViewConstants(Enum):
    ERROR_MESSAGE = "error_message"
