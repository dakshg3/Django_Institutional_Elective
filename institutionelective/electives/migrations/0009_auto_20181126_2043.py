# Generated by Django 2.1.2 on 2018-11-26 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electives', '0008_auto_20181126_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='cur_time',
            field=models.CharField(blank=True, default=datetime.datetime.now, max_length=15),
        ),
    ]