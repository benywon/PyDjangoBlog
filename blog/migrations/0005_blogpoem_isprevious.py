# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150930_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpoem',
            name='isprevious',
            field=models.BooleanField(default=False),
        ),
    ]
