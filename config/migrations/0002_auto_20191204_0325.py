# Generated by Django 2.2.5 on 2019-12-04 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuraciones',
            name='valor_config',
            field=models.CharField(max_length=200),
        ),
    ]
