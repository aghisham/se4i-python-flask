from json import dumps
from django.http import JsonResponse
from .models import User


def get_all(request):
    """Get all users"""
    users = dumps(list(User.objects.all()))
    return JsonResponse(users, safe=False)


def get_user(request, user_id):
    """Get user by id"""
    try:
        users = dumps(User.objects.get(pk=user_id))
        return JsonResponse(users, safe=False)
    except:
        return JsonResponse("Not exist", safe=False)
