
from Expensesmanagement import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('view_expenses/', views.view_expenses, name='view_expenses'),
    path('add_category/', views.add_category, name = 'add_category'),
]