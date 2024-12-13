from django import forms
from .models import Usuario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'contrasena']

class BuscarClienteForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=50, required=False)
