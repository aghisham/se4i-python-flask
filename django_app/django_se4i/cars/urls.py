from django.urls import path
from . import views


app_name = "cars"
urlpatterns = [
    path("", views.get_all, name="all_cars")
]
