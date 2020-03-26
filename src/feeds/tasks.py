from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task
from .getfeed import create_models
from .models import RssUrl


@shared_task
def get_xml_data():
    Urls = RssUrl.objects.all()
    for url in Urls:
        url = url.url
        response = requests.get(url)
        create_models(response)
        return 'Feeds Saved Successfully!'