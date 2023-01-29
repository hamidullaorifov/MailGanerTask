# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-29 08:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='body',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='message',
            field=models.TextField(),
        ),
    ]
