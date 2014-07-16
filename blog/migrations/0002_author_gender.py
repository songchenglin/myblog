# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.CharField(default=b'S', max_length=8, choices=[(b'M', b'male'), (b'F', b'female'), (b'S', b'shemale')]),
            preserve_default=True,
        ),
    ]
