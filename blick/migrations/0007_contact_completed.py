# Generated by Django 3.0.8 on 2020-08-04 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blick', '0006_contact_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
