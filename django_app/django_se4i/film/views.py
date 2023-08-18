from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Film
from json import dumps


def index(request):
    return JsonResponse(" Index", safe=False)


def show(request):
    users = dumps(list(Film.objects.all()))
    return JsonResponse(users, safe=False)
    #films = Film.objects.all()
    #return render(request, "film.html", {'films': films})
