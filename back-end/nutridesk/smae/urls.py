from django.urls import path
from . import views

urlpatterns = [
    path('', views.smae.as_view(), name='smae'),
]