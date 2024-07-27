

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# Home page
from Ecommerce.models import User, Identification, Address


def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        keys = ['username', 'password', 'email', 'first_name', 'last_name', 'phone']
        user = get_user_POST(request,keys)
        if validate_user(user):
            user.identification.save()
            user.save()
            return redirect('login')
    elif request.method == 'GET':
        return render(request,'registration/signup.html')
    else:
        return render(request, 'registration/signup.html')

# login page
def user_login(request):
    if request.method == 'POST':
        keys = ['username', 'password']
        user = get_user_POST(request,keys,False)
        user = authenticate(username=user.username, password=user.password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'registration/login.html')

# logout page
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('logout_done')
    else:
        return redirect('error')


#getter from POST
def get_value_POST(request, key):
    return request.POST[key]

def get_user_POST(request,keys,get_identification=True):
    user = User()
    for key in keys:
        if key in request.POST.keys():
            if key == 'password':
                user.set_password(get_value_POST(request, key))
            else:
                user.__setattr__(key,get_value_POST(request, key))
    if get_identification:
        identification = get_identification_POST(request)
        user.identification = identification
    return user

def get_identification_POST(request):
    identification = Identification()
    doc_type = ''
    if request.POST.get('NIF',False) == True:
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
def validate_user(user): ##TODO: validate user
    return True
