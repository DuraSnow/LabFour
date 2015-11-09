# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('authorid', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('writerid', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
