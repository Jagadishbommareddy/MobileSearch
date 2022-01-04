from .models import *
from django import forms
class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name']