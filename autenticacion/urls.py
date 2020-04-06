from django.urls import path
from django.contrib.auth.views import login, logout
from autenticacion.views import usuario_login, usuario_logout

urlpatterns = [

    path('login/$', login, name='login'),
    path('logout/$', logout, name='logout'),

]
