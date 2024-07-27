from django.db import models
from django.db.models import Model


class CreditCard(Model):
    number = models.CharField(unique=True, max_length=16)
    holder = models.CharField(max_length=50)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)