# Generated by Django 4.1.3 on 2023-02-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towner', '0005_bookingdetails_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='gender',
            field=models.CharField(default='drama', max_length=20),
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='language',
            field=models.CharField(default='', max_length=20),
        ),
    ]
