from django import forms
from .models import Asistencia

# Formulario basado en el modelo Asistencia
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_ingreso = cleaned_data.get("hora_ingreso")
        hora_salida = cleaned_data.get("hora_salida")

        # Validación: la hora de salida debe ser mayor a la hora de ingreso
        if hora_ingreso and hora_salida:
            if hora_salida <= hora_ingreso:
                raise forms.ValidationError("La hora de salida debe ser posterior a la hora de ingreso.")
        
        return cleaned_data
