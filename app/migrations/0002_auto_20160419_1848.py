# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostlist',
            name='ip',
            field=models.GenericIPAddressField(unique=True, verbose_name='IP\u5730\u5740'),
        ),
    ]
