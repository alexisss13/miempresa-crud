# Generated by Django 5.2.1 on 2025-05-18 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='empleados/')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_CURSO', 'En curso'), ('FINALIZADO', 'Finalizado')], max_length=50)),
                ('imagen', models.ImageField(upload_to='proyectos/')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='gestion.empleado')),
            ],
        ),
    ]
