from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from .form import RegisterCard
from .models import Targetas

def home(request):
    if request.user.is_authenticated:
        return redirect('consulta_ticket')
    else:
        return render(request, "home.html", {})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = request.POST.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('home')
            else:
                messages.error(request, 'Cuenta inexistente o contraseña incorrecta.')
        else:
            messages.error(request, 'Error en el formulario. Verifica tus credenciales.')

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def cuenta(request):
    
    if request.method == "POST":
        form = RegisterCard(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            duenno = request.user
            nombre = data["nombreTargeta"]
            tipo = data["tipoTargeta"]
            banco = data["BancoTargeta"]
            vencimiento = data["fechaVancimiento"]

            targeta = Targetas(
                duenno = duenno,
                nombreTargeta = nombre,
                tipoTargeta = tipo,
                BancoTargeta = banco,
                fechaVancimiento = vencimiento
            )

            targeta.save()
    
    form = RegisterCard()
    cards = Targetas.objects.all().filter(duenno = request.user.id)

    return render(request, "cuenta.html", {"form": form, "cards": cards})

def deleteCard(request, id):
    card = Targetas.objects.get(id = id)
    card.delete()
    return redirect("cuenta")