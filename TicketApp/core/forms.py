from logging import PlaceHolder
from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    # Personaliza los mensajes de error y ayuda para las contraseñas
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Tu contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula y un número.",
        error_messages={
            'password_mismatch': _("Las contraseñas no coinciden."),
            'password_too_short': _("La contraseña es demasiado corta. Debe contener al menos 8 caracteres."),
            'password_common': _("La contraseña es demasiado común. Elige una contraseña más segura."),
            'password_no_upper': _("La contraseña debe contener al menos una letra mayúscula."),
            'password_no_digit': _("La contraseña debe contener al menos un número.")
        }
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(self.fields['password1'].error_messages['password_no_upper'])
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError(self.fields['password1'].error_messages['password_no_digit'])
        return password1

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')