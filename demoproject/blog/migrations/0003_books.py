# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_books'),
    ]

    operations = [
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
