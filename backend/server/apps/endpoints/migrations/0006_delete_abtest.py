# Generated by Django 5.0.1 on 2024-02-01 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0005_alter_flight_arrival_date_alter_flight_departure_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ABTest',
        ),
    ]
