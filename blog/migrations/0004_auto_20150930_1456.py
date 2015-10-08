# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_goduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='GodTweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet', models.CharField(max_length=50)),
                ('pos', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='blogsblog',
            name='auther',
        ),
        migrations.AddField(
            model_name='blogpoem',
            name='auther',
            field=models.CharField(default=b'\xe7\x8e\x8b\xe7\x82\xb3\xe5\xae\x81', max_length=50),
        ),
        migrations.AddField(
            model_name='blogsblog',
            name='authers',
            field=models.CharField(default=b'\xe7\x8e\x8b\xe7\x82\xb3\xe5\xae\x81', max_length=150),
        ),
    ]
