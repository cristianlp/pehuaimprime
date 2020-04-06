from django.urls import path
from entidades.views import entidades, entidad_create, entidad_edit, entidad_delete

urlpatterns = [
    
        path('create/', entidad_create, name='entidad_create'),
        path('<int:pk>/edit/', entidad_edit, name='entidad_edit'),
        path('<int:pk>/delete/', entidad_delete, name='entidad_delete'),
		path('', entidades, name='entidades')
     
]