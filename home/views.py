from django.shortcuts import render
from django.db.models import Sum
from pedidos.models import Pedido, Movimiento

def home(request):
    total_pedidos = Pedido.objects.all().aggregate(Sum('cantidad_pedida'))['cantidad_pedida__sum']
    total_entregados = Movimiento.objects.all().aggregate(Sum('cantidad_entregada'))['cantidad_entregada__sum']

    total_pedidos = 0 if total_pedidos is None else total_pedidos
    total_entregados = 0 if total_entregados is None else total_entregados

    context = {'total_pedidos': total_pedidos, 'total_entregados': total_entregados, 'total_pendientes': total_pedidos - total_entregados}

    return render(request, 'home.html', context)