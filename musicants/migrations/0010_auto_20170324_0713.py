# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicants', '0009_auto_20170324_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicant',
            name='instrument',
            field=models.CharField(default='', max_length=200, verbose_name='Музыкальный инструмент'),
        ),
        migrations.AlterField(
            model_name='musicant',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='musicant',
            name='type_of_music',
            field=models.CharField(default='', max_length=100, verbose_name='Направление музыки'),
        ),
    ]