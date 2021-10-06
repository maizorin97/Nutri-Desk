from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_planes.as_view(), name='planes'),
    path('generar_plan/', views.generar_planes, name='generar_plan')
]