# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dive_log', '0001_squashed_0004_auto_20150125_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('second', models.IntegerField(verbose_name='Sekund')),
                ('depth', models.DecimalField(null=True, verbose_name='Djup', max_digits=4, decimal_places=1, blank=True)),
                ('temperature', models.DecimalField(null=True, verbose_name='Temperatur', max_digits=3, decimal_places=1, blank=True)),
                ('heart_rate', models.IntegerField(null=True, verbose_name='Puls', blank=True)),
                ('dive', models.ForeignKey(to='dive_log.Dive')),
            ],
            options={
                'verbose_name': 'Datapunkt',
                'verbose_name_plural': 'Datapunkter',
            },
        ),
    ]
