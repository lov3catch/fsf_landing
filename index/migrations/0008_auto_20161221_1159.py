# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20161217_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='see_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='see_available',
        ),
        migrations.AddField(
            model_name='order',
            name='is_available',
            field=models.BooleanField(default=False, verbose_name='доступен для обработки менеджером'),
        ),
        migrations.AddField(
            model_name='order',
            name='send_to_manager',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата просмотра менеджером'),
        ),
        migrations.AddField(
            model_name='order',
            name='send_to_moderator',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата просмотра модератором'),
        ),
    ]
