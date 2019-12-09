from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task
from .models import ScoreCard


@shared_task
def get_number():
    url = 'http://mapps.cricbuzz.com/cbzios/match/24129/scorecard'
    resp = requests.get(url).json()
    current = resp['Innings'][0]
    score = current['score']
    wicket = current['wkts']
    overs = current['ovr']
    ScoreCard.objects.create(score=score, wicket=wicket, overs=overs)
    return 'Score Saved Successfully!'