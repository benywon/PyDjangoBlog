# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogpic_isshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='godtweet',
            name='username',
            field=models.CharField(default=b'\xe7\x8e\x8b\xe7\x82\xb3\xe5\xae\x81', max_length=50),
        ),
    ]
