# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20170430_2126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('user', 'data_post_id')]),
        ),
    ]
