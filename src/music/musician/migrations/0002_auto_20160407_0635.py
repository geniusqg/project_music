# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicians',
            name='letter_index',
            field=models.CharField(max_length=10, verbose_name='\u6b4c\u624b\u540d\u5b57\u9996\u5b57\u6bcd'),
        ),
    ]
