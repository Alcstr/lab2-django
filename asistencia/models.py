from django.db import models

# Modelo para registrar la asistencia
class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre completo")
    documento = models.CharField(max_length=50, verbose_name="Documento de identidad")
    correo = models.EmailField(verbose_name="Correo electrónico")
    fecha = models.DateField(verbose_name="Fecha")
    hora_ingreso = models.TimeField(verbose_name="Hora de ingreso")
    hora_salida = models.TimeField(verbose_name="Hora de salida")
    presente = models.BooleanField(default=False, verbose_name="¿Estuvo presente?")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        return f"{self.nombre_completo} - {self.fecha}"
