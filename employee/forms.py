from django import forms
from django.forms import fields
from django.forms.models import model_to_dict
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
