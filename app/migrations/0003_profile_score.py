# Generated by Django 4.0.5 on 2022-06-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_auditor_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
