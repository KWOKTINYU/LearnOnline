# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_remove_userfavorite_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '\u8bfe\u7a0b'), (2, '\u8bfe\u7a0b\u673a\u6784'), (3, '\u8bb2\u5e08')], default=2, verbose_name='\u6536\u85cf\u7c7b\u578b '),
        ),
    ]
