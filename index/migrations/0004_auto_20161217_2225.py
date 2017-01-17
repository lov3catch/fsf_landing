# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_manager_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='see_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата просмотра'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='code',
            field=models.CharField(default=index.models.unique_code, max_length=10, verbose_name='код'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='статус модератора'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='username',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
    ]