"""
weather.admin
-------------
Model admin register file
"""
from django.contrib import admin
from . import models


class CityWeatherAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'slug',
        'country_slug',
    )
    list_display = (
        'name',
        'slug',
        'country_slug',
        'created_at',
        'updated_at',
    )

    search_fields = [
        'name',
        'slug',
        'country_slug',
    ]


admin.site.register(models.CityWeather, CityWeatherAdmin)


class LogResponseAdmin(admin.ModelAdmin):

    fields = (
        'status_response',
        'response',
        'log_date',
    )
    list_display = (
        'status_response',
        'response',
        'log_date',
        'created_at',
        'updated_at',
    )

    search_fields = [
        'status_response',
        'response',
        'log_date',
    ]


admin.site.register(models.LogResponse, LogResponseAdmin)


class CityWeatherLogAdmin(admin.ModelAdmin):

    fields = (
        'city',
        'response_log',
    )
    list_display = (
        'city',
        'response_log',
        'created_at',
        'updated_at',
    )

    search_fields = [
        'city',
        'response_log',
    ]


admin.site.register(models.CityWeatherLog, CityWeatherLogAdmin)
