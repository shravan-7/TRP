# Generated by Django 5.0.6 on 2024-07-17 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourist_App', '0002_user_location_prefs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewphoto',
            name='photo_data',
        ),
        migrations.AlterField(
            model_name='reviewphoto',
            name='photo',
            field=models.ImageField(upload_to='review_images'),
        ),
    ]
