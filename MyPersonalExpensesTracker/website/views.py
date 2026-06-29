from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from Expensesmanagement.models import Expense, Category, User  
from django.forms import modelform_factory
from django.core.exceptions import ObjectDoesNotExist

UserForm = modelform_factory(User, exclude=[])

def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username, password=password).exists():
                user = User.objects.get(username=username, password=password)
                # redirect to the user's dashboard
    else:
        return render(request, 'website/login.html', {'error': 'Invalid username or password'})

def welcome(request):
    return HttpResponse("Welcome to the Personal Expenses Tracker!")
# Create your views here.
