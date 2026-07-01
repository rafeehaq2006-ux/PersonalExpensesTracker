from django.shortcuts import redirect, render
from django.forms import modelform_factory

from Expensesmanagement.models import Expense
from .forms import ExpenseForm, CategoryForm

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'Expensesmanagement/Dashboard.html')

def add_expense(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return render(request, 'Expensesmanagement/Dashboard.html')
        else:
            return render(request, 'Expensesmanagement/AddExpense.html', {'form': form})
    else:
        form = ExpenseForm()
    return render(request, 'Expensesmanagement/AddExpense.html', {'form': form})

def view_expenses(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'Expensesmanagement/ViewExpenses.html', {'expenses': Expense.objects.filter(user=request.user)})

def add_category(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            print('USER:', request.user)
            print('USER ID:', request.user.id)
            category.save()
            return render(request, 'Expensesmanagement/Dashboard.html')
        else:
            return render(request, 'Expensesmanagement/AddCategory.html', {'form': form})
    else:
        form = CategoryForm()
    return render(request, 'Expensesmanagement/AddCategory.html', {'form': form})
# Create your views here.
