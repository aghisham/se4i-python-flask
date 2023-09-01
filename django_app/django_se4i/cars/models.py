from django.db import models


class Car(models.Model):

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    des = models.CharField(max_length=200)

    def __str__(self):
        return self.id
    