from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import RssUrl, News


def home_view(request):
    LatestNews = News.objects.all().last()
    title = LatestNews.title
    description = LatestNews.description
    link = LatestNews.link
    response = {
        'title': title,
        'description': description,
        'full_story': link
    }
    return JsonResponse(response)