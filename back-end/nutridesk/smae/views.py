from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Alimento

class smae(ListView):
    template_name = "info.html"
    model = Alimento
    context_object_name = 'lista_alimentos'
