# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dive_log', '0002_datapoint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datapoint',
            options={'ordering': ['second'], 'verbose_name': 'Datapunkt', 'verbose_name_plural': 'Datapunkter'},
        ),
    ]
