# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eddb', '0003_auto_20171029_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='edsm_id',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
