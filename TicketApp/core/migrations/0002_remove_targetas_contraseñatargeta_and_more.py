# Generated by Django 4.2.5 on 2023-10-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targetas',
            name='contraseñaTargeta',
        ),
        migrations.AlterField(
            model_name='targetas',
            name='tipoTargeta',
            field=models.CharField(max_length=50),
        ),
    ]
