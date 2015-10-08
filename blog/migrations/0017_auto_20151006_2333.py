# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20151006_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpic',
            name='thumb',
            field=models.ImageField(default=b'', upload_to=b'./FileDir/Thumb/'),
        ),
        migrations.AlterField(
            model_name='userposition',
            name='username',
            field=models.CharField(default=b'god', max_length=150),
        ),
    ]
