# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_userposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposition',
            name='Ip',
            field=models.IPAddressField(default=b'127.0.0.1'),
        ),
        migrations.AlterField(
            model_name='userposition',
            name='username',
            field=models.CharField(default=b'god', max_length=50),
        ),
    ]
