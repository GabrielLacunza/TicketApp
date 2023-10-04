from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario al "home"
                return redirect('home')  # 'home' debe coincidir con el nombre de la URL en urls.py
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

