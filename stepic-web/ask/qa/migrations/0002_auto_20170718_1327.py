# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
    ]
