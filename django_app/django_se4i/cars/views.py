from django.shortcuts import render,HttpResponse

from .models import Car


def home(request):
    return render(request, "list_cars.html")

def get_cars(request):
    """Get all cars"""
    cars = Car.objects.all()
    return render(request, "cars/list_cars.html", {'list': cars})