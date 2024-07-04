from django.urls import path

from Ecommerce import views

urlpatterns_site = [path('error/', views.error, name='error'),
                    ]