# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-21 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmaerd', '0004_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]