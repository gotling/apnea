# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbreviation', models.CharField(max_length=3, verbose_name='F\xf6rkortning')),
                ('name', models.CharField(max_length=64, verbose_name='Namn')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
