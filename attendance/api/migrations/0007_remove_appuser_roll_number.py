# Generated by Django 2.2 on 2019-04-19 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190419_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='roll_number',
        ),
    ]
