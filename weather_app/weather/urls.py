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
        'weather',
        views.WeatherAPI.as_view(),
        name='weather_url',
    ),
]