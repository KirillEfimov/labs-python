# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
