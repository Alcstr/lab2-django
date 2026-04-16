from django.urls import path
from . import views

urlpatterns = [
    # Ruta para el formulario principal de asistencia
    path('', views.asistencia_view, name='asistencia_form'),
    
    # Ruta para mostrar el mensaje de éxito
    path('exito/', views.exito_view, name='asistencia_exito'),
]
