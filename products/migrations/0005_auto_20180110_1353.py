# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-10 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
    ]