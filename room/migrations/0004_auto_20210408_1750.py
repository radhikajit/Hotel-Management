# Generated by Django 3.0.3 on 2021-04-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20210408_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='price',
        ),
        migrations.AddField(
            model_name='room_type',
            name='price',
            field=models.IntegerField(default=1000),
        ),
    ]
