from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.lista_planes.as_view(), name='planes'),
    path('generar_plan/', views.generar_planes, name='generar_plan'),
    path('getDatos/',views.get_datos,name='get_datos')
]