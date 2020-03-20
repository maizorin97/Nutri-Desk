from django.shortcuts import render

from django.views.generic import CreateView, ListView, TemplateView

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

def generar_planes(request):
    if request.method == 'POST':
        pass
        """user_form = forms.FormaRegistroUsuario(request.POST)
        info_form = forms.FormaDatosFisiologicos(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            info = info_form.save(commit=False)
            info.usuario = user
            info.save()
            # exito
            return redirect("ingresar")
        else:
            return render(request, "registro.html",{'user_form':user_form,'info_form':info_form})"""
    else:
        current_user = request.user
        from core.models import InfoUsuario
        from smae.models import Alimento, Grupo
        infoUser = InfoUsuario.objects.get(usuario=current_user)#filter(usuario=current_user)#.all()
        listaGrupos = Grupo.objects.all()
        listaAlimentos = Alimento.objects.all()
        from datetime import datetime as dt
        edad = dt.now().year - infoUser.fecha_nacimiento.year + (dt.now().month - infoUser.fecha_nacimiento.month)*(1/12)
        return render(request,'generar_plan.html',{'infoUser':infoUser,'edad':edad,'listaAlimentos':listaAlimentos,'listaGrupos':listaGrupos})