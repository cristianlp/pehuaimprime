from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages

from .models import Pedido, PRIORIDADES_TYPE, Movimiento
from entidades.models import Entidad
from .forms import PedidoForm, MovimientoForm

from django.contrib.auth.decorators import login_required


@login_required
def pedidos(request):
    pedidos = Pedido.objects.all().order_by('entidad')
    context = {'pedidos': pedidos}

    return render(request, 'pedidos.html', context)

@login_required
def pedido_create(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        pedido = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)

        pedido.observaciones = observaciones

        pedido.save()

        messages.success(request, "El pedido fue agregado correctamente")

        return redirect(reverse('pedidos', args=()))           

    entidades = Entidad.objects.all().order_by('nombre')
    context = {'form': form, 'entidades': entidades, 'prioridades': PRIORIDADES_TYPE}

    return render(request, 'pedido_create.html', context)

@login_required
def pedido_edit(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        messages.error(request, "El pedido no existe")
        return redirect(reverse('pedidos', args=()))

    form = PedidoForm(request.POST or None, instance=pedido)

    if form.is_valid():
        pedido = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)
        prioridad = request.POST.get('prioridad', None)
        
        pedido.prioridad = prioridad
        pedido.observaciones = observaciones

        pedido.save()

        messages.success(request, "El pedido fue actualizado correctamente")

        return redirect(reverse('pedidos', args=()))           

    entidades = Entidad.objects.all().order_by('nombre')
    context = {'pedido': pedido, 'form': form, 'entidades': entidades, 'prioridades': PRIORIDADES_TYPE}

    return render(request, 'pedido_edit.html', context)


def pedido_delete(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        messages.error(request, "El pedido no existe")
        return redirect(reverse('pedidos', args=()))


    tiene_movimientos = Movimiento.objects.filter(pedido=pedido).count() != 0
    if tiene_movimientos:
        messages.error(request, "No es posible borrar este pedido por tener movimientos asociados")
    else:
        pedido_borrado = pedido
        pedido.delete()
        messages.success(request, "El pedido %s fue borrado correctamente" % (pedido_borrado))
   
    return redirect(reverse('pedidos', args=()))           


@login_required
def movimientos(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        messages.error(request, "El pedido no existe")
        return redirect(reverse('pedidos', args=()))

    movimientos = Movimiento.objects.filter(pedido=pedido).order_by('fecha_entrega')

    context = {'movimientos': movimientos, 'pedido': pedido}

    return render (request, 'movimientos.html', context)

@login_required
def movimiento_create(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        messages.error(request, "El pedido no existe")
        return redirect(reverse('pedidos', args=()))

    form = MovimientoForm(request.POST or None)
    if form.is_valid():
        movimiento = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)
        entregado_por = request.POST.get('entregado_por', None)

        movimiento.observaciones = observaciones
        movimiento.entregado_por = entregado_por
        movimiento.pedido = pedido

        movimiento.save()

        messages.success(request, "El movimiento de entrega fue agregado correctamente")
        return redirect(reverse('movimientos', kwargs={'pk': pedido.pk}))           

    context = {'pedido': pedido, 'form': form}

    return render(request, 'movimiento_create.html', context)


@login_required
def movimiento_edit(request, pk):
    try:
        movimiento = Movimiento.objects.get(pk=pk)
    except Movimiento.DoesNotExist:
        messages.error(request, "El movimiento no existe")
        return redirect(reverse('movimientos', args=()))

    form = MovimientoForm(request.POST or None, instance=movimiento)
    if form.is_valid():
        movimiento = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)
        entregado_por = request.POST.get('entregado_por', None)

        movimiento.observaciones = observaciones
        movimiento.entregado_por = entregado_por
        
        movimiento.save()
        messages.success(request, "El movimiento de entrega fue actualizado correctamente")
        return redirect(reverse('movimientos', kwargs={'pk': movimiento.pedido.pk}))           

    context = {'movimiento': movimiento, 'form': form}

    return render(request, 'movimiento_edit.html', context)

@login_required
def movimiento_delete(request, pk):
    try:
        movimiento = Movimiento.objects.get(pk=pk)
    except Movimiento.DoesNotExist:
        messages.error(request, "El movimiento no existe")
        return redirect(reverse('movimientos', args=()))

    pedido_pk = movimiento.pedido.pk

    print(pedido_pk)

    movimiento.delete()

    messages.success(request, "El movimiento fue borrado correctamente")

    return redirect(reverse('movimientos', kwargs={'pk': pedido_pk}))           


