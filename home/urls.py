from django.urls import path
from home.views import home, HomeView

urlpatterns = [
    path('api/totales/', HomeView.as_view()),
    path('', home, name='home')
]