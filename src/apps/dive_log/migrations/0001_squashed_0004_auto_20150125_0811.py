# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    #replaces = [(b'dive_log', '0001_squashed_0003_auto_20150125_0429'), (b'dive_log', '0002_dive_duration'), (b'dive_log', '0003_auto_20150125_0804'), (b'dive_log', '0004_auto_20150125_0811')]

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
        ),
        migrations.AddField(
            model_name='dive',
            name='session',
            field=models.ForeignKey(to='dive_log.Session'),
        ),
        migrations.AddField(
            model_name='dive',
            name='discipline',
            field=models.ForeignKey(verbose_name='Disciplin', blank=True, to='discipline.Discipline', null=True),
        ),
        migrations.RemoveField(
            model_name='dive',
            name='rest_duration',
        ),
        migrations.RemoveField(
            model_name='dive',
            name='dive_duration',
        ),
        migrations.AddField(
            model_name='dive',
            name='dive_duration',
            field=models.DurationField(null=True, verbose_name='Dyktid', blank=True),
        ),
        migrations.AddField(
            model_name='dive',
            name='rest_duration',
            field=models.DurationField(null=True, verbose_name='Vila', blank=True),
        ),
        migrations.AlterField(
            model_name='dive',
            name='distance',
            field=models.IntegerField(help_text='i meter', null=True, verbose_name='Distans'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='temperature',
            field=models.IntegerField(help_text='i celsius', null=True, verbose_name='Temperatur', blank=True),
        ),
    ]
