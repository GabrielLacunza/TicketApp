from django.db import models

# Create your models here.
class Ticket(models.Model):
  destino = models.CharField(max_length=40, verbose_name="Destino de parada", name="destino")
  origen = models.CharField(max_length=40, verbose_name="Origen de parada", name="origen")
  salida = models.DateTimeField(verbose_name="Momento de salida", name="salida")
  bus = models.CharField(max_length=50, verbose_name="Matricula del bus", name="bus")
  compannia = models.CharField(max_length=40, verbose_name="Compañia de viaje", name="compannia")

  def __str__(self):
    return f"{self.destino} {self.salida}"

class Usuario(models.Model):
  #por hacer
  def __str__(self):
    return self.name
