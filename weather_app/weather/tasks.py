"""
weather.tasks
-------------
Celery tasks file
"""
from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings

from weather.open_weather_utils import OpenWeather


@shared_task(name='make_async_api_call')
def make_async_api_call(city_name: str, country_slug: str):
    """
    Save the data log for A specific city
    :param city_name: Identifier for the city
    :param country_slug: Identifier fot the country
    """
    open_weather = OpenWeather(
        city_name=city_name,
        country_slug=country_slug
    )
    open_weather.retrieve_weather_data()


def schedule_api_call(city_name: str, country_slug: str):
    """
    Sends to execute a the data log for A specific city
    :param city_name: Identifier for the city
    :param country_slug: Identifier fot the country
    """
    kwargs = dict(
        city_name=city_name,
        country_slug=country_slug,
    )
    make_async_api_call.apply_async(
        kwargs=kwargs,
        eta=(datetime.now() + timedelta(seconds=settings.TIME_ELAPSE_FOR_TASK))
    )

