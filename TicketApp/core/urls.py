from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.iniciar_sesion, name='login'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
