from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import redirect, render
from Expensesmanagement.models import Expense, Category
from django.forms import modelform_factory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

def login(request):
    if request.user.is_authenticated:
        return render(request, 'Expensesmanagement/Dashboard.html')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return render(request, 'Expensesmanagement/Dashboard.html')
        else:
            return render(request, 'website/Login.html', {'form': form})
    form = AuthenticationForm()
    return render(request, 'website/Login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('welcome')

def welcome(request):
    return render(request, 'website/welcome.html')

def register(request):
    if request.user.is_authenticated:
        return render(request, 'Expensesmanagement/Dashboard.html')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    
    return render(request, 'website/Register.html', {'form': form})

# Create your views here.
