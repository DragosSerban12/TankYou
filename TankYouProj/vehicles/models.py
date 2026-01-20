from django.db import models
from users.models import Usuario

class Vehiculo(models.Model):
    TIPO_COMBUSTIBLE_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diésel'),
    ]

    usuario = models.ForeignKey(verbose_name='Usuario', to=Usuario, on_delete=models.CASCADE, related_name='vehiculos')
    matricula = models.CharField(verbose_name='Matricula', max_length=50, unique=True)
    modelo = models.CharField(verbose_name='Modelo', max_length=50)
    marca = models.CharField(verbose_name='Marca', max_length=50)
    color = models.CharField(verbose_name='Color', max_length=30)
    tipo_combustible = models.CharField(verbose_name='Tipo de combustible', max_length=20, choices=TIPO_COMBUSTIBLE_CHOICES)
    anyo_compra = models.IntegerField(verbose_name='Año de compra', default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['matricula'], name='unique_matricula')
        ]

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['marca', 'modelo', 'matricula']

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"