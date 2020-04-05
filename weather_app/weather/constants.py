from decimal import Decimal
from enum import Enum

from weather.utils import decimal_range


class ApiConstants(Enum):
    OK_STATUS_CODE = 200


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
    NORTH_A = decimal_range(
            start=Decimal(str(348.75)),
            stop=Decimal(str(360)),
            step=Decimal(str(0.01))
    )
    NORTH_B = decimal_range(
        start=Decimal(str(0)),
        stop=Decimal(str(11.25)),
        step=Decimal(str(0.01))
    )
    NORTH_NORTHEAST = decimal_range(
            start=Decimal(str(11.25)),
            stop=Decimal(str(33.75)),
            step=Decimal(str(0.01))
    )
    NORTH_EAST = decimal_range(
            start=Decimal(str(33.75)),
            stop=Decimal(str(56.25)),
            step=Decimal(str(0.01))
    )
    EAST_NORTHEAST = decimal_range(
            start=Decimal(str(56.25)),
            stop=Decimal(str(78.75)),
            step=Decimal(str(0.01))
    )
    EAST = decimal_range(
            start=Decimal(str(78.75)),
            stop=Decimal(str(101.25)),
            step=Decimal(str(0.01))
    )
    EAST_SOUTHEAST = decimal_range(
            start=Decimal(str(101.25)),
            stop=Decimal(str(123.75)),
            step=Decimal(str(0.01))
    )
    SOUTH_EAST = decimal_range(
            start=Decimal(str(123.75)),
            stop=Decimal(str(146.25)),
            step=Decimal(str(0.01))
    )
    SOUTH_SOUTHEAST = decimal_range(
            start=Decimal(str(146.25)),
            stop=Decimal(str(168.75)),
            step=Decimal(str(0.01))
    )
    SOUTH = decimal_range(
            start=Decimal(str(168.75)),
            stop=Decimal(str(191.25)),
            step=Decimal(str(0.01))
    )
    SOUTH_SOUTHWEST = decimal_range(
            start=Decimal(str(191.25)),
            stop=Decimal(str(213.75)),
            step=Decimal(str(0.01))
    )
    SOUTH_WEST = decimal_range(
            start=Decimal(str(213.75)),
            stop=Decimal(str(236.25)),
            step=Decimal(str(0.01))
    )
    WEST_SOUTHWEST = decimal_range(
            start=Decimal(str(236.25)),
            stop=Decimal(str(258.75)),
            step=Decimal(str(0.01))
    )
    WEST = decimal_range(
            start=Decimal(str(258.75)),
            stop=Decimal(str(281.25)),
            step=Decimal(str(0.01))
    )
    WEST_NORTHWEST = decimal_range(
            start=Decimal(str(281.25)),
            stop=Decimal(str(303.75)),
            step=Decimal(str(0.01))
    )
    NORTH_WEST = decimal_range(
            start=Decimal(str(303.75)),
            stop=Decimal(str(326.25)),
            step=Decimal(str(0.01))
    )
    NORTH_NORTHWEST = decimal_range(
            start=Decimal(str(326.25)),
            stop=Decimal(str(348.75)),
            step=Decimal(str(0.01))
    )
