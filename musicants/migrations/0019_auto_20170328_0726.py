# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 07:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musicants', '0018_auto_20170328_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 28, 7, 26, 32, 222358, tzinfo=utc), verbose_name='date published'),
        ),
    ]
