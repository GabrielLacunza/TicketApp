from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ticket
from .forms import  TicketSearchForm, TicketAddForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

class TicketCreate(CreateView):
    model = Ticket
    form_class = TicketAddForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_ticket')
    
class TicketUpdate(UpdateView):
    model = Ticket
    form_class = TicketAddForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_ticket')

class TicketList(ListView):
    model = Ticket
    template_name = 'admin/listar_Tickets.html'
    # paginate_by = 4

class TicketDelete(DeleteView):
    model = Ticket
    template_name = 'admin/borrar_Ticket.html'
    success_url = reverse_lazy('list_ticket')


def Consulta_tickets(request, origen, destino):
    tickets = Ticket.objects.get(origen=origen, destino=destino)
    return render(request, "admin/listar_Tickets.html", 
                  {'tickets': tickets})

def consulta_ticket(request):
    tickets = None

    if request.method == 'POST':
        form = TicketSearchForm(request.POST)

        if form.is_valid():
            origen = form.cleaned_data.get('origen')
            destino = form.cleaned_data.get('destino')
            queryset = Ticket.objects.all()

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
    return render(request, 'detalle_ticket.html', {'ticket': ticket})

# Funcion para asignar el ticket al usuario y modificar su status a 'Reservado'
def reserva_ticket(request, numero_ticket):
    ticket = get_object_or_404(Ticket, numero_ticket=numero_ticket)

    if ticket.ticket_status == 'Activo':
        ticket.reservado_por = request.user
        ticket.ticket_status = 'Reservado'
        ticket.save()

        messages.success(request, 'Ticket reserved successfully!')

        return redirect('ticket_detalle', numero_ticket=numero_ticket)  # Redirect to ticket detail page