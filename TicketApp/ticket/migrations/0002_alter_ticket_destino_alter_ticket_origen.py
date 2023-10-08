# Generated by Django 4.2.5 on 2023-10-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='destino',
            field=models.CharField(choices=[('Santiago', 'Santiago'), ('Valparaiso', 'Valparaiso'), ('Viña del mar', 'Viña del mar'), ('Quilpue', 'Quilpue'), ('Temuco', 'Temuco'), ('Villa Alemana', 'Villa Alemana'), ('Pucon', 'Pucon'), ('Villarica', 'Villarica'), ('Los Angeles', 'Los Angeles'), ('La Serena', 'La Serena'), ('Chillán', 'Chillán'), ('Rancagua', 'Rancagua'), ('Cartagena', 'Cartagena'), ('Buin', 'Buin'), ('Arica', 'Arica'), ('Cañete', 'Cañete'), ('Chañaral', 'Chañaral'), ('Limache', 'Limache'), ('Copiapo', 'Copiapo'), ('Concepcion', 'Concepcion'), ('Linares', 'Linares'), ('Pitrufquen', 'Pitrufquen'), ('Concon', 'Concon'), ('Osorno', 'Osorno'), ('Lonquimay', 'Lonquimay'), ('Lota', 'Lota'), ('Melipilla', 'Melipilla'), ('Ovalle', 'Ovalle'), ('La Ligua', 'La Ligua'), ('La Calera', 'La Calera'), ('Olmue', 'Olmue')], max_length=40, verbose_name='Destino de parada'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='origen',
            field=models.CharField(choices=[('Santiago', 'Santiago'), ('Valparaiso', 'Valparaiso'), ('Viña del mar', 'Viña del mar'), ('Quilpue', 'Quilpue'), ('Temuco', 'Temuco'), ('Villa Alemana', 'Villa Alemana'), ('Pucon', 'Pucon'), ('Villarica', 'Villarica'), ('Los Angeles', 'Los Angeles'), ('La Serena', 'La Serena'), ('Chillán', 'Chillán'), ('Rancagua', 'Rancagua'), ('Cartagena', 'Cartagena'), ('Buin', 'Buin'), ('Arica', 'Arica'), ('Cañete', 'Cañete'), ('Chañaral', 'Chañaral'), ('Limache', 'Limache'), ('Copiapo', 'Copiapo'), ('Concepcion', 'Concepcion'), ('Linares', 'Linares'), ('Pitrufquen', 'Pitrufquen'), ('Concon', 'Concon'), ('Osorno', 'Osorno'), ('Lonquimay', 'Lonquimay'), ('Lota', 'Lota'), ('Melipilla', 'Melipilla'), ('Ovalle', 'Ovalle'), ('La Ligua', 'La Ligua'), ('La Calera', 'La Calera'), ('Olmue', 'Olmue')], max_length=40, verbose_name='Origen de parada'),
        ),
    ]
