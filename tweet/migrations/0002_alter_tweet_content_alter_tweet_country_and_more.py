# Generated by Django 4.1.3 on 2022-11-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tag',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]