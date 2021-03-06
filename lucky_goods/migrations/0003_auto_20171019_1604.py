# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lucky_goods', '0002_luckyuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='luckyuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='luckyuser',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='order',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LuckyUser',
        ),
    ]
