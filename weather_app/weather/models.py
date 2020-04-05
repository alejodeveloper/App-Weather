"""
weather.models
--------------
Model for the weather app
"""
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from .exceptions import CityDoesNotExistsException


class CityWeather(models.Model):
    """
    Class model for city
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=25, null=False, blank=False)
    country_slug = models.CharField(max_length=25, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["name", "slug"]),
            models.Index(fields=["country_slug"])
        ]

    @classmethod
    def get_city(cls, city_slug: str):
        """
        Get a CityWeather object by its slug
        :param city_slug: Slug identifier of the city
        :return: A instance of CityWeather
        """
        try:
            city = cls.objects.get(slug=city_slug)
            return city
        except ObjectDoesNotExist:
            exception_message = f"The city with slug {city_slug} doesn't exists"
            raise CityDoesNotExistsException(exception_message)


class LogResponse(models.Model):
    """
    Class model for logging the API response
    """
    log_date = models.DateField(blank=False, null=False)
    response = models.TextField(null=False, blank=False)
    status_response = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["log_date", "status_response"])
        ]

    @classmethod
    def save_log_response(cls, status_code: int, response_data: dict):
        """
        Saves a log for a specific response to the API
        :param status_code: Status code of the response
        :param response_data: Response data
        :return: The instance created for the data
        """
        created_log = cls.objects.create(
            log_date=date.today(),
            status_response=status_code,
            response=response_data
        )

        return created_log


class CityWeatherLog(models.Model):
    """
    Model to associate the response to the model
    """
    city = models.ForeignKey(
        CityWeather, null=True, blank=True, on_delete=models.SET_NULL
    )
    response_log = models.ForeignKey(
        LogResponse, null=False, blank=False, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_city_weather_log(
            cls, city_slug: str, status_code: int, response_data: dict
    ):
        """
        Saves a log response for a specific city
        :param city_slug: Slug identifier of the city
        :param status_code: Status code of the response
        :param response_data: Response data from the request
        """
        city = CityWeather.get_city(city_slug)
        response_log = LogResponse.save_log_response(
            status_code=status_code,
            response_data=response_data
        )
        cls.objects.create(
            city=city,
            response_log=response_log
        )