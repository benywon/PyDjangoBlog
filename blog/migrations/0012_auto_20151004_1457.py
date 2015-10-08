# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_godtweet_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='goduser',
            name='email',
            field=models.EmailField(default=b'none@none.com', max_length=100),
        ),
        migrations.AddField(
            model_name='goduser',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='godtweet',
            name='username',
            field=models.CharField(default=b'god', max_length=50),
        ),
    ]
