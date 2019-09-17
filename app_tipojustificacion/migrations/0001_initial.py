# Generated by Django 2.2.5 on 2019-09-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoJustificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200)),
                ('artcct', models.CharField(max_length=200)),
                ('dia_trabajado', models.BooleanField()),
                ('cant_mes', models.IntegerField()),
                ('cant_año', models.IntegerField()),
                ('claustro', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('requisitos', models.CharField(max_length=200)),
                ('horas', models.IntegerField()),
                ('tipo_justificacion', models.ManyToManyField(to='app_tipojustificacion.TipoJustificacion')),
            ],
        ),
    ]
