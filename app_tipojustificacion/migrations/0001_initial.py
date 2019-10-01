# Generated by Django 2.2.5 on 2019-10-01 18:43

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
                ('claustro', models.CharField(choices=[('Docente', 'Docente'), ('No Docente', 'No Docente')], max_length=11)),
                ('cargo', models.CharField(max_length=20)),
            ],
        ),
    ]
