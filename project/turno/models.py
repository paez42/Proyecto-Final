from django.db import models
from django.utils import timezone

# Create your models here.
class TurnoLugar(models.Model):
    """Lugar de Turno"""

    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="descripcíon"
    )

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "lugar de turno"
        verbose_name_plural = "lugares de turnos"


class Turno(models.Model):
    categoria_id = models.ForeignKey(
        TurnoLugar, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="lugar de turno"
    )
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(
        null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "turno"
        verbose_name_plural = "turnos"