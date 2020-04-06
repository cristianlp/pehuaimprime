from django.db import models
from django.db.models import Sum
from entidades.models import Entidad

PRIORIDADES_TYPE = (
    ('M', 'Media'),
    ('B', 'Baja'),
    ('A', 'Alta'),
)

ICONOS_PRIORIDADES = {'B': 'fas fa-arrow-circle-down', 'M': 'fas fa-arrow-circle-right', 'A': 'fas fa-arrow-circle-up'  }

#TODO idea --> asociar con productos para poder diferenciar el contenido del pedido (máscaras, vinchas, etc)
class Pedido(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    cantidad_pedida = models.IntegerField(default=1)
    prioridad = models.CharField(max_length=15, choices=PRIORIDADES_TYPE, default="M")

    observaciones = models.TextField(blank=True, null=True)

    @property
    def icono_prioridad(self):
        return (self.prioridad, ICONOS_PRIORIDADES[self.prioridad])
        

    #True si el pedido aún no fue satisfecho
    @property
    def is_pendiente(self):
        return self.cantidad_pedida > self.cantidad_entregada


    @property
    def cantidad_pendiente(self):
        return self.cantidad_pedida - self.cantidad_entregada    

    @property
    def cantidad_entregada(self):
        cantidad_entregada = self.movimientos.aggregate(Sum('cantidad_entregada'))['cantidad_entregada__sum']
        cantidad_entregada = 0 if cantidad_entregada is None else cantidad_entregada

        return cantidad_entregada

    @property
    def pedidos_pendientes(self):
        #pendientes = self.objects.filter(cantidad_pedida < cantidad_entregada).order_by('fecha_pedido')
        #return pendientes
        pass #FIXME

    def __str__(self):
        return "%s [Fecha pedido: %s]" % (self.entidad, self.fecha_pedido.strftime('%d/%m/%Y'))


class Movimiento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="movimientos")
    cantidad_entregada = models.IntegerField()
    fecha_entrega = models.DateField()
    entregado_por = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s [Cant.Entregada: %s]" % (self.pedido, self.cantidad_entregada)
