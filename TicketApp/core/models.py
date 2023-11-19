from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
  #por hacer
  def __str__(self):
    return self.name

class Targetas(models.Model):
  duenno = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
  nombre = models.CharField(name="nombreTargeta", verbose_name="Nombre de la targeta", max_length=50)
  tipo = models.CharField(name="tipoTargeta", max_length=50)
  banco = models.CharField(name="BancoTargeta", verbose_name="Banco de la targeta", max_length=30)
  vencimiento = models.DateField(name="fechaVancimiento", verbose_name="Fecha de vencimiento", auto_now=False, auto_now_add=False)
  
  def __str__(self) -> str:
    return f"{self.nombreTargeta} - {self.BancoTargeta}"