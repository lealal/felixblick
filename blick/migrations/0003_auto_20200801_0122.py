# Generated by Django 3.0.8 on 2020-08-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blick', '0002_listing_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]