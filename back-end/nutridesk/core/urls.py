from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('registro/', views.registro.as_view(), name='registro'),
    path('ingresar/', views.ingresar.as_view(), name='ingresar'),
    path('cerrar/', views.cerrar.as_view(), name='cerrar'),
    path('error/', views.error.as_view(), name='error'),
]