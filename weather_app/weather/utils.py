"""
weather.utils
-------------
Utility file for diverse purposes
"""
from datetime import datetime
from decimal import Decimal


def decimal_range(
        start: Decimal = Decimal(str(0)),
        stop: Decimal = Decimal(str(1)),
        step: Decimal = Decimal(str(0.1))
):
    """
    Utility function to make a range between decimals
    :param start: Decimal that indicates the begin of range 0.0 by default
    :param stop: Decimal that indicates the end of range by default 1
    :param step: Decimal that indicates the step between values of the range
    0.1 by default
    :return: a generator with the range values
    """

    while start < stop:
        yield start
        start += step


def transform_number_date(timestamp: int) -> datetime:
    """
    Transform a timestamp into a datetime object
    :param timestamp: Integer with the timestamp value
    :return: A datetime object from the timestamp
    """
    date_return = datetime.fromtimestamp(timestamp)

    return date_return
