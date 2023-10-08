from django.shortcuts import render
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
    # Recuperamos la instancia de la carrera
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