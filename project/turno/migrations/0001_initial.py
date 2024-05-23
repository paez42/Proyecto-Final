# Generated by Django 5.0.6 on 2024-05-23 18:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TurnoLugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcíon')),
            ],
            options={
                'verbose_name': 'lugar de turno',
                'verbose_name_plural': 'lugares de turnos',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('unidad_medida', models.CharField(max_length=100)),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('fecha_actualizacion', models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='fecha de actualización')),
                ('categoria_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='turno.turnolugar', verbose_name='lugar de turno')),
            ],
            options={
                'verbose_name': 'turno',
                'verbose_name_plural': 'turnos',
            },
        ),
    ]