# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw_member', '0003_member_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
