from django.views.generic.detail import DetailView
from nutriblog.models import Articulo
from django.shortcuts import render
from .models import Articulo
from django.views.generic import TemplateView, ListView
# Create your views here.


class nutriblog(ListView):
    model = Articulo
    template_name = "nutriblog.html"


class detalleArticulo(DetailView):
    model = Articulo
    template_name = "detalle_articulo.html"
