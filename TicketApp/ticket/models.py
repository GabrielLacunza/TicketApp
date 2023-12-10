from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

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

class Ticket(models.Model):
    status_eleccion = [
        ('Activo', 'Activo'),
        ('Reservado', 'Reservado'),
        ('Cerrado', 'Cerrado')
    ]

    numero_ticket = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destino = models.CharField(max_length=40, choices=Eleccion_lugar, verbose_name="Destino de parada", name="destino")
    origen = models.CharField(max_length=40, choices=Eleccion_lugar, verbose_name="Origen de parada", name="origen")
    salida = models.DateTimeField(verbose_name="Momento de salida", name="salida")
    bus = models.CharField(max_length=50, verbose_name="Matricula del bus", name="bus")
    compannia = models.CharField(max_length=40, verbose_name="Compañia de viaje", name="compannia")
    ticket_status = models.CharField(max_length=15, choices=status_eleccion, default='Activo')
    reservado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp de creación")


 
    def save(self, *args, **kwargs):  # Si es que no se define el campo 'Salida', se autogenerara con la fecha actual
        if not self.salida:
            self.salida = datetime.now()
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.destino} {self.salida}"

