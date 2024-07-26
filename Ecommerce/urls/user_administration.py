
from django.urls import path, include
from django.views.generic import TemplateView

from Ecommerce import views

urlpatterns_user = [
    #path('accounts/login/', views.user_login, name='login'),
    path('accounts/signup/', views.user_signup, name='signup'),
    path('accounts/password_reset/', views.send_email, name='password_reset'),
    path('accounts/password_reset_done/', TemplateView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('accounts/logout/done/', TemplateView.as_view(template_name='registration/logout_done.html'), name='logout_done'),

]
