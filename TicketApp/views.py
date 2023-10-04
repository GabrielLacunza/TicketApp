from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ticket
from .forms import  TicketForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    return render(request, "home.html", {})


#=========================== Crud Tickets
class TicketCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_Ticket')
    
class TicketUpdate(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'admin/añadir_Tickets.html'
    success_url = reverse_lazy('list_Ticket')

class TicketList(ListView):
    model = Ticket
    template_name = 'admin/listar_Tickets.html'
    # paginate_by = 4

class TicketDelete(DeleteView):
    model = Ticket
    template_name = 'admin/borrar_Ticket.html'
    success_url = reverse_lazy('list_Ticket')