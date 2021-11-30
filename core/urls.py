from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('panel/', views.panel_control, name='panel'),
    path('registro/', views.registro, name='registro'),
    path('ingresar/', views.ingresar.as_view(), name='ingresar'),
    path('perfil/', views.perfil, name='perfil'),
    path('cerrar/', views.cerrar.as_view(), name='cerrar'),
    path('error/', views.error.as_view(), name='error'),
    path('contacto/', views.contacto.as_view(), name='contacto'),
]
