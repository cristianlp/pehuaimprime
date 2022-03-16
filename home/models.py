from django.db.models import Sum

from rest_framework import viewsets
#from .serializers import HomeSerializer

from pedidos.models import Movimiento

# class HomeViewSet(viewsets.ModelViewSet):
#     queryset = Movimiento.objects.all().aggregate(Sum('cantidad_entregada'))['cantidad_entregada__sum']
#     serializer_class = HomeSerializer