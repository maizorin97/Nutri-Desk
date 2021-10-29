from django.views.generic.detail import DetailView
from nutriblog.models import Articulo
from django.shortcuts import render
from .models import Articulo
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
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
        page = request.GET.get('page', 1)
        busqueda = request.POST['busqueda']
        articulos = Articulo.objects.filter(
            autor__icontains=busqueda).order_by('-id') | Articulo.objects.filter(titulo__icontains=busqueda).order_by('-id')
        paginator = Paginator(articulos, 6)
        try:
            articulos = paginator.page(page)
        except InvalidPage:
            # if the page contains no results (EmptyPage exception) or
            # the page number is not an integer (PageNotAnInteger exception)
            # return the first page
            articulos = paginator.page(1)
        return render(request, 'busqueda.html',
                      {'busqueda': busqueda,
                       'articulos': articulos})
    else:
        return render(request, 'busqueda.html',
                      {})
