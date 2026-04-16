from django import forms
from .models import Solicitud

# Formulario basado en el modelo Solicitud
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
