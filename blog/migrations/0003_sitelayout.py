# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170719_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('intro_title', models.CharField(max_length=30)),
                ('intro_text', models.CharField(max_length=100)),
            ],
        ),
    ]