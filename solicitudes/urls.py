from django.urls import path
from . import views

urlpatterns = [
    # Ruta para el formulario principal de solicitudes
    path('', views.solicitud_view, name='solicitud_form'),
    
    # Ruta para mostrar el mensaje de éxito
    path('exito/', views.exito_view, name='solicitud_exito'),
]
