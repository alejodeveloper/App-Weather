"""
weather.tasks
-------------
Celery tasks file
"""
from celery import Celery

celery_app = Celery()


@celery_app.task(name='make_asyncapi_call')
def make_asyncapi_call(city_name: str, country_slug: str):
    print("tes")


def schedule_api_call(city_name: str, country_slug: str):
    celery_app.conf.beat_schedule = {
        'add-every-3600-seconds': {
            'task': 'tasks.make_asyncapi_call',
            'schedule': 5.0,
            'args': (city_name, country_slug)
        },
    }