from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.nutriblog.as_view(), name='nutriblog'),
    path('articulo/<int:pk>', views.detalleArticulo.as_view(), name='articulo'),
]
