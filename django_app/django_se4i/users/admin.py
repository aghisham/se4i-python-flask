from django.contrib import admin
from .models import User


class UserAdminView(admin.ModelAdmin):
    """Class UserAdminView"""

    list_display = ["name", "email"]


admin.site.register(User, UserAdminView)
