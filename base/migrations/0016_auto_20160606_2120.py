# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20160906_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorizzazione',
            name='scadenza',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='autorizzazione',
            name='tipo_gestione',
            field=models.CharField(choices=[('M', 'Manuale'), ('A', 'Approvazione automatica'), ('N', 'Negazione automatica')], default='M', max_length=1),
        ),
    ]