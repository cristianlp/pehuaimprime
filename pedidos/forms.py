from django import forms
from .models import Pedido, Movimiento

from datetime import datetime, date

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = (
           'entidad', 'cantidad_pedida',
        )

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = (
            'cantidad_entregada', 'fecha_entrega', 
        )

    
    def clean_fecha_entrega(self):
        fecha_entrega = self.cleaned_data['fecha_entrega']
        hoy = date.today()
        if fecha_entrega > hoy:
            raise forms.ValidationError("Verificar que fecha de entrega sea menor o igual a la fecha actual")
        
        return fecha_entrega

