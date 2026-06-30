from django.shortcuts import redirect, render
from django.forms import modelform_factory

from Expensesmanagement.models import Expense
from .forms import ExpenseForm

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
    return render(request, 'Expensesmanagement/ViewExpenses.html')

# Create your views here.
