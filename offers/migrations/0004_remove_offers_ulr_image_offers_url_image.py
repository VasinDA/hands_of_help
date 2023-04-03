# Generated by Django 4.1.1 on 2023-04-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_remove_offers_ulr_image_offers_request_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='ulr_image',
        ),
        migrations.AddField(
            model_name='offers',
            name='url_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
