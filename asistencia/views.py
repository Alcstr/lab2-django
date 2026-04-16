from django.shortcuts import render, redirect
from .forms import AsistenciaForm

# Vista para mostrar el formulario y procesar datos
def asistencia_view(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            # Si es válido, guarda los datos en la base de datos
            form.save()
            return redirect('asistencia_exito') # Redirige a la URL de confirmación
    else:
        # Si no es POST, muestra un formulario en blanco
        form = AsistenciaForm()
        
    return render(request, 'asistencia/formulario.html', {'form': form})

# Vista de confirmación de éxito
def exito_view(request):
    return render(request, 'asistencia/confirmacion.html')
