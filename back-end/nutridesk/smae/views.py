from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Alimento

class info(TemplateView):
    template_name = "info.html"

class lista_smae(ListView):
    template_name = "lista_smae.html"
    model = Alimento
    context_object_name = 'lista_alimentos'
