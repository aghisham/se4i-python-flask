from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path("", views.get_all, name="all_users"),
    path("<int:user_id>", views.get_user, name="get_user"),
]
