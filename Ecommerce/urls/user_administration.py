from django.urls import path
from django.views.generic import TemplateView

from Ecommerce import views

urlpatterns_user = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('logout_page/', TemplateView.as_view(template_name='logout.html'), name='logout_page'),
]