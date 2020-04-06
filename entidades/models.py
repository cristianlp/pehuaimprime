from django.db import models

class Entidad(models.Model):
    nombre = models.CharField(max_length=255) #nombre entidad (ej. hospital pehuajo)
    contacto = models.CharField(max_length=255) #datos del contacto
    telefono_contacto = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre