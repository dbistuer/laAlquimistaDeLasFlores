from django.db import models
from django.db.models import Model


class Address(Model):
    street = models.CharField(max_length=200)
    floor = models.IntegerField()
    door = models.IntegerField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)