from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_planes.as_view(), name='planes'),
    path('ver_plan/<int:plan_id>/', views.ver_plan, name='ver_plan'),
    path('generar_plan/', views.generar_planes, name='generar_plan')
]