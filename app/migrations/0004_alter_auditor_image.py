# Generated by Django 4.0.5 on 2022-06-15 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditor',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
