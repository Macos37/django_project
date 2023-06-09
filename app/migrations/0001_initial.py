# Generated by Django 4.2.1 on 2023-05-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Модель')),
                ('max_load_capacity', models.IntegerField(default=0, verbose_name='Максимальная грузоподьемность')),
            ],
            options={
                'verbose_name_plural': 'Truck Types',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.IntegerField(verbose_name='Бортовой номер')),
                ('current_load', models.IntegerField(verbose_name='Текущий вес')),
                ('type_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trucks', to='app.truckmodel')),
            ],
            options={
                'verbose_name_plural': 'Trucks',
            },
        ),
    ]
