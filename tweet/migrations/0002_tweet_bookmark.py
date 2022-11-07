# Generated by Django 4.1.3 on 2022-11-06 15:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='bookmark',
            field=models.ManyToManyField(related_name='add_bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
