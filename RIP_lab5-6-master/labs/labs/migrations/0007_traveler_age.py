# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0006_remove_traveler_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='age',
            field=models.IntegerField(blank=True, default=19),
            preserve_default=False,
        ),
    ]
