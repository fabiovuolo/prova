# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-06-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0006_auto_20170127_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolosegmento',
            name='sedi_sottostanti',
            field=models.BooleanField(db_index=True, default=False, help_text='Se selezionato, il segmento viene applicato utilizzando la sede selezionata e le sedi sottostanti.'),
        ),
    ]
