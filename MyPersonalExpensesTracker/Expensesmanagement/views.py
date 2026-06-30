from django.shortcuts import redirect, render

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'Expensesmanagement/Dashboard.html')

def add_expense(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'Expensesmanagement/AddExpense.html')

def view_expenses(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'Expensesmanagement/ViewExpenses.html')
# Create your views here.
