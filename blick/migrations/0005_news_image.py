# Generated by Django 3.0.8 on 2020-08-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blick', '0004_listing_repbuyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]