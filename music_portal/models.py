from django.db import models


class Login(models.Model):
    name = models.CharField('Имя', max_length=200, error_messages={'required': "something..."})
    
    def __str__(self):
        return self.name


class Sing_in(models.Model):
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField()
    password = models.CharField('Пароль', max_length=200)

    def __str__(self):
        return self.name

