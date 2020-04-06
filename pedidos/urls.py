from django.urls import path
from pedidos.views import pedidos, pedido_create, pedido_edit, pedido_delete, movimiento_create, movimiento_delete, movimiento_edit, movimientos

urlpatterns = [
    
        path('create/', pedido_create, name='pedido_create'),
        path('<int:pk>/edit/', pedido_edit, name='pedido_edit'),
        path('<int:pk>/delete/', pedido_delete, name='pedido_delete'),

        #movimientos de entrega de pedidos
        path('<int:pk>/entrega/create/', movimiento_create, name='movimiento_create'),
        path('<int:pk>/entrega/edit/', movimiento_edit, name='movimiento_edit'),
        path('<int:pk>/entrega/delete/', movimiento_delete, name='movimiento_delete'),
        path('<int:pk>/entregas/', movimientos, name='movimientos'),

		path('', pedidos, name='pedidos')
]