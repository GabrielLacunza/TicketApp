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
    class Meta:
        model = Ticket
        fields = ['origen','destino','salida','bus','compannia',]
        
        labels = {
            'origen': 'Lugar de origen',
            'destino': 'Lugar de destino',
            'salida': "Horario de salida",
            'bus': "Nombre de la compañia",
            'compannia': 'Compañia del bus' 
        }
        widgets = {
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'salida': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'bus': forms.TextInput(attrs={'class': 'form-control'}),
            'compannia': forms.TextInput(attrs={'class': 'form-control'}),

        }

class TicketSearchForm(forms.Form):
    origen = forms.ChoiceField(choices=Eleccion_lugar, required=False)
    destino = forms.ChoiceField(choices=Eleccion_lugar, required=False)

