# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [(b'dive_log', '0001_initial'), (b'dive_log', '0002_auto_20150124_2359'), (b'dive_log', '0003_auto_20150125_0020')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField()),
                ('stop', models.TimeField()),
                ('distance', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('comment', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('stop', models.TimeField()),
                ('comment', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dive',
            name='session',
            field=models.ForeignKey(to='dive_log.Session'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dive',
            name='distance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='dive',
            options={'verbose_name': 'Dyk'},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['date', 'time'], 'verbose_name': 'Session', 'verbose_name_plural': 'Sessioner'},
        ),
        migrations.RemoveField(
            model_name='session',
            name='start',
        ),
        migrations.RemoveField(
            model_name='session',
            name='stop',
        ),
        migrations.AddField(
            model_name='session',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 1, 24, 23, 20, 4, 175295, tzinfo=utc), verbose_name='Tid'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dive',
            name='comment',
            field=models.CharField(max_length=512, verbose_name='Kommentar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dive',
            name='distance',
            field=models.IntegerField(default=0, verbose_name='L\xe4ngd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dive',
            name='stop',
            field=models.TimeField(verbose_name='Stopp'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dive',
            name='temperature',
            field=models.IntegerField(verbose_name='Temperatur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='session',
            name='comment',
            field=models.CharField(max_length=512, verbose_name='Kommentar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(verbose_name='Datum'),
            preserve_default=True,
        ),
    ]
