# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-14 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170514_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='male', max_length=6),
        ),
    ]
