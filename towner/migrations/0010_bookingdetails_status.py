# Generated by Django 4.1.3 on 2023-02-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towner', '0009_rename_gender_moviedetails_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
