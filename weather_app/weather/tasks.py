"""
weather.tasks
-------------
Celery tasks file
"""
from datetime import datetime, timedelta

from celery import shared_task


@shared_task(name='make_asyncapi_call')
def make_asyncapi_call():
    print("test")


def schedule_api_call(city_name: str, country_slug: str):
    make_asyncapi_call.apply_async(eta=datetime.now() + timedelta(seconds=10))
