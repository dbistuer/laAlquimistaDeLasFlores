from django.db import models
from django.db.models import Model


class Address(Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)