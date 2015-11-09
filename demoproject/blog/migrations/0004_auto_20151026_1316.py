# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='writerid',
            new_name='authorid',
        ),
    ]
