'''
https://docs.python.org/3/library/xml.etree.elementtree.html
'''

import requests
import xml.etree.ElementTree as ET


url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
response = requests.get(url)
root = ET.fromstring(response.content)


for news in root.iter('item'):
    title = news.find('title').text
    description = news.find('description').text
    link = news.find('link').text
    date = news.find('pubDate').text
    print('Title -> {}\n'.format(title))
    print('Description -> {}\n'.format(description))
    print('Full story -> {}\n'.format(link))
    print('Date Published -> {}\n'.format(date))
    print('_____________________________________________')
