# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0002_auto_20170329_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='name',
            field=models.CharField(error_messages={'required': 'something...'}, max_length=200, verbose_name='Имя'),
        ),
    ]