from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "index.html"
    #def get(self, request, *args, **kwargs):
        #return render(request, self.template_name, {'title':"Nutri-desk | index"})

class registro(TemplateView):
    template_name = "registro.html"

class ingresar(TemplateView):
    template_name = "ingresar.html"

class cerrar(TemplateView):
    template_name = "cerrar.html"

class error(TemplateView):
    template_name = "error.html"
