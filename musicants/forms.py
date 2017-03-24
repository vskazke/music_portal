from django import forms
from .models import *


class Musicant(forms.ModelForm):
          
    class Meta:
        model = Musicant
        exclude = ['']

