from django.shortcuts import render, redirect
from .forms import SolicitudForm

# Vista para mostrar el formulario y procesar datos
def solicitud_view(request):
    if request.method == 'POST':
        # Se incluye request.FILES para manejar la subida de archivos
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            # Si es válido, guarda los datos en la base de datos
            form.save()
            return redirect('solicitud_exito') # Redirige a la URL de confirmación
    else:
        # Si no es POST, muestra un formulario en blanco
        form = SolicitudForm()
        
    return render(request, 'solicitudes/formulario.html', {'form': form})

# Vista de confirmación de éxito
def exito_view(request):
    return render(request, 'solicitudes/confirmacion.html')
