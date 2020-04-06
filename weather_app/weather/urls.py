"""
weather.urls
------------
Urls route for the weather app
"""
from . import views
from django.urls import path

app_name = 'weather_urls'

urlpatterns = [
    path(
        'v1/weather',
        views.WeatherAPI.as_view(),
        name='weather_url',
    ),
    path(
        'v2/weather',
        views.WeatherLogAPI.as_view(),
        name='weather_url_v2',
    ),
]