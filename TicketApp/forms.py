from logging import PlaceHolder
from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['origen','destino','compannia']
        
        labels = {
            'origen': 'Lugar de origen',
            'destino': 'Lugar de destino',
            'compannia': 'Compañia del bus' 
        }