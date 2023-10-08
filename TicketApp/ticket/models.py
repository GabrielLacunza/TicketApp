from django.db import models


Eleccion_lugar = (
    ('Santiago', 'Santiago'),
    ('Valparaiso', 'Valparaiso'),
    ('Viña del mar', 'Viña del mar'),
    ('Quilpue', 'Quilpue'),
    ('Temuco', 'Temuco'),
    ('Villa Alemana', 'Villa Alemana'),
    ('Pucon', 'Pucon'),
    ('Villarica', 'Villarica'),
    ('Los Angeles', 'Los Angeles'),
    ('La Serena', 'La Serena'),
    ('Chillán', 'Chillán'),
    ('Rancagua', 'Rancagua'),
    ('Cartagena', 'Cartagena'),
    ('Buin', 'Buin'),
    ('Arica', 'Arica'),
    ('Cañete', 'Cañete'),
    ('Chañaral', 'Chañaral'),
    ('Limache', 'Limache'),
    ('Copiapo', 'Copiapo'),
    ('Concepcion', 'Concepcion'),
    ('Linares', 'Linares'),
    ('Pitrufquen', 'Pitrufquen'),
    ('Concon', 'Concon'),
    ('Osorno', 'Osorno'),
    ('Lonquimay', 'Lonquimay'),
    ('Lota', 'Lota'),
    ('Melipilla', 'Melipilla'),
    ('Ovalle', 'Ovalle'),
    ('La Ligua', 'La Ligua'),
    ('La Calera', 'La Calera'),
    ('Olmue', 'Olmue'),
)


# Create your models here.
class Ticket(models.Model):
  destino = models.CharField(max_length=40, choices=Eleccion_lugar,verbose_name="Destino de parada", name="destino")
  origen = models.CharField(max_length=40, choices=Eleccion_lugar,verbose_name="Origen de parada", name="origen")
  salida = models.DateTimeField(verbose_name="Momento de salida", name="salida")
  bus = models.CharField(max_length=50, verbose_name="Matricula del bus", name="bus")
  compannia = models.CharField(max_length=40, verbose_name="Compañia de viaje", name="compannia")

  def __str__(self):
    return f"{self.destino} {self.salida}"

class Usuario(models.Model):
  #por hacer
  def __str__(self):
    return self.name
