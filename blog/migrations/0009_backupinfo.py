# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151002_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackUpInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
