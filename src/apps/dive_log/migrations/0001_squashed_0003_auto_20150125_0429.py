# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'dive_log', '0001_initial'), (b'dive_log', '0002_dive_discipline'), (b'dive_log', '0003_auto_20150125_0429')]

    dependencies = [
        ('discipline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField(null=True, blank=True)),
                ('rest_duration', models.IntegerField(help_text='Sekunder', null=True, verbose_name='Vila innan')),
                ('dive_duration', models.IntegerField(help_text='Sekunder', null=True, verbose_name='Dyktid', blank=True)),
                ('distance', models.IntegerField(null=True, verbose_name='Distans')),
                ('temperature', models.IntegerField(null=True, verbose_name='Temperatur', blank=True)),
                ('comment', models.CharField(max_length=512, verbose_name='Kommentar', blank=True)),
            ],
            options={
                'verbose_name': 'Dyk',
                'verbose_name_plural': 'Dyk',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Datum')),
                ('time', models.TimeField(verbose_name='Tid')),
                ('comment', models.CharField(max_length=512, verbose_name='Kommentar', blank=True)),
            ],
            options={
                'ordering': ['date', 'time'],
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessioner',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dive',
            name='session',
            field=models.ForeignKey(to='dive_log.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dive',
            name='discipline',
            field=models.ForeignKey(blank=True, to='discipline.Discipline', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dive',
            name='rest_duration',
            field=models.IntegerField(help_text='Sekunder', null=True, verbose_name='Vila innan', blank=True),
            preserve_default=True,
        ),
    ]
