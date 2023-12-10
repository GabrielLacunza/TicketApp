from datetime import datetime
from logging import PlaceHolder
from django import forms
from .models import Ticket

from django import forms

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

class TicketAddForm(forms.ModelForm):
    destino = forms.ChoiceField(choices=Eleccion_lugar, label='Lugar de destino')
    origen = forms.ChoiceField(choices=Eleccion_lugar, label='Lugar de origen')

    class Meta:
        model = Ticket
        fields = ['origen','destino','salida','bus','compannia',]
        
        labels = {
            'salida': "Horario de salida",
            'bus': "Nombre de la compañia",
            'compannia': 'Compañia del bus' 
        }
        widgets = {
            'salida': forms.DateTimeInput(attrs={"type": "datetime-local", "min": datetime.now().strftime("%Y-%m-%dT%H:%M")})
        }

class TicketSearchForm(forms.Form):
    origen = forms.ChoiceField(choices=Eleccion_lugar, required=False)
    destino = forms.ChoiceField(choices=Eleccion_lugar, required=False)

class ReportForm(forms.Form):
    title = forms.CharField(max_length=255)
    start_time = forms.DateTimeField(label='Start Time')
    end_time = forms.DateTimeField(label='End Time')