from django import forms
from .models import *


class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    
    class Meta:
        model = Login
        exclude = ['']

