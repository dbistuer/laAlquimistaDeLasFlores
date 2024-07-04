from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

# Create your models here.


class Identification(Model):
    NIF_NIE = models.CharField(unique=True, max_length=10) ###TODO: Add validator
    is_National = models.BooleanField(default=False)


class CreditCard(Model):
    card_number = models.CharField(unique=True, max_length=16)
    card_holder = models.CharField(max_length=50)
    expiration_date = models.DateField()
    security_code = models.CharField(max_length=3)


class Address(Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50,null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=14, null=True, blank=True)
    identification = models.OneToOneField(Identification, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)


class Client(Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.DO_NOTHING, null=True, blank=True)


class Employee(Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    is_manager = models.BooleanField(default=False)