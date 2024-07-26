from django.db.models import Model
from django.db import models


class Identification(Model):
    NIF_NIE = models.CharField(unique=True, max_length=10) ###TODO: Add validator
    is_National = models.BooleanField(default=False)