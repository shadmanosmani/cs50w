# Generated by Django 3.1.6 on 2021-02-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
