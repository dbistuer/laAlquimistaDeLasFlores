from enum import Enum

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _


# Create your views here.
# Home page
from Ecommerce.models import User, Identification, Address
from Ecommerce.paths import get_path
from Ecommerce.paths.types import Type_Path
from Ecommerce.paths.user import User_Path


def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        user = get_user_POST(request)
        if validate_user(user):
            user.identification.save()
            user.save()
            return redirect('login')
    elif request.method == 'GET':
        return render(request, get_path(Type_Path.USER,User_Path.SIGNUP))
    else:
        return render(request, get_path(Type_Path.USER,User_Path.SIGNUP))
    return render(request, get_path(Type_Path.USER,User_Path.SIGNUP))

# login page
def user_login(request):
    if request.method == 'POST':
        user = get_user_POST(request)
        user = authenticate(request, username=user.username, password=user.password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        return render(request, get_path(Type_Path.USER,User_Path.LOGIN))
    return render(request, get_path(Type_Path.USER,User_Path.LOGIN),)

# logout page
def user_logout(request):
    logout(request)
    return redirect('logout_page')


#getter from POST
def get_user_form(request,is_client=True):
    user = User()
    user.is_client = is_client
    user.username = get_value_POST(request,'username')
    user.password = get_value_POST(request, 'password')
    user.email = get_value_POST(request,'email')
    user.first_name = get_value_POST(request,'first_name')
    user.last_name = get_value_POST(request,'last_name')
    user.phone = get_value_POST(request,'phone')
    user.address = get_value_POST(request,'address')
    user.city = get_value_POST(request,'city')
    user.province = get_value_POST(request,'province')
    user.postal_code = get_value_POST(request,'postal_code')
    user.country = get_value_POST(request,'country')
    identification = Identification()
    isNational = True
    if isNational:
        identification.NIF = get_value_POST('NIF')
        identification.is_National = True
    else:
        identification.NIE = get_value_POST('NIE')
        identification.is_National = False

def get_value_POST(request, key):
    return request.POST[key]

def get_user_POST(request):
    user = User()
    keys = ['username', 'password', 'email', 'first_name', 'last_name', 'phone']
    for key in keys:
        if key in request.POST.keys():
            user.__setattr__(key,get_value_POST(request, key))

    identification = get_identification_POST(request)
    user.identification = identification
    return user

def get_identification_POST(request):
    identification = Identification()
    doc_type = ''
    if request.POST.get('NIE',False) == False:
        identification.is_National = True
    else:
        identification.is_National = False
    identification.__setattr__('NIF_NIE',get_value_POST(request,'identification'))
    return identification

def get_address_POST(request):
    address = Address()
    keys = ['address', 'city', 'province', 'postal_code', 'country']
    for key in keys:
        if key in request.POST.keys():
            address.__setattr__(key,get_value_POST(request, key))
    return address

#validate user
def validate_user(user):
    return True
