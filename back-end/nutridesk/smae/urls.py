from django.urls import path
from . import views

urlpatterns = [
    path('', views.info.as_view(), name='info'),
    path('lista', views.lista_smae.as_view(), name='lista_smae'),
]