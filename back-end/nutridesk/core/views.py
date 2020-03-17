from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from datetime import timedelta
from django.utils import timezone

from . import models, forms


class index(TemplateView):
    template_name = "index.html"

class ingresar(LoginView):
    template_name = "ingresar.html"
    form_class = forms.FormaInicioSesion
    success_url = "/index"

    def get_success_url(self):
        return super().get_success_url()

def registro(request):
    if request.method == 'POST':
        user_form = forms.FormaRegistroUsuario(request.POST)
        info_form = forms.FormaDatosFisiologicos(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            info = info_form.save(commit=False)
            info.usuario = user
            info.save()
            # exito
            return redirect("ingresar")
        else:
            return render(request, "registro.html",{'user_form':user_form,'info_form':info_form})
    else:
        user_form = forms.FormaRegistroUsuario()
        info_form = forms.FormaDatosFisiologicos()
        return render(request,'registro.html',{'user_form':user_form,'info_form':info_form})

class panel_control(TemplateView):
    template_name = "panel_control.html"

class perfil(UpdateView):
    model = models.InfoUsuario
    template_name = "perfil.html"
    pk_url_kwarg = 'id'
    fields = ['sexo','fecha_nacimiento','peso','altura']
    #form_class = forms.FormaInicioSesion
    success_url = "/panel"
    
class cerrar(LogoutView):
    template_name = "cerrar.html"

class error(TemplateView):
    template_name = "error.html"
