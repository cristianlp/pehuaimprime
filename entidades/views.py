from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages

from .models import Entidad
from pedidos.models import Pedido

from .forms import EntidadForm

def entidades(request):
    entidades = Entidad.objects.all().order_by('nombre')
    context = {'entidades': entidades}

    return render(request, 'entidades.html', context)

def entidad_create(request):
    form = EntidadForm(request.POST or None)
    if form.is_valid():
        entidad = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)
        telefono_contacto = request.POST.get('telefono_contacto', None) 

        entidad.observaciones = observaciones
        entidad.telefono_contacto = telefono_contacto

        entidad.save()

        messages.success(request, "La entidad fue agregada correctamente")

        return redirect(reverse('entidades', args=()))           

    context = {'form': form}

    return render(request, 'entidad_create.html', context)


def entidad_edit(request, pk):
    try:
        entidad = Entidad.objects.get(pk=pk)
    except Entidad.DoesNotExist:
        messages.error(request, "La entidad no existe")
        return redirect(reverse('entidades', args=()))

    form = EntidadForm(request.POST or None, instance=entidad)
    if form.is_valid():
        entidad = form.save(commit=False)

        observaciones = request.POST.get('observaciones', None)
        telefono_contacto = request.POST.get('telefono_contacto', None) 

        entidad.observaciones = observaciones
        entidad.telefono_contacto = telefono_contacto

        entidad.save()

        messages.success(request, "La entidad fue actualizada correctamente")

        return redirect(reverse('entidades', args=()))           

    context = {'form': form, 'entidad': entidad}

    return render(request, 'entidad_edit.html', context)


def entidad_delete(request, pk):
    try:
        entidad = Entidad.objects.get(pk=pk)
    except Entidad.DoesNotExist:
        messages.error(request, "La entidad no existe")
        return redirect(reverse('entidades', args=()))

    tiene_pedidos = Pedido.objects.filter(entidad=entidad).count() != 0
    if tiene_pedidos:
        messages.error(request, "No es posible borrar esta entidad por tener pedidos asociados")
    else:
        nombre_entidad = entidad.nombre
        entidad.delete()
        messages.success(request, "La entidad %s fue borrada correctamente" % (nombre_entidad))

    return redirect(reverse('entidades', args=()))

