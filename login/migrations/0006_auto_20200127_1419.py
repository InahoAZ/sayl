# Generated by Django 2.2.5 on 2020-01-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0003_auto_20200125_0801'),
        ('login', '0005_auto_20200120_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalcustomuser',
            name='cargos_cache',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='cargos_cache',
        ),
        migrations.AddField(
            model_name='customuser',
            name='cargos_cache',
            field=models.ManyToManyField(to='cargos.CargosCache'),
        ),
    ]
