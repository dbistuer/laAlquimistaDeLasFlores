from django.urls import path
from django.views.generic import TemplateView

from Ecommerce import views

urlpatterns_site = [
    path('error/', views.error, name='error'),
]