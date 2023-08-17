from django.db import models


class User(models.Model):
    """User model"""

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
