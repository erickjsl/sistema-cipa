
from django import forms
from .models import Incidentes  # Corrigido aqui

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidentes  # Corrigido aqui
        fields = '__all__'
