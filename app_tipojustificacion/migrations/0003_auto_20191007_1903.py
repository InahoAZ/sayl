# Generated by Django 2.2.5 on 2019-10-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tipojustificacion', '0002_auto_20191001_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipojustificacion',
            name='cargo',
            field=models.CharField(max_length=20),
        ),
    ]