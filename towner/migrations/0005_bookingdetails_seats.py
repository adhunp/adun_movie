# Generated by Django 4.1.3 on 2023-02-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towner', '0004_remove_seatinfo_seatname_seatinfo_seat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='seats',
            field=models.CharField(default='', max_length=20),
        ),
    ]
