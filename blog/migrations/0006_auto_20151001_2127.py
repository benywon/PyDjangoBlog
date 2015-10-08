# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpoem_isprevious'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('headImg', models.ImageField(upload_to=b'./FileDir/Image/')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='blogpoem',
            name='nav',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='godtweet',
            name='tweet',
            field=models.CharField(max_length=250),
        ),
    ]
