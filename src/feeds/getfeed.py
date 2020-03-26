'''
https://docs.python.org/3/library/xml.etree.elementtree.html
'''

import requests
import xml.etree.ElementTree as ET
from .models import RssUrl, News


def create_models(response):
    root = ET.fromstring(response.content)
    for news in root.iter('item'):
        title = news.find('title').text
        description = news.find('description').text
        link = news.find('link').text
        News.objects.create(title= title, description=description, link= link)
