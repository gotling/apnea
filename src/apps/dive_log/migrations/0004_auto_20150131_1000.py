# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dive_log', '0003_auto_20150131_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dive',
            options={'ordering': ['id'], 'verbose_name': 'Dyk', 'verbose_name_plural': 'Dyk'},
        ),
    ]
