# Generated by Django 4.1.3 on 2022-11-07 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='basic_profile/guest.png', null=True, upload_to='%y/%m/'),
        ),
    ]
