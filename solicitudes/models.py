from django.db import models

# Modelo para registrar una solicitud
class Solicitud(models.Model):
    TIPO_OPCIONES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    documento = models.CharField(max_length=50, verbose_name="Documento")
    correo = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.BigIntegerField(verbose_name="Teléfono")
    tipo = models.CharField(max_length=20, choices=TIPO_OPCIONES, verbose_name="Tipo de solicitud")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha")
    archivo = models.FileField(upload_to='archivos_solicitudes/', blank=True, null=True, verbose_name="Archivo adjunto")

    def __str__(self):
        return f"{self.asunto} - {self.nombre}"
