from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ticket
from .forms import  TicketSearchForm, TicketAddForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from qrcode import *
from django.conf import settings
from core.models import Targetas
import json
# Create your views here.

class TicketCreate(CreateView):
    model = Ticket
    form_class = TicketAddForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_ticket')
    
def edit_ticket(request, numero_ticket):
    ticket = get_object_or_404(Ticket, numero_ticket=numero_ticket)

    if request.method == 'POST':
        form = TicketAddForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketAddForm(instance=ticket)

    return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})

class TicketUpdate(UpdateView):
    model = Ticket
    form_class = TicketAddForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_ticket')

# Funcion para listar tickets
def ticket_list(request):
    if request.user.is_superuser:   # SUPERUSUARIO: Lista todos los tickets
        tickets = Ticket.objects.all() 
    else:                           # USUARIO: Lista los tickets que el usuario tiene reservados
        tickets = Ticket.objects.filter(reservado_por=request.user) 

    return render(request, 'admin/listar_Tickets.html', {'tickets': tickets})

class TicketDelete(DeleteView):
    model = Ticket
    template_name = 'admin/borrar_Ticket.html'
    success_url = reverse_lazy('list_ticket')



def Consulta_tickets(request, origen, destino):
    tickets = Ticket.objects.get(origen=origen, destino=destino)
    return render(request, "admin/listar_Tickets.html", 
                  {'tickets': tickets})


# Consulta de los tickets para el template buscatickets.html
# Esta funcion solo trabajara con tickets con el estado 'Activo' 
def consulta_ticket(request):
    tickets = None

    if request.method == 'POST':
        form = TicketSearchForm(request.POST)
        if form.is_valid():
            origen = form.cleaned_data.get('origen')
            destino = form.cleaned_data.get('destino')
            queryset = Ticket.objects.filter(ticket_status='Activo')

            if origen:
                queryset = queryset.filter(origen__icontains=origen)
            if destino:
                queryset = queryset.filter(destino__icontains=destino)
            
                
            tickets = queryset

    else:
        form = TicketSearchForm()

    return render(request, 'buscatickets.html', {'form': form, 'tickets': tickets})


def formulariotickets(request):
    return render(request,'buscatickets.html')



# === Funciones para el proceso de reserva

# Funcion para visualizar con detalle el ticket antes de reservarlo
def ticket_detalle(request, numero_ticket):  
    ticket = get_object_or_404(Ticket, numero_ticket=numero_ticket)
    targetas = Targetas.objects.filter(duenno=request.user)

    if request.method == "POST":
        data = request.POST
        if Targetas.objects.get(nombreTargeta=data["Targetas"]):
            return redirect("reserva_ticket", numero_ticket=numero_ticket)

    return render(request, 'detalle_ticket.html', {'ticket': ticket, "targetas": targetas})

# Funcion para asignar el ticket al usuario y el status de dicho ticket a 'Reservado'
def reserva_ticket(request, numero_ticket):
    ticket = get_object_or_404(Ticket, numero_ticket=numero_ticket)

    if ticket.ticket_status == 'Activo':
        ticket.reservado_por = request.user
        ticket.ticket_status = 'Reservado'
        ticket.save()

        messages.success(request, 'Ticket reservado correctamente')

        return redirect('list_ticket') 
    
    else:
        messages.error(request, 'Error, ticket no disponible')
        return redirect('ticket_not_available', ticket_id=ticket.id)

def qrCode(request, numero_ticket):
    ticket = Ticket.objects.get(numero_ticket=numero_ticket)
    data = {
        "numero_ticket": numero_ticket,
        "origen": ticket.origen,
        "destino": ticket.destino,
        "salida": str(ticket.salida),
        "bus": ticket.bus
    }
    img = make(json.dumps(data))
    img_name = 'qr' + numero_ticket + '.png'
    img.save(f"{settings.MEDIA_ROOT}/{img_name}")

    return render(request, "qrCode.html", {"img_name": img_name})