# Generated by Django 2.2.5 on 2019-10-07 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_justificacion', '0002_auto_20191007_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='justificacion',
            name='fecha_solicitud',
            field=models.DateField(default=datetime.datetime(2019, 10, 7, 4, 39, 39, 415307)),
        ),
    ]
