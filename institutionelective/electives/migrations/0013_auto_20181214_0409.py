# Generated by Django 2.0.5 on 2018-12-14 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electives', '0012_allocated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='end',
        ),
        migrations.RemoveField(
            model_name='timer',
            name='start',
        ),
        migrations.AddField(
            model_name='timer',
            name='hrs',
            field=models.CharField(default=10, max_length=20),
        ),
        migrations.AddField(
            model_name='timer',
            name='mins',
            field=models.CharField(default=30, max_length=20),
        ),
    ]
