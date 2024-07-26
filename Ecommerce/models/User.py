from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

from Ecommerce.models.Address import Address
from Ecommerce.models.CreditCard import CreditCard
from Ecommerce.models.Identification import Identification


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50,null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    identification = models.OneToOneField(Identification, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)

class Client(Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.DO_NOTHING, null=True, blank=True)

class Employee(Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    is_manager = models.BooleanField(default=False)