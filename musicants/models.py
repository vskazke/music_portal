from django.db import models
import datetime

now = datetime.datetime.now()


class Musicant(models.Model):
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField()
    type_of_music = models.CharField('Направление музыки', max_length=100, default='')
    instrument = models.CharField('Музыкальный инструмент', max_length=200, default='')
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
