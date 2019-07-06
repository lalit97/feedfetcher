from django.shortcuts import render, HttpResponse
from .tasks import get_number


def home_view(request):
    num = get_number()
    return HttpResponse(num)