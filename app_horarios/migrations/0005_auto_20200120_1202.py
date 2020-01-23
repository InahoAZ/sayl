# Generated by Django 2.2.5 on 2020-01-20 12:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_horarios', '0004_horariosfijos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horariosfijos',
            name='agente',
        ),
        migrations.AddField(
            model_name='horariosfijos',
            name='agente',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
