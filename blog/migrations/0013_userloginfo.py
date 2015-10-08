# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151004_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ip', models.CharField(max_length=150)),
                ('User', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
