from django.contrib import admin
from django.urls import path
from . import views
from .views import ticket_detalle, reserva_ticket, ticket_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('consulta_ticket/', views.consulta_ticket, name='consulta_ticket'),
    path('add_ticket', views.TicketCreate.as_view(), name="add_ticket"),
    path('formulariotickets', views.formulariotickets, name='formulariotickets' ),

    path('add_ticket', views.TicketCreate.as_view(), name="add_ticket"),
    
    path('edit_ticket/<uuid:pk>', views.TicketUpdate.as_view(), name='edit_ticket'),
    
    path('list_ticket', ticket_list, name="list_ticket"),
    
    path('del_ticket/<uuid:pk>', views.TicketDelete.as_view(), name="del_ticket"),

    path("qr_code/<str:numero_ticket>", views.qrCode, name="qrCode"),
    

    # ==== Funciones para el reservado de tickets

    path('ticket/<uuid:numero_ticket>/', ticket_detalle, name='ticket_detalle'),
    path('reserva/<uuid:numero_ticket>/', reserva_ticket, name='reserva_ticket'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)