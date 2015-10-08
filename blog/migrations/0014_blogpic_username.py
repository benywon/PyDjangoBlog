# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_userloginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpic',
            name='username',
            field=models.CharField(default=b'god', max_length=50),
        ),
    ]
