# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests


@shared_task
def get_number():
    url = 'http://mapps.cricbuzz.com/cbzios/match/livematches'
    resp = requests.get(url).json()
    return resp