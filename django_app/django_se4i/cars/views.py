from json import dumps
from django.http import JsonResponse
from .models import Car

def get_all(request):
    """Get all cars"""
    cars = dumps(list(Car.objects.all()))
    return JsonResponse(cars, safe=False)