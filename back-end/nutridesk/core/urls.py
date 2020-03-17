from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('panel/', views.panel_control.as_view(), name='panel'),
    path('registro/', views.registro, name='registro'),
    path('ingresar/', views.ingresar.as_view(), name='ingresar'),
    path('perfil/<int:id>/', views.perfil.as_view(), name='perfil'),
    path('cerrar/', views.cerrar.as_view(), name='cerrar'),
    path('error/', views.error.as_view(), name='error'),
]
