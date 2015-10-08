# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151001_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headFile', models.FileField(upload_to=b'./FileDir/File/')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
