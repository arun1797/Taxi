# Generated by Django 5.0.2 on 2024-04-02 06:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(max_length=10)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_number', models.TextField(max_length=10, unique=True)),
                ('start_place', models.CharField(max_length=100)),
                ('end_place', models.CharField(max_length=100)),
                ('star_date', models.DateField()),
                ('end_date', models.DateField()),
                ('vehicle_name', models.CharField(max_length=100)),
                ('vehicle_no', models.TextField()),
                ('start_kilometer', models.TextField()),
                ('end_kilometer', models.TextField()),
                ('toll', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('guest_name', models.CharField(max_length=100)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.drivermodel')),
            ],
        ),
    ]
