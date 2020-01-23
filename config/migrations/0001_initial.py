# Generated by Django 2.2.5 on 2020-01-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuraciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_universidad', models.CharField(max_length=200)),
                ('nombre_facultad', models.CharField(max_length=200)),
                ('direccion_facultad', models.CharField(max_length=200)),
                ('tiempo_tolerancia', models.FloatField()),
                ('porcentaje_frente_aula', models.FloatField()),
                ('horas_a_cumplir_default', models.FloatField()),
            ],
        ),
    ]
