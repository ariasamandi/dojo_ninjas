# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-17 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20180417_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='my_app.Dojo'),
        ),
    ]
