# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dive_log', '0005_session_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-date', '-time'], 'verbose_name': 'Session', 'verbose_name_plural': 'Sessioner'},
        ),
    ]
