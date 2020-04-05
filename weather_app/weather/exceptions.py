"""
weather.exceptions
------------------
Exceptions for weather django app
"""


class CityDoesNotExistsException(Exception):
    def __init__(self, message: str = None, *args, **kwargs):
        if message is None:
            message = "The queried city object doesn exists"

        Exception.__init__(self, message, *args, **kwargs)


class APIRequestException(Exception):
    def __init__(self, message: str = None, *args, **kwargs):
        if message is None:
            message = "The call to the API didn't return 200"

        Exception.__init__(self, message, *args, **kwargs)

