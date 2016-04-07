# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6b4c\u624b\u540d\u5b57')),
                ('link_url', models.URLField(verbose_name='\u6b4c\u624b\u4fe1\u606f\u94fe\u63a5')),
                ('letter_index', models.CharField(max_length=1, verbose_name='\u6b4c\u624b\u540d\u5b57\u9996\u5b57\u6bcd')),
            ],
            options={
                'ordering': ('letter_index',),
            },
        ),
    ]
