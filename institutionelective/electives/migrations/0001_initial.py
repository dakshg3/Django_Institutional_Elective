# Generated by Django 2.1.2 on 2018-11-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('usn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('choice1', models.CharField(max_length=40)),
                ('choice2', models.CharField(max_length=40)),
                ('choice3', models.CharField(max_length=40)),
                ('choice4', models.CharField(max_length=40)),
                ('choice5', models.CharField(max_length=40)),
            ],
        ),
    ]