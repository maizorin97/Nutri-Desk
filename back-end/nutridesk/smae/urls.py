from django.urls import path
from . import views

urlpatterns = [
    path('', views.info.as_view(), name='info'),
]