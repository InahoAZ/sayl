# Generated by Django 2.2.5 on 2019-11-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tipojustificacion', '0005_historicaltipojustificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltipojustificacion',
            name='cargo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tipojustificacion',
            name='cargo',
            field=models.CharField(max_length=20),
        ),
    ]
