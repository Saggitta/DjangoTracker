from django import forms
from django.forms import ModelForm

from .models import Expense, Income


# Create a expense form
class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        # specify fields to include in form from Model
        fields = "__all__"
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "currency": forms.Select(attrs={"class": "form-control"}),
            "type": forms.TextInput(attrs={"class": "form-control"}),
        }


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = "__all__"
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "currency": forms.Select(attrs={"class": "form-control"}),
            "type": forms.TextInput(attrs={"class": "form-control"}),
        }
