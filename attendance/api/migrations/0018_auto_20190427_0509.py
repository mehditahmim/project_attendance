# Generated by Django 2.2 on 2019-04-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190427_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='picture',
            new_name='img',
        ),
        migrations.AddField(
            model_name='image',
            name='processed_img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pro_images/'),
        ),
    ]
