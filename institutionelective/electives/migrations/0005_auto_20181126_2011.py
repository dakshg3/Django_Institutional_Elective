# Generated by Django 2.1.2 on 2018-11-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electives', '0004_choices_cur_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='cur_time',
            field=models.CharField(blank=True, default='14:41:37:277633', max_length=8),
        ),
    ]
