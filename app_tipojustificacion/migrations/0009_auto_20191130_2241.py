# Generated by Django 2.2.5 on 2019-11-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tipojustificacion', '0008_auto_20191109_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltipojustificacion',
            name='cargo',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='tipojustificacion',
            name='cargo',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
