# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music_portal', '0003_auto_20170331_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='sing_in',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Пароль'),
            preserve_default=False,
        ),
    ]
