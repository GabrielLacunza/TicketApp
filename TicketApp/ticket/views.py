from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ticket
from .forms import  TicketSearchForm, TicketAddForm, ReportForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from qrcode import *
from django.conf import settings
from core.models import Targetas
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from fpdf import FPDF
from django.http import HttpResponse
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

# ================================= GENERACION DE REPORTES


# Esta funcion se encargara de;
# - Consultar todos los tickets que esten creados en un rango de fechas (el rango son 2 parametros)
# - Genera un grafico con la distribucion de status de los tickets
# - Inserta este grafico en un PDF y lo envia como retorno
def generate_report_pdf(title, start_time, end_time):
    # Consulta de tickets segun el rango entregado
    tickets = Ticket.objects.filter(fecha_creacion__range=[start_time, end_time])

        
    # Conversion de la queryset en un dataframe de Pandas
    df = pd.DataFrame.from_records(tickets.values())

    if 'ticket_status' in df.columns:
        # Conteo total de tickets
        total_tickets = len(df)

        # Conteo de cantidad de status de tickets (Reservado, activo, cerrado) 
        # Se establece esto porque la consulta puede agarrar tickets con un solo o mas status en comun
        ticket_status_counts = df['ticket_status'].value_counts()

        # Generacion del grafico
        plt.bar(ticket_status_counts.index, ticket_status_counts.values)
        plt.title('Distribucion de ticket segun estado')
        plt.xlabel('Estado ticket')
        plt.ylabel('Conteo')

        # Guardado del grafico en un png.
        image_path = 'report_plot.png'
        plt.savefig(image_path)
        plt.close()

        # Creado de pdf e insercion del grafico en el
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Title: {title}", ln=True, align='L')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Total Tickets: {total_tickets}", ln=True, align='L')
        pdf.ln(10)
        pdf.image(image_path, x=10, y=pdf.get_y(), w=190)

        # Save the PDF with the provided title
        pdf_filename = f"{title}_report.pdf"
        pdf.output(pdf_filename)

        return pdf_filename
    else:
        # Error si es que la columna 'ticket_status' no se encuentra en el dataframe
        # Este error suele ocurrir cuando la consulta no agarra ningun ticket
        return f"Error: 'ticket_status' column not found in DataFrame for title: {title}"


# Metodo para generar el formulario para la generacion del reporte
def generate_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # Metodo para guardar el reporte en la base de datos (NO UTILIZAR)
            #report = Report(title=title, data="")
            #report.save()

            # Genera el pdf y retorna el link para su descarga
            pdf_path = generate_report_pdf(title,start_time, end_time)
            return redirect('download_report', pdf_path=pdf_path)
    else:
        form = ReportForm()

    return render(request, 'admin/generate_report.html', {'form': form})

# Metodo que recive un archivo PDF para descargarlo automaticamente
def download_report(request, pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_path}"'
        return response
    