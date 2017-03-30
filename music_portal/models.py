from django.db import models


class Login(models.Model):
    name = models.CharField('Имя', max_length=200)


class Sing_in(models.Model):
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField()
