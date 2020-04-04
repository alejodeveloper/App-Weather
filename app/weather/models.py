"""
weather.models
--------------
Model for the weather app
"""

from django.db import models


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


class CityWeatherLog(models.Model):
    """
    Model to associate the response to the model
    """
    city = models.ForeignKey(
        CityWeather, null=False, blank=False, on_delete=models.SET_NULL
    )
    log = models.ForeignKey(
        LogResponse, null=False, blank=False, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
