# Generated by Django 4.1.3 on 2023-02-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towner', '0006_moviedetails_gender_moviedetails_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedetails',
            name='time_am',
        ),
        migrations.RemoveField(
            model_name='moviedetails',
            name='time_pm',
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]
