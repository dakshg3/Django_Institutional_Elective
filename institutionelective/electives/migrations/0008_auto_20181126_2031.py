# Generated by Django 2.1.2 on 2018-11-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electives', '0007_auto_20181126_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='cur_time',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
