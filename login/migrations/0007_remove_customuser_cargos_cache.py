# Generated by Django 2.2.5 on 2020-01-27 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200127_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='cargos_cache',
        ),
    ]
