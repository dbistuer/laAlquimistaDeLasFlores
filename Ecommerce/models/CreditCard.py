from django.db import models
from django.db.models import Model


class CreditCard(Model):
    card_number = models.CharField(unique=True, max_length=16)
    card_holder = models.CharField(max_length=50)
    expiration_date = models.DateField()
    security_code = models.CharField(max_length=3)