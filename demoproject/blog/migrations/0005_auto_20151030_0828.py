# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151026_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publication_date',
            field=models.CharField(max_length=30),
        ),
    ]
