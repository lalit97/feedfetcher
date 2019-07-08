from django.shortcuts import render, HttpResponse
from .tasks import get_number


def home_view(request):
    resp = get_number.delay()
    return HttpResponse('hello world!')


    #url = resp['url']['match']
