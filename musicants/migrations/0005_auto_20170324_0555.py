# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 05:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicants', '0004_musicants_instrument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicants',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='musicants',
            name='tipe_of_music',
        ),
    ]
