from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_planes.as_view(), name='planes'),
]