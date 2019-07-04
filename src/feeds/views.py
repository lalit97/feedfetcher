from django.shortcuts import render, HttpResponse



def home_view(request):
    return HttpResponse('Hello world!')