from django.views.generic.detail import DetailView
from nutriblog.models import Articulo
from django.shortcuts import render
from .models import Articulo
from django.views.generic import TemplateView, ListView
# Create your views here.


class nutriblog(ListView):
    paginate_by = 6
    model = Articulo
    template_name = "nutriblog.html"
    ordering = ['-id']


class detalleArticulo(DetailView):
    model = Articulo
    template_name = "detalle_articulo.html"


def busqueda(request):
    if request.method == 'POST':
        busqueda = request.POST['busqueda']
        articulos = Articulo.objects.filter(
            autor__icontains=busqueda).order_by('-id') | Articulo.objects.filter(titulo__icontains=busqueda).order_by('-id')
        return render(request, 'busqueda.html',
                      {'busqueda': busqueda,
                       'articulos': articulos})
    else:
        return render(request, 'busqueda.html',
                      {})
