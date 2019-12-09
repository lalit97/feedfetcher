from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .tasks import get_number
from .models import ScoreCard

def home_view(request):
    get_number.delay()  # will store result for the next call
    LatestScore = ScoreCard.objects.all().last()
    score = LatestScore.score
    wicket = LatestScore.wicket
    overs = LatestScore.overs
    response = {
        'score': score,
        'wicket': wicket,
        'overs': overs
    }
    return JsonResponse(response)