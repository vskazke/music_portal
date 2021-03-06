# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musicants', '0024_auto_20170330_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 31, 7, 49, 8, 769855, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='musicant',
            name='type_of_music',
            field=models.CharField(default='', error_messages={'required': 'Please enter your name'}, max_length=100, verbose_name='Направление музыки'),
        ),
    ]
