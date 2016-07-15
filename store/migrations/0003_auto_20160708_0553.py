# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=8),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
