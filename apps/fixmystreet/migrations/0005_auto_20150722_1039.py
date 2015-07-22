# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixmystreet', '0004_auto_20150708_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalfmsuser',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
    ]
