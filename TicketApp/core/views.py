from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages

def home(request):
    return render(request, "home.html", {})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # Redirigir al usuario al inicio de sesión
            return redirect('login')  # 'login' debe coincidir con el nombre de la URL en urls.py
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
                # Agrega un mensaje de error cuando la cuenta no existe
                messages.error(request, 'Cuenta inexistente o contraseña incorrecta.')
        else:
            # Si el formulario no es válido, también muestra un mensaje de error
            messages.error(request, 'Error en el formulario. Verifica tus credenciales.')

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

