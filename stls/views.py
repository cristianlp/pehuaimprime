from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Stl
from .forms import StlForm

from django.contrib.auth.decorators import login_required

@login_required
def stls(request):
    stls = Stl.objects.all().order_by('nombre')
    return render(request, 'stls.html', {'stls': stls})

@login_required
def stl_upload(request):

    if request.method == 'POST':
        form = StlForm(request.POST, request.FILES)
        if form.is_valid():
            stl = form.save(commit=False)
            observaciones = request.POST.get('observaciones', None)
            stl.observaciones = observaciones

            stl.save()
            messages.success(request, "El stl fue subido correctamente")
            return redirect(reverse('stls', args=()))           
    else:
        form = StlForm()

    return render (request, 'stl_upload.html', {'form': form})

@login_required
def stl_delete(request, pk):
    try:
        stl = Stl.objects.get(pk=pk)
    except Stl.DoesNotExist:
        messages.error(request, "El STL no existe")
        return redirect(reverse('stls', args=()))           

    stl.delete()
    messages.success(request, "El STL fue borrado correctamente")

    return redirect(reverse('stls', args=()))           
