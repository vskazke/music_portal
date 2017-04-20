from django import forms
from .models import *


class MusicantForm(forms.ModelForm):
    
    INSTRUMENT = (
            ('gitar', 'Гитара'),
            ('piano', 'Пианино'),
            ('violanchel', 'Виолончель'),
            ('skripka', 'Скрипка'),
            ('barabani', 'Барабаны'),
            ('bokal', 'Вокал'),
    )
    instrument = forms.MultipleChoiceField(
        label='Музыкальный инструмент',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=INSTRUMENT,
    )

    class Meta:
        model = Musicant
        exclude = ['pub_date', 'musicant', 'public']
