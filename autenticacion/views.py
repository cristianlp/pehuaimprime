from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse

from django.contrib import messages
from .forms import LoginForm


def usuario_login(request):

    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('pedidos', args=()))
        else:
            messages.error(request, "Verifique el usuario y/o contraseña")

    return render(request, "login.html", {'form': form})


def usuario_logout(request):
    logout(request)
    return redirect(reverse('autenticacion:login', args=[]))

