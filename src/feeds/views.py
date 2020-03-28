from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import RssUrl, News
from rest_framework import generics
from .serializers import NewsSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by('-id')[:5]
    serializer_class = NewsSerializer
