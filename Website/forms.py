from django import forms
from .models import Budget
from .models import EmailSignup


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['budget_name', 'earned_income', 'housing_expense', 'food_expense', 'medical_expense',
                  'child_care_expense', 'taxes']


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailSignup
        fields = ['email']
