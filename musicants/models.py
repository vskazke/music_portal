from django.db import models

class Musicants(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    pub_date = models.DateTimeField('date published')
