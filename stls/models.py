from django.db import models
from django.dispatch import receiver

class Stl(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='archivos')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

@receiver(models.signals.post_delete, sender=Stl)
def limpiar_archivos(sender, instance, **kwargs):
    instance.archivo.delete(False)         