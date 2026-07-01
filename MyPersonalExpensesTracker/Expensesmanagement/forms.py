from .models import Category, Expense
from django.forms import DateInput, ModelForm, NumberInput
from django.core.exceptions import ValidationError

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'amount': NumberInput(attrs={'type': 'number', 'step': '0.01'})  
        }
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be a positive number.")
        return amount
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is not None and date > date.today():
            raise ValidationError("Date cannot be in the future.")
        return date

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        exclude = ['user']
        widgets = {
            'name': NumberInput(attrs={'type': 'text'})
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise ValidationError("Category name cannot be empty.")
            return name