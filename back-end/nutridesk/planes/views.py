from django.shortcuts import render

from django.views.generic import CreateView, ListView

from .models import Plan

# Create your views here.
"""class crear_plan(CreateView):
    template_name = "registro.html"
    form_class = forms.FormaRegistroUsuario
    success_url = "/ingresar"

    def get_success_url(self):
        return super().get_success_url()"""

class lista_planes(ListView):
    template_name = "lista_planes.html"
    model = Plan
    context_object_name = 'lista_planes'