# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogpic_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('Ip', models.IPAddressField()),
                ('latitude', models.FloatField(default=b'0.0')),
                ('longtitude', models.FloatField(default=b'0.0')),
                ('position', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
