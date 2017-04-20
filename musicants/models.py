from django.db import models
from django.utils import timezone
from music_portal.models import Sing_in
from django.contrib.auth.models import User



class Musicant(models.Model):
    LEVEL = (
            ('elementary', 'Начальный'),
            ('average', 'Средний'),
            ('high', 'Высокий'),
            ('professional', 'Профессионал'),
    )
    musicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField()
    type_of_music = models.CharField('Направление музыки', max_length=100, default='', error_messages={'required': 'Please enter your name'})
    instrument = models.CharField('Музыкальный инструмент', max_length=200, default='')
    level = models.CharField('Уровень владения инструментом', max_length=50, choices=LEVEL, default='')
    public = models.BooleanField(default=False)
    #  pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.name

    


