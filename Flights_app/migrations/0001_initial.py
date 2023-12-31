# Generated by Django 5.0 on 2023-12-06 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aircraft_Model', models.CharField(max_length=50)),
                ('Aircraft_serialnumber', models.CharField(max_length=50, unique=True)),
                ('Manufacturer', models.CharField(max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_Name', models.CharField(max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Airport_Name', models.CharField(max_length=200, unique=True)),
                ('Country', models.CharField(default='India', max_length=100)),
                ('ICAO_Code', models.CharField(max_length=4, unique=True)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Flights_app.cities')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flight_name', models.CharField(max_length=200, unique=True)),
                ('Flight_Id', models.CharField(max_length=200, unique=True)),
                ('Flight_from', models.CharField(max_length=200)),
                ('Flight_to', models.CharField(max_length=200)),
                ('Departure_Flight_Time', models.DateTimeField()),
                ('Aparture_Flight_Time', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='Flights_app.airport')),
                ('Departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='Flights_app.airport')),
                ('Flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Flights_app.aircraft')),
            ],
        ),
    ]
