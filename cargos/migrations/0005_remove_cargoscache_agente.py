# Generated by Django 2.2.5 on 2020-01-27 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0004_cargoscache_agente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargoscache',
            name='agente',
        ),
    ]
