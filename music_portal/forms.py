from django import forms
from .models import *


class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    
    class Meta:
        model = Login
        exclude = ['']

    def clean(self):
        username = self.cleaned_data['name']
        password = self.cleaned_data['password']

        if not username or not password:
            raise forms.ValidationError('ddddd')




class Sing_in(forms.ModelForm):
    #  name = forms.CharField(error_messages={'required': 'this field is required'})
    #  email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 
    
    class Meta:
        model = Sing_in
        exclude = ['']


