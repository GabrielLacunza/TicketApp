from django.forms import ModelForm, DateInput, ChoiceField
from .models import Targetas
from datetime import date


class RegisterCard(ModelForm):
  OpcionesTipo =(
    ("Credito", "Credito"),
    ("Debito", "Debito"),
    ("Prepago", "Prepago")
  )

  tipoTargeta = ChoiceField(choices=OpcionesTipo, label="Tipo de targeta bancaria")

  class Meta:
    model=Targetas
    exclude=["duenno"]
    widgets={
      "fechaVancimiento": DateInput(attrs={"type": "date", "min": date.today()})
    }