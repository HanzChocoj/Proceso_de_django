from django import forms
from .models import Administrador  # o el nombre correcto de tu modelo

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador  # debe coincidir con tu modelo exacto
        fields = ['first_name', 'last_name', 'email']  # o los campos que tenga tu modelo
