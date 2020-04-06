from django.urls import path
from stls.views import stls, stl_upload, stl_delete

urlpatterns = [
    
        path('upload/', stl_upload, name='stl_upload'),
        path('<int:pk>/delete/', stl_delete, name='stl_delete'),
		path('', stls, name='stls')
     
]